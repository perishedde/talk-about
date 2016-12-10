#!/usr/bin/python
import sys
import json
import random

def import_data(filename):
    with open(filename) as data_file:
        return json.load(data_file)

def extract_tag_params():
    tags = []
    if len(sys.argv) > 1:
        for tag in sys.argv[1:]:
            tags.append(tag.lower())
    return tags

def filter_quotes(quotes, filter_tags):
    result = []
    # extract matching quotes
    if (len(filter_tags) == 0):
        result = quotes
    else:
        for quote in quotes:
            for tag in quote.get('tags'):
                if tag in filter_tags:
                    result.append(quote)
    return result

def show_one(filtered_quotes):
    if len(filtered_quotes) == 0:
        print "Sorry! I've found no quotation... :'-('"
    else:
        quote = random.choice(filtered_quotes)
        print "\nQuotation:\n\"%s\"\n\nBy:\n%s\n\nSource:\n%s\n" % ( quote.get('text'), quote.get('person'), quote.get('source') )

quotes = import_data('quote-repository.json')
tags = extract_tag_params()
filtered_quotes = filter_quotes(quotes, tags)
show_one(filtered_quotes)
