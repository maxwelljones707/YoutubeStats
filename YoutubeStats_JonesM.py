"""
Youtube Statistics
Name: Max Jones
Date: Winter 2020
"""

import re, urllib.request

def stats(url = input("What video would you like to analyze? Please enter the video URL here: ") ):
    stream = urllib.request.urlopen(url)
    text = stream.read().decode("UTF-8")
    numbers = []

    views_pattern = r"([0-9]*[,]*[0-9]*[,]*[0-9]*[,/][0-9]*) views"
    name_pattern = r"<title>(.*) - YouTube</title>"


    views_regex = re.compile(views_pattern)
    name_regex = re.compile(name_pattern)

    views_results = views_regex.findall(text)
    name_results = name_regex.findall(text)

    print("The video " + "'" + str(name_results[0]) + "' has " + str(views_results[0]) + " views.")

stats()

