import pdfplumber
import re
import io
from collections import OrderedDict

def read_text_by_lines(pdf_file):
    text_file = open('sample.txt', 'w',encoding="utf-8") 
    pdf = pdfplumber.open(pdf_file)
    for page in range(len(pdf.pages)):
        text_file.write(pdf.pages[page].extract_text())
    text_file.close()

    Lines = []
    fs=open('sample.txt','r',encoding="utf-8")
    lines = fs.readlines()
    for line in lines: 
        if not line.isspace():
            Lines.append(line)
    demo_file=open('demo.txt', 'w',encoding="utf-8")          
    demo_file.writelines(Lines)   

    fs.close()
    demo_file.close()

    return Lines