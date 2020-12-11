#!/bin/sh

# AUTHOR: Oghenero Ekwevugbe
# PURPOSE: This script captures the last line of jenkins logs in docker container and sends the output to output.log in home directory
# FURTHER INSTRUSTION: Schedule script to run as a cronjob (crontab -e => * * * * * /home/<username>/script/jenkins_logs.sh)
# DATE MODIFIED: 12/10/2020

CONTAINER_ID='532a135a747b'
NO_OF_LINE='1'
USERNAME='ec2-user'

echo " "

sudo docker logs --tail $NO_OF_LINE $CONTAINER_ID &> /home/$USERNAME/output.log

echo "************* Jenkins Logs Captured Successfully! ********"

echo "     View output.log in Home Directory for output    "

echo " "
