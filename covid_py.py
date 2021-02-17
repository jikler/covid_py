
import json
from pprint import pprint
from docxtpl import DocxTemplate
 
with open('users.json', 'r', encoding='utf-8') as f: #открыли файл с данными
    text = json.load(f) #загнали все, что получилось в переменную

    for txt in text['users']: #создали цикл, который будет работать построчно
        (txt['name'], ':', txt['id'])


# from docxtpl import DocxTemplate

doc = DocxTemplate("temp.docx")
context = { 
'fio' : txt['name'],
'sex' : "МУЖСКОЙ",
'id' : "1234567",
'group' : "Муж",
'birthday' : "13.03.1988",
'age' : "9",
'rndid' : "1234567890",
'order_date' : "25/01/2021",
'order_time' : "08:05",
'delivery_date' : "27/01/2021",
'delivery_time' : "10:55"
}
doc.render(context)
doc.save("Справка.docx")