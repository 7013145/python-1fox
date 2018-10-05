#!/usr/bin/python

import json
import time
import logging
import requests


sleep_time = 3*3 + 1
sleep_max = 60 * 5


def httpGet(url, resource, params):
    sleep_count = 0
    sleep_alarm = False
    while True:

        try:
            r =requests.get(url+resource, params=params, timeout=sleep_time)
            data = r.json()
        except:
            if sleep_count == 0:
                start_time = str(time.strftime("%a %H:%M %Z", time.localtime()))
            time.sleep(1) # Safety in case http timeout is not called
            sleep_count += (sleep_time + 1)
            logging.info("Sleeping in httpGet, " + str(sleep_count) + " seconds")
            if sleep_alarm == False and sleep_count >= sleep_max:
                string = "resource has been down for over " + str(sleep_max/60) + " minutes"
                logging.info(string)
                sleep_alarm = True
            continue
        else:
            if sleep_alarm == True:
                string = "resource is now back up after being down since " + start_time
                logging.info(string)
                sleep_count = 0
                sleep_alarm = False
            break
    return data
