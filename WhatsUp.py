#!/usr/bin/env python3
#Import dependencies
import urllib.request
import os
import re
from collections import defaultdict
from bs4 import BeautifulSoup
from argparse import ArgumentParser

#Thanks to *shikantaza* on IRC
################################################################ 
#             _   _                   _                        #
#            | \ | |                 | |                       #
#            |  \| | __ _ _ __   __ _| |_ __ ___               #
#            | . ` |/ _` | '_ \ / _` | | '_ ` _ \              #
#            | |\  | (_| | |_) | (_| | | | | | | |             #
#            \_| \_/\__,_| .__/ \__,_|_|_| |_| |_|             #
#                        | |                                   #
#                        |_|                                   #
#                                                              #
# ############################################################ #
#              ©2016 Napalm - All Rights Reserved              #
################################################################ 

#Calls and creates ArgumentParser for -u & --url
parser = ArgumentParser()
parser.add_argument("-u", "--url", dest="url", help="URL to scan", metavar="url")
args = parser.parse_args()
#If Args provided continue
if args.url:
    #Download and extract text from BuiltWith
    soup = BeautifulSoup(urllib.request.urlopen("http://builtwith.com/app/lookup.aspx?"+args.url+"&proper=true"), "html.parser")
    results = defaultdict(list)
    #Searches for http links with values
    for techItem in soup.find_all("div", class_="techItem"):
        tag = techItem.find("a", href=re.compile("^http"))
        url = tag['href']
        nameTag = techItem.find_previous("li", class_="active").find("span")
        name = nameTag.text
        results[name].append(url)

    for name, urls in results.items():
        #If you want the output to be like whats below this line, remove the #'s from those lines
        #Example Output if you remove those #'s
        #Web Servers
        #===========
        #nginx
        
        #print(name)
        #print("=" * len(name))
        
        #Finalizes the urls for output
        final = '%s\n' % '\n'.join(urls)
        #Replaces [*] from before the lines
        final1 = final.replace("http://trends.builtwith.com/", "[*] ")
        #Replaces The leftover / after (eg: cms) with a Dash
        final2 = final1.replace("/", " - ")
        #Replaces the Dashes in the ur with Spaces.
        final3 = final2.replace("-", " ")
        #Prints the final output
        print(final2)
else:
    #If no arguments provided, show this usage
    print("M8..... What are you doing, we need the url.")
    print("Usage: ")
    pathtoscript = os.path.dirname(os.path.abspath(__file__))
    print("python3 "+pathtoscript+"-u www.example.com")
