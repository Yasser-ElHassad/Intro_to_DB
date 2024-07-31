import mysql.connector
try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = 'root',
        passwd = 'root'
        
    )
    cursor = mydb.cursor()
    cursor.execute("create database alx_book_store")
    mydb.commit()

    print(f"Database 'alx_book_store' created successfully!")
    mydb.close()


except:
    print(f'Database creation failed!')

