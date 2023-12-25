#Importingrequiredmodules
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Style
import mysql.connector
import datetime
import calendar
import os
import sys

def log_in():
    global mydb,logged_in
    host=log_host_txtbx.get()
    user=log_user_txtbx.get()
    db=log_db_txtbx.get()
    passwd=log_passwd_txtbx.get()

try:
    mydb=mysql.connector.connect(host=host,user=user,
    passwd=passwd,database=db)
    logged_in=True
    login_window.destroy()
    #Savelogininfoifsuccessful
    myfile=open('mysql_database.txt',mode='w')
    data=[str(remember_var.get()),host,user,db,passwd]
    for i in data:
        myfile.write(i+'\n')
    myfile.close()
except Exceptionase:
    message='Invalidlogininformation.\n\nThefollowingerroroccurred:\n\n'
    +str(e)
    messagebox.showerror('LoginError',message)
def see_pass():
    if log_passwd_txtbx['show']:
        log_passwd_txtbx.configure(show='')
    else:
        log_passwd_txtbx.configure(show='*')
def enter_default():
    log_host_txtbx.insert(0,'localhost')
    log_user_txtbx.insert(0,'root')
    log_db_txtbx.insert(0,'test')
    log_passwd_txtbx.insert(0,'')
#Loginwindow
logged_in=False
login_window=Tk()
screen_width=int(login_window.winfo_screenwidth()/2)
screen_height=int(login_window.winfo_screenheight()/2)
login_window.title("Login")
login_window.geometry('240x200+'+str(screen_width-120)+'+'+str(screen_height-100))
log_mssg='''PleaselogintoyourMySQLdatabase.'''
log_lbl=Label(login_window,text=log_mssg)
log_lbl.pack(pady=5)

mygrid=Frame(login_window)
mygrid.pack()

log_host=Label(mygrid,text='Host:',font=("ComicSansMS",11,"bold"))
log_host.grid(row=1,column=0,sticky='e',padx=3)
log_host_txtbx=Entry(mygrid)
log_host_txtbx.grid(row=1,column=1,sticky='nsew',pady=1)
log_user=Label(mygrid,text='User:',font=("ComicSansMS",11,"bold"))
log_user.grid(row=2,column=0,sticky='e')
log_user_txtbx=Entry(mygrid)
log_user_txtbx.grid(row=2,column=1,sticky='nsew',pady=1)
log_db=Label(mygrid,text='Database:',font=("ComicSansMS",11,"bold"))
log_db.grid(row=3,column=0,sticky='e')
log_db_txtbx=Entry(mygrid)
log_db_txtbx.grid(row=3,column=1,sticky='nsew',pady=1)
log_passwd=Label(mygrid,text='Password:',font=("ComicSansMS",11,"bold"))
log_passwd.grid(row=4,column=0,sticky='e')
log_passwd_txtbx=Entry(mygrid,show='*')
log_passwd_txtbx.grid(row=4,column=1,sticky='nsew',pady=1)
eye_bt=Button(mygrid,text=chr(128065),command=see_pass)
eye_bt.grid(row=4,column=1,sticky='e')
remember_var=IntVar()
remember_var.set(1)
remember_me=Checkbutton(mygrid,text="Rememberme",variable=remember_var)
remember_me.grid(row=5,column=1,sticky='w')
log_button=Button(login_window,width=10,text='Login',command=log_in)
log_button.pack()
#
if os.path.exists('to_do_list_data.txt'):
    myfile=open('to_do_list_data.txt',mode='r')
    data=myfile.readlines()
    txt_bx_list=[log_host_txtbx,log_user_txtbx,log_db_txtbx,
    log_passwd_txtbx]
    if data[0].strip()=='1':
        for i in range(4):
            txt_bx_list[i].insert(0,data[i+1].strip())
    else:
        enter_default()
        myfile.close()
else:
    enter_default()
login_window.mainloop()

if notlogged_in:
#dontopenwindow
    sys.exit()
#Settingupmysql
cursor=mydb.cursor()
#CreatingWindow
main=Tk()
#GettingCheckboxImages
try:
    unchecked_pic=PhotoImage(file='Unchecked.png')
    checked_pic=PhotoImage(file='Checked.png')
    tristate_pic=PhotoImage(file='Tristate.png')
except:
    main.withdraw()#Don'tCreatewindowiferroroccurs
    message='Error:Image(s)notFoundinthesamedirectoryas.pyfile.\n'\
        'Fix:Keeptheimages-Unchecked.png,Checked.pngandTristate.png
provided,
        in the same'\
        'directory as the.py file.' 
    messagebox.showerror('Image(s)Not Found',message)

    sys.exit()
#Settingupwindowsize,titleandscreenplacement
main.title("ToDoListManager")
main.geometry('1050x600+'+str(screen_width-525)+'+'+str(screen_height-325))
#Variables
Today_datetime=datetime.date.today()#Datetimeformoftoday'sdate
Today_str=Today_datetime.strftime(format='%d/%m/%Y')#Stringformoftoday's
date
#Variablesforprioritymenu
PriorityList=['Highest','High','Medium','Low','Lowest']
PriorityVar=StringVar()
PriorityVar2=StringVar()
PriorityVar.set(PriorityList[2])
PriorityVar2.set(PriorityList[2])
#Variabletoswitchbetweenaddingtaskandsubtask
AddTypeVar=IntVar()
AddTypeVar.set(1)
#Alistforalltasks
TaskList=[]
#Functionsrelatedtocheckboxtreeview
#Additionalfunctionalitytotreeviewsothateachrowworksasacheckboxbetween3
state-checked,unchecked
#andtristate(whennotallchildrenarechecked)
defget_checked():
#Returnsthelistofcheckeditemsthatdonothaveanychild.
checked=[]
def get_checked_children(item):
    if nottree.tag_has("unchecked",item):
        ch=tree.get_children(item)
        if notchandtree.tag_has("checked",item):
            checked.append(item)
        else:
            for c in ch:
                get_checked_children(c)
ch=tree.get_children("")
for c in ch:
    get_checked_children(c)
return checked
def change_state(item,state):
#Replacethecurrentstateoftheitem.
    tags=tree.item(item,"tags")
    states=("checked","unchecked","tristate")
    new_tags=[]
    for t in tags:
        if t not in states:
            new_tags.append(t)
    new_tags.append(state)
    tree.item(item,tags=tuple(new_tags))
    
def tag_add(item,tag):
    tags=tree.item(item,"tags")
    tree.item(item,tags=tags+(tag,))
    
def tag_del(item,tag):
    tags=list(tree.item(item,"tags"))
    if tag in tags:
        tags.remove(tag)
        tree.item(item,tags=tuple(tags))
def check_descendant(item):
#Checktheboxesofitem'sdescendants.
    children=tree.get_children(item)
    for iid in children:
        change_state(iid,"checked")
        check_descendant(iid)
def check_ancestor(item):
#Checktheboxofitemandchangethestateoftheboxesofitem'sancestors
#accordingly.
    change_state(item,"checked")
    parent=tree.parent(item)
    if parent:
        children=tree.get_children(parent)
        b=[]
        for c in children:
            if'checked'intree.item(c,'tags'):
            b.append(True)
        else:
            b.append(False)
        if False in b:
#atleastoneboxisnotcheckedanditem'sboxischecked
            tristate_parent(parent)
        else:
#allboxesofthechildrenarechecked
            check_ancestor(parent)
def tristate_parent(item):
#Puttheboxofitemintristateandchangethestateoftheboxesofitem's
#ancestors
#accordingly.
    change_state(item,"tristate")
    parent=tree.parent(item)
    if parent:
        tristate_parent(parent)
def uncheck_descendant(item):
#Unchecktheboxesofitem'sdescendant.
    children=tree.get_children(item)
    for iid in children:
        change_state(iid,"unchecked")
        uncheck_descendant(iid)
def uncheck_ancestor(item):
#Unchecktheboxofitemandchangethestateoftheboxesofitem'sancestors
#accordingly.
    change_state(item,"unchecked")
    parent=tree.parent(item)
    if parent:
        children=tree.get_children(parent)
        b=[]
    for c in children:
        if'unchecked'intree.item(c,'tags'):
            b.append(True)
        else:
            b.append(False)
    if False in b:
#atleastoneboxischeckedanditem'sboxisunchecked
        tristate_parent(parent)
    else:
#noboxischecked
        uncheck_ancestor(parent)
        
def box_click(event):
#Checkoruncheckboxwhenclicked.
    x,y,widget=event.x,event.y,event.widget
    elem=widget.identify("element",x,y)
    if "image"inelem:
#aboxwasclicked
        item=tree.identify_row(y)
        if tree.tag_has("unchecked",item)ortree.tag_has("tristate",item):
            check_ancestor(item)
            check_descendant(item)
        else:
            uncheck_descendant(item)
            uncheck_ancestor(item)
        UpdateProgressStatus(item)
#Functionsfortheapp__________________________________________________________
_____________________________________________________________________________
def CreateTable():
    statement='''CREATETABLEto_do_list_data
(Task_NameVARCHAR(150),
ParentVARCHAR(150),
Due_DateDATE,
PriorityVARCHAR(10),
Inserted_timeDATETIME,
StatusVarchar(12))'''
    cursor.execute(statement)
    
def UpdateTreeview():
    statement='''SELECT*FROMto_do_list_data'''
    cursor.execute(statement)
    records=cursor.fetchall()
#print(records)
    def change_status(task_name,status):
        if status=='checked':
            change_state(item=task_name,state='checked')
        elif status=='unchecked':
            change_state(item=task_name,state='unchecked')
        else:
            change_state(item=task_name,state='tristate')
for row in records:
    if row[1]=='':
        tree.insert(row[1],'end',row[0],text=row[0],
            values=(row[2].strftime(format='%d/%m/%Y'),'Incomplete',row[3],"0%"),
            open=True,
            tags='unchecked')
        change_status(task_name=row[0],status=row[5])
    else:
        tree.insert(row[1],'end',row[0],text=row[0],values=('','','',''),open=True,
            tags='unchecked')
        change_status(task_name=row[0],status=row[5])
    for child in tree.get_children(''):
        UpdateProgressStatus(child,callfrom='updater')
def get_all_tasks(parent):
#getsalltasksregardlessofwhetherithaschildrenornot
    if len(tree.get_children(parent))==0:
        TaskList.append(parent)
    else:
        TaskList.append(parent)
        forchildintree.get_children(parent):
        get_all_tasks(child)
    return TaskList

def show_selection(event):
#Thisfunctiondefineswhenuserselectsordeselectsarowandwhatchanges
#shouldtake
#placeaccordingly
    def reset_priority(values):
        if values[2]=='Highest':
            PriorityVar2.set(PriorityList[0])
        elif values[2]=='High':
            PriorityVar2.set(PriorityList[1])
        elif values[2]=='Medium':
            PriorityVar2.set(PriorityList[2])
        elif values[2]=='Low':
            PriorityVar2.set(PriorityList[3])
        else:
            PriorityVar2.set(PriorityList[4])
    def when_selected():
        values=(tuple(tree.item(selected)['values']))
        for widget in [EditButton,DeleteButton,AddTaskButton,
        ChangeTaskNameEntry,NameEntry]:
            widget.configure(state='normal')
        SelectedTaskLabel.configure(text=tree.item(tree.tag_has('selected')[0])['text'])
        if tree.parent(selected)=='':
            ChangePriority.configure(fg='black')
            ChangeDate.configure(fg='black')
            DateEntryLabel2.configure(state='normal')
            DateChangeButton2.configure(state='normal')
            PrioritySelection2.configure(state='normal')
            DateEntryLabel2.configure(text=values[0])
            reset_priority(values=values)
        else:
            ChangePriority.configure(fg='grey')
            ChangeDate.configure(fg='grey')
            DateEntryLabel2.configure(state='disabled')
            DateChangeButton2.configure(state='disabled')
            PrioritySelection2.configure(state='disabled')
        ChangeTaskName.configure(fg='black')
        ChangeTaskNameEntry.delete(0,'end')
        ChangeTaskNameEntry.insert(0,tree.item(tree.tag_has('selected')[0])['text'])
        NameLabel.configure(fg='black')
        if AddTaskButton['text']=='AddSubtask':
            SubtaskLabel.configure(fg='black')
            AddTaskButton.configure(state='normal')
            SelectedTaskLabel.configure(text=tree.item(tree.tag_has('selected')[0])['text'])
            SelectedTaskLabel.configure(fg='black')
            DateEntryLabel2.configure(text=Today_str)
        def when_deselected():
            for widgetin[ChangePriority,ChangeDate,ChangeTaskName]:
                widget.configure(fg='grey')
            DateEntryLabel2.configure(text=Today_str)
            ChangeTaskNameEntry.delete(0,'end')
            PriorityVar2.set(PriorityList[2])
            for widgetin[EditButton,DeleteButton,
                DateEntryLabel2,DateChangeButton2,
                PrioritySelection2,ChangeTaskNameEntry]:
            widget.configure(state='disabled')
            if AddTaskButton['text']=='AddSubtask':
                SelectedTaskLabel.configure(text="(Pleaseselectatask)")
                AddTaskButton.configure(state='disabled')
                for widgetin[SelectedTaskLabel,SubtaskLabel,NameLabel]:
                    widget.configure(fg='grey')
                NameEntry.configure(state='disabled')
            else:
                AddTaskButton.configure(state='normal')
                NameLabel.configure(fg='black')
                NameEntry.configure(state='normal')
if len(tree.get_children())!=0:
    previous_selection=tree.tag_has('selected')
    current_selection=tree.selection()
    if previous_selection:
        tag_del(previous_selection[0],'selected')
        if previous_selection[0]==current_selection[0]:
#onlydeselectwhenuserclicksonsamerowagain.
            tree.selection_remove(current_selection[0])
            when_deselected()
            return
    if current_selection:
        selected=current_selection[0]
        tag_add(current_selection[0],'selected')
        when_selected()
    else:
        when_deselected()
    else:
        when_deselected()
        
def AddTypeSwitch():
    global SubtaskLabel,SelectedTaskLabel
    if AddTypeVar.get()==2:#SubtaskToggledon
        if len(tree.get_children())!=0:
#toavoiderrorifthereisnomaintask
            AddTaskFrame.configure(text='AddSubtask',font=("ComicSansMS",13,"bold"))
            AddTaskButton.configure(text='AddSubtask',state='disabled',width=12,
        font=("Comic
        SansMS",9,"bold"))
            SelectedTaskLabel.grid(row=1,column=1,sticky='w')
            AddTaskButton.grid(row=3,column=0,columnspan=2)
            SetDateLabel.grid_remove()
            DateEntryFrame.grid_remove()
            PriorityLabel.grid_remove()
            PrioritySelection.grid_remove()
            show_selection(event=None)
            SubtaskLabel.grid(row=1,column=0,sticky='e')
#RowresizeforAddTaskFrame
            for row in range(0,4):
                Grid.rowconfigure(AddTaskFrame,row,weight=1)
        else:
            messagebox.showinfo("Addatask","Youneedatleastonetasktoadd
            subtasks")
            AddType_task.select()
            AddTypeSwitch()
    else:#MainTaskToggledon
        AddTaskFrame.configure(text='AddTask')
        AddTaskButton.configure(text="AddTask")
        SetDateLabel.grid()
        DateEntryFrame.grid()
        PriorityLabel.grid()
        PrioritySelection.grid()
        SubtaskLabel.grid_remove()
        SelectedTaskLabel.grid_remove()
        AddTaskButton.grid(row=5,column=0,columnspan=2)
#RowresizeforAddTaskFrame
        for row in range(0,6):
            Grid.rowconfigure(AddTaskFrame,row,weight=1)
            show_selection(event=None)
def InsertValues(event=None):
    if NameEntry.get()!="":
        try:
#Treeviewcannothavetaskwhichhassamename.Itreturnsanerror.
#getinserttime
            cursor.execute('SELECTNOW()')
            now=cursor.fetchone()
#Toenterataskonlywhentasknameisnotblank
            task_name=NameEntry.get()
            day=DateEntryLabel['text']
            date=datetime.datetime.strptime(day,'%d/%m/%Y')
            priority=PriorityVar.get()
#Whenthebuttonisinmaintask
            if AddTypeVar.get()==1:
                tree.insert("",'end',task_name,text=task_name,values=(day,'Incomplete',
priority,
"0%"),open=True,
tags='unchecked')
#insertingvaluesinmysql
                statement='''INSERTINTO
to_do_list_data(Task_Name,Parent,Due_Date,Priority,Inserted_time,Status)
VALUES(%s,%s,%s,%s,%s,%s)'''
                values=(task_name,'',date,priority,now[0],'unchecked')
cursor.execute(statement,values)
mydb.commit()
#Iftreehassomethingselected,deselectwhenaddingnewmaintask
            if tree.tag_has('selected'):
                show_selection(event)
#WhentheButtonisinSubtask
            else:
                parent_task=tree.tag_has('selected')[0]
                tree.insert(parent_task,'end',task_name,text=task_name,values=("","","",""),
                    open=True,
                    tags='unchecked')
#Updatestatusandprogressintree
                UpdateProgressStatus(task_name,callfrom='Add_Subtask')
#Updateancestorcheckbox
                uncheck_ancestor(task_name)
#insertingvaluesinmysql
                parent_task_text=tree.item(parent_task)['text']
                statement='''INSERTINTO
to_do_list_data(Task_Name,Parent,Due_Date,Priority,Inserted_time,Status)
VALUES(%s,%s,%s,%s,%s,%s)'''
                values=(task_name,parent_task_text,None,'',None,'unchecked')
                cursor.execute(statement,values)
                mydb.commit()
            NameEntry.delete(0,'end')
            tree.see(task_name)
        except:
#Showerrorthattaskexists
        messagebox.showinfo('Invalidtaskname',
'Sorry!Thetaskalreadyexistsasparentorsubtaskinthetree.')
        NameEntry.delete(0,'end')
    else:
#Showerroriftheuserhaslefttasknameblank
        messagebox.showinfo("Addtaskname","Youcannotleavetasknameempty")
def get_progress_value(parent):
    CheckedList=get_checked()
    def Get_childs(parent):
        children_dict={}
        lvlvalue=100
        def Children(item,lvlvalue):
            if len(tree.get_children(item))==0:
                children_dict[item]=lvlvalue
            else:
                lvlvalue/=len(tree.get_children(item))
                for obj in tree.get_children(item):
                    Children(item=obj,lvlvalue=lvlvalue)
                    Children(item=parent,lvlvalue=lvlvalue)
                    returnchildren_dict
        dict01=Get_childs(parent)
        keys=list(dict01.keys())
        ProgressVariable=0
        for TickedIteminCheckedList:
#iteratethroughtickeditems
            if TickedIteminkeys:
                LevelValue=dict01[TickedItem]
                ProgressVariable+=LevelValue
            return ProgressVariable
def UpdateProgressStatus(item,callfrom='clicked'):
    def get_top_most(row):
        k=row
        parent=tree.parent(k)
        if not parent:
            return row
        else:
            return get_top_most(parent)
    task=get_top_most(item)
#updateprogressvalueandstatus
    if tree.tag_has('checked',task):
#checkedvalues
        values=(tuple(tree.item(task)['values']))
        tree.item(task,values=(values[0],'Completed',values[2],"100%"))
    elif tree.tag_has('unchecked',task):
#uncheckedvalues
        values=(tuple(tree.item(task)['values']))
        tree.item(task,values=(values[0],'Incomplete',values[2],"0%"))
    else:
#tristatevalues
        progress=get_progress_value(parent=task)#getprogressvalue
#Tokeeppercentagewith2decimalplaces
        if progress>=10:
            percentage=str(progress)[0:5]
        else:
            percentage=str(progress)[0:4]
        values=(tuple(tree.item(task)['values']))
        tree.item(task,values=(values[0],'InProgress',values[2],percentage+'%'))
    if callfrom=='clicked':
        update_sql(task)
def update_sql(parent_task):
    def set_checked(task):
        statement='''UPDATEto_do_list_data
SETStatus='checked'
WHERETask_Name=%s'''
        cursor.execute(statement,(task,))
        mydb.commit()
    def set_unchecked(task):
        statement='''UPDATEto_do_list_data
SETStatus='unchecked'
WHERETask_Name=%s'''
        cursor.execute(statement,(task,))
        mydb.commit()
    def set_tristate(task):
        statement='''UPDATEto_do_list_data
SETStatus='tristate'
WHERETask_Name=%s'''
        cursor.execute(statement,(task,))
        mydb.commit()
    TasksList=get_all_tasks(parent_task)
    for task in TasksList:
        if tree.tag_has('checked',task):
            set_checked(task)
        elif tree.tag_has('unchecked',task):
            set_unchecked(task)
        else:
            set_tristate(task)
    TaskList.clear()
def select_date(edit):
    select_date_window=Toplevel()
    select_date_window.geometry('310x400+'+str(screen_width-155)+'+'+
str(screen_height
-200))
    select_date_window.title('SelectDate')
    select_date_window.grab_set()#Sothatusercannotinteractwiththeprevious
    window
#Variables
    current_year=Today_datetime.year
    current_month=Today_datetime.month
    YearVar=StringVar()
    MonthVar=StringVar()
    months=('January','February','March','April','May','June','July','August',
'September','October','November','December')
    DateVar=IntVar()
    DateVar.set(Today_datetime.day)
#Functions:
    def refresh_calendar(year,month):
#cleartheframeofpreviouscontents
        for widget in calendar_frame.winfo_children():
            widget.destroy()
#Createwidgetsinframe
            calendar_title=Label(calendar_frame,
                text=months[month-1]+""+str(year),
                font=("ComicSansMS",14,"bold"))
            calendar_title.grid(row=0,column=0,columnspan=7)
            count=0
            for i in['Mon','Tue','Wed','Thur','Fri','Sat','Sun']:
                Label(calendar_frame,text=i,
                    font=("ComicSansMS",12,"bold")).grid(row=1,column=count,
                sticky='nsew')
                count+=1
                mycalendar=calendar.monthcalendar(year,month)
                week_count=0
                for week in mycalendar:
                    week_count+=1
                    day_count=0#resetday
                    for day in week:
                        if day==0:
                            Radiobutton(calendar_frame,text='',indicator=0,
                                            variable=DateVar,width=3,value=day,borderwidth=0,
                                            state='disabled').grid(row=week_count+1,column=day_count,
                                            sticky='nsew')
                        else:
                            Radiobutton(calendar_frame,text=day,font='bold',indicator=0,
                                variable=DateVar,width=3,value=day,selectcolor='#7CDCFF',
                                command=lambdaday=day,month=month,year=year:
                                date_selected(month,year,day)).grid(
                                row=week_count+1,
                                column=day_count,
                                sticky='nsew')
                            day_count+=1
    def update_monthbox():
        selected_month=MonthVar.get()
        if int(YearVar.get())==current_year:
            MonthBox.configure(values=months[current_month-1:])
        if selected_monthinmonths[current_month-1:]:
            MonthVar.set(selected_month)
        else:
            MonthBox.configure(values=months)
            MonthVar.set(selected_month)
    def update_calendar():
#Updatethecalendar
        selected_month=months.index(MonthVar.get())+1
        selected_year=int(YearVar.get())
        refresh_calendar(selected_year,selected_month)
#Checkfordatevalidityandupdatebottomtext
        selected_date=DateVar.get()
        no_of_days=calendar.monthrange(selected_year,selected_month)[1]
        valid_date=True
        try:
            datetime.date(selected_year,selected_month,selected_date)
        except:
            valid_date=False
        if valid_date:
            date_selected(selected_month,selected_year,selected_date)
        else:
            DateVar.set(no_of_days)
            date_selected(selected_month,selected_year,no_of_days)
    def date_selected(month,year,day):
        selected_date=datetime.date(year,month,day)
        selected_date=selected_date.strftime('%d/%m/%Y')
        SelectedDate.configure(text=selected_date)
    def confirm_date():
        date,month,year=SelectedDate['text'].split('/')
        selected_date=datetime.date(int(year),int(month),int(date))
        if selected_date>=Today_datetime:
            if edit:
                DateEntryLabel2.configure(text=SelectedDate['text'])
            else:
                DateEntryLabel.configure(text=SelectedDate['text'])
                select_date_window.destroy()
        else:
            messagebox.showerror('InvalidDate','Theselecteddatehasalreadypassed.'
                'Pleaseselectavaliddate.')
#Widgets
        title=Label(select_date_window,text='SelectDueDate',font=("ComicSansMS",18,
            "bold"))
        title.grid(row=0,column=0,columnspan=4,pady=10)
        if edit:
            title.configure(text='SelectNewDueDate')
        MonthLabel=Label(select_date_window,text='Month:')
        MonthLabel.grid(row=1,column=0,stick='e',pady=7)
        MonthBox=Spinbox(select_date_window,textvariable=MonthVar,
                values=months,width=12,
                command=update_calendar,
                state='readonly')
        MonthBox.grid(row=1,column=1,sticky='w')
        YearLabel=Label(select_date_window,text='Year:')
        YearLabel.grid(row=1,column=2,stick='e')
        YearBox=Spinbox(select_date_window,textvariable=YearVar,
                from_=int(current_year),to=2100,width=5,
                command=lambda:[update_monthbox(),update_calendar()],
                state='readonly')
        YearBox.grid(row=1,column=3,sticky='w')
        calendar_frame=LabelFrame(select_date_window,text="Calendar",labelanchor='n')
        calendar_frame.grid(row=2,column=0,columnspan=4,sticky='nsew',padx=5)
        lower_frame=Frame(select_date_window)
        lower_frame.grid(row=3,column=0,columnspan=4,sticky='nsew')
        SelectedDateLabel=Label(lower_frame,text="SelectedDate:",font=("ComicSans
        MS",
                11))
        SelectedDateLabel.grid(row=0,column=0,sticky='e')
        SelectedDate=Label(lower_frame,text=Today_str,
                font=("ComicSansMS",11,'bold'),fg='#0078A3')
        SelectedDate.grid(row=0,column=1,sticky='w',pady=10)
        confirm_button=Button(lower_frame,text="Confirm",
                command=confirm_date,width=10,
                font=("ComicSansMS",11,'bold'))
        confirm_button.grid(row=0,column=2,columnspan=2)
        for cols in range(4):
            Grid.columnconfigure(select_date_window,cols,weight=1)
            Grid.columnconfigure(lower_frame,cols,weight=1)
        Grid.rowconfigure(select_date_window,2,weight=1)
        for i in range(7):
            Grid.columnconfigure(calendar_frame,i,weight=1)
            Grid.rowconfigure(calendar_frame,i,weight=1)
            #SetDefaultvalueinspinboxes
            MonthVar.set(months[current_month-1])
            MonthBox.configure(values=months[current_month-1:])
            YearVar.set(current_year)
            #Defaultcalendar:
            refresh_calendar(current_year,current_month)
def edit_task():
    selected=tree.tag_has('selected')[0]
    oldname=tree.item(selected)['text']
    NewName=ChangeTaskNameEntry.get()
    AllTasks=get_all_tasks(parent='')
    if NewNameinAllTasksandNewName!=oldname:
        messagebox.showinfo("Cannotedit","Taskalreadyintasklist.Pleaserephrase.")
        return
    else:
        pass
    NewDate_str=DateEntryLabel2['text']
    NewDate_datetime=datetime.datetime.strptime(NewDate_str,'%d/%m/%Y')
    NewPriority=PriorityVar2.get()
#gettingoldvaluesandchangingtonewones
    values=(tuple(tree.item(selected)['values']))
    if tree.parent(selected)=='':
        tree.item(selected,text=NewName,values=(NewDate_str,values[1],NewPriority,
            values[3]))
        statement='''UPDATEto_do_list_data
            SETDue_Date=%s
            WHERETask_Name=%s'''
        cursor.execute(statement,(NewDate_datetime,oldname))
        mydb.commit()
        statement='''UPDATEto_do_list_data
            SETPriority=%s
            WHERETask_Name=%s'''
        cursor.execute(statement,(NewPriority,oldname))
        mydb.commit()
    else:
        tree.item(selected,text=NewName)
        children=tree.get_children(selected)
    for child in children:
        statement='''UPDATEto_do_list_data
        SETParent=%s
        WHERETask_Name=%s'''
        cursor.execute(statement,(NewName,child))
        mydb.commit()
#UpdateMySQL
        statement='''UPDATEto_do_list_data
        SETTask_Name=%s
        WHERETask_Name=%s'''
    cursor.execute(statement,(NewName,oldname))
    mydb.commit()
#Deselectitem
    show_selection(event=None)
def delete_task():
#Gettheselectedtasktobedeleted
    ToBeDeleted=tree.tag_has('selected')[0]
    tag_del(ToBeDeleted,'selected')
#Getchildtasksofselected
    ToBeDeletedList=[]
    def del_from_mysql(item):
        if len(tree.get_children(item))==0:
            ToBeDeletedList.append(item)
        else:
            ToBeDeletedList.append(item)
            for child in tree.get_children(item):
                del_from_mysql(child)
        del_from_mysql(ToBeDeleted)
        for task in ToBeDeletedList:
            statement='''DELETEFROMto_do_list_data
            WHERETask_Name=%s'''
            cursor.execute(statement,(task,))
            mydb.commit()
#UpdateTreeview
        tree.delete(ToBeDeleted)
        show_selection(event=None)
def delete_all():
    if tree.get_children():
        confirm=messagebox.askokcancel("Confirmation","Areyousureyouwantto
        deleteall
            items?")
    if confirm:
        for parent_taskintree.get_children():
            tree.delete(parent_task)
#Deleteallfrommysql
            cursor.execute("DELETEFROMto_do_list_data")
            mydb.commit()
    else:
        messagebox.showinfo('Notasksleft','Therearenotaskslefttodelete!')
        show_selection(event=None)
def Exit():
    ExitVar=messagebox.askokcancel("ExitApplication","DoyouwanttoexitYourToDo
        ListManager?")
    if ExitVar:
        main.destroy()
        sys.exit()
#
_____________________________________________________________________________________
______
#Labels
Title=Label(main,text="ToDoListmanager",font=("ComicSansMS",25,"bold"))
Title.grid(row=0,column=0,columnspan=3)
#Frames
LeftFrame=Frame(main)
LeftFrame.grid(row=1,column=0,sticky='nsew',pady=5)
sep=ttk.Separator(main,orient='vertical')
sep.grid(row=1,column=1,sticky='nsew',pady=5)
RightFrame=Frame(main)
RightFrame.grid(row=1,column=2,sticky='nsew',pady=5)
#ScrollBar
VertScrollBar=Scrollbar(main,orient='vertical')
VertScrollBar.grid(row=1,column=3,sticky='ns',pady=5)
HoriScrollBar=Scrollbar(RightFrame,orient='horizontal')
HoriScrollBar.pack(side='bottom',fill='x')
#LabelFrames
AddTaskFrame=LabelFrame(LeftFrame,text='AddTask',font=("ComicSansMS",13,
"bold"))
AddTaskFrame.pack(fill='both',expand=True,padx=5)
EditTaskFrame=LabelFrame(LeftFrame,text="EditTask",font=("ComicSansMS",13,
"bold"))
EditTaskFrame.pack(fill='both',expand=True,padx=5)
DeleteTaskFrame=LabelFrame(LeftFrame,text="DeleteTask",font=("ComicSansMS",
13,
"bold"))
DeleteTaskFrame.pack(fill='both',expand=True,padx=5)
#InsideAddLabelFrame
#RadioButton
AddTypeFrame=Frame(AddTaskFrame)
AddTypeFrame.grid(row=0,column=0,columnspan=2,sticky='nsew')
AddType_task=Radiobutton(AddTypeFrame,text='AddTask',indicator=0,
variable=AddTypeVar,value=1,
width=12,command=AddTypeSwitch)
AddType_task.grid(row=0,column=0,sticky='e')
AddType_subtask=Radiobutton(AddTypeFrame,
text='AddSubtask',indicator=0,
variable=AddTypeVar,value=2,
width=12,command=AddTypeSwitch)
AddType_subtask.grid(row=0,column=1,sticky='w')
#Labels
NameLabel=Label(AddTaskFrame,text="Task:",font=("ComicSansMS",11,"bold"))
NameLabel.grid(row=2,column=0,sticky='e')
SetDateLabel=Label(AddTaskFrame,text="SetDueDate:",font=("ComicSansMS",11,
"bold"))
SetDateLabel.grid(row=3,column=0,sticky='e')
PriorityLabel=Label(AddTaskFrame,text="SetPriority:",font=("ComicSansMS",11,
"bold"))
PriorityLabel.grid(row=4,column=0,sticky='e')
SelectedTaskLabel=Label(AddTaskFrame,text="",font=("ComicSansMS",11,"bold"))
SubtaskLabel=Label(AddTaskFrame,text="Subtaskto:",font=("ComicSansMS",11,
"bold"))
#Entry
NameEntry=Entry(AddTaskFrame)
NameEntry.grid(row=2,column=1,padx=5,sticky='we')
NameEntry.bind('<Return>',InsertValues)
#DateEntry
DateEntryFrame=Frame(AddTaskFrame)
DateEntryFrame.grid(row=3,column=1,padx=5,sticky='nsew')
DateEntryLabel=Label(DateEntryFrame,text=Today_str)
DateEntryLabel.pack(side='left')
DateChangeButton=Button(DateEntryFrame,text='ChangeDate',command=lambda
edit=False:select_date(edit))
DateChangeButton.pack(side='left',padx=10)
#Menu
PrioritySelection=OptionMenu(AddTaskFrame,PriorityVar,*PriorityList)
PrioritySelection.grid(row=4,column=1,padx=5,sticky='w')
#Button
AddTaskButton=Button(AddTaskFrame,text="AddTask",width=12,
command=InsertValues,font=("ComicSansMS",9,"bold"))
AddTaskButton.grid(row=5,column=0,columnspan=2)
#RowandColumnresizeforAddTypeFrame
Grid.rowconfigure(AddTypeFrame,0,weight=1)
forcolumninrange(0,2):
Grid.columnconfigure(AddTypeFrame,column,weight=1)
#ColumnresizeforAddTaskFrame
forcolumninrange(0,2):
Grid.columnconfigure(AddTaskFrame,column,weight=1)
#RowresizeforAddTaskFrame
forrowinrange(0,6):
Grid.rowconfigure(AddTaskFrame,row,weight=1)
#InsideEditLabelFrame
#Labels:
ChangeTaskName=Label(EditTaskFrame,text='ChangeTask:',font=("ComicSans
MS",11,
"bold"),fg='grey')
ChangeTaskName.grid(row=0,column=0,sticky='e')
ChangeDate=Label(EditTaskFrame,text='ChangeDueDate:',font=("ComicSansMS",
11,
"bold"),fg='grey')
ChangeDate.grid(row=1,column=0,sticky='e')
ChangePriority=Label(EditTaskFrame,text='ChangePriority:',font=("ComicSansMS",
11,
"bold"),fg='grey')
ChangePriority.grid(row=2,column=0,sticky='e')
#Entry
ChangeTaskNameEntry=Entry(EditTaskFrame,state='disabled')
ChangeTaskNameEntry.grid(row=0,column=1,padx=5,sticky='we')
#DateEntryforedit
DateEntryFrame2=Frame(EditTaskFrame)
DateEntryFrame2.grid(row=1,column=1,padx=5,sticky='nsew')
DateEntryLabel2=Label(DateEntryFrame2,text=Today_str,state='disabled')
DateEntryLabel2.pack(side='left')
DateChangeButton2=Button(DateEntryFrame2,text='ChangeDate',state='disabled',
command=lambdaedit=True:select_date(edit))
DateChangeButton2.pack(side='left',padx=10)
#Menu
PrioritySelection2=OptionMenu(EditTaskFrame,PriorityVar2,*PriorityList)
PrioritySelection2.grid(row=2,column=1,padx=5,sticky='w')
PrioritySelection2.configure(state='disabled')
#Button:
EditButton=Button(EditTaskFrame,text='EditTask',width=12,state='disabled',
command=edit_task,font=("ComicSansMS",9,"bold"))
EditButton.grid(row=3,column=0,columnspan=2)
#Resizing
forrowinrange(0,4):
Grid.rowconfigure(EditTaskFrame,row,weight=1)
forcolinrange(0,2):
Grid.columnconfigure(EditTaskFrame,col,weight=1)
#InsideDeleteLabelFrame
#Buttons:
DeleteButton=Button(DeleteTaskFrame,text='Delete',width=12,
state='disabled',font=("ComicSansMS",9,"bold"),
command=delete_task)
DeleteButton.grid(row=0,column=1)
DeleteAllButton=Button(DeleteTaskFrame,text='DeleteAll',width=12,font=("Comic
Sans
MS",9,"bold"),command=delete_all)
DeleteAllButton.grid(row=0,column=0)
#ColumnresizeforDeleteTaskFrame
Grid.rowconfigure(DeleteTaskFrame,0,weight=1)
forcolumninrange(0,2):
Grid.columnconfigure(DeleteTaskFrame,column,weight=1)
#Exitbutton
Exit_button=Button(main,text="Exit",command=Exit,width=8)
Exit_button.grid(row=2,column=0,columnspan=3,pady=7)
#TreeView
style=Style()
style.configure('Treeview',rowheight=30)
tree=ttk.Treeview(RightFrame,style='Treeview',selectmode='browse')
tree['columns']=('EndDate','Status','Priority','Progress')
#Columnproperties
tree.column('#0',width=250,minwidth=200)
tree.column('EndDate',width=90,minwidth=70)
tree.column('Status',width=90,minwidth=80)
tree.column('Priority',width=90,minwidth=80)
tree.column('Progress',width=90,minwidth=80)
#ColumnNames
tree.heading('#0',text='Task',anchor='w')
tree.heading('EndDate',text='EndDate',anchor='w')
tree.heading('Status',text='Status',anchor='w')
tree.heading('Priority',text='Priority',anchor='w')
tree.heading('Progress',text='Progress',anchor='w')
#tags
tree.tag_configure('checked',image=checked_pic)
tree.tag_configure('unchecked',image=unchecked_pic)
tree.tag_configure('tristate',image=tristate_pic)
#ToupdateCheckboxandstatusandprogressvalueswhenuserselectstreerow
tree.bind("<Button-1>",box_click,True)
tree.bind('<<TreeviewSelect>>',show_selection)
#Treeviewplacement
tree.pack(fill='both',expand=True,padx=5,pady=2)
#SettingupScrollbar
VertScrollBar.configure(command=tree.yview)
tree.configure(yscrollcommand=VertScrollBar.set)
HoriScrollBar.configure(command=tree.xview)
tree.configure(xscrollcommand=HoriScrollBar.set)
#Resizetoadjustwindowwidth
for column in range(0,3):
    ifcolumn==1:#Don'tdoitforcol1
        continue
    Grid.columnconfigure(main,column,weight=column+1)
#Resizetoadjustwindowheight
Grid.rowconfigure(main,1,weight=1)
#Checkalltablesinmysqlforolddata
cursor.execute('SHOWTABLES')
all_tables=cursor.fetchall()
    for table in all_tables:
        if table[0]=='to_do_list_data':
            UpdateTreeview()
            break
else:
    CreateTable()
#Showwarningwhenexiting
main.mainloop()
#File-Handling
mydb=mysql.connector.connect(host="localhost",user="root",passwd="tiger",
        database="test")
cursor=mydb.cursor()
cursor.execute('SELECT*FROMto_do_list_data')
r=cursor.fetchall()
f=open("data.txt","w")
for i in r:
    task=i[0]
    parent=i[1]
    duedt=i[2]
    priority=i[3]
    instime=i[4]
    sts=i[5]
    rec=("Task:"+str(task)+","+"ParentTask:"+str(parent)+","+"Due
Date:"+str(duedt)+",
"+"Priority:"+str(priority)+","+"Taskinsertedon:"+str(instime)+",
"+"Status:"+str(sts)+'\n')
f.writelines(rec)
f.close()