import pymysql
import os

    
def lambda_handler(event, context):
    try:
        endpoint = event["endpoint"]
        username = event["username"]
        password = event["password"]
        database_name = event["database_name"]
        port = event["port"]

        connection = pymysql.connect(
            host=endpoint,
            user=username,
            password=password,
            database=database_name,
            port=port
        )
        

        with connection.cursor() as cursor:
            sql = "SELECT * FROM clientes LIMIT 5;"
            cursor.execute(sql)
            result = cursor.fetchall()  
        
        connection.close()

        
        return {
            "statusCode": 200,
            "body": result
        }
    
    except Exception as e:
        return {
            "statusCode": 500,
            "body": e
        }