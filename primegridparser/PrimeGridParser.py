#!/usr/bin/env python

import requests, argparse, time
from bs4 import BeautifulSoup
from prettytable import from_html_one, SINGLE_BORDER, DOUBLE_BORDER
from colorama import init, Fore, Back, Style

VERSION = "0.4.0"
AUTHOR = "Copyright (C) 2022, by Michael John"
DESC = "Show a PrimeGrid user\'s badges."

def parse_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    for line_break in soup.findAll('br'):
        line_break.replaceWith(' ')
    return soup.find_all('table')[1]

badges = [
    ("Color/Credit Needed", "Badge", "Shield", "Color"),
    ("Bronze", "10,000", "100M", Fore.LIGHTYELLOW_EX),
    ("Silver", "100,000", "200M", Fore.LIGHTWHITE_EX),
    ("Gold", "500,000", "500M", Fore.YELLOW),
    ("Amethyst", "1M", "1B", Fore.LIGHTRED_EX),
    ("Ruby", "2M", "2B", Fore.RED),
    ("Turquoise", "5M", "5B", Fore.CYAN),
    ("Jade", "10M", "10B", Fore.GREEN),
    ("Sapphire", "20M", "20B", Fore.BLUE),
    ("Emerald", "50M", "50B", Fore.LIGHTGREEN_EX)
]

def colorize_cells(table: str):

    for badge in badges:
        table = table.replace(badge[0], badge[3]+badge[0]+Style.RESET_ALL)
    return table

def process_cells(table: str):

    table = table.replace("(none)", "      ")
    return table

def main():
    start = time.time()

    parser = argparse.ArgumentParser(prog="PrimeGridParser", description=DESC)
    parser.add_argument('userid', metavar='userid', type=int, help='PrimeGrid user-id')
    parser.add_argument('-s', '--single', help='use singleborder lines', action='store_true')
    parser.add_argument('-d', '--double', help='use double border lines', action='store_true')
    parser.add_argument('-c', '--color', help='use colorized output', action='store_true')
    parser.add_argument('-n', '--none', help='suppress (none) output', action='store_true')
    parser.add_argument('-q', '--quiet', help='suppress debug timing output', action='store_true')
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
        #table = table.replace("Gold", "GOLD") # Column 1""
        if vars(args)["color"] == True:
            table = colorize_cells(table)
        if vars(args)["none"] == True:
            table = process_cells(table)
        print(table)
    except IndexError:
        #print("Keine Badge-Tabelle gefunden, falsche userid?")
        print("Found no badges table, maybe wrong userid?")
    except requests.exceptions.ConnectionError as e:
        print(e)
    end = time.time()
    if not vars(args)["quiet"]:
        print('[{:2.3} seconds elapsed]'.format((end - start)))
