#!/usr/bin/env python

import requests
import pandas as pd
from bs4 import BeautifulSoup
import argparse
import time
from lxml import html

VERSION = "0.1.0"
AUTHOR = "Copyright (C) 2022, by Michael John"

class HTMLTableParser:
    
    def parse_url(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml') # or use 'html.parser'
        soup.prettify(formatter=lambda s: s.replace(u'\xc2\xa0', ''))
        soup.prettify(formatter=lambda s: s.replace("<br>", ' '))
        #soup.prettify(formatter=lambda s: s.replace(u'\x09', ' '))
        #return [(table['id'],self.parse_html_table(table))\
        #        for table in soup.find_all('table')]  

        #delimiter = ' ' #'###'                           # unambiguous string
        for line_break in soup.findAll('br'):       # loop through line break tags
            line_break.replaceWith(' ') #u'\x0a')

        return soup.find_all('table')[1] # Grab the first table

    def parse_html_table(self, table):
        n_columns = 0
        n_rows=0
        column_names = []

        # Find number of rows and columns
        # we also find the column titles if we can
        for row in table.find_all('tr'):
            
            # Determine the number of rows in the table
            td_tags = row.find_all('td')
            if len(td_tags) > 0:
                n_rows+=1
                if n_columns == 0:
                    # Set the number of columns for our table
                    n_columns = len(td_tags)
                    
            # Handle column names if we find them
            th_tags = row.find_all('th') 
            if len(th_tags) > 0 and len(column_names) == 0:
                for th in th_tags:
                    column_names.append(th.get_text())

        # Safeguard on Column Titles
        if len(column_names) > 0 and len(column_names) != n_columns:
            raise Exception("Column titles do not match the number of columns")

        columns = column_names if len(column_names) > 0 else range(0,n_columns)
        df = pd.DataFrame(columns = columns,
                            index= range(0,n_rows))
        row_marker = 0
        for row in table.find_all('tr'):
            column_marker = 0
            columns = row.find_all('td')
            for column in columns:
                df.iat[row_marker,column_marker] = column.get_text().replace('\t','')
                column_marker += 1
            if len(columns) > 0:
                row_marker += 1
                
        # Convert to float if possible
        for col in df:
            try:
                df[col] = df[col].astype(str).replace('nan','')
            except ValueError:
                pass
        
        return df

def main():

    start = time.time()

    parser = argparse.ArgumentParser(description='Show a PrimeGrid user\'s badges.')
    parser.add_argument('userid', metavar='userid', type=int, # nargs='+',
                        help='PrimeGrid user-id')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + VERSION + ' ' + AUTHOR)
    args = parser.parse_args()
    #print(args.accumulate(args.integers))

    url = "https://www.primegrid.com/show_badges.php?userid=" + str(args.userid) # 130644"

    try:
        hp = HTMLTableParser()
        table = hp.parse_url(url) #[0][1] # Grabbing the table from the tuple
        print(hp.parse_html_table(table)) #.replace("NaN"," "))
    except IndexError:
        #print("Keine Badge-Tabelle gefunden, falsche userid?")
        print("Found no badges table, maybe wrong userid?")
    except requests.exceptions.ConnectionError as e:
        print(e)
    
    end = time.time()
    print('[{:2.3} seconds elapsed]'.format((end - start)))

main()