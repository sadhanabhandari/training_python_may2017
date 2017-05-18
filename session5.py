import MySQLdb


'''
Created on May 16, 2017

@author: Sadhna
'''

conn_db = MySQLdb.connect("localhost","root","Amulet123!","connect_db")
cursor = conn_db.cursor()

#sql_query ="""create table company(
#company_name char(20),
#company_password char(20))"""
#sql_query=""" INSERT INTO company(company_name,company_password) VALUE ("Apple", "helloworld")"""
sql_query="""LOAD DATA LOCAL INFILE "FL_insurance_sample.csv"
             INTO TABLE company 
             FIELDS TERMINATED BY ','
                 ENCLOSED BY '"'
             LINES TERMINATED BY '\n'
             IGNORE 1 LINES 
             (company_name,company_password)
             """
             
cursor.execute(sql_query)
conn_db.commit()
conn_db.close()
