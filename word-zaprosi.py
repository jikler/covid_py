"""
в word документ вставить 
{{ director }}
далее будет подстановка из словаря context
"""

from docxtpl import DocxTemplate
import openpyxl

test=[]
wb = openpyxl.load_workbook('users.xlsx')
sheet=wb.get_active_sheet()

for row in sheet['A2':'K2']:
    for cellObj in row:
        if cellObj.value==None or cellObj.value==" ":
            continue
        #print(cellObj.value)
        test.append(cellObj.value)
print(test)

x=0
while x<len(test):
    doc = DocxTemplate("temp.docx")
    context = {
        'fio' : test[x],
        'sex' : test[x+4],
        'id' : test[x+2],
        'group' : test[x+5],
        'birthday' : test[x+3],
        'age' : test[x+4],
        'rndid' : test[x+11],
        'order_date' : test[x+7],
        'order_time' : test[x+8],
        'delivery_date' : test[x+9],
        'delivery_time' : test[x+10]
    }
    doc.render(context)
    doc.save(test[x]+'.docx')    
    x+=5

