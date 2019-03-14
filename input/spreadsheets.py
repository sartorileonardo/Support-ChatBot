#Autor: Leonardo Sartori
#Contact: leonardogt4@hotmail.com

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('PlanilhaPerguntasRespostas').sheet1

pp = pprint.PrettyPrinter()

def read_all():
    registers = sheet.get_all_records()
    pp.pprint(registers) 

def read_row(line):
    register = sheet.row_values(line) 
    pp.pprint(register)   

def read_col(col):
    register = sheet.col_values(col)
    pp.pprint(register)   

def read_cell(line, col):
    register = sheet.cell(line,col).value
    pp.pprint(register)   

def update_cell(line, col, text):
    sheet.update_cell(line, col, text)

def insert_row(text_col_one, text_col_two, index):
    row = [text_col_one, text_col_two]
    sheet.insert_row(row,index)

def delete_row(row):
    sheet.delete_row(3)

def count_rows():
    number = sheet.row_count
    pp.pprint(number)   

#Call the function read all
read_all()

