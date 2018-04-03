#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 14:40:24 2018

@author: nate levy, alan sato
"""
import re
import urllib.request
from urllib.request import Request
from http.cookiejar import CookieJar


def yoink(url):
    #get the text of the site
    
    cj = CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    site = opener.open(req).read().decode('utf-8')
    #make text document
    doc_name = name_doc(url)
    text = open(doc_name, 'w+')
    text.write(site)
    #find links
    links = []
    maybe = re.findall(r'(?<=href=")([\/[a-z0-9A-Z\.\:-]+)', site)
    
    #sanitize & doublecheck
    for m in maybe:
       # m = m.group()
        m = m.replace('https://', 'http://')
        m = m.replace('www.', '')
        if m[0] == '/':
            m = url + m
        if 'muhlenberg' in m and 'media' not in m and 'impact' not in m and 'main' not in m and 'twitter' not in m and 'G' not in m:
            if m.count('.') < 2:
                m = m.rstrip('/')
                links.append(m)

    return links

def name_doc(url):
    name = url.replace('https://', '')
    name = name.replace('http://', '')
    name = name.replace('/', ' slash ')
    name = name.replace('.', ' dot ')
    name = name.replace('muhlenberg', '')
    name = name + '.txt'
    return name

def main():
    start_url = 'http://muhlenberg.edu'
    next = [start_url]
    past_links = []
    count = 0
    while len(next) !=0 and count <= 500:
        next_url = next.pop(0)
        if next_url not in past_links:
            print('accessing '+next_url + '\t{0}'.format(count))
            count += 1
            found = yoink(next_url)
            past_links.append(next_url)
            for f in found:
                if f not in past_links:
                    next.append(f)
                    
    print('complete!')
main()