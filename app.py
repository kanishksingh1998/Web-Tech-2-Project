import csv 
import pandas as pd 
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, jsonify, request, session


import sqlite3
from sqlite3 import Error

def sql_connection():

	try:

		con = sqlite3.connect('mydatabase.db')

		return con

	except Error:

		print(Error)

def sql_table(con):

	cursorObj = con.cursor()
	flag = 0 #value of 1 indicates that table is already present and populated
	if flag == 0:
		cursorObj.execute("DROP TABLE university")
	cursorObj.execute("CREATE TABLE IF NOT EXISTS university(SRN text, SUBJECT text, CBT1 integer, CBT2 integer, PRIMARY KEY (SRN,SUBJECT))")
	
	#creating another table to store info about students' login info
	if flag == 0:
		cursorObj.execute("DROP TABLE login")
	cursorObj.execute("CREATE TABLE IF NOT EXISTS login(SRN text, email text, password text, PRIMARY KEY (SRN))")
	if flag == 0:	
		cursorObj.execute("INSERT INTO login VALUES('PES1201700001', 'PES1201700001@gmail.com', 'PES1201700001')")
		cursorObj.execute("INSERT INTO login VALUES('PES1201700002', 'PES1201700002@gmail.com', 'PES1201700002')")
		cursorObj.execute("INSERT INTO login VALUES('PES1201700003', 'PES1201700003@gmail.com', 'PES1201700003')")
		cursorObj.execute("INSERT INTO login VALUES('PES1201700004', 'PES1201700004@gmail.com', 'PES1201700004')")
		cursorObj.execute("INSERT INTO login VALUES('PES1201700005', 'PES1201700005@gmail.com', 'PES1201700005')")
		cursorObj.execute("INSERT INTO login VALUES('PES1201700006', 'PES1201700006@gmail.com', 'PES1201700006')")
		cursorObj.execute("INSERT INTO login VALUES('PES1201700007', 'PES1201700007@gmail.com', 'PES1201700007')")
		cursorObj.execute("INSERT INTO login VALUES('PES1201700008', 'PES1201700008@gmail.com', 'PES1201700008')")

	#these values are only entered on creation of table
	if flag == 0:
		cursorObj.execute("INSERT INTO university VALUES('PES1201700001', 'Compiler Design', 30, 27)")
		cursorObj.execute("INSERT INTO university VALUES('PES1201700001', 'Web Tech 2', 30, 27)")
		cursorObj.execute("INSERT INTO university VALUES('PES1201700001', 'Cloud Computing', 30, 27)")
		cursorObj.execute("INSERT INTO university VALUES('PES1201700001', 'Topics in Deep Learning', 30, 27)")
		cursorObj.execute("INSERT INTO university VALUES('PES1201700001', 'System Modelling', 30, 27)")

		cursorObj.execute("INSERT INTO university VALUES('PES1201700002', 'Compiler Design', 31, 23)")
		cursorObj.execute("INSERT INTO university VALUES('PES1201700002', 'Web Tech 2', 31, 23)")
		cursorObj.execute("INSERT INTO university VALUES('PES1201700002', 'Cloud Computing', 31, 23)")
		cursorObj.execute("INSERT INTO university VALUES('PES1201700002', 'Topics in Deep Learning', 31, 23)")
		cursorObj.execute("INSERT INTO university VALUES('PES1201700002', 'System Modelling', 31, 23)")

		cursorObj.execute("INSERT INTO university VALUES('PES1201700003', 'Compiler Design', 19, 23)")
		cursorObj.execute("INSERT INTO university VALUES('PES1201700003', 'Web Tech 2', 19, 23)")
		cursorObj.execute("INSERT INTO university VALUES('PES1201700003', 'Cloud Computing', 19, 23)")
		cursorObj.execute("INSERT INTO university VALUES('PES1201700003', 'Topics in Deep Learning', 19, 23)")
		cursorObj.execute("INSERT INTO university VALUES('PES1201700003', 'System Modelling', 19, 23)")
		
		cursorObj.execute("INSERT INTO university VALUES('PES1201700004', 'Compiler Design', 37, 39)")
		cursorObj.execute("INSERT INTO university VALUES('PES1201700004', 'Web Tech 2', 37, 39)")
		cursorObj.execute("INSERT INTO university VALUES('PES1201700004', 'Cloud Computing', 37, 39)")
		cursorObj.execute("INSERT INTO university VALUES('PES1201700004', 'Topics in Deep Learning', 37, 39)")
		cursorObj.execute("INSERT INTO university VALUES('PES1201700004', 'System Modelling', 37, 39)")

		cursorObj.execute("INSERT INTO university VALUES('PES1201700005', 'Compiler Design', 26, 26)")
		cursorObj.execute("INSERT INTO university VALUES('PES1201700005', 'Web Tech 2', 26, 26)")
		cursorObj.execute("INSERT INTO university VALUES('PES1201700005', 'Cloud Computing', 26, 26)")
		cursorObj.execute("INSERT INTO university VALUES('PES1201700005', 'Topics in Deep Learning', 26, 26)")
		cursorObj.execute("INSERT INTO university VALUES('PES1201700005', 'System Modelling', 26, 26)")

		cursorObj.execute("INSERT INTO university VALUES('PES1201700006', 'Compiler Design', 16, 16)")
		cursorObj.execute("INSERT INTO university VALUES('PES1201700006', 'Web Tech 2', 17, 26)")
		cursorObj.execute("INSERT INTO university VALUES('PES1201700006', 'Cloud Computing', 24, 26)")
		cursorObj.execute("INSERT INTO university VALUES('PES1201700006', 'Topics in Deep Learning', 27, 29)")
		cursorObj.execute("INSERT INTO university VALUES('PES1201700006', 'System Modelling', 36, 36)")
		
		cursorObj.execute("INSERT INTO university VALUES('PES1201700007', 'Compiler Design', 36, 16)")
		cursorObj.execute("INSERT INTO university VALUES('PES1201700007', 'Web Tech 2', 36, 16)")
		cursorObj.execute("INSERT INTO university VALUES('PES1201700007', 'Cloud Computing', 36, 16)")
		cursorObj.execute("INSERT INTO university VALUES('PES1201700007', 'Topics in Deep Learning', 36, 16)")
		cursorObj.execute("INSERT INTO university VALUES('PES1201700007', 'System Modelling', 36, 16)")
		
		cursorObj.execute("INSERT INTO university VALUES('PES1201700008', 'Compiler Design', 30, 10)")
		cursorObj.execute("INSERT INTO university VALUES('PES1201700008', 'Web Tech 2', 20, 21)")
		cursorObj.execute("INSERT INTO university VALUES('PES1201700008', 'Cloud Computing', 24, 20)")
		cursorObj.execute("INSERT INTO university VALUES('PES1201700008', 'Topics in Deep Learning', 36, 36)")
		cursorObj.execute("INSERT INTO university VALUES('PES1201700008', 'System Modelling', 10, 20)")
	
	#cursorObj.execute("ALTER TABLE university ADD CONSTRAINT STUD_ID PRIMARY KEY (SRN, SUBJECT);")

	con.commit()

con = sql_connection()

sql_table(con)



app=Flask(__name__)
app.secret_key = "this is a random string"

@app.route('/page-login')
def pagelogin():
	return(render_template("page-login.html"))

from pytrie import StringTrie

def prefixsearch(arr,prefix):
	trie = StringTrie()
	for key in arr:
		trie[key] = key
	return trie.values(prefix)

@app.route('/SRNsearch', methods=['GET'])
def SRNsearch():
	#print("hello")
	searchSRN = request.args.get('SRN')
	con = sqlite3.connect('mydatabase.db')
	cur = con.cursor()
	print("prefix: ",searchSRN)
	srns = cur.execute("SELECT SRN from login")
	srns = list(srns)
	SRN=[]
	for i in range(len(srns)):
		SRN.append(srns[i][0])
	print(SRN)
	srns = prefixsearch(SRN,searchSRN)
	print(srns)
	SRN = []
	for i in range(len(srns)):
		SRN.append(srns[i])
	print("matched",SRN)
	return jsonify({"data":SRN})
	#return jsonify({"hello":"hi"})
	#return(render_template("page-login.html",serialnumber=searchSRN))


@app.route('/page-register')
def pageregister():
	'''
	srn=request.form['SRN']
	email=request.form['email']
	password=request.form['password']
	'''
	return(render_template("page-register.html"))

@app.route('/about')
def about():
	return(render_template("about.html"))

@app.route('/data',methods=['POST'])
def data():
	srn=request.form['SRN']
	email=request.form['email']
	password=request.form['password']
	
	con = sqlite3.connect('mydatabase.db')
	cur = con.cursor()
	entities = (srn, email, password)
	cur.execute('''INSERT INTO login VALUES(?, ?, ?)''',entities)
	con.commit()
	#given this data, candidate add to the database and continue to to data.html to get their marks
	#adding session for srn to be able to be used by progress page
	session['SRN'] = srn
	
	return(render_template("data.html",SRN=srn))   

@app.route('/progress-sign-in', methods=['POST'])
def progress1():
	srn=request.form['SRN']
	email=request.form['email']
	password=request.form['password']
	
	#verifying email and password
	con = sqlite3.connect('mydatabase.db')
	cur = con.cursor()
	cur.execute("SELECT SRN,email,password from login where SRN = '%s' and email = '%s' and password = '%s'" % (srn,email,password))
	rows = cur.fetchall()
	if len(rows) == 0:
		return(render_template("page-login.html"))

	#adding session for srn to be able to be used by progress page
	session['SRN'] = srn
	
	con = sqlite3.connect('mydatabase.db')
	cur = con.cursor()
	#FOR COMPILER DESIGN
	cur.execute("SELECT CBT1, CBT2 from university where SUBJECT = 'Compiler Design' and SRN = '%s'" % (srn))
	rows = cur.fetchall()
	if len(rows) > 0:
		print("hello")
		for row in rows:
			cbt1 = int(row[0])
			cbt2 = int(row[1])			
			total_score = cbt1+cbt2
		cursor_avg = cur.execute("SELECT avg(CBT1), avg(CBT2) from university where SUBJECT = 'Compiler Design'")
		for row in cursor_avg:
			avg_cbt_score = row[0]+row[1]

		
			
   		
		cursor_total_count = cur.execute("SELECT count(SRN) from university where SUBJECT = 'Compiler Design'")
		for row in cursor_total_count:
			total_count = int(row[0]) 
		
		cursor_percentile = cur.execute("SELECT count(SRN) from university where SUBJECT = 'Compiler Design' and CBT1 + CBT2 > %s" % (total_score))
		for row in cursor_percentile:
			higher_scorers_count = int(row[0])
		
		percentile_value = (total_count - higher_scorers_count)*100/total_count

		#now marks needed for top grades will be calculated
		sgrade = 88 - (total_score/2) if 88 - (total_score/2) <=60 else 'Not Possible' 
		agrade = 76 - (total_score/2) if 76 - (total_score/2) <=60 else 'Not Possible'
		bgrade = 64 - (total_score/2)	if 64 - (total_score/2) <=60 else 'Not Possible'
		
		#dictionary of results to be passed onto the html page is created
		cd = {}
		cd['avg'] = avg_cbt_score
		cd['total'] = total_score
		cd['perc'] = percentile_value
		cd['s'] = sgrade
		cd['a'] = agrade
		cd['b'] = bgrade

	else:
		cd = {}
		cd['avg'] = 'NA'
		cd['total'] = 'NA'
		cd['perc'] = 'NA'
		cd['s'] = 'NA'
		cd['a'] = 'NA'
		cd['b'] = 'NA'
			
	#FOR Web Tech 2
	cur.execute("SELECT CBT1, CBT2 from university where SUBJECT = 'Web Tech 2' and SRN = '%s'" % (srn))
	rows = cur.fetchall()
	if len(rows) > 0:
		print("hello")
		for row in rows:
			cbt1 = int(row[0])
			cbt2 = int(row[1])			
			total_score = cbt1+cbt2
		cursor_avg = cur.execute("SELECT avg(CBT1), avg(CBT2) from university where SUBJECT = 'Web Tech 2'")
		for row in cursor_avg:
			avg_cbt_score = row[0]+row[1]

		
			
   		
		cursor_total_count = cur.execute("SELECT count(SRN) from university where SUBJECT = 'Web Tech 2'")
		for row in cursor_total_count:
			total_count = int(row[0]) 
		
		cursor_percentile = cur.execute("SELECT count(SRN) from university where SUBJECT = 'Web Tech 2' and CBT1 + CBT2 > %s" % (total_score))
		for row in cursor_percentile:
			higher_scorers_count = int(row[0])
		
		percentile_value = (total_count - higher_scorers_count)*100/total_count

		#now marks needed for top grades will be calculated
		sgrade = 88 - (total_score/2) if 88 - (total_score/2) <=60 else 'Not Possible' 
		agrade = 76 - (total_score/2) if 76 - (total_score/2) <=60 else 'Not Possible'
		bgrade = 64 - (total_score/2)	if 64 - (total_score/2) <=60 else 'Not Possible'
		
		#dictionary of results to be passed onto the html page is created
		wt = {}
		wt['avg'] = avg_cbt_score
		wt['total'] = total_score
		wt['perc'] = percentile_value
		wt['s'] = sgrade
		wt['a'] = agrade
		wt['b'] = bgrade

	else:
		wt = {}
		wt['avg'] = 'NA'
		wt['total'] = 'NA'
		wt['perc'] = 'NA'
		wt['s'] = 'NA'
		wt['a'] = 'NA'
		wt['b'] = 'NA'
	
	#FOR CLOUD COMPUTING
	cur.execute("SELECT CBT1, CBT2 from university where SUBJECT = 'Cloud Computing' and SRN = '%s'" % (srn))
	rows = cur.fetchall()
	if len(rows) > 0:
		print("hello")
		for row in rows:
			cbt1 = int(row[0])
			cbt2 = int(row[1])			
			total_score = cbt1+cbt2
		cursor_avg = cur.execute("SELECT avg(CBT1), avg(CBT2) from university where SUBJECT = 'Cloud Computing'")
		for row in cursor_avg:
			avg_cbt_score = row[0]+row[1]

		
			
   		
		cursor_total_count = cur.execute("SELECT count(SRN) from university where SUBJECT = 'Cloud Computing'")
		for row in cursor_total_count:
			total_count = int(row[0]) 
		
		cursor_percentile = cur.execute("SELECT count(SRN) from university where SUBJECT = 'Cloud Computing' and CBT1 + CBT2 > %s" % (total_score))
		for row in cursor_percentile:
			higher_scorers_count = int(row[0])
		
		percentile_value = (total_count - higher_scorers_count)*100/total_count

		#now marks needed for top grades will be calculated
		sgrade = 88 - (total_score/2) if 88 - (total_score/2) <=60 else 'Not Possible' 
		agrade = 76 - (total_score/2) if 76 - (total_score/2) <=60 else 'Not Possible'
		bgrade = 64 - (total_score/2)	if 64 - (total_score/2) <=60 else 'Not Possible'
		
		#dictionary of results to be passed onto the html page is created
		cc = {}
		cc['avg'] = avg_cbt_score
		cc['total'] = total_score
		cc['perc'] = percentile_value
		cc['s'] = sgrade
		cc['a'] = agrade
		cc['b'] = bgrade

	else:
		cc = {}
		cc['avg'] = 'NA'
		cc['total'] = 'NA'
		cc['perc'] = 'NA'
		cc['s'] = 'NA'
		cc['a'] = 'NA'
		cc['b'] = 'NA'
	
	#cursorObj.execute("SELECT id, name, address, salary from COMPANY")

	#FOR TOPICS IN DEEP LEARNING
	cur.execute("SELECT CBT1, CBT2 from university where SUBJECT = 'Topics in Deep Learning' and SRN = '%s'" % (srn))
	rows = cur.fetchall()
	if len(rows) > 0:
		print("hello")
		for row in rows:
			cbt1 = int(row[0])
			cbt2 = int(row[1])			
			total_score = cbt1+cbt2
		cursor_avg = cur.execute("SELECT avg(CBT1), avg(CBT2) from university where SUBJECT = 'Topics in Deep Learning'")
		for row in cursor_avg:
			avg_cbt_score = row[0]+row[1]

		
			
   		
		cursor_total_count = cur.execute("SELECT count(SRN) from university where SUBJECT = 'Topics in Deep Learning'")
		for row in cursor_total_count:
			total_count = int(row[0]) 
		
		cursor_percentile = cur.execute("SELECT count(SRN) from university where SUBJECT = 'Topics in Deep Learning' and CBT1 + CBT2 > %s" % (total_score))
		for row in cursor_percentile:
			higher_scorers_count = int(row[0])
		
		percentile_value = (total_count - higher_scorers_count)*100/total_count

		#now marks needed for top grades will be calculated
		sgrade = 88 - (total_score/2) if 88 - (total_score/2) <=60 else 'Not Possible' 
		agrade = 76 - (total_score/2) if 76 - (total_score/2) <=60 else 'Not Possible'
		bgrade = 64 - (total_score/2)	if 64 - (total_score/2) <=60 else 'Not Possible'
		
		#dictionary of results to be passed onto the html page is created
		tdl = {}
		tdl['avg'] = avg_cbt_score
		tdl['total'] = total_score
		tdl['perc'] = percentile_value
		tdl['s'] = sgrade
		tdl['a'] = agrade
		tdl['b'] = bgrade

	else:
		tdl = {}
		tdl['avg'] = 'NA'
		tdl['total'] = 'NA'
		tdl['perc'] = 'NA'
		tdl['s'] = 'NA'
		tdl['a'] = 'NA'
		tdl['b'] = 'NA'


	#FOR SYSTEM MODELLING
	cur.execute("SELECT CBT1, CBT2 from university where SUBJECT = 'System Modelling' and SRN = '%s'" % (srn))
	rows = cur.fetchall()
	if len(rows) > 0:
		print("hello")
		for row in rows:
			cbt1 = int(row[0])
			cbt2 = int(row[1])			
			total_score = cbt1+cbt2
		cursor_avg = cur.execute("SELECT avg(CBT1), avg(CBT2) from university where SUBJECT = 'System Modelling'")
		for row in cursor_avg:
			avg_cbt_score = row[0]+row[1]

		
			
   		
		cursor_total_count = cur.execute("SELECT count(SRN) from university where SUBJECT = 'System Modelling'")
		for row in cursor_total_count:
			total_count = int(row[0]) 
		
		cursor_percentile = cur.execute("SELECT count(SRN) from university where SUBJECT = 'System Modelling' and CBT1 + CBT2 > %s" % (total_score))
		for row in cursor_percentile:
			higher_scorers_count = int(row[0])
		
		percentile_value = (total_count - higher_scorers_count)*100/total_count

		#now marks needed for top grades will be calculated
		sgrade = 88 - (total_score/2) if 88 - (total_score/2) <=60 else 'Not Possible' 
		agrade = 76 - (total_score/2) if 76 - (total_score/2) <=60 else 'Not Possible'
		bgrade = 64 - (total_score/2)	if 64 - (total_score/2) <=60 else 'Not Possible'
		
		#dictionary of results to be passed onto the html page is created
		sms = {}
		sms['avg'] = avg_cbt_score
		sms['total'] = total_score
		sms['perc'] = percentile_value
		sms['s'] = sgrade
		sms['a'] = agrade
		sms['b'] = bgrade

	else:
		sms = {}
		sms['avg'] = 'NA'
		sms['total'] = 'NA'
		sms['perc'] = 'NA'
		sms['s'] = 'NA'
		sms['a'] = 'NA'
		sms['b'] = 'NA'
	
	final_result = {}
	final_result['cd'] = cd
	final_result['wt'] = wt
	final_result['cc'] = cc
	final_result['sms'] = sms
	final_result['tdl'] = tdl
		
		
				
			

		
		
	
	#first validate password. If password is correct then continue to progress-sign-in and display all the data n progress

	return(render_template("progress.html",SRN=srn,result=final_result))


@app.route('/progress', methods=['POST'])
def progress2():
	name=request.form['NAME']
	subject=request.form['SUBJECT']
	cbt1=request.form['CBT1']
	cbt2=request.form['CBT2']
	srn = session['SRN']
	#take the given data and add it to the database and perform the evaluation of the student and go to progress
	#most important site to handle all the data n show the progress n everything


	#enter student's info into database
	con = sqlite3.connect('mydatabase.db')
	cur = con.cursor()
	entities = (srn, subject, cbt1, cbt2)
	cur.execute('''INSERT INTO university VALUES(?, ?, ?, ?)''',entities)
	con.commit()
	#FOR COMPILER DESIGN
	cur.execute("SELECT CBT1, CBT2 from university where SUBJECT = 'Compiler Design' and SRN = '%s'" % (srn))
	rows = cur.fetchall()
	if len(rows) > 0:
		print("hello")
		for row in rows:
			cbt1 = int(row[0])
			cbt2 = int(row[1])			
			total_score = cbt1+cbt2
		cursor_avg = cur.execute("SELECT avg(CBT1), avg(CBT2) from university where SUBJECT = 'Compiler Design'")
		for row in cursor_avg:
			avg_cbt_score = row[0]+row[1]

		
			
   		
		cursor_total_count = cur.execute("SELECT count(SRN) from university where SUBJECT = 'Compiler Design'")
		for row in cursor_total_count:
			total_count = int(row[0]) 
		
		cursor_percentile = cur.execute("SELECT count(SRN) from university where SUBJECT = 'Compiler Design' and CBT1 + CBT2 > %s" % (total_score))
		for row in cursor_percentile:
			higher_scorers_count = int(row[0])
		
		percentile_value = (total_count - higher_scorers_count)*100/total_count

		#now marks needed for top grades will be calculated
		sgrade = 88 - (total_score/2) if 88 - (total_score/2) <=60 else 'Not Possible' 
		agrade = 76 - (total_score/2) if 76 - (total_score/2) <=60 else 'Not Possible'
		bgrade = 64 - (total_score/2)	if 64 - (total_score/2) <=60 else 'Not Possible'
		
		#dictionary of results to be passed onto the html page is created
		cd = {}
		cd['avg'] = avg_cbt_score
		cd['total'] = total_score
		cd['perc'] = percentile_value
		cd['s'] = sgrade
		cd['a'] = agrade
		cd['b'] = bgrade

	else:
		cd = {}
		cd['avg'] = 'NA'
		cd['total'] = 'NA'
		cd['perc'] = 'NA'
		cd['s'] = 'NA'
		cd['a'] = 'NA'
		cd['b'] = 'NA'
			
	#FOR Web Tech 2
	cur.execute("SELECT CBT1, CBT2 from university where SUBJECT = 'Web Tech 2' and SRN = '%s'" % (srn))
	rows = cur.fetchall()
	if len(rows) > 0:
		print("hello")
		for row in rows:
			cbt1 = int(row[0])
			cbt2 = int(row[1])			
			total_score = cbt1+cbt2
		cursor_avg = cur.execute("SELECT avg(CBT1), avg(CBT2) from university where SUBJECT = 'Web Tech 2'")
		for row in cursor_avg:
			avg_cbt_score = row[0]+row[1]

		
			
   		
		cursor_total_count = cur.execute("SELECT count(SRN) from university where SUBJECT = 'Web Tech 2'")
		for row in cursor_total_count:
			total_count = int(row[0]) 
		
		cursor_percentile = cur.execute("SELECT count(SRN) from university where SUBJECT = 'Web Tech 2' and CBT1 + CBT2 > %s" % (total_score))
		for row in cursor_percentile:
			higher_scorers_count = int(row[0])
		
		percentile_value = (total_count - higher_scorers_count)*100/total_count

		#now marks needed for top grades will be calculated
		sgrade = 88 - (total_score/2) if 88 - (total_score/2) <=60 else 'Not Possible' 
		agrade = 76 - (total_score/2) if 76 - (total_score/2) <=60 else 'Not Possible'
		bgrade = 64 - (total_score/2)	if 64 - (total_score/2) <=60 else 'Not Possible'
		
		#dictionary of results to be passed onto the html page is created
		wt = {}
		wt['avg'] = avg_cbt_score
		wt['total'] = total_score
		wt['perc'] = percentile_value
		wt['s'] = sgrade
		wt['a'] = agrade
		wt['b'] = bgrade

	else:
		wt = {}
		wt['avg'] = 'NA'
		wt['total'] = 'NA'
		wt['perc'] = 'NA'
		wt['s'] = 'NA'
		wt['a'] = 'NA'
		wt['b'] = 'NA'
	
	#FOR CLOUD COMPUTING
	cur.execute("SELECT CBT1, CBT2 from university where SUBJECT = 'Cloud Computing' and SRN = '%s'" % (srn))
	rows = cur.fetchall()
	if len(rows) > 0:
		print("hello")
		for row in rows:
			cbt1 = int(row[0])
			cbt2 = int(row[1])			
			total_score = cbt1+cbt2
		cursor_avg = cur.execute("SELECT avg(CBT1), avg(CBT2) from university where SUBJECT = 'Cloud Computing'")
		for row in cursor_avg:
			avg_cbt_score = row[0]+row[1]

		
			
   		
		cursor_total_count = cur.execute("SELECT count(SRN) from university where SUBJECT = 'Cloud Computing'")
		for row in cursor_total_count:
			total_count = int(row[0]) 
		
		cursor_percentile = cur.execute("SELECT count(SRN) from university where SUBJECT = 'Cloud Computing' and CBT1 + CBT2 > %s" % (total_score))
		for row in cursor_percentile:
			higher_scorers_count = int(row[0])
		
		percentile_value = (total_count - higher_scorers_count)*100/total_count

		#now marks needed for top grades will be calculated
		sgrade = 88 - (total_score/2) if 88 - (total_score/2) <=60 else 'Not Possible' 
		agrade = 76 - (total_score/2) if 76 - (total_score/2) <=60 else 'Not Possible'
		bgrade = 64 - (total_score/2)	if 64 - (total_score/2) <=60 else 'Not Possible'
		
		#dictionary of results to be passed onto the html page is created
		cc = {}
		cc['avg'] = avg_cbt_score
		cc['total'] = total_score
		cc['perc'] = percentile_value
		cc['s'] = sgrade
		cc['a'] = agrade
		cc['b'] = bgrade

	else:
		cc = {}
		cc['avg'] = 'NA'
		cc['total'] = 'NA'
		cc['perc'] = 'NA'
		cc['s'] = 'NA'
		cc['a'] = 'NA'
		cc['b'] = 'NA'
	
	#cursorObj.execute("SELECT id, name, address, salary from COMPANY")

	#FOR TOPICS IN DEEP LEARNING
	cur.execute("SELECT CBT1, CBT2 from university where SUBJECT = 'Topics in Deep Learning' and SRN = '%s'" % (srn))
	rows = cur.fetchall()
	if len(rows) > 0:
		print("hello")
		for row in rows:
			cbt1 = int(row[0])
			cbt2 = int(row[1])			
			total_score = cbt1+cbt2
		cursor_avg = cur.execute("SELECT avg(CBT1), avg(CBT2) from university where SUBJECT = 'Topics in Deep Learning'")
		for row in cursor_avg:
			avg_cbt_score = row[0]+row[1]

		
			
   		
		cursor_total_count = cur.execute("SELECT count(SRN) from university where SUBJECT = 'Topics in Deep Learning'")
		for row in cursor_total_count:
			total_count = int(row[0]) 
		
		cursor_percentile = cur.execute("SELECT count(SRN) from university where SUBJECT = 'Topics in Deep Learning' and CBT1 + CBT2 > %s" % (total_score))
		for row in cursor_percentile:
			higher_scorers_count = int(row[0])
		
		percentile_value = (total_count - higher_scorers_count)*100/total_count

		#now marks needed for top grades will be calculated
		sgrade = 88 - (total_score/2) if 88 - (total_score/2) <=60 else 'Not Possible' 
		agrade = 76 - (total_score/2) if 76 - (total_score/2) <=60 else 'Not Possible'
		bgrade = 64 - (total_score/2)	if 64 - (total_score/2) <=60 else 'Not Possible'
		
		#dictionary of results to be passed onto the html page is created
		tdl = {}
		tdl['avg'] = avg_cbt_score
		tdl['total'] = total_score
		tdl['perc'] = percentile_value
		tdl['s'] = sgrade
		tdl['a'] = agrade
		tdl['b'] = bgrade

	else:
		tdl = {}
		tdl['avg'] = 'NA'
		tdl['total'] = 'NA'
		tdl['perc'] = 'NA'
		tdl['s'] = 'NA'
		tdl['a'] = 'NA'
		tdl['b'] = 'NA'


	#FOR SYSTEM MODELLING
	cur.execute("SELECT CBT1, CBT2 from university where SUBJECT = 'System Modelling' and SRN = '%s'" % (srn))
	rows = cur.fetchall()
	if len(rows) > 0:
		print("hello")
		for row in rows:
			cbt1 = int(row[0])
			cbt2 = int(row[1])			
			total_score = cbt1+cbt2
		cursor_avg = cur.execute("SELECT avg(CBT1), avg(CBT2) from university where SUBJECT = 'System Modelling'")
		for row in cursor_avg:
			avg_cbt_score = row[0]+row[1]

		
			
   		
		cursor_total_count = cur.execute("SELECT count(SRN) from university where SUBJECT = 'System Modelling'")
		for row in cursor_total_count:
			total_count = int(row[0]) 
		
		cursor_percentile = cur.execute("SELECT count(SRN) from university where SUBJECT = 'System Modelling' and CBT1 + CBT2 > %s" % (total_score))
		for row in cursor_percentile:
			higher_scorers_count = int(row[0])
		
		percentile_value = (total_count - higher_scorers_count)*100/total_count

		#now marks needed for top grades will be calculated
		sgrade = 88 - (total_score/2) if 88 - (total_score/2) <=60 else 'Not Possible' 
		agrade = 76 - (total_score/2) if 76 - (total_score/2) <=60 else 'Not Possible'
		bgrade = 64 - (total_score/2)	if 64 - (total_score/2) <=60 else 'Not Possible'
		
		#dictionary of results to be passed onto the html page is created
		sms = {}
		sms['avg'] = avg_cbt_score
		sms['total'] = total_score
		sms['perc'] = percentile_value
		sms['s'] = sgrade
		sms['a'] = agrade
		sms['b'] = bgrade

	else:
		sms = {}
		sms['avg'] = 'NA'
		sms['total'] = 'NA'
		sms['perc'] = 'NA'
		sms['s'] = 'NA'
		sms['a'] = 'NA'
		sms['b'] = 'NA'
	
	final_result = {}
	final_result['cd'] = cd
	final_result['wt'] = wt
	final_result['cc'] = cc
	final_result['sms'] = sms
	final_result['tdl'] = tdl
	
	return(render_template("progress.html",SRN=srn,result=final_result))

@app.route('/')
def index():
	 return(render_template("index.html"))

if (__name__=="__main__"):
	 app.run(debug=True,port = 5010)
	

