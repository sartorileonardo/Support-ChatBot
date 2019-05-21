#!/usr/bin/python3

# -*- coding: latin-1 -*-

#Autor: Leonardo Sartori
#Contact: leonardogt4@hotmail.com

import schedule  
import time 
from os import popen 

def run_aiml_build():  
    print("I'm working...")  
    popen("python3 aiml_build.py")

#schedule.every(30).seconds.do(run_aiml_build)
schedule.every().day.at("12:00").do(run_aiml_build)

while True:  
    schedule.run_pending()
    time.sleep(1)
