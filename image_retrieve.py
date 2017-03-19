import mysql.connector
from mysql.connector import Error, MySQLConnection
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QApplication, QDialog, QWidget, QMainWindow
import os

class imageRetrieve():
        def write_file(self,data, filename):
            with open(filename, 'wb') as f:
                f.write(data)

        def read_blob(self,author_id, filename):
            # select photo column of a specific author
            query = "SELECT img_addr FROM image_data WHERE img_id = %s"


            try:
                # query blob data form the authors table
                conn= mysql.connector.connect(host='localhost',database='python_mysql',user='root',password='2864')
                cursor = conn.cursor()
                cursor.execute(query, (author_id,))
                photo = cursor.fetchone()[0]

                # write blob data into a file
                self.write_file(photo, filename)

            except Error as e:
                errorstr = str(e)
                QtGui.QMessageBox.warning(self, 'Sorry!', errorstr)

            finally:
                cursor.close()
                conn.close()

        def main(self):
            self.read_blob(1, "1.png")
            self.read_blob(2, "2.png")
            self.read_blob(3, "3.png")
            self.read_blob(4, "4.png")
            self.read_blob(5, "5.png")
            self.read_blob(6, "6.png")
            self.read_blob(7, "7.png")
            self.read_blob(8, "8.png")
            self.read_blob(9, "9.png")
            self.read_blob(10, "10.png")
            self.read_blob(11, "11.png")
            self.read_blob(12, "12.png")

        def remove_images(self):
            os.remove("1.png")
            os.remove("2.png")
            os.remove("3.png")
            os.remove("4.png")
            os.remove("5.png")
            os.remove("6.png")
            os.remove("7.png")
            os.remove("8.png")
            os.remove("9.png")
            os.remove("10.png")
            os.remove("11.png")
            os.remove("12.png")

if __name__ == '__main__':
    imageRetrieve = imageRetrieve()
    imageRetrieve.main()

