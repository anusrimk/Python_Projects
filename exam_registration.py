# Importing modules
from tkinter import ttk
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
import os
import mysql.connector


# Main Loop
# Setting up mysql
mydb = mysql.connector.connect(host='localhost', user='root', passwd='tiger', database='test')
cursor = mydb.cursor()
root = tk.Tk()
root.state("zoomed")

mydb = mysql.connector.connect(host='localhost', user='root', passwd='tiger', database='test')
cursor = mydb.cursor()

# Creating Labels
root.geometry("1350x750+0+0")
root.title("Exam Registration System")
root.configure(background='powder blue')

## FUNCTIONS
# Function for calculate cost
def calculate_cost():
    if len(list(str(aadhar_num.get())))!=12:
        messagebox.showwarning("Error","Please enter valid Aadhar Card Number")

    elif len(list(str(phone_num.get())))!=10:
        messagebox.showwarning("Error","Please enter valid Mobile Number")

    elif len(list(str(pin_code.get())))!=6:
        messagebox.showwarning("Error","Please enter valid Pin Code")
        
    else:
        fees_exam()
        messagebox.showinfo("Success","Registration Successful")

def fees_exam():
    # JEE FOR BOYS GENERAL CATEGORY 
    if exam_type.get() =='JEE' and gender_type.get() =='Male' and category_type .get() == 'General':
        total_cost.set(650)

    # JEE FOR BOYS OBC CATEGORY 
    elif exam_type.get() == 'JEE' and gender_type.get() == 'Male' and category_type .get() ==  'OBC':
        total_cost.set(650)

    # JEE FOR BOYS SC/ST CATEGORY 
    elif exam_type.get() =='JEE'  and gender_type.get() =='Male'  and category_type.get() == 'SC/ST':
        total_cost.set(325)

    # JEE FOR GIRLS GENERAL CATEGORY 
    elif exam_type.get() == 'JEE'  and gender_type.get() =='Female' and category_type.get() ==  'General':
        total_cost.set(325)

    # JEE FOR GIRLS OBC CATEGORY 
    elif exam_type.get() == 'JEE'  and gender_type.get() =='Female' and category_type .get() ==  'OBC':
         total_cost.set(325)

    # JEE FOR GIRLS SC/ST CATEGORY 
    elif exam_type.get() == 'JEE'  and gender_type.get() =='Female' and category_type.get() == 'SC/ST':
        total_cost.set(325)

    # NEET FOR BOYS GENERAL CATEGORY 
    elif exam_type.get() == 'NEET' and gender_type.get() =='Male' and category_type.get() ==  'General':
        total_cost.set(1600)

    # NEET FOR BOYS OBC CATEGORY 
    elif exam_type.get() == 'NEET' and gender_type.get() =='Male' and category_type.get() ==  'OBC':
        total_cost.set(1500)

    # NEET FOR BOYS SC/ST CATEGORY 
    elif exam_type.get() == 'NEET' and gender_type.get() =='Male' and category_type.get() == 'SC/ST':
        total_cost.set(900)

    # NEET FOR GIRLS GENERAL CATEGORY 
    elif exam_type.get() == 'NEET' and gender_type.get() =='Female' and category_type.get() ==  'General':
        total_cost.set(1600)

    # NEET FOR GIRLS OBC CATEGORY 
    elif exam_type.get() == 'NEET' and gender_type.get() =='Female' and category_type.get() ==  'OBC':
        total_cost.set(1500)

    # NEET FOR GIRLS SC/ST CATEGORY 
    elif exam_type.get() == 'NEET' and gender_type.get() =='Female' and category_type.get() == 'SC/ST':
        total_cost.set(900)

    #SAT FOR BOYS GENERAL CATEGORY 
    elif exam_type.get() == 'SAT' and gender_type.get() =='Male' and category_type.get() ==  'General':
        total_cost.set(8500)

    #SAT FOR BOYS OBC CATEGORY 
    elif exam_type.get() == 'SAT' and gender_type.get() =='Male' and category_type.get() ==  'OBC':
        total_cost.set(8500)

    #SAT FOR BOYS SC/ST CATEGORY 
    elif exam_type.get() == 'SAT' and gender_type.get() =='Male' and category_type.get() == 'SC/ST':
        total_cost.set(8500)

    #SAT FOR GIRLS GENERAL CATEGORY 
    elif exam_type.get() == 'SAT' and gender_type.get() =='Female' and category_type.get() ==  'General':
        total_cost.set(8500)

    #SAT FOR GIRLS OBC CATEGORY 
    elif exam_type.get() == 'SAT' and gender_type.get() =='Female' and category_type.get() ==  'OBC':
        total_cost.set(8500)

    #SAT FOR GIRLS SC/ST CATEGORY 
    elif exam_type.get() == 'SAT' and gender_type.get() =='Female' and category_type.get() == 'SC/ST':
        total_cost.set(8500)

    #CET FOR BOYS GENERAL CATEGORY 
    elif exam_type.get() == 'CET' and gender_type.get() =='Male' and category_type.get() ==  'General':
        total_cost.set(800)

    #CET FOR BOYS OBC CATEGORY 
    elif exam_type.get() == 'CET' and gender_type.get() =='Male' and category_type.get() ==  'OBC':
        total_cost.set(600)

    #CET FOR BOYS SC/ST CATEGORY 
    elif exam_type.get() == 'CET' and gender_type.get() =='Male' and category_type.get() == 'SC/ST':
        total_cost.set(600)

    #CET FOR GIRLS GENERAL CATEGORY 
    elif exam_type.get() == 'CET' and gender_type.get() =='Female' and category_type.get() ==  'General':
        total_cost.set(800)

    #CET FOR GIRLS OBC CATEGORY 
    elif exam_type.get() == 'CET' and gender_type.get() =='Female' and category_type.get() ==  'OBC':
        total_cost.set(600)

    #CET FOR GIRLS SC/ST CATEGORY 
    elif exam_type.get() == 'CET' and gender_type.get() =='Female' and category_type.get() == 'SC/ST':
        total_cost.set(600)

    #BIT SAT FOR BOYS GENERAL CATEGORY 
    elif exam_type.get() == 'BIT SAT' and gender_type.get() =='Male' and category_type.get() ==  'General':
        total_cost.set(3400)

    #BIT SAT FOR BOYS OBC CATEGORY 
    elif exam_type.get() ==  'BIT SAT'  and gender_type.get() =='Male' and category_type.get() ==  'OBC':
        total_cost.set(3400)

    #BIT SAT FOR BOYS SC/ST CATEGORY 
    elif exam_type.get() ==  'BIT SAT'  and gender_type.get() =='Male' and category_type.get() == 'SC/ST':
        total_cost.set(3400)

    #BIT SAT FOR GIRLS GENERAL CATEGORY 
    elif exam_type.get() ==  'BIT SAT'  and gender_type.get() =='Female' and category_type.get() ==  'General':
        total_cost.set(2900)

    #BIT SAT FOR GIRLS OBC CATEGORY 
    elif exam_type.get() ==  'BIT SAT'  and gender_type.get() =='Female' and category_type.get() == 'OBC':
        total_cost.set(2900)

    #BIT SAT FOR GIRLS SC/ST CATEGORY 
    elif exam_type.get() ==  'BIT SAT'  and gender_type.get() =='Female' and category_type.get() == 'SC/ST':
        total_cost.set(2900)

    # This function is for printing of receipt and MySQL integration
def see_reciept():
    if not cand_name.get():
        messagebox.showwarning("Error", "Some Entry is left unfilled")

    elif not father_name.get():
        messagebox.showwarning("Error", "Some Entry is left unfilled")

    elif not mother_name.get():
        messagebox.showwarning("Error", "Some Entry is left unfilled")

    elif not aadhar_num.get():
        messagebox.showwarning("Error", "Some Entry is left unfilled")

    elif nationality.get()=='Select':
        messagebox.showwarning("Error", "Some Entry is left unfilled")

    elif not address_cur.get():
        messagebox.showwarning("Error", "Some Entry is left unfilled")

    elif not residence_place.get():
        messagebox.showwarning("Error", "Some Entry is left unfilled")

    elif not city_name.get():
        messagebox.showwarning("Error", "Some Entry is left unfilled")

    elif not district_name.get():
        messagebox.showwarning("Error", "Some Entry is left unfilled")

    elif not state_name.get():
        messagebox.showwarning("Error", "Some Entry is left unfilled")

    elif not pin_code.get():
        messagebox.showwarning("Error", "Some Entry is left unfilled")

    elif not email_add.get():
        messagebox.showwarning("Error", "Some Entry is left unfilled")

    elif not phone_num.get():
        messagebox.showwarning("Error", "Some Entry is left unfilled")

    elif not pass_status_10.get():
        messagebox.showwarning("Error", "Some Entry is left unfilled")

    elif not name_exam_10.get():
        messagebox.showwarning("Error", "Some Entry is left unfilled")

    elif not school_board_10.get():
        messagebox.showwarning("Error", "Some Entry is left unfilled")

    elif not pass_year_10.get():
        messagebox.showwarning("Error", "Some Entry is left unfilled")

    elif not pass_status_12.get():
        messagebox.showwarning("Error", "Some Entry is left unfilled")

    elif not name_exam_12.get():
        messagebox.showwarning("Error", "Some Entry is left unfilled")

    elif not school_board_12.get():
        messagebox.showwarning("Error", "Some Entry is left unfilled")

    elif not pass_year_12.get():
        messagebox.showwarning("Error", "Some Entry is left unfilled")

    elif not mod_pay.get():
        messagebox.showwarning("Error", "Please select a mode of payment")

    else:
        # Declaration of variables to be used in tables
        root2 = Tk()
        root2.title("Exam Registration")
        root2.geometry("350x300")
        cand_name_table = cand_name.get()
        father_name_table = father_name.get()
        mother_name_table = mother_name.get()
        aadhar_card_num = aadhar_num.get()
        natio_table=nationality.get()
        address_cur_table=address_cur.get()
        residence_place_table=residence_place.get()
        city_name_table=city_name.get()
        district_name_table=district_name.get()
        state_name_table=state_name.get()
        pin_code_table=pin_code.get()
        email_add_table=email_add.get()
        phone_num_table=phone_num.get()
        pass_status_10_table=pass_status_10.get()
        name_exam_10_table=name_exam_10.get()
        school_board_10_table=school_board_10.get()
        pass_year_10_table=pass_year_10.get()
        pass_status_12_table=pass_status_12.get()
        name_exam_12_table=name_exam_12.get()
        school_board_12_table=school_board_12.get()
        pass_year_12_table=pass_year_12.get()
        mod_pay_table=mod_pay.get()
        ge_type=gender_type.get()
        ca_type=category_type.get()
        ex_type=exam_type.get()

        
        # Command for inserting the values into Table
        statement = '''INSERT INTO examregister(CANDIDATE_NAME,FATHER_NAME,MOTHER_NAME,AADHAR_NUMBER,NATIONALITY,GENDER_TYPE,CATEGORY_TYPE,
EXAM_TYPE,CURRENT_ADDRESS,RESIDENCE_PLACE,CITY_NAME,DISTRICT_NAME,STATE_NAME,PIN_CODE,EMAIL_ADDRESS,PHONE_NUMBER,PASS_STATUS_10,
NAME_EXAM_10,SCHOOL_BOARD_10,PASS_YEAR_10,PASS_STATUS_12,NAME_EXAM_12,SCHOOL_BOARD_12,PASS_YEAR_12,MOD_PAYMENT)
values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''


        #Inserting the values
        values=(
        cand_name_table, father_name_table, mother_name_table, aadhar_card_num, natio_table, ge_type, ca_type, ex_type,address_cur_table, residence_place_table, city_name_table, district_name_table,
        state_name_table, pin_code_table, email_add_table, phone_num_table,pass_status_10_table, name_exam_10_table, school_board_10_table, pass_year_10_table, pass_status_12_table,
        name_exam_12_table, school_board_12_table, pass_year_12_table, mod_pay_table)

        cursor.execute(statement, values)
        mydb.commit()


        #Adding titles for the values
        cand_name_table = 'Name of Candidate:' + cand_name.get()
        father_name_table ='Name of Father:' + father_name.get()
        mother_name_table = 'Name of Mother:' + mother_name.get()
        aadhar_card_num = 'Aadhar Card Number:' + aadhar_num.get()
        natio_table='Nationality:' + nationality.get()
        ge_type='Gender:' +ge_type
        ca_type='Category:' +ca_type
        ex_type='Exam Name:' +ex_type
        address_cur_table='Current Address:' + address_cur.get()
        residence_place_table='Place of Residence:' + residence_place.get()
        city_name_table='City Name:' + city_name.get()
        district_name_table='District Name:' + district_name.get()
        state_name_table='State Name:' + state_name.get()
        pin_code_table='Pin Code:' + pin_code.get()
        email_add_table='Email Address:' + email_add.get()
        phone_num_table='Phone Number:' + phone_num.get()
        pass_status_10_table='Pass Status of Class 10:' + pass_status_10.get()
        name_exam_10_table='Name of Class 10 Exam:' + name_exam_10.get()
        school_board_10_table='Class 10 School Board:' + school_board_10.get()
        pass_year_10_table='Passing Year of Class 10:' + pass_year_10.get()
        pass_status_12_table='Pass Status of Class 12:' + pass_status_12.get()
        name_exam_12_table='Name of Class 12 Exam:' + name_exam_12.get()
        school_board_12_table='Class 12 School Board:' + school_board_12.get()
        pass_year_12_table='Passing/Appearing Year of Class 12:' + pass_year_12.get()
        mod_pay_table='Mode of Payment:' + mod_pay.get()

        #Second window after registration

        title = Label(root2, text="Registration Details", font=('Calibri', 16, 'bold'))
        title.grid(row=0, column=0, columnspan=1)

        #Personal Details section

        Label(root2, text=cand_name_table, font=('Calibri', 13)).grid(row=1, column=0, sticky='nw')
        Label(root2, text=father_name_table, font=('Calibri', 13)).grid(row=1, column=1, sticky='nw')
        Label(root2, text=mother_name_table, font=('Calibri', 13)).grid(row=1, column=2, sticky='nw')
        Label(root2, text=aadhar_card_num, font=('Calibri', 13)).grid(row=1, column=3, sticky='nw')
        Label(root2, text=natio_table, font=('Calibri', 13)).grid(row=2, column=0, sticky='nw')
        Label(root2, text=ge_type, font=('Calibri', 13)).grid(row=2, column=1, sticky='nw')
        Label(root2, text=ca_type, font=('Calibri', 13)).grid(row=2, column=2, sticky='nw')
        Label(root2, text=ex_type, font=('Calibri', 13)).grid(row=2, column=3, sticky='nw')
        Label(root2, text=mod_pay_table, font=('Calibri', 13)).grid(row=7, column=0, sticky='nw')


        #Contact Details section
        Label(root2, text=address_cur_table, font=('Calibri', 13)).grid(row=3, column=0, sticky='nw')
        Label(root2, text=residence_place_table, font=('Calibri', 13)).grid(row=3, column=1, sticky='nw')
        Label(root2, text=city_name_table, font=('Calibri', 13)).grid(row=3, column=2, sticky='nw')
        Label(root2, text=district_name_table, font=('Calibri', 13)).grid(row=3, column=3, sticky='nw')
        Label(root2, text=state_name_table, font=('Calibri', 13)).grid(row=4, column=0, sticky='nw')
        Label(root2, text=pin_code_table, font=('Calibri', 13)).grid(row=4, column=1, sticky='nw')
        Label(root2, text=email_add_table, font=('Calibri', 13)).grid(row=4, column=2, sticky='nw')
        Label(root2, text=phone_num_table, font=('Calibri', 13)).grid(row=4, column=3, sticky='w')


        #Academic Details section
        Label(root2, text=pass_status_10_table, font=('Calibri', 13)).grid(row=5, column=0, sticky='nw')
        Label(root2, text=name_exam_10_table, font=('Calibri', 13)).grid(row=5, column=1, sticky='nw')
        Label(root2, text=school_board_10_table, font=('Calibri', 13)).grid(row=5, column=2, sticky='nw')
        Label(root2, text=pass_year_10_table, font=('Calibri', 13)).grid(row=5, column=3, sticky='nw')
        
        Label(root2, text=pass_status_12_table, font=('Calibri', 13)).grid(row=6, column=0, sticky='nw')
        Label(root2, text=name_exam_12_table, font=('Calibri', 13)).grid(row=6, column=1, sticky='nw')
        Label(root2, text=school_board_12_table, font=('Calibri', 13)).grid(row=6, column=2, sticky='nw')
        Label(root2, text=pass_year_12_table, font=('Calibri', 13)).grid(row=6, column=3, sticky='nw')

        # Resizing
        for row in range(0, 8):
            Grid.rowconfigure(root2, row, weight=1)
        for col in range(0, 9):
            Grid.columnconfigure(root2, col, weight=1)

#Frame1=Personal Details
title = Label(root, text='Exam Registration System', font=("Arial", 20, 'bold'))
title.grid(row=0, column=0, columnspan=3, padx=600, pady=20)
details = LabelFrame(root, text="Enter Personal Details:", padx=5, pady=5, font=("Arial", 13, 'bold'))
details.grid(row=1, column=0, sticky=NW, padx=5, columnspan=2)

labels_frame = Frame(details)
labels_frame.pack(expand=True, fill='both', side=LEFT)

entries_frame = Frame(details)
entries_frame.pack(expand=True, fill='both', side=RIGHT)

can_name = Label(labels_frame, text='Name of Candidate:', font=("Calibri", 13))
can_name.pack(pady=(20,0), expand=True, fill='both')

fa_name = Label(labels_frame, text='Name of Father:', font=("Calibri", 13))
fa_name.pack(pady=(20,0), expand=True, fill='both')

mo_name = Label(labels_frame, text='Name of Mother:', font=("Calibri", 13))
mo_name.pack(pady=(20,0), expand=True, fill='both')

aa_num = Label(labels_frame, text='Aadhar Card Number:', font=("Calibri", 13))
aa_num.pack(pady=(20,0), expand=True, fill='both')

na_lity = Label(labels_frame, text='Nationality:', font=("Calibri", 13))
na_lity.pack(pady= (20,0), expand=True, fill='both')

ge_type = Label(labels_frame, text='Gender:', font=("Calibri", 13))
ge_type.pack(pady=(20,0), expand=True, fill='both')

ca_type = Label(labels_frame, text='Category:', font=("Calibri", 13))
ca_type.pack(pady=(20,0), expand=True, fill='both')

ex_type = Label(labels_frame, text='Exam Name:', font=("Calibri", 13))
ex_type.pack(pady=(20,0), expand=True, fill='both')

mod_type = Label(labels_frame, text='Mode of Payment:', font=("Calibri", 13))
mod_type.pack(pady=(20,0), expand=True, fill='both')

# Entries for the person to input his data
cand_name = Entry(entries_frame)
cand_name.pack(expand=True, fill='both', pady=(20,10))

father_name = Entry(entries_frame)
father_name.pack(expand=True, fill='both', pady=(20,20))

mother_name = Entry(entries_frame)
mother_name.pack(expand=True, fill='both', pady=(15,30))

aadhar_num = Entry(entries_frame)
aadhar_num.pack(expand=True, fill='both', pady=(5,25))

nationality = Entry(entries_frame)
nationality.pack(expand=True, fill='both', pady=(10,10))


#Drop Down Boxes
gender_type= StringVar()
category_type= StringVar()
exam_type= StringVar()
mod_pay= StringVar()

gender_type.set('Select')
category_type.set('Select')
exam_type.set('Select')
mod_pay.set('Select')


drop_menu1 = OptionMenu(entries_frame, gender_type, "Male","Female")
drop_menu1.pack(pady=(20,0))

drop_menu2 = OptionMenu(entries_frame, category_type, "General","OBC","SC/ST")
drop_menu2.pack(pady=(20,0))

drop_menu3 = OptionMenu(entries_frame, exam_type, "JEE","NEET","SAT","CET","BIT SAT")
drop_menu3.pack(pady=(20,0))

drop_menu4 = OptionMenu(entries_frame, mod_pay, "Credit Card","Debit Card","Google Pay","UPI")
drop_menu4.pack(pady=(20,0))

#Frame2=Contact Details
details1 = LabelFrame(root, text="Enter Contact Details:", padx=5, pady=5, font=("Arial", 13, 'bold'))
details1.grid(row=1, column=1, sticky=NW, padx=5, columnspan=2)

labels_frame1 = Frame(details1)
labels_frame1.pack(expand=True, fill='both', side=LEFT)

entries_frame1 = Frame(details1)
entries_frame1.pack(expand=True, fill='both', side=RIGHT)

address_cur = Label(labels_frame1, text='Current Address:', font=("Calibri", 13))
address_cur.pack(pady=(20,0), expand=True, fill='both')

residence_place = Label(labels_frame1, text='Place of Residence:', font=("Calibri", 13))
residence_place.pack(pady=(20,0), expand=True, fill='both')

city_name= Label(labels_frame1, text='City Name:', font=("Calibri", 13))
city_name.pack(pady=(20,0), expand=True, fill='both')

district_name= Label(labels_frame1, text='District Name:', font=("Calibri", 13))
district_name.pack(pady=(20,0), expand=True, fill='both')

state_name = Label(labels_frame1, text='State Name:', font=("Calibri", 13))
state_name.pack(pady=(20,0), expand=True, fill='both')

pin_code= Label(labels_frame1, text='Pin Code:', font=("Calibri", 13))
pin_code.pack(pady=(20,0), expand=True, fill='both')

email_add = Label(labels_frame1, text='Email Address:', font=("Calibri", 13))
email_add.pack(pady=(20,0), expand=True, fill='both')

phone_num= Label(labels_frame1, text='Phone Number:', font=("Calibri", 13))
phone_num.pack(pady=(20,0), expand=True, fill='both')

# Entries for the person to input his data
address_cur = Entry(entries_frame1)
address_cur .pack(expand=True, fill='both', pady=20)

residence_place = Entry(entries_frame1)
residence_place .pack(expand=True, fill='both', pady=20)

city_name = Entry(entries_frame1)
city_name .pack(expand=True, fill='both', pady=20)

district_name = Entry(entries_frame1)
district_name.pack(expand=True, fill='both', pady=20)

state_name = Entry(entries_frame1)
state_name .pack(expand=True, fill='both', pady=20)

pin_code = Entry(entries_frame1)
pin_code .pack(expand=True, fill='both', pady=20)

email_add = Entry(entries_frame1)
email_add .pack(expand=True, fill='both', pady=20)

phone_num = Entry(entries_frame1)
phone_num .pack(expand=True, fill='both', pady=20)

#Frame3=Academic Details
details2 = LabelFrame(root, text="Enter Academic Details:", padx=5, pady=5, font=("Arial", 13, 'bold'))
details2.grid(row=1, column=2, sticky=NW, padx=5, columnspan=2)

labels_frame2 = Frame(details2)
labels_frame2.pack(expand=True, fill='both', side=LEFT)

entries_frame2 = Frame(details2)
entries_frame2.pack(expand=True, fill='both', side=RIGHT)

pass_status_10= Label(labels_frame2, text='Pass Status of Class 10:', font=("Calibri", 13))
pass_status_10.pack(pady=(20,0), expand=True, fill='both')

name_exam_10= Label(labels_frame2, text='Name of Class 10 Exam:', font=("Calibri", 13))
name_exam_10.pack(pady=(20,0), expand=True, fill='both')

school_board_10= Label(labels_frame2, text='Class 10 School Board:', font=("Calibri", 13))
school_board_10.pack(pady=(20,0), expand=True, fill='both')

pass_year_10= Label(labels_frame2, text='Passing Year of Class 10:', font=("Calibri", 13))
pass_year_10.pack(pady=(20,0), expand=True, fill='both')

pass_status_12= Label(labels_frame2, text='Pass/Appearing Status of Class 12:', font=("Calibri", 13))
pass_status_12.pack(pady=(20,0), expand=True, fill='both')

name_exam_12= Label(labels_frame2, text='Name of Class 12 Exam:', font=("Calibri", 13))
name_exam_12.pack(pady=(20,0), expand=True, fill='both')

school_board_12= Label(labels_frame2, text='Class 12 School Board:', font=("Calibri", 13))
school_board_12.pack(pady=(20,0), expand=True, fill='both')

pass_year_12= Label(labels_frame2, text='Passing/Appearing Year of Class 12:', font=("Calibri", 13))
pass_year_12.pack(pady=(20,0), expand=True, fill='both')

# Entries for the person to input his data
pass_status_10 = Entry(entries_frame2)
pass_status_10 .pack(expand=True, fill='both', pady=20)

name_exam_10= Entry(entries_frame2)
name_exam_10 .pack(expand=True, fill='both', pady=20)

school_board_10 = Entry(entries_frame2)
school_board_10 .pack(expand=True, fill='both', pady=20)

pass_year_10 = Entry(entries_frame2)
pass_year_10.pack(expand=True, fill='both', pady=20)

pass_status_12 = Entry(entries_frame2)
pass_status_12.pack(expand=True, fill='both', pady=20)

name_exam_12= Entry(entries_frame2)
name_exam_12.pack(expand=True, fill='both', pady=20)

school_board_12= Entry(entries_frame2)
school_board_12.pack(expand=True, fill='both', pady=20)

pass_year_12= Entry(entries_frame2)
pass_year_12.pack(expand=True, fill='both', pady=20)

#Frame4=Cost
total_cost = StringVar()
sit_1 = StringVar()

# Function for setting up for costs of Different Combinations, command for button Calculate Fee


# Labels and Entry
cost_details = LabelFrame(root, text="Exam Fees:", padx=5, pady=5, font=("Arial", 13, 'bold'))
cost_details.grid(row=2, column=2, sticky=NW, padx=5)

total_cost_label = Label(cost_details, text="Total:", font=("Calibri", 13))
total_cost_label.grid(row=0, column=0, pady=15, sticky='e', padx=15)

total_cost_entry = Label(cost_details, textvariable=total_cost, font=("Arial", 13, 'bold'))
total_cost_entry.grid(row=0, column=1, pady=31, sticky='w')

# Calculate Fees button
see_cost = Button(cost_details, text="Calculate Fees", command=calculate_cost,width=25)
see_cost.grid(row=1, column=0, columnspan=2)

# Function for creating a table called examregister
def create_table():
    statement = '''CREATE TABLE examregister
    (CANDIDATE_NAME CHAR(50),
    FATHER_NAME CHAR(50),
    MOTHER_NAME CHAR(50),
    AADHAR_NUMBER VARCHAR(100),
    NATIONALITY CHAR(20),
    GENDER_TYPE CHAR(20),
    CATEGORY_TYPE CHAR(20),
    EXAM_TYPE CHAR(20),
    CURRENT_ADDRESS VARCHAR(100),
    RESIDENCE_PLACE VARCHAR(100),
    CITY_NAME CHAR(40),
    DISTRICT_NAME CHAR(40),
    STATE_NAME CHAR(40),
    PIN_CODE VARCHAR(50),
    EMAIL_ADDRESS VARCHAR(50),
    PHONE_NUMBER VARCHAR(50),
    PASS_STATUS_10 CHAR(20),
    NAME_EXAM_10 CHAR(20),
    SCHOOL_BOARD_10 CHAR(20),
    PASS_YEAR_10 VARCHAR(50),
    PASS_STATUS_12 CHAR(20),
    NAME_EXAM_12 CHAR(20),
    SCHOOL_BOARD_12 CHAR(20),
    PASS_YEAR_12 VARCHAR(50),
    MOD_PAYMENT CHAR(20)

    )'''

    cursor.execute(statement)
    mydb.commit()

# Command for showing the tables to be used for checking if examregister table exists
cursor.execute('SHOW TABLES')

all_tables = cursor.fetchall()  # Fetching of all tables, to check whether examregister exists
# Checks whether examregister is created or not and stores its existence into some form of variables
for table in all_tables:

    if table[0] == 'examregister':
        exists = True
        break
else:
    exists = False
# Uses that variable and creates the table if not created
if not exists:
    create_table()

def retrive_data():
    # Currently all widgets are packed
    root1 = Tk()
    root1.title("Exam Register")
    global tree
    Label(root1, text="Exam Registration Database", font=('Arial',15,'bold')).pack(pady=10)
    tree = ttk.Treeview(root1)
    tree.pack(padx=5)
    tree["columns"] = ("one", "two", "three", 'four', 'five', 'six', 'seven','eight', 'nine', 'ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty',
                       'twentyone','twentytwo','twentythree','twentyfour')
    tree.column('#0', width=100)
    tree.column("one", width=100)
    tree.column("two", width=100)
    tree.column("three", width=100)
    tree.column("four", width=100)
    tree.column("five", width=100)
    tree.column("six", width=100)
    tree.column("seven", width=100)
    tree.column("eight", width=100)
    tree.column("nine", width=100)
    tree.column("ten", width=100)
    tree.column("eleven", width=100)
    tree.column("twelve", width=100)
    tree.column("thirteen", width=100)
    tree.column("fourteen", width=100)
    tree.column("fifteen", width=100)
    tree.column("sixteen", width=100)
    tree.column("seventeen", width=100)
    tree.column("eighteen", width=100)
    tree.column("nineteen", width=100)
    tree.column("twenty", width=100)
    tree.column("twentyone", width=100)
    tree.column("twentytwo", width=100)
    tree.column("twentythree", width=100)
    tree.column("twentyfour", width=100)
    

    tree.heading('#0', text='Name of Candidate:')
    tree.heading("one", text='Name of Father:')
    tree.heading("two", text='Name of Mother:')
    tree.heading("three", text='Aadhar Card Number:')
    tree.heading("four", text='Nationality:')
    tree.heading("five", text='Gender:')
    tree.heading("six", text='Category:')
    tree.heading("seven", text='Exam Name:')
    tree.heading("eight", text='Current Address:')
    tree.heading("nine", text='Place of Residence:')
    tree.heading("ten", text='City Name:')
    tree.heading("eleven", text='District Name:')
    tree.heading("twelve", text='State Name:')
    tree.heading("thirteen", text='Pin Code:')
    tree.heading("fourteen", text='Email Address:')
    tree.heading("fifteen", text='Phone Number:')
    tree.heading("sixteen", text='Pass Status of Class 10:')
    tree.heading("seventeen", text='Name of Class 10 Exam:')
    tree.heading("eighteen", text='Class 10 School Board:')
    tree.heading("nineteen", text='Passing Year of Class 10:')
    tree.heading("twenty", text='Pass Status of Class 12:')
    tree.heading("twentyone", text='Name of Class 12 Exam:')
    tree.heading("twentytwo", text='Class 12 School Board:')
    tree.heading("twentythree", text='Passing/Appearing Year of Class 12:')
    tree.heading("twentyfour", text='Mode of Payment:')

    cursor.execute(
        ''' SELECT * FROM examregister ''')
    record = cursor.fetchall()  # Fetches all the data about the ticket/receipt

    # Prints all the information
    for row in record:
        tree.insert("", 'end', text=row[0],
                    values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],
                            row[21],row[22],row[23],row[24]))


# See Receipt button
see_details = Button(root, text="Register", command=see_reciept, width=20)
see_details.grid(row=3, column=0, padx=40, columnspan=2)

# Function for the button retrieve_data, this fucntion opens up a new window
search_existing = Button(root, text="Show Registration", command=retrive_data, width=20)
search_existing.grid(row=3, column=2, pady=20)

root.mainloop()