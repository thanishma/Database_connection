import mysql.connector
connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="insta"
)
cursor=connection.cursor()

drop_table="drop table if exists table_name2"
cursor.execute(drop_table)

create_table="""CREATE TABLE table_name2 (id int auto_increment primary key,name varchar(30),age int)"""
cursor.execute(create_table)

insert_table="insert into table_name2 (name,age) values(%s,%s)"
data=[('Thanishma',21),('Bunny',18),('John',20),('peter',15),('mary',25)]
cursor.executemany(insert_table,data)

print("Table printed successfully")
select_query="select * from  table_name2"
cursor.execute(select_query)



rows=cursor.fetchall()
for row in rows:
    print(row)


connection.commit()
cursor.close()
connection.close()