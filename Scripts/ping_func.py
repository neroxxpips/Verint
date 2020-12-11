#!/usr/bin/python3

'''
This function ping google.com for every 10 secs for 5 minutes continuously.
- Must use pip3 to install pythonping module

'''
from pythonping import ping
import time
import json
import socket

def ping_server(event, context): # to test code outside of aws lambda remove both arguments(event, context)
    
    cnt = 1
    host = 'www.google.com'

    initial_min = 0 # in seconds
    duration = 300 #(5 * 60 ) in seconds

    try:
        while initial_min < duration:
            
            ip = socket.gethostbyname(host)
            ping(ip, count=1)
            print("www.google.com is Online!")
            print(f"{cnt} Waiting for 10 secs...")
            time.sleep(10) # sleeps for 10 secs
            initial_min += 10
            cnt += 1

    except socket.error:
        print(host, 'Offline')

    return {
        'statusCode': 200,
        'body': json.dumps('Ping Google Server Successfully!')
    }
    


        


