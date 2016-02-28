#!/usr/bin/env python3
import urllib.request
import os
import re
from collections import defaultdict
from bs4 import BeautifulSoup
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-u", "--url", dest="url", help="URL to scan", metavar="url")
args = parser.parse_args()
if args.url:
    soup = BeautifulSoup(urllib.request.urlopen("http://builtwith.com/app/lookup.aspx?"+args.url+"&proper=true"), "html.parser")
    results = defaultdict(list)
    for techItem in soup.find_all("div", class_="techItem"):
        tag = techItem.find("a", href=re.compile("^http"))
        url = tag['href']
        nameTag = techItem.find_previous("li", class_="active").find("span")
        name = nameTag.text
        results[name].append(url)

    for name, urls in results.items():
        #print(name)
        #print("=" * len(name))

        final = '%s\n' % '\n'.join(urls)
        final1 = final.replace("http://trends.builtwith.com/", "[*] ")
        final2 = final1.replace("/", " - ")
        final3 = final2.replace("-", " ")
        print(final2)
else:
    print("M8..... What are you doing, we need the url.")
    print("Usage: ")
    pathtoscript = os.path.dirname(os.path.abspath(__file__))
    print("python3 "+pathtoscript+"-u www.example.com")
