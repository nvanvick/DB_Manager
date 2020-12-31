import sqlite3
import os

def version():
	try:
		print(sqlite3.version)
	except Exception as e:
		print(e)
	
def version_info():
	try:
		print(sqlite3.version_info)
	except Exception as e:
		print(e)

def connect():
	try:
		database = input('db>')
		return sqlite3.connect(database),database
	except Exception as e:
		print(e)
	
def execute():
	try:
		data = connection.cursor().execute(input('SQL> ')).fetchall()
		for row in data:
			print(row)
	except Exception as e:
		print(e)

def commit():
	try:
		connection.commit()
	except Exception as e:
		print(e)

def close():
	try:
		connection.close()
	except Exception as e:
		print(e)
		
function_dict = {'version':version, 'version_info':version_info, 'connect':connect, 'execute':execute, 'commit':commit, 'close':close, 'quit':quit}
connection = None
database = ''

while True:
	function = input(database+'>')
	if function == 'connect':
		connection_data = connect()
		connection = connection_data[0]
		database = connection_data[1]
	elif function == 'close':
		close()
		database = ''
	else:
		try:
			function_dict[function]()
		except Exception as e:
			print('Function '+str(e)+' does not exist')