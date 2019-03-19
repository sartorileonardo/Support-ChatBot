#!/usr/bin/env python
# -*- coding: latin-1 -*-

#Autor: Leonardo Sartori
#Contact: leonardogt4@hotmail.com

import gspread
from oauth2client.service_account import ServiceAccountCredentials

class spreadsheet():

    def __init__(self):
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        client = gspread.authorize(creds)
        sheet = client.open('PlanilhaPerguntasRespostas').sheet1
        self.sheet=sheet
        self.teste='teste'

    def read_all(self):
        return self.sheet.get_all_records()    
        
    def read_row(self,line):
        register = self.sheet.row_values(line) 
        return register   

    def read_col(self, col):
        register = self.sheet.col_values(col)
        return register   

    def read_cell(self, line, col):
        register = self.sheet.cell(line,col).value
        return register   

    def update_cell(self, line, col, text):
        self.sheet.update_cell(line, col, text)

    def insert_row(self,text_col_one, text_col_two, index):
        row = [text_col_one, text_col_two]
        self.sheet.insert_row(row,index)

    def delete_row(self, row):
        self.sheet.delete_row(3)

    def count_rows(self ):
        number = self.sheet.row_count
        return number   

