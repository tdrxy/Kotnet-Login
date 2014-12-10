#!/usr/bin/env python

import mechanize
import re

def auto_login():

    br[uID] = "rxxxxxxxx" #USERNAME
    br[pwID]= "xxxxxxxxx" #PASSWORD  

    url = "https://netlogin.kuleuven.be/cgi-bin/wayf2.pl?inst=kuleuven&lang=nl&submit=Ga+verder+%2F+Continue"

    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.open(url)
    br.select_form(name = "netlogin")
    form = str(br.form)

    uID = "uid"
    dynamic_pwID = re.findall(r"(pwd\d+)", form) #pwID changes when page is refreshed
    pwID = dynamic_pwID[0]

    res = br.submit()


if __name__ == '__main__':
    try:
        auto_login()
        print "Logged in"
    except Exception as e:
        print e
