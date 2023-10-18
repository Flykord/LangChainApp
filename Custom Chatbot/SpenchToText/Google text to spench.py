# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 09:23:15 2023

@author: vazquezd
"""

# Import the required module for text 
# to speech conversion 
from gtts import gTTS 

# This module is imported so that we can 
# play the converted audio 
import os 

# The text that you want to convert to audio 
mytext = 'Welcome to geeksforgeeks!'

# Language in which you want to convert 
language = 'en'

mytext = 'Passing the text and language to the engine,'+ 'here we have marked slow=False. Which tells' + 'the module that the converted audio should have a high speed'
 
myobj = gTTS(text=mytext, lang=language, slow=False) 

# Saving the converted audio in a mp3 file named 
# welcome 
myobj.save("welcomeTrans.mp3") 

# Playing the converted file 
os.system("mpg321 welcome.mp3") 
