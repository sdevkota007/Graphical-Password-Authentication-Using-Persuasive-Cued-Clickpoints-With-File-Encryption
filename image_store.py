def read_file(filename):
    with open(filename, 'rb') as f:
        photo = f.read()
    return photo
from mysql.connector import MySQLConnection, Error
import mysql.connector

def update_blob(author_id, filename):
    # read file
    data = read_file(filename)

    # prepare update query and data
    query = "update image_data SET img_addr = %s WHERE img_id  = %s"

    args = (data, author_id)


    try:
        conn= mysql.connector.connect(host='localhost',database='python_mysql',user='root',password='2864')
        cursor = conn.cursor()
        cursor.execute(query, args)
        conn.commit()
        cursor.close()
        conn.close()
    except Error as e:
        print(e)
    finally:
        print('test')
        # cursor.close()
        # conn.close()


def main():
    update_blob(1, "1.png")
    update_blob(2, "2.png")
    update_blob(3, "3.png")
    update_blob(4, "4.png")
    update_blob(5, "5.png")
    update_blob(6, "6.png")
    update_blob(7, "7.png")
    update_blob(8, "8.png")
    update_blob(9, "9.png")
    update_blob(10, "10.png")
    update_blob(11, "11.png")
    update_blob(12, "12.png")



if __name__ == '__main__':
    main()


