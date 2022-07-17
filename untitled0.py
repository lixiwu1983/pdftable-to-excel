# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 19:58:25 2022

@author: lxw
"""

import pdfplumber
import pandas as pd
pdf=pdfplumber.open(r"C:\Users\lxw\lxw2.pdf")
pages = pdf.pages


tables = pdf.pages[0].extract_table()
data = pd.DataFrame(tables[1:], columns=tables[0])
data
data.to_excel(r"C:\Users\lxw\test\lxw.xlsx", index=False)

#tables = pdf.pages[1].extract_table()
#data = pd.DataFrame(tables[1:], columns=tables[0])
#data
#data.to_excel(r"C:\Users\lxw\test\lxw2.xlsx", index=False)

#tables = pdf.pages[2].extract_table()
#data = pd.DataFrame(tables[1:], columns=tables[0])
#data
#data.to_excel(r"C:\Users\lxw\test\lxw3.xlsx", index=False)

#tables = pdf.pages[3].extract_table()
#data = pd.DataFrame(tables[1:], columns=tables[0])
#data
#data.to_excel(r"C:\Users\lxw\test\lxw4.xlsx", index=False)
