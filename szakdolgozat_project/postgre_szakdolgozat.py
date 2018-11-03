import psycopg2
from psycopg2 import Error
from urllib.parse import urlparse, urljoin
import datetime
import json

def postgres_authorize(pgpw):
    try:
        conn = psycopg2.connect(user = 'postgres', password = pgpw, host = '127.0.0.1', port = '5432', database = 'szakdolgozat', connect_timeout = 5)
        conn.close()
        return True
    except:
        return False	
	
def get_for_validation(pgpw, arg):
	try:
		connection = psycopg2.connect(user = 'postgres', password = pgpw, host = '127.0.0.1', port = '5432', database = 'szakdolgozat')
		print_log('[postgre connection] INFO: PostgreSQL connection is open')
		cursor = connection.cursor()

		url = urljoin(arg, '/')
		cursor.execute('SELECT * FROM accepted_sources WHERE url=%s;', (url,))
		record = cursor.fetchone()

		if record is None:
			print_log('[postgre select] INFO: Validation failed for requested URL')
		else:
			print_log('[postgre select] INFO: Validation succeeded for requested URL')
		return record
		
	except (Exception, psycopg2.DatabaseError) as error:
		print_log('[postgre error] ERROR: Error while connecting to PostgreSQL '.format(error))
		return None
		
	finally:
		if(connection):
			cursor.close()
			connection.close()
			print_log('[postgre connection] INFO: PostgreSQL connection is closed')

def get_from_db(pgpw, arg):
	try:
		connection = psycopg2.connect(user = 'postgres', password = pgpw, host = '127.0.0.1', port = '5432', database = 'szakdolgozat')
		print_log('[postgre connection] INFO: PostgreSQL connection is open')
		cursor = connection.cursor()
		cursor.execute('SELECT response FROM scrapytable WHERE url=%s;', (arg,))
		record = cursor.fetchone()
		
		if record is None:
			print_log('[postgre select] INFO: Row not found in table')
			return None
		print_log('[postgre select] INFO: Row selected from table')
		return (json.dumps(record[0])).encode('utf-8')
		
	except (Exception, psycopg2.DatabaseError) as error:
		print_log('[postgre error] ERROR: Error while connecting to PostgreSQL '.format(error))
		return None
		
	finally:
		if(connection):
			cursor.close()
			connection.close()
			print_log('[postgre connection] INFO: PostgreSQL connection is closed')
			
def insert_to_db(pgpw, arg, response, record):
	try:	
		connection = psycopg2.connect(user = 'postgres', password = pgpw, host = '127.0.0.1', port = '5432', database = 'szakdolgozat')
		print_log('[postgre connection] INFO: PostgreSQL connection is open')
		cursor = connection.cursor() 
		cursor.execute('INSERT INTO scrapytable (url, response, source_id) VALUES( %s, %s, %s);', (arg,(json.dumps(response)), record[0]))
		connection.commit()
		print_log('[postgre insert] INFO: Record inserted successfully into table')
		
	except (Exception, psycopg2.DatabaseError) as error:
		if(connection):
			connection.rollback()
			print_log('[postgre error] ERROR: Failed inserting record into table {}'.format(error))
			
	finally:
		if(connection):
			cursor.close()
			connection.close()
			print_log('[postgre connection] INFO: PostgreSQL connection is closed')
			
def delete_related_spiders(pgpw, arg):
	try:	
		connection = psycopg2.connect(user = 'postgres', password = pgpw, host = '127.0.0.1', port = '5432', database = 'szakdolgozat')
		print_log('[postgre connection] INFO: PostgreSQL connection is open')
		cursor = connection.cursor() 
		cursor.execute('DELETE FROM scrapytable s WHERE s.source_id IN (SELET id FROM accepted_sources WHERE spider = %s);', (arg))
		connection.commit()
		print_log('[postgre delete] INFO: Records successfully deleted from table')
		
	except (Exception, psycopg2.DatabaseError) as error:
		if(connection):
			connection.rollback()
			print_log('[postgre error] ERROR: Failed deleting from table {}'.format(error))
			
	finally:
		if(connection):
			cursor.close()
			connection.close()
			print_log('[postgre connection] INFO: PostgreSQL connection is closed')
			
			
def print_log(arg):
	print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S ') + arg)
	
def print_delimiter():
	print('==============================================================================================================')