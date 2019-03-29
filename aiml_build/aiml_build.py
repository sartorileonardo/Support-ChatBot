#!/usr/bin/python3

# -*- coding: latin-1 -*-

#Autor: Leonardo Sartori
#Contact: leonardogt4@hotmail.com

from spreadsheets import spreadsheet
sheet = spreadsheet()

#def open_file():
file = open("support.aiml", "w")

def open_aiml_tag():
    return ("<?xml version = \"1.0\" encoding=\"UTF-8\"?>"+"\n<aiml version=\"1.0.1\" encoding=\"UTF-8\">\n")

def close_amil_tag():
    return "</aiml>"

def write_pattern_tag(question_message):
    return "\t\t<pattern>\n"+"\t\t\t"+question_message+"\n"+"\t\t</pattern>\n"

def open_category_tag():
    return "\t<category>\n"

def close_category_tag():
    return "\t</category>\n"

def write_template_tag(responseMessage):
    return "\t\t<template>\n"+"\t\t\t"+responseMessage+"\n"+"\t\t</template>\n"

def add_questions_default(listQuestion, listResponse):
    text = ""
    text += open_aiml_tag() + open_category_tag()
        
    listaPerguntasRespostas = list(zip(listQuestion[1:], listResponse[1:]))
    for line in listaPerguntasRespostas:
        text += write_pattern_tag(line[0]) + write_template_tag(line[1])
    text += close_category_tag()
    text += close_amil_tag()
    file.write(text)
    file.close()
        
add_questions_default(sheet.read_col(1), sheet.read_col(2))
