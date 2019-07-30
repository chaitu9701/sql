import sqlite3
"""
CRUD -- create, read, update, delete
"""


"""
Drop table
"""
conn = sqlite3.connect('test.db')
print("Opened database successfully")
conn.execute(""" DROP TABLE IF EXISTS COMPANY; """)
print("Table Company droped successfully")
conn.commit()
conn.close()




"""
create table
"""
conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("""CREATE TABLE IF NOT EXISTS COMPANY (
         ID             INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);""")
print("Table  Company created successfully")
conn.commit()
conn.close()


"""
Insert
"""
conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

conn.commit()
print("Records inserted into company successfully")
conn.close()



"""
READ
"""
conn = sqlite3.connect('test.db')
print("Opened database successfully")

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
   print( "ID = ", row[0])
   print( "NAME = ", row[1])
   print( "ADDRESS = ", row[2])
   print( "SALARY = ", row[3], "\n")

conn.close()



"""
Update
"""
conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
conn.commit
print ("Total number of rows updated :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
   print( "ID = ", row[0])
   print( "NAME = ", row[1])
   print( "ADDRESS = ", row[2])
   print( "SALARY = ", row[3], "\n")

print("Operation done successfully")
conn.close()


"""
delete records
"""
conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("DELETE FROM COMPANY WHERE SALARY = 25000.00 AND ID = 1")
conn.commit
print("Deleleted records successfully")
conn.close()
