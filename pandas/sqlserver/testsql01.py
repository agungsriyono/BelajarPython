import pymssql  
conn = pymssql.connect(server='DESKTOP-V2GTU7E', database='AdventureWorks2017')  
cursor = conn.cursor()  
cursor.execute('SELECT * from Production.WorkOrder;')  
row = cursor.fetchone()  
while row:  
    print(str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[6 ]))     
    row = cursor.fetchone()