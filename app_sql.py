
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox 
from tkinter import ttk #вкладки
from docxtpl import DocxTemplate
import sqlite3
import pandas as pd


def clicked():
    res = "Привет {}".format(txt.get())
    lbl.configure(text=res)

def createDoc():
    doc.render(context)
    doc.save("Справка.docx")
    # print(combo['values'])
    # messagebox.showinfo('COVID GENERATOR 69', 'Справка на рабочем столе!')

window = Tk()
window.title("COVID GENERATOR 69")
window.geometry()
window.resizable(width=False, height=False)

# подключаемся к базе данных начало
conn = sqlite3.connect("users.db") # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()
# подключаемся к базе данных конец

df = pd.read_sql("SELECT * FROM users", conn)

valueName = df['name'].tolist()
valueId = df['id'].tolist()
valueBirth = df['birthday'].tolist()
valueSex = df['sex'].tolist()

# print(valueName)

# вкладки начало
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
# tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Главная')
tab_control.add(tab2, text='Добавить')
# tab_control.add(tab3, text='Удалить')

# tab 1 начало
# cursorR = conn.execute("SELECT * from users")
# results = cursorR.fetchall()
# value = StringVar()

nameTitle = Label(tab1, text='ФИО пациента:', background="#eee", justify=LEFT, font=("Arial Bold", 10), padx=10, pady=5)
nameTitle.grid(sticky = W, column=0, row=0)

# выпадающий список начало
combo = Combobox(tab1, font=("Arial", 10), width=46, state = "readonly")
# combo['values'] = [item for result in results for item in result if item]
combo['values'] = valueName
# combo['values'] = row[1]
combo.current(0)  # установите вариант по умолчанию 
combo.grid(column=0, row=1, padx=10, pady=0)

# print(combo['values'])

# выпадающий список конец

idTitle = Label(tab1, text='Индивидуальный номер:', background="#eee", font=("Arial Bold", 10), padx=10, pady=5)
idTitle.grid(sticky = W, column=0, row=2)
idImg = Label(tab1, text='img', background="#eee")
idImg.grid(column=1, row=2)
idNum = Label(tab1, text = valueId, background="#eee")
idNum.grid(column=2, row=2)

sexTitle = Label(tab1, text='Пол:', background="#eee", font=("Arial Bold", 10), padx=10, pady=5)
sexTitle.grid(sticky = W, column=0, row=4)
sexRes = Label(tab1, text=valueSex, background="#eee")
sexRes.grid(column=1, row=4)

birthdayTitle = Label(tab1, text='Дата рождения:', background="#eee", font=("Arial Bold", 10), padx=10, pady=5)
birthdayTitle.grid(sticky = W, column=0, row=5)
birthdayRes = Label(tab1, text=valueBirth, background="#eee")
birthdayRes.grid(column=1, row=5)
age = Label(tab1, text='Полных лет:', background="#eee", font=("Arial Bold", 10), padx=10, pady=5)
age.grid(sticky = W, column=2, row=5)
ageRes = Label(tab1, text='23', background="#eee")
ageRes.grid(column=3, row=5)

groupTitle = Label(tab1, text='Референсная группа:', background="#eee", font=("Arial Bold", 10), padx=10, pady=5)
groupTitle.grid(sticky = W, column=0, row=6)
groupRes = Label(tab1, text='Жен', background="#eee")
groupRes.grid(column=1, row=6)

orderTitle = Label(tab1, text='№ заказа:', background="#eee", font=("Arial Bold", 10), padx=10, pady=5)
orderTitle.grid(sticky = W, column=0, row=7)
orderImg = Label(tab1, text='img2', background="#eee")
orderImg.grid(column=1, row=7)
orderNum = Label(tab1, text='1234567890', background="#eee")
orderNum.grid(column=2, row=7)

dataOrderTitle = Label(tab1, text='Дата заказа:', background="#eee", font=("Arial Bold", 10), padx=10, pady=5)
dataOrderTitle.grid(sticky = W, column=0, row=8)
dataOrderDay = Label(tab1, text="25/01/2021", background="#eee")
dataOrderDay.grid(column=1, row=8)
dataOrderTime = Label(tab1, text='08:12', background="#eee")
dataOrderTime.grid(column=2, row=8)

dataDeliveryTitle = Label(tab1, text='Дата доставки:', background="#eee", font=("Arial Bold", 10), padx=10, pady=5)
dataDeliveryTitle.grid(sticky = W, column=0, row=9)
dataDeliveryDay = Label(tab1, text="28/01/2021", background="#eee")
dataDeliveryDay.grid(column=1, row=9)
dataDeliveryTime = Label(tab1, text='09:20', background="#eee")
dataDeliveryTime.grid(column=2, row=9)

# кнопка начало
btnStart = Button(tab1, text="Создать справку", command=createDoc)
btnStart.grid(column=0, row=11, padx=0, pady=10)
# кнопка конец

# кнопка начало
def delUser():

    # удаляем пользователя начало
    cursor.execute("DELETE FROM users WHERE name = ?", (combo.get(),))
    conn.commit()
    # удаляем пользователя конец

    print(combo.get())

    cursorDel = conn.execute("SELECT name from users")
    results = cursorDel.fetchall()
    combo['values'] = [item for result in results for item in result if item]
    combo.current(0)

    messagebox.showinfo("COVID GENERATOR 69", "Пользователь удален")

btnDelUser = Button(tab1, text="Удалить пользователя", command=delUser)
btnDelUser.grid(column=1, row=11, padx=0, pady=10)
# кнопка конец

# создаем справку начало
doc = DocxTemplate("temp.docx")
context = { 
'fio' : combo.get(),
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
# doc.render(context)
# doc.save("Справка.docx")
# создаем справку конец

# tab 1 конец

# tab 2 начало
nameTitle2 = Label(tab2, text='ФИО', background="#eee", font=("Arial Bold", 10), padx=10, pady=5)
nameTitle2.grid(sticky = W, column=0, row=0)
# инпут начало
nameInp = Entry(tab2, width=36)
nameInp.grid(column=0, row=1, padx=10, pady=5)
# инпут конец

dateTitle2 = Label(tab2, text='Дата рождения:', background="#eee", font=("Arial Bold", 10), padx=10, pady=5)
dateTitle2.grid(sticky = W, column=0, row=2)
# инпут начало
dateInp = Entry(tab2, width=36)
dateInp.grid(column=0, row=3, padx=10, pady=5)
# инпут конец

idTitle2 = Label(tab2, text='ID', background="#eee", font=("Arial Bold", 10), padx=5, pady=5)
idTitle2.grid(sticky = W, column=0, row=4)
# инпут начало
idInp = Entry(tab2, width=36)
idInp.grid(column=0, row=5, padx=10, pady=5)
# инпут конец

# выпадающий список начало
sexTitle2 = Label(tab2, text='Пол:', background="#eee", padx=5, font=("Arial Bold", 10), pady=5)
sexTitle2.grid(sticky = W, column=0, row=6, padx=10, pady=5)
comboSex = Combobox(tab2, width=15, state = "readonly")
comboSex['values'] = ("МУЖСКОЙ", "ЖЕНСКИЙ")
comboSex.current(0)  # установите вариант по умолчанию  
comboSex.grid(sticky = W, column=0, row=7)
# выпадающий список конец

# добавляем пользователя по нажатию на кнопку начало
def clickedAdd():

    # добавляем пользователя начало
    # Вставляем множество данных в таблицу используя безопасный метод "?"
    users = [(nameInp.get().upper(), idInp.get(), dateInp.get(), comboSex.get().upper())]

    cursor.executemany("INSERT INTO users VALUES (?,?,?,?)", users)
    conn.commit()
    # добавляем пользователя конец

    cursorR = conn.execute("SELECT name from users")
    results = cursorR.fetchall()
    combo['values'] = [item for result in results for item in result if item]
    combo.current(0)

    nameInp.delete(0, 'end')
    idInp.delete(0, 'end')
    dateInp.delete(0, 'end')

    messagebox.showinfo("COVID GENERATOR 69", "Пользователь добавлен")

# кнопка начало
btnStart2 = Button(tab2, text="Добавить", command=clickedAdd)
btnStart2.grid(column=0, row=11)
# кнопка конец
# добавляем пользователя по нажатию на кнопку конец

# tab 2 конец

# # tab 3 конец
# nameTitle3 = Label(tab3, text='ФИО пациента:', background="#eee", padx=5, font=("Arial Bold", 10), pady=5)
# nameTitle3.grid(sticky = W, column=0, row=0)
# # выпадающий список начало
# comboName3 = Combobox(tab3, font=("Arial", 10), width=36, state = "readonly")
# comboName3['values'] = ("СОЛДАТКИН АЛЕКСЕЙ ВЛАДИМИРОВИЧ", "Женский")
# comboName3.current(0)  # установите вариант по умолчанию  
# comboName3.grid(column=0, row=1)
# # выпадающий список конец

# # кнопка начало
# btnStart3 = Button(tab3, text="Удалить", command=clicked)
# btnStart3.grid(column=0, row=3)
# # кнопка конец

# # tab 3 конец

tab_control.pack(expand=1, fill='both')
# вкладки конец

window.iconbitmap('icon.ico')
window.mainloop()