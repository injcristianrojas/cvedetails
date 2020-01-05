#!/usr/bin/env python

import urllib.request
import urllib.parse
import json

URL = ("http://www.cvedetails.com/json-feed.php?numrows=30"
"&vendor_id=%s"
"&product_id=%s"
"&version_id=%s"
"&hasexp=0&opec=0&opov=0&opcsrf=0&opfileinc=0&opgpriv=0&opsqli=0&opxss=0&opdirt=0&opmemc=0&ophttprs=0&opbyp=0&opginf=0&opdos=0&orderby=3&cvssscoremin=0")

USER_AGENT = 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0'

if __name__ == "__main__":
    params = ('Apache', 'HTTP Server', '2.4.2')
    quoted_params = tuple(urllib.parse.quote(param) for param in params)
    full_url = URL % quoted_params
    print(full_url)
    request_config = urllib.request.Request(
        full_url, 
        data = None, 
        headers = {
            'User-Agent': USER_AGENT
        }
    )
    request = urllib.request.urlopen(request_config)
    raw_data = request.read()
    print(raw_data)