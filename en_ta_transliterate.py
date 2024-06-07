#!/usr/bin/env python

"""
Module for transliterating tamil to english by using Google's transliteration API
"""

import urllib.request
import urllib.parse
import urllib
import json


def transliterate(english_text):
    url = "https://inputtools.google.com/request"
    params = {
        'text': english_text,
        'itc': 'ta-t-i0-und',
        'num': 13,
        'cp': 0,
        'cs': 0,
        'ie': 'utf-8',
        'oe': 'utf-8'
    }

    encoded_params = urllib.parse.urlencode(params)
    full_url = f"{url}?{encoded_params}"

    try:
        with urllib.request.urlopen(full_url) as response:
            output = json.loads(response.read().decode('utf-8'))  # Decode the response
            if output[0] == 'SUCCESS':
                return 0, output[1][0][1][0]
            else:
                return 1, ''
    except urllib.error.HTTPError as e:
        print(f"Error: {e.code} - {e.reason}")
        return 1, ''


if __name__ == "__main__":
    text = "eppidi enna ethukku ennikku eppothaavathu puththakangkalai sariyaana"
    print(text)
    print(transliterate(text)[1])
