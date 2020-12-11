#!/usr/bin/python3

'''
This function ping google.com for every 10 secs for 5 minutes continuously.

'''
import os
from pythonping import ping
from datetime import datetime 
import time

def ping_server():
    
    cnt = 0
    # begin_time = datetime.now()
    # duration = begin_time + datetime.timedelta(minutes = 5)
    # # try:
    while cnt < 10:
        
        ping('www.google.com', verbose=True)
        time.sleep(10)
        cnt += 1

ping_server()
        


