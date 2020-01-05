#!/usr/bin/env python

import urllib.request
import urllib.parse
import json
import argparse

URL = ("http://www.cvedetails.com/json-feed.php?numrows=30"
"&vendor_id=%s"
"&product_id=%s"
"&version_id=%s"
"&hasexp=0&opec=0&opov=0&opcsrf=0&opfileinc=0&opgpriv=0&opsqli=0&opxss=0&opdirt=0&opmemc=0&ophttprs=0&opbyp=0&opginf=0&opdos=0&orderby=3&cvssscoremin=0")

USER_AGENT = 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0'

def get_cve_data_json(vendor, product, version):
    params = (vendor, product, version)
    quoted_params = tuple(urllib.parse.quote(param) for param in params)
    full_url = URL % quoted_params
    request_config = urllib.request.Request(
        full_url, 
        data = None, 
        headers = {
            'User-Agent': USER_AGENT
        }
    )
    request = urllib.request.urlopen(request_config)
    raw_data = request.read()
    encoding = request.info().get_content_charset('utf-8')
    return json.loads(raw_data.decode(encoding))

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--vendor", help="Vendor (optional)", action="store", default="0", dest="vendor"
    )
    parser.add_argument(
        "--product", help="Product (required)", action="store", required=True, dest="product"
    )
    parser.add_argument(
        "--version", help="Version (required)", action="store", required=True, dest="version"
    )
    args = parser.parse_args()
    
    params = (args.vendor, args.product, args.version)
    print(json.dumps(get_cve_data_json(*params), indent=4, sort_keys=True))

