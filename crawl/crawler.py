#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 14:40:24 2018

@author: nate levy
"""

import re
import urllib.request
from urllib.request import Request
from http.cookiejar import CookieJar

DEBUG = False

def log(s):
    if DEBUG == True:
        print(s)

def yoink(url, rel_c, abs_c):
    #data to give the sites so they let this crawl them
    cj = CookieJar() #some sites require cookies to access
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj)) #found this on stackoverflow. it's how you do the cookies.
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'}) #spoof a browser
    
    #convert html source to string
    site = opener.open(req).read().decode('utf-8')
    
    #find links, format everything to prevent double-yoinking.
    links = []
    maybe = re.findall(r'(?<=href=")([\/[a-z0-9A-Z\.\:-]+)', site)
    
    #fix formatting, append valid sites to links
    rel = 0
    ab = 0
    for m in maybe:
        # convert incomplete links to complete links,
        # check for relative vs absolute links
        if m[0] == '/': # if relative
            log("\t" + m)
            rel_c += 1
            m = url + m
        else: # if absolute
            log("\t" + m)
            abs_c += 1
            m = m.replace('https://', 'http://')
            m = m.replace('www.', '') 
            
        #forgive me. there's just some sites that don't work. this was trial and error.
        if ('muhlenberg' in m and 'media' and 'gconn' not in m 
        and 'impact' not in m and 'main' not in m and 'twitter' not in m 
        and 'G' not in m and 'weekly' not in m):
            # generalization to exclude non-html. this omits some legit sites, 
            # like trexler.muhlenberg.edu, but 500 sites is 500 sites.
            if m.count('.') < 2:
                m = m.rstrip('/')
                links.append(m)
    log("rel: {0} ab: {1}".format(rel, ab))
    
    #make text document            
    site_2_doc(url, site, rel_c, abs_c)
    
    return links, rel_c, abs_c

#write the string to a new text document
def site_2_doc(url, site, rels, absols):
    doc_name = name_doc(url)
    text = open(doc_name, 'w+')
    text.write("URL: {0}\n".format(url))
    text.write("{0} relative links\n".format(rels))
    text.write("{0} absolute links\n\n".format(absols))
    text.write(site)
    
# give a valid file name that still captures the contents of the url
def name_doc(url):
    name = url.replace('https://', '')
    name = name.replace('http://', '')
    name = name.replace('/', '-')
    name = name.replace('.', 'dot-')
    name = name.replace('muhlenberg', '')
    name = name + '.txt'
    name = name.lstrip('dot edu ')
    name = name.lstrip('- ')
    return name

def main():
    start_url = 'http://muhlenberg.edu'
    next = [start_url]
    past_links = dict()
    count = 0
    rc = 0
    ac = 0
    while len(next) !=0 and count <= 500:
        next_url = next.pop(0)
        if next_url not in past_links:
            print('accessing '+next_url + '\t{0}'.format(count))
            count += 1
            site_data = yoink(next_url, rc, ac)
            found = site_data[0]
            rc = site_data[1]
            ac = site_data[2]
            past_links[next_url] = 1
            for f in found:
                if f not in past_links:
                    next.append(f)
                    
    print('complete!')
main()