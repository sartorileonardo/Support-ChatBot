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

#Read only one register of six line
#register = sheet.row_values(6)

#Read only one register of six line
#register = sheet.col_values(6)

#Read only one cell
#register = sheet.cell(6,11).value

#Update only one cell
#sheet.update_cell(6, 11, 'blablabla')

#Insert row
#row = ["Pergunta 123", "Resposta 123"]
#index = 3
#sheet.insert_row(row,index)

#Delete row
#sheet.insert_row(3)

#Show count of lines
#sheet.row_count

#Read all registers
registers = sheet.get_all_records()

pp.pprint(registers)
