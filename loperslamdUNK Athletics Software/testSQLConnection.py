







#This file will be used to ensure we can properly connect to our SQL database. We will probably run the SQL database locally so it is easier to connect to through the Python executable. Some additional settings will have to be changed to host our Microsoft SQL Server with Internet access. - Blake

# Example from https://stackoverflow.com/questions/33725862/connecting-to-microsoft-sql-server-using-python :


#Note!: For running your own tests to see if you can get a server set up, you may have to change the Server name and Database name... these settings are specific to my PC.

#Determine your interpreter's file path...:
# import sys
# print(sys.version)
# print(sys.executable)

import pyodbc
cnxn = pyodbc.connect("Driver={SQL Server};"
                      "Server=LAPTOP-3JNM76RU;"
                      "Database=LoperSlamdUNKDB;"
                      "Trusted_Connection=yes;")
#Another note: we will have to put a username and password on here when we make it accessible via the Internet.

cursor = cnxn.cursor()
cursor.execute("INSERT INTO dbo.Teams (Name, Description) VALUES ('Example Team Name', 'We are the example team!')")
cursor.execute('SELECT * FROM dbo.Teams')

for row in cursor:
    print('row = %r' % (row,))
