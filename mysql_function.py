import mysql.connector as mc

def my_sqlq_func():
	tables=[]
	data_base=[]
	flag=0
	try:
		conxn=mc.connect(host='localhost',user='root',password='ADMIN',database='test')
		cursr=conxn.cursor()
		cursr.execute('SHOW DATABASES')
		for a in cursr:
			if a not in data_base:
				data_base.append(a)
		print(data_base)

		for i in data_base:
			if i[0]=='reckon':
				print("reckon exist")
				flag=1

		if flag==0:
			print("reckon not there")
			cursr.execute('CREATE DATABASE reckon')
			try:
				cursr.execute('USE RECKON')
				cursr.execute('SHOW TABLES')
				for a in cursr:
					if a not in data_base:
						tables.append(a)
				print(tables)
				if tables==[]:
					cursr.execute('CREATE TABLE log_details(name varchar(20),mobileno int,password varchar(50),Confirmpassword varchar(50))')
					print("table created successfuly")
				else:
					print("table exist already")

			except:
				print("a error is there while connecting reckon")

	except Exception as es:
		print("error")
		print("error",f"Error due to:{str(es)}")

my_sqlq_func()

'''try:
        database = client.create_database(id=reckon)
        print(f"Database created: {database.id}")

    except CosmosResourceExistsError:
        print("Database already exists.")
    try:
    	tables=cusrsor.execute('show tables')
    	print(tables)
        #cursor.execute('create table log_details(name varchar(20),mobileno int,password varchar(50),Confirmpassword varchar(50))')
    except:
    	print("table exist already")'''