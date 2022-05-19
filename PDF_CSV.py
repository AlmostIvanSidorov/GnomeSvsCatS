import csv

import PyPDF2

data = open('/home/ivansidorov/Altinity/UdemyCourse/'
            'Complete-Python-3-Bootcamp/'
            '15-PDFs-and-Spreadsheets/example.csv',
            encoding='utf-8')

csv_data = csv.reader(data)

data_lines = list(csv_data)

data.close()

f = open("/home/ivansidorov/Altinity/UdemyCourse/"
         "Complete-Python-3-Bootcamp/"
         "15-PDFs-and-Spreadsheets/Working_Business_Proposal.pdf", "rb")

pdf_reader = PyPDF2.PdfFileReader(f)

print(pdf_reader.numPages)

f.close()
