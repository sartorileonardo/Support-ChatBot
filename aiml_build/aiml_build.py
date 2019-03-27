#!/usr/bin/python3

# -*- coding: latin-1 -*-

#Autor: Leonardo Sartori
#Contact: leonardogt4@hotmail.com

from spreadsheets import spreadsheet
sheet = spreadsheet()
'''
#Sample AIML with normal question:
<aiml version="1.0.1" encoding="UTF-8">
<!-- basic_chat.aiml -->
    <category>
        <pattern>HELLO</pattern>
        <template>
            Well, hello!
        </template>
    </category>
    
    <category>
        <pattern>WHAT ARE YOU</pattern>
        <template>
            I'm a bot, silly!
        </template>
    </category>
    
</aiml>
#Sample AIML with random question:
<?xml version = "1.0" encoding = "UTF-8"?>
<aiml version = "1.0.1" encoding ="UTF-8"?>
   <category>
      <pattern>HI</pattern>
      
      <template>
         <random>
            <li> Hello! </li>
            <li> Hi! Nice to meet you! </li>
         </random>
      </template>
      
   <category>      
</aiml>
'''

#def open_file():
file = open("support.aiml", "w")

def open_aiml_tag():
    file.write("<?xml version = \"1.0\" encoding=\"UTF-8\"?>")
    file.write("\n<aiml version=\"1.0.1\" encoding=\"UTF-8\">\n")

def close_amil_tag():
    file.write("</aiml>")

def write_pattern_tag(question_message):
    file.write("\t\t<pattern>\n")
    file.write("\t\t\t"+question_message+"\n")
    file.write("\t\t</pattern>\n")

def open_category_tag():
    file.write("\t<category>\n")

def close_category_tag():
    file.write("\t</category>\n")

def write_template_tag(responseMessage):
    file.write("\t\t<template>\n")
    file.write("\t\t\t"+responseMessage+"\n")
    file.write("\t\t</template>\n")

def add_questions_default(listQuestion, listResponse):
    #open_aiml_tag()
    #open_category_tag()
    for lineQuestion in listQuestion:
        #write_pattern_tag(lineQuestion)
        print(lineQuestion)  
        for lineResponse in listResponse:
            
            print(lineResponse) 
            #write_template_tag(lineResponse)    
            
    #close_category_tag()
    #close_amil_tag()

    
def close_file():
    # Close opend file
    file.close()

#Test
#open_file()

list1 = ['Pergunta 1', 'Pergunta 2']
list2 = ['Resposta 1', 'Resposta 2']

#add_questions_default(sheet.read_col(1), sheet.read_col(2))
add_questions_default(list1, list2)

#Obs: To test add sheet in same directory
#TODO: Align question with responses in aiml out.
#TODO: Convert file.write commands in only one string with contacts
