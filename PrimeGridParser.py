#!/usr/bin/env python

import requests, argparse, time
from bs4 import BeautifulSoup
from prettytable import from_html_one, SINGLE_BORDER, DOUBLE_BORDER

VERSION = "0.2.0"
AUTHOR = "Copyright (C) 2022, by Michael John"
DESC = "Show a PrimeGrid user\'s badges."

def parse_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    for line_break in soup.findAll('br'):
        line_break.replaceWith(' ')
    return soup.find_all('table')[1]

def main():
    start = time.time()

    parser = argparse.ArgumentParser(description=DESC)
    parser.add_argument('userid', metavar='userid', type=int, help='PrimeGrid user-id')
    parser.add_argument('-s', '--single', help='use singleborder lines', action='store_true')
    parser.add_argument('-d', '--double', help='use double border lines', action='store_true')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + VERSION + ' ' + AUTHOR)
    args = parser.parse_args()
    url = "https://www.primegrid.com/show_badges.php?userid=" + str(args.userid)
    # my userid is 130644 in case you are curious
    try:
        table = parse_url(url)
        table = from_html_one(str(table),max_width=10)
        if vars(args)["single"] == True:
            table.set_style(SINGLE_BORDER)
        if vars(args)["double"] == True:
            table.set_style(DOUBLE_BORDER)
        table = table.get_string(fields=["Project", "Current Credit", "Current Badge", "Credit Level for Next Badge", "Next Badge", "Credit Needed for Next Badge"],max_width=10)
        print(table)
    except IndexError:
        #print("Keine Badge-Tabelle gefunden, falsche userid?")
        print("Found no badges table, maybe wrong userid?")
    except requests.exceptions.ConnectionError as e:
        print(e)
    end = time.time()
    print('[{:2.3} seconds elapsed]'.format((end - start)))

main()