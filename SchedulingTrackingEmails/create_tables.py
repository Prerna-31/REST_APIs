import sqlite3

connection = sqlite3.connect('./SchedulingTrackingEmails/data.db')

cursor = connection.cursor()

create_sql = "CREATE TABLE IF NOT EXISTS custOwnedProduct(custId VARCHAR2(8) , productName VARCHAR2(10) NOT NULL, domain VARCHAR2(20) NOT NULL, startDate Date, duration NUMBER(2))"

cursor.execute(create_sql)

connection.close()
