from faker import Faker
import mysql.connector
import random

db = mysql.connector.connect(host="localhost",user="khurana",passwd="ishika321",database="skincare_suggestion")

mycursor = db.cursor()

fake=Faker()

def insert_bulk_entries(n):
	data=[]
	for _ in range(1,n+1):
		username=fake.user_name()
		email=fake.email()
		password=fake.password()
		created_at=fake.date_time_this_year()
		gender=fake.random_element(['Male','Female'])
		#age=
		data.append((username,email,password,created_at,gender))

	mycursor.executemany(
		"INSERT INTO user (username,email,password,created_at,gender) VALUES (%s,%s,%s,%s,%s)",data)

	db.commit()
	print(f"{n} user(s) with gender inserted successfully.")

	insert_bulk_entries(1000)

'''fake.name()
fake.address()'''
#new change





