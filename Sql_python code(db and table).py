import mysql.connector as sqltor

mydb = sqltor.connect(host = "localhost",
                                        user = "root",
                                        passwd="tiger",
                                        database="testdb")

mc = mydb.cursor()

#Create admin table
mc.execute("""CREATE TABLE Admin
                        (RollNo INTEGER(10) PRIMARY KEY,
                        USN VARCHAR(30),
                        Name VARCHAR(50),
                        Class INTEGER(10),
                        Section VARCHAR(25),
                        SubComb VARCHAR(50),
                        Language VARCHAR(50))""")

#Create teacher table
##mc.execute("""CREATE TABLE Teacher
##                        (RollNo INTEGER ,
##                        SubID INTEGER,
##                        Marks INTEGER,
##                        FOREIGN KEY (SubID) REFERENCES subject (SubID) ON DELETE CASCADE,
##                        FOREIGN KEY (RollNo) REFERENCES admin (RollNo) ON DELETE CASCADE""")

#Create Subject table
mc.execute("""CREATE TABLE Subject
                      (SubID INTEGER PRIMARY KEY,
                        Subject VARCHAR(50))""")
#Insert subject table records
mc.execute("""INSERT INTO Subject(SubID,Subject) VALUES (001,"Physics")""")
mc.execute("""INSERT INTO Subject(SubID,Subject) VALUES (002,"Chemistry")""")
mc.execute("""INSERT INTO Subject(SubID,Subject) VALUES (003,"Maths")""")
mc.execute("""INSERT INTO Subject(SubID,Subject) VALUES (004,"English")""")
mc.execute("""INSERT INTO Subject(SubID,Subject) VALUES (005,"Computer Science")""")
mc.execute("""INSERT INTO Subject(SubID,Subject) VALUES (006,"Biology")""")
mc.execute("""INSERT INTO Subject(SubID,Subject) VALUES (007,"Kannada")""")
mc.execute("""INSERT INTO Subject(SubID,Subject) VALUES (008,"Hindi")""")
mydb.commit()
#Create Login table
mc.execute("""CREATE TABLE Login(Username VARCHAR(50),Password VARCHAR(50),Designation VARCHAR(50))""")
#Insert login table records
mc.execute("""INSERT INTO Login(Username,Password,Designation) VALUES("Praadnya","tiger ","Admin")""")
mc.execute("""INSERT INTO Login(Username,Password,Designation) VALUES("Misha","lion ","Teacher ")""")
mydb.commit()
print("Records inserted")






