# Web sacraper script for extracting relevant data for further processing

# imports
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import re
import json

# extracting data
url = 'https://pakwired.com/100-best-quotes-time/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
quotes = soup.select('blockquote.shortcode_quote p') #select the p tags with the quotes within the blockquote tags
names = soup.select('blockquote.shortcode_quote cite')

# correcting special characters in quotes
for i,line in enumerate(quotes):
    line_str = line.string
    line_fixed = re.sub(u'\u201c','"',line_str)  # left double quote
    line_fixed = re.sub(u'\u201d','"',line_fixed) # right double quote
    line_fixed = re.sub(u'\u2018','\'',line_fixed) # left single quote
    line_fixed = re.sub(u'\u2019','\'',line_fixed) # right single quote
    line_fixed = re.sub(u'\u2012','-',line_fixed) # hyphen
    line_fixed = re.sub(u'\u2013','-',line_fixed) # hyphen
    line_fixed = re.sub(u'\u2014','-',line_fixed) # hyphen
    for j,char in enumerate(line_fixed):
        if (char.isdigit()):
            line_fixed = line_fixed.strip(char).strip('.') # removing quote number in format <num>.
    quotes[i] = line_fixed
    # print(line_fixed)

# fixing names
for k,line in enumerate(names):
    line_str = line.string
    # line_fixed = re.sub(u'\u2013','',line_str)
    line_fixed = line_str.strip(u'\u2013').strip(' ')
    names[k] = line_fixed

# dictionary of names and corresponding quotes
compiled_dict = dict(zip(names, quotes))

with open('data.json', 'w') as outfile:
    json.dump(compiled_dict, outfile)

