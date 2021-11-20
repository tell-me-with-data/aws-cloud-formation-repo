import boto3
import csv
import psycopg2
from myconfig import *

def insert_data(category_tuple):
    conn = None
    try:
        conn = psycopg2.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
        cur = conn.cursor()
        sql = """INSERT INTO production.category(category_id, category_name, load_date) VALUES(%s,%s, CURRENT_DATE);"""
        cur.execute(sql, category_tuple)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    bucket='raw-data-sales-db'
    key='raw-stage/categories.csv'
    csv_obj = s3.Object(bucket,key)
    data = csv_obj.get()['Body'].read().decode('utf-8').splitlines()
    lines = csv.reader(data, delimiter=';')
    headers = next(lines)
    for line in lines:
        insert_data(tuple(line))