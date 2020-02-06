import csv
import datetime
import xml.etree.ElementTree as ET

import requests


def generate_key_notes_dataset(filename, url, parser, parser_header):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(parser_header)
        root = get_xml(url)
        parser(root, writer)


def get_xml(url_string):
    headers = {
        'Accept': 'application/xml',
    }
    result = requests.get(url_string,
                          headers=headers)
    return ET.fromstring(result.content)


def parse_item(item):
    for field in list(item):
        if field.tag == 'pubDate':
            data = field.text.replace('GMT', '')
            data = data.replace('PDT', '')
            date = datetime.datetime.strptime(str(data.strip()), '%a, %d %b %Y %H:%M:%S')
            date_formatted = date.strftime("%d/%m/%Y")
        if field.tag == 'title':
            title = field.text
    return [date_formatted, title]


def parse(root, writer):
    index = 0
    for item in root.iter('item'):
        row = parse_item(item)
        row.insert(0, str(index))
        writer.writerow(row)
        index += 1


generate_key_notes_dataset('apple_keynotes_events.csv',
                           'https://applehosted.podcasts.apple.com/apple_keynotes_hd/apple_keynotes_hd.xml', parse,
                           ['id', 'date', 'title'])
