# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16hXhgn81cn6vVkWtn51dtjXKhcn2CBG4
"""

#importing some modules
import RPi.GPIO as GPIO  
import time  
import random

#making threshold variable
threshold = 20

#TASK -1
def temp_humi():
  temp = round(random.uniform(0,50),2)#rounding upto 2 decimals
  humidity = round(random.uniform(20,90),2)
  print("Temp: %d C" % temp +' '+"Humid: %d %%" % humidity)
  return temp,humidity;

#TASK -2 PIN SETUP 

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)  
GPIO.setup(25, GPIO.IN) #reading the data  

#TASK-3

def controlling_part(temp ,humidity):
  if (temp<threshold):
    print("Weather is cold! and the value of humidity is :"humidity)
  else:
    print("Weather is HOT! and the value of humidity is :"humidity)

  
while True:  
     try:  
        if (GPIO.input(25) == True):
          temp,humidity = temp_humi()
          controlling_part(temp,humidity)
        sleep(.01)  
    except KeyboardInterrupt:  
        exit()