import tkinter as tk
from tkinter import*
from tkinter.font import Font
import tkinter.messagebox as MessageBox
from tkinter import ttk
import mysql.connector as sqltor

# Screen1
root3 = Tk()
root3.title("LOGIN")
root3.resizable(0,0)
root3.geometry('%dx%d+%d+%d' % (550, 500, 50, 200))
canvas = Canvas(root3,width = 550,height = 500, bg = 'slate gray')
canvas.grid(column = 0 , row = 0)

global root2

#Admin code
def admin():
    def view_button():
        root1 = Tk()
        root1.title("VIEW")
        root1.resizable(0,0)
        canvas1 = Canvas(root1,width = 700,height = 500, bg = 'slate gray')
        canvas1.grid(column = 0 , row = 0)
        mydb = sqltor.connect(host = "localhost", user = "root", passwd="tiger",database="testdb")
        mc = mydb.cursor()    

        #update according to change function
        def update_rows(rows):
            trv.delete(*trv.get_children())
            for i in rows:
                trv.insert('', 'end',values=i)

        #search function
        def search():  
            mydb = sqltor.connect(host = "localhost", user = "root", passwd="tiger",database="testdb")
            mc = mydb.cursor()
            s=search_entry.get()
            se = s.lower()
            
            search_entry.delete(0, 'end')
            q1="SELECT * FROM admin where RollNo='"+s+"'"
            mc.execute(q1)
            rows=mc.fetchall()
            if rows==[]:
                update_rows(rows)
                MessageBox.showinfo("SEARCH","No records present")        
            else:        
                update_rows(rows)


        #Display All function
        def display():    
            mydb = sqltor.connect(host = "localhost", user = "root", passwd="tiger",database="testdb")
            mc = mydb.cursor()
            q3="select * from admin"
            mc.execute(q3)
            rows=mc.fetchall()
            update_rows(rows)    

        #search widgets       
        search_label=Label(root1,text="Search",bg="white",fg="black",font=18).place(x=20,y=390)
        search_entry=Entry(root1,font=15)
        search_entry.insert(END, 'Enter Roll no')
        search_entry.place(x=100,y=390)
        search_button=Button(root1,text="OK",bg="white",font=20,command=search).place(x=350,y=390)
        display_button=Button(root1,text="Refresh",bg="white",font=20,command=display).place(x=405,y=390)

        #Treeview connection,configuration
        trv=ttk.Treeview(root1,style='Treeview',height=7,show="headings",)
        vsb = ttk.Scrollbar(root1,orient="vertical",command=trv.yview)
        trv.configure(yscrollcommand=vsb.set)
        vsb.place(x=538, y=176, height=20+103+20)
        trv["columns"]=(0,1,2,3,4,5,6)
        trv.place(x=20,y=150)
        #styling table
        style = ttk.Style(root1)
        style.theme_use("clam")
        #table column
        trv.column(0,width=50)
        trv.column(1,width=50)
        trv.column(2,width=70)
        trv.column(3,width=70)
        trv.column(4,width=70)
        trv.column(5,width=120)
        trv.column(6,width=100)
        #table headings
        trv.heading(0,text="RollNo",anchor=tk.W)
        trv.heading(1,text="USN",anchor=tk.W)
        trv.heading(2,text="Name",anchor=tk.W)
        trv.heading(3,text="Class",anchor=tk.W)
        trv.heading(4,text="Section",anchor=tk.W)
        trv.heading(5,text="Subject Combination",anchor=tk.W)
        trv.heading(6,text="Language",anchor=tk.W)
        #standard display of records
        display()

    def insert_button():
                #update according to change function
        def update_rows(rows):
            trv.delete(*trv.get_children())
            for i in rows:
                trv.insert('', 'end',values=i)

        def insert():
                rn = rn_entry.get();
                usn = usn_entry.get();
                name = name_entry.get();
                clas = class_entry.get();
                section = section_entry.get();
                subcomb = subcomb_entry.get();
                lang = lang_entry.get();
                mydb = sqltor.connect(host = "localhost", user = "root", passwd="tiger",database="testdb")
                mc = mydb.cursor()
                try:
                    if (rn==" " or usn==" " or name==" " or clas==" " or section==" " or subcomb==" " or lang==" "):
                        MessageBox.showinfo("INSERT","All fields are required")
                    else:
                        mc.execute("INSERT INTO admin VALUES('"+rn+"','"+usn+"','"+name+"','"+clas+"','"+section+"','"+subcomb+"','"+lang+"')")
                        mc.execute("commit")#update database
                        #update table
                        mc.execute("SELECT * FROM admin")
                        rows=mc.fetchall()
                        update_rows(rows)
                        MessageBox.showinfo("INSERT","Inserted successfully")
                        mydb.close()
                except sqltor.IntegrityError as err:
                        MessageBox.showinfo("INSERT","Record already exists")
                except sqltor.DatabaseError as err2:
                        MessageBox.showinfo("INSERT","Incorrect values")

                rn_entry.delete(0, 'end')
                usn_entry.delete(0, 'end')
                name_entry.delete(0, 'end')
                class_entry.delete(0, 'end')
                section_entry.delete(0, 'end')
                subcomb_entry.delete(0, 'end')
                lang_entry.delete(0, 'end')
            

        root1 = Tk()
        root1.title("INSERT")
        root1.resizable(0,0)
        canvas1 = Canvas(root1,width = 500,height = 500, bg = 'slate gray')
        canvas1.grid(column = 0 , row = 0)
        
        #Treeview connection,configuration
        trv=ttk.Treeview(root1,height=7,show="headings",)

        rn_entry = Entry(root1,font=15)
        rn_entry.place(x=220,y=50)
        rn_label = Label(root1,text="RollNo",bg="white",font=18).place(x=20,y=50)

        usn_entry = Entry(root1,font=15)
        usn_entry.place(x=220,y=100)
        rn_label = Label(root1,text="USN",bg="white",font=18).place(x=20,y=100)

        name_entry = Entry(root1,font=15)
        name_entry.place(x=220,y=150)
        rn_label = Label(root1,text="Name",bg="white",font=18).place(x=20,y=150)

        class_entry = Entry(root1,font=15)
        class_entry.place(x=220,y=200)
        rn_label = Label(root1,text="Class",bg="white",font=18).place(x=20,y=200)

        section_entry = Entry(root1,font=15)
        section_entry.place(x=220,y=250)
        rn_label = Label(root1,text="Section",bg="white",font=18).place(x=20,y=250)

        subcomb_entry = Entry(root1,font=15)
        subcomb_entry.place(x=220,y=300)
        rn_label = Label(root1,text="Subject Combination",bg="white",font=18).place(x=20,y=300)

        lang_entry = Entry(root1,font=15)
        lang_entry.place(x=220,y=350)
        rn_label = Label(root1,text="Language",bg="white",font=18).place(x=20,y=350)

        submit_button = Button(root1,text="SUBMIT",bg="white",font=20,command=insert).place(x=280,y=420)


    def update_button():

                #update according to change function
        def update_rows(rows):
            trv.delete(*trv.get_children())
            for i in rows:
                trv.insert('', 'end',values=i)
 

        def update():       
            rn = rn_entry.get();
            name = name_entry.get();
            clas = class_entry.get();
            section = section_entry.get();
            subcomb = subcomb_entry.get();
            lang = lang_entry.get();

            mydb = sqltor.connect(host = "localhost", user = "root", passwd="tiger",database="testdb")
            mc = mydb.cursor()

            q="SELECT * FROM admin WHERE RollNo='"+rn+"';"
            mc.execute(q)
            r=mc.fetchall()
            if r==[]:
                MessageBox.showinfo("UPDATE","Record does not exist ")
            else:
                try:   
                    if (rn==" " or name==" " or clas==" " or section==" " or subcomb==" " or lang==" "):
                       MessageBox.showinfo("UPDATE","All fields are required")
                    else:
                        mc.execute("UPDATE admin SET Name='"+name+"', Class='"+clas+"', Section='"+section+"', SubComb='"+subcomb+"', Language='"+lang+"' WHERE RollNo='"+rn+"'")
                        mc.execute("commit")#update database
                        #update table
                        mc.execute("SELECT * FROM admin")
                        rows=mc.fetchall()
                        update_rows(rows)
                        MessageBox.showinfo("UPDATE","Updated successfully")
                        mydb.close()

                except sqltor.IntegrityError as err:
                    MessageBox.showinfo("UPDATE","Record with this Roll no already exists")
                except sqltor.DatabaseError as err2:
                    MessageBox.showinfo("UPDATE","Incorrect values")

            rn_entry.delete(0, 'end')
            name_entry.delete(0, 'end')
            class_entry.delete(0, 'end')
            section_entry.delete(0, 'end')
            subcomb_entry.delete(0, 'end')
            lang_entry.delete(0, 'end')  
                


        root1 = Tk()
        root1.title("UPDATE")
        root1.resizable(0,0)
        canvas1 = Canvas(root1,width = 500,height = 450, bg = 'slate gray')
        canvas1.grid(column = 0 , row = 0)
        
        #Treeview connection,configuration
        trv=ttk.Treeview(root1,height=7,show="headings",)

        rn_entry = Entry(root1,font=15)
        rn_entry.place(x=220,y=25)
        rn_label = Label(root1,text="RollNo",bg="white",font=18).place(x=20,y=25)

        name_entry = Entry(root1,font=15)
        name_entry.place(x=220,y=75)
        rn_label = Label(root1,text="Name",bg="white",font=18).place(x=20,y=75)

        class_entry = Entry(root1,font=15)
        class_entry.place(x=220,y=125)
        rn_label = Label(root1,text="Class",bg="white",font=18).place(x=20,y=125)

        section_entry = Entry(root1,font=15)
        section_entry.place(x=220,y=175)
        rn_label = Label(root1,text="Section",bg="white",font=18).place(x=20,y=175)

        subcomb_entry = Entry(root1,font=15)
        subcomb_entry.place(x=220,y=225)
        rn_label = Label(root1,text="Subject Combination",bg="white",font=18).place(x=20,y=225)

        lang_entry = Entry(root1,font=15)
        lang_entry.place(x=220,y=275)
        rn_label = Label(root1,text="Language",bg="white",font=18).place(x=20,y=275)

        submit_button = Button(root1,text="SUBMIT",bg="white",font=20,command=update).place(x=280,y=345)


    def delete_button():
                #update according to change function
        def update_rows(rows):
            trv.delete(*trv.get_children())
            for i in rows:
                trv.insert('', 'end',values=i)


        def delete():
            mydb = sqltor.connect(host = "localhost", user = "root", passwd="tiger",database="testdb")
            mc = mydb.cursor()

            result=MessageBox.askquestion("DELETE", "Are you sure?")
            rn = rn_entry.get();
            q="SELECT * FROM admin WHERE RollNo='"+rn+"';"
            mc.execute(q)
            r=mc.fetchall()
            
            try:
                if result=="yes":
                    if r==[]:
                        MessageBox.showinfo("DELETE","Record does not exist ")
                    else:
                        mc.execute("DELETE FROM admin WHERE RollNo='"+rn+"' ")
                        mc.execute("commit")#update databse
                        #update table
                        mc.execute("SELECT * FROM admin")
                        rows=mc.fetchall()
                        update_rows(rows)
                        MessageBox.showinfo("DELETE","Deleted successfully")
                else:
                    rn_delete.delete(0, 'end')
            except sqltor.DatabaseError as err2:
                MessageBox.showinfo("DELETE","Incorrect values")
            
            rn_entry.delete(0, 'end')
            mydb.close()
                      
        
        root1 = Tk()
        root1.title("DELETE")
        root1.resizable(0,0)
        canvas1 = Canvas(root1,width = 500,height = 300, bg = 'slate gray')
        canvas1.grid(column = 0 , row = 0)
        

        #Treeview connection,configuration
        trv=ttk.Treeview(root1,height=7,show="headings",)

        rn_entry = Entry(root1,font=15)
        rn_entry.place(x=220,y=50)
        rn_label = Label(root1,text="RollNo",bg="white",font=18).place(x=20,y=50)

        submit_button = Button(root1,text="SUBMIT",bg="white",font=20,command=delete).place(x=280,y=150)
        #view_button = Button(root, text="VIEW",bg="white",command=view_button).place(x=160,y=150)
        
    root2.destroy()
    root = Tk()
    root.title("ADMIN")
    root.resizable(0,0)
    root.geometry('%dx%d+%d+%d' % (300, 500, 50, 200))
    canvas = Canvas(root,width = 300,height = 500, bg = 'slate gray')
    canvas.grid(column = 0 , row = 0)
    #center_window()

    insert_button = Button(root, text="INSERT",width=20,bg="white",fg="black",font=20,command=insert_button).place(x=20,y=150)
    update_button = Button(root, text="UPDATE",width=20,bg="white",fg="black",font=20,command=update_button).place(x=20,y=250)
    delete_button = Button(root, text="DELETE",width=20,bg="white",fg="black",font=20,command=delete_button).place(x=20,y=350)
    view_button = Button(root, text="VIEW",width=20,bg="white",fg="black",font=20,command=view_button).place(x=20,y=450)




def teacher():
    global subid
    root2.destroy()
    root = Tk()
    root.title("TEACHER")
    root.resizable(0,0)
    root.geometry('%dx%d+%d+%d' % (450, 500, 50, 200))
    canvas = Canvas(root,width = 450,height = 500, bg = 'slate gray')
    canvas.grid(column = 0 , row = 0)
    #center_window()
    subid = Entry(root,width=15,font=15)
    subid.place(x=220,y=70)
    subid_label = Label(root,text="SUBJECT ID",width=15,bg="white",font=18).place(x=20,y=70)

    def view_button():
        root1 = Tk()
        root1.title("VIEW")
        root1.resizable(0,0)
        canvas1 = Canvas(root1,width = 700,height = 500, bg = 'slate gray')
        canvas1.grid(column = 0 , row = 0)
        mydb = sqltor.connect(host = "localhost", user = "root", passwd="tiger",database="testdb")
        mc = mydb.cursor()    

        trv=ttk.Treeview(root1,height=7,show="headings",)
        #update according to change function
        def update_rows(rows):
            trv.delete(*trv.get_children())
            for i in rows:
                trv.insert('', 'end',values=i)

        #search function
        def search():
            sid=subid.get();
            mydb = sqltor.connect(host = "localhost", user = "root", passwd="tiger",database="testdb")
            mc = mydb.cursor()
            s=search_entry.get()
            search_entry.delete(0, 'end')
            q2="select admin.*,subject.Subject,teacher.Marks from admin INNER JOIN teacher ON teacher.RollNo=admin.RollNo INNER JOIN subject ON teacher.SubID=subject.SubID where teacher.RollNo='"+s+"' and teacher.SubID='"+sid+"'"
            mc.execute(q2)
            rows=mc.fetchall()
            if rows==[]:
                update_rows(rows)
                MessageBox.showinfo("SEARCH","No records present")        
            else:        
                update_rows(rows)

        #Display All function
        def display():
            sid=subid.get();
            mydb = sqltor.connect(host = "localhost", user = "root", passwd="tiger",database="testdb")
            mc = mydb.cursor()
            mc.execute(" select admin.*,subject.Subject,teacher.Marks from admin INNER JOIN teacher ON teacher.RollNo=admin.RollNo INNER JOIN subject ON teacher.SubID=subject.SubID WHERE teacher.SubID='"+sid+"';")
            rows=mc.fetchall()
            update_rows(rows)


        #search widgets       
        search_label=Label(root1,text="Search",bg="white",font=18).place(x=20,y=390)
        search_entry=Entry(root1,font=15)
        search_entry.insert(END, 'Enter Roll no')
        search_entry.place(x=100,y=390)
        search_button=Button(root1,text="OK",bg="white",font=20,command=search).place(x=350,y=390)

        DisplayAll=Button(root1,text="Refresh",bg="white",font=20,command=display).place(x=405,y=390)

        #Treeview connection,configuration
        trv=ttk.Treeview(root1,height=7,show="headings",)
        vsb = ttk.Scrollbar(orient="vertical",command=trv.yview)
        trv.configure(yscrollcommand=vsb.set)
        vsb.place(x=678, y=176, height=20+103+20)
        trv["columns"]=(0,1,2,3,4,5,6,7,8)
        trv.place(x=20,y=150)
        #styling table
        style = ttk.Style(root1)
        style.theme_use("clam")
        #table column
        trv.column(0,width=50)
        trv.column(1,width=50)
        trv.column(2,width=70)
        trv.column(3,width=70)
        trv.column(4,width=70)
        trv.column(5,width=120)
        trv.column(6,width=100)
        trv.column(7,width=70)
        trv.column(8,width=70)
        #table headings
        trv.heading(0,text="RollNo",anchor=tk.W)
        trv.heading(1,text="USN",anchor=tk.W)
        trv.heading(2,text="Name",anchor=tk.W)
        trv.heading(3,text="Class",anchor=tk.W)
        trv.heading(4,text="Section",anchor=tk.W)
        trv.heading(5,text="Subject Combination ",anchor=tk.W)
        trv.heading(6,text="Language",anchor=tk.W)
        trv.heading(7,text="Subject",anchor=tk.W)
        trv.heading(8,text="Marks",anchor=tk.W)
        #standard display of records
        display()


    
    def insert_button():
        #update according to change function
        def update_rows(rows):
            trv.delete(*trv.get_children())
            for i in rows:
                trv.insert('', 'end',values=i)

        def insert():
            global sid
            sid = subid.get();
            rn = rn_entry.get();
            marks = marks_entry.get();
            
            mydb = sqltor.connect(host = "localhost", user = "root", passwd="tiger",database="testdb")
            mc = mydb.cursor()

            q="SELECT * FROM admin WHERE RollNo='"+rn+"';"
            mc.execute(q)
            r=mc.fetchall()
            if r==[]:
                MessageBox.showinfo("INSERT","Record does not exist ")
            else:
                try:
                    if (rn==" " or marks==" "):
                        MessageBox.showinfo("INSERT","All fields are required")
                    else:
                        mc.execute("INSERT INTO teacher VALUES('"+rn+"','"+sid+"','"+marks+"')")
                        mc.execute("commit")#update database
                        #update table
                        mc.execute("SELECT * FROM teacher")
                        rows=mc.fetchall()
                        update_rows(rows)
                        MessageBox.showinfo("INSERT","Inserted successfully")
                        mydb.close()
                except sqltor.DatabaseError as err2:
                        MessageBox.showinfo("INSERT","Marks have already been inserted")

            rn_entry.delete(0, 'end')
            marks_entry.delete(0, 'end')
            mydb.close()


        root1 = Tk()
        root1.title("INSERT")
        root1.resizable(0,0)
        canvas1 = Canvas(root1,width = 500,height = 300, bg = 'slate gray')
        canvas1.grid(column = 0 , row = 0)
        #Treeview connection,configuration
        trv=ttk.Treeview(root1,height=7,show="headings",)

        rn_entry = Entry(root1,font=15)
        rn_entry.place(x=220,y=50)
        rn_label = Label(root1,text="RollNo",width=10,bg="white",font=18).place(x=20,y=50)

        marks_entry = Entry(root1,font=15)
        marks_entry.place(x=220,y=100)
        marks_label = Label(root1,text="Marks",width=10,bg="white",font=18).place(x=20,y=100)

        submit_button = Button(root1,text="SUBMIT",width=12,bg="white",font=20,command=insert).place(x=280,y=200)

    def update_button():
        #update according to change function
        def update_rows(rows):
            trv.delete(*trv.get_children())
            for i in rows:
                trv.insert('', 'end',values=i)

        def update():
            global sid
            sid = subid.get();
            rn = rn_entry.get();
            marks = marks_entry.get();
            
            mydb = sqltor.connect(host = "localhost", user = "root", passwd="tiger",database="testdb")
            mc = mydb.cursor()

            q="SELECT * FROM teacher WHERE RollNo='"+rn+"';"
            mc.execute(q)
            r=mc.fetchall()
            if r==[]:
                MessageBox.showinfo("UPDATE","Record does not exist ")
            else:
                try:   
                    if (rn==" " or marks==" "):
                       MessageBox.showinfo("UPDATE","All fields are required")
                    else:
                        mc.execute("UPDATE teacher SET marks='"+marks+"' WHERE RollNo='"+rn+"' AND SubID='"+sid+"'")
                        mc.execute("commit")#update database
                        #update table
                        mc.execute("SELECT * FROM admin")
                        rows=mc.fetchall()
                        update_rows(rows)
                        MessageBox.showinfo("UPDATE","Updated successfully")

                except sqltor.DatabaseError as err2:
                    MessageBox.showinfo("UPDATE","Record with this Roll no does not exists")

            rn_entry.delete(0, 'end')
            marks_entry.delete(0, 'end')
            mydb.close()
            
        root1 = Tk()
        root1.title("UPDATE")
        root1.resizable(0,0)
        canvas1 = Canvas(root1,width = 500,height = 300, bg = 'slate gray')
        canvas1.grid(column = 0 , row = 0)
        #Treeview connection,configuration
        trv=ttk.Treeview(root1,height=7,show="headings",)

        rn_entry = Entry(root1,font=15)
        rn_entry.place(x=220,y=50)
        rn_label = Label(root1,text="RollNo",width=10,bg="white",font=18).place(x=20,y=50)

        marks_entry = Entry(root1,font=15)
        marks_entry.place(x=220,y=100)
        marks_label = Label(root1,text="Marks",width=10,bg="white",font=18).place(x=20,y=100)

        submit_button = Button(root1,text="SUBMIT",width=12,bg="white",font=20,command=update).place(x=280,y=200)       

    insert_button = Button(root, text="INSERT",width=20,bg="white",fg="black",font=20,command=insert_button).place(x=20,y=150)
    update_button = Button(root, text="UPDATE",width=20,bg="white",fg="black",font=20,command=update_button).place(x=20,y=250)
    view_button = Button(root, text="VIEW",width=20,bg="white",fg="black" ,font=20,command=view_button).place(x=20,y=350)




def talogin():
    global root2
    root3.destroy()
    root2 = Tk()
    root2.title("LOGIN")
    root2.resizable(0,0)
    root2.geometry('%dx%d+%d+%d' % (750, 600, 50, 200))
    canvas = Canvas(root2,width = 750,height = 600, bg = 'slate gray')
    canvas.grid(column = 0 , row = 0)
   

    def login():
        u=user.get()
        x=u.lower()
        p=passw.get()
        d=desig.get()
        y=d.lower()
        mydb = sqltor.connect(host = "localhost", user = "root", passwd="tiger",database="testdb")
        mc = mydb.cursor()
        q1="SELECT * FROM login WHERE Username='"+u+"'"
        mc.execute(q1)
        output = mc.fetchall()
        for i in output:
            a=i[0].lower()
            b=i[2].lower()
            if a==x and i[1]==p and b==y:
                MessageBox.showinfo("LOGIN","Login successful")
                if y=="admin":
                    admin()
                elif y=="teacher":
                    teacher()
            else:
                MessageBox.showinfo("LOGIN","Login unsuccessful")

    def reset_win():
        root4 = Tk()
        root4.title("LOGIN")
        root4.resizable(0,0)
        root4.geometry('%dx%d+%d+%d' % (750, 600, 50, 200))
        canvas = Canvas(root4,width = 750,height = 600, bg = 'slate gray')
        canvas.grid(column = 0 , row = 0)

        def reset():
            o = opwd.get();
            w = npwd.get();
            mydb = sqltor.connect(host = "localhost", user = "root", passwd="tiger",database="testdb")
            mc = mydb.cursor()
            mc.execute("UPDATE login SET Password='"+w+"' WHERE Password='"+o+"'")
            mc.execute("commit")
            MessageBox.showinfo("RESET","Successful")            
            root4.destroy()
            
            
        pane1 = Label(root4, bg="gray76",height=25,width=68).place(x=129,y=160)
        opwd = Entry(root4,textvariable="o",font=15,show="*")
        opwd.place(x=335,y=260)
        opwdl = Label(root4, text="Current password",width=15,bg="white",font=18).place(x=145,y=260)

        npwd = Entry(root4,textvariable="w",font=15, show="*")
        npwd.place(x=335,y=310)
        npwdl = Label(root4, text="New Password",width=15,bg="white",font=18).place(x=145,y=310)
        ok_button = Button(root4,text="OK",width=12,bg="white",font=20,command=reset).place(x=280,y=470)
        


    pane1 = Label(root2, bg="gray76",height=25,width=60).place(x=129,y=160)

    user = Entry(root2,textvariable="u",font=15)
    user.place(x=305,y=260)
    userl = Label(root2, text="Username",width=10,bg="white",font=18).place(x=145,y=260)

    passw = Entry(root2,textvariable="p",font=15, show="*")
    passw.place(x=305,y=310)
    passwl = Label(root2, text="Password",width=10,bg="white",font=18).place(x=145,y=310)

    desig = Entry(root2,font=15)
    desig.place(x=305,y=360)
    desigl = Label(root2, text="Designation",width=10,bg="white",font=18).place(x=145,y=360)

    login_button = Button(root2,text="LOGIN",width=12,bg="white",font=20,command=login).place(x=180,y=470)
    reset_button = Button(root2,text="RESET PASSWORD",width=18,bg="white",font=20,command=reset_win).place(x=340,y=470)

    
def slogin():
    mydb = sqltor.connect(host = "localhost", user = "root", passwd="tiger",database="testdb")
    mc = mydb.cursor()   
    root3.destroy()
    root2 = Tk()
    root2.title("STUDENT LOGIN")
    root2.resizable(0,0)
    root2.geometry('%dx%d+%d+%d' % (500, 300, 50, 200))
    canvas = Canvas(root2,width = 500,height = 300, bg = 'slate gray')
    canvas.grid(column = 0 , row = 0)

    rollno = Entry(root2,font=15)
    rollno.place(x=150,y=30)
    rollnol = Label(root2, text="Roll No",width=10,bg="white",font=18).place(x=20,y=30)

    def report():
        mydb = sqltor.connect(host = "localhost", user = "root", passwd="tiger",database="testdb")
        mc = mydb.cursor()    
        rid=rollno.get()
        mc.execute("SELECT * from admin where RollNo='"+rid+"'")
        output=mc.fetchall()
        if output==[]:
            MessageBox.showinfo("LOGIN","Roll No does not exist")
        else:
            root4 = Toplevel()
            root4.title("REPORT CARD")
            root4.resizable(0,0)
            root4.geometry('%dx%d+%d+%d' % (700, 800, 50, 200))
            canvas = Canvas(root4,width = 700,height = 800, bg = 'slate gray')
            canvas.grid(column = 0 , row = 0)
            
            imgpath1 = 'C:/Users/kulka/OneDrive/Desktop/PRAADNYA/PRADS12/sql_reportcard/12th project/try4_logo.png'          
            photo = PhotoImage(file=imgpath1)
            label = Label(root4,image=photo)
            label.image = photo 
            label.place(x=490,y=10)
            
    # SUBJECTS    
            namel = Label(root4, text="Student Name : ",width=17,bg="white",font=18).place(x=25,y=50)
            mc.execute("SELECT Name FROM admin WHERE RollNo='"+rid+"'")
            sname=mc.fetchone()
            namel2 = Label(root4, text=sname,width=17,bg="white",font=18).place(x=250,y=50)
            rolll = Label(root4, text="Roll No. : ",width=10,bg="white",font=18).place(x=25,y=100)
            roll1 = Label(root4, text=rid,width=10,bg="white",font=18).place(x=200,y=100)
            subl = Label(root4, text="Subject",width=10,bg="white",font=18).place(x=25,y=200)
            markl = Label(root4, text="Marks",width=10,bg="white",font=18).place(x=250,y=200)
            s1p= Label(root4, text="Physics",width=10,bg="white",font=18).place(x=25,y=250)
            s2c = Label(root4, text="Chemistry",width=10,bg="white",font=18).place(x=25,y=300)
            s3m = Label(root4, text="Maths",width=10,bg="white",font=18).place(x=25,y=350)
            s4e = Label(root4, text="English",width=10,bg="white",font=18).place(x=25,y=400)
            mc.execute("SELECT SubComb FROM admin WHERE RollNo='"+rid+"'")
            o1=mc.fetchone()
            if o1[0]=='PCMC':
                s5c = Label(root4, text="Comp Sc.",width=10,bg="white",font=18).place(x=25,y=450)
                mc.execute("SELECT Marks FROM teacher WHERE RollNo='"+rid+"' AND SubID='5'")
                mcs=mc.fetchone()
                markl = Label(root4, text=mcs,width=10,bg="white",font=18).place(x=250,y=450)
            else:
                s5b = Label(root4, text="Biology",width=10,bg="white",font=18).place(x=25,y=450)
                mc.execute("SELECT Marks FROM teacher WHERE RollNo='"+rid+"' AND SubID='6'")
                mb=mc.fetchone()
                markl = Label(root4, text=mb,width=10,bg="white",font=18).place(x=250,y=450)

            mc.execute("SELECT Language FROM admin WHERE RollNo='"+rid+"'")
            o2=mc.fetchone()
            if o2[0]=='Kannada':
                s6k = Label(root4, text="Kannada",width=10,bg="white",font=18).place(x=25,y=500)
                mc.execute("SELECT Marks FROM teacher WHERE RollNo='"+rid+"' AND SubID='7'")
                mk=mc.fetchone()
                markl = Label(root4, text=mk,width=10,bg="white",font=18).place(x=250,y=500)
            else:
                s6h = Label(root4, text="Hindi",width=10,bg="white",font=18).place(x=25,y=500)
                mc.execute("SELECT Marks FROM teacher WHERE RollNo='"+rid+"' AND SubID='8'")
                mh=mc.fetchone()
                markl = Label(root4, text=mh,width=10,bg="white",font=18).place(x=250,y=500)

    #MARKS
            mc.execute("SELECT Marks FROM teacher WHERE RollNo='"+rid+"' AND SubID='1'")
            mp=mc.fetchone()
            markl = Label(root4, text=mp,width=10,bg="white",font=18).place(x=250,y=250)

            mc.execute("SELECT Marks FROM teacher WHERE RollNo='"+rid+"' AND SubID='2'")
            mch=mc.fetchone()
            markl = Label(root4, text=mch,width=10,bg="white",font=18).place(x=250,y=300)

            mc.execute("SELECT Marks FROM teacher WHERE RollNo='"+rid+"' AND SubID='3'")
            mm=mc.fetchone()
            markl = Label(root4, text=mm,width=10,bg="white",font=18).place(x=250,y=350)    

            mc.execute("SELECT Marks FROM teacher WHERE RollNo='"+rid+"' AND SubID='4'")
            me=mc.fetchone()
            markl = Label(root4, text=me,width=10,bg="white",font=18).place(x=250,y=400)

            mc.execute("SELECT SUM(Marks) FROM teacher WHERE RollNo='"+rid+"'")
            o3 = mc.fetchone()
            per=round((o3[0]*100)/600,2)
            
            totall = Label(root4, text="Total percentage : ",width=20,bg="white",font=18).place(x=25,y=600)
            total = Label(root4, text=per,width=10,bg="white",font=18).place(x=300,y=600)

            resultl= Label(root4, text="Result : ",width=10,bg="white",font=18).place(x=25,y=650)

            if per>50:
                rel= Label(root4, text="PASS",width=10,bg="white",font=18).place(x=200,y=650)
            else:
                rel=Label(root4, text="FAIL",width=10,bg="white",font=18).place(x=200,y=650)

    report_button = Button(root2,text="Report card",width=12,bg="white",font=20,command=report).place(x=120,y=125)

    
ta_button = Button(root3,text="Teacher/Admin",width=12,bg="white",font=20,command=talogin).place(x=206,y=300)
s_button = Button(root3,text="Student",width=12,bg="white",font=20,command=slogin).place(x=206,y=400)

imgpath = 'C:/Users/kulka/OneDrive/Desktop/PRAADNYA/PRADS12/sql_reportcard/12th project/try3_logo.png'
img = PhotoImage(file=imgpath)
panel = Label(root3, image = img).place(x=158,y=10)


    






