# Still need to set up an events table. Then we'll fill this thing in.
import pyodbc


class EventsController:
    def __init__(self):
        self.cnxn = pyodbc.connect(
            "Driver={SQL Server};"
            "Server=MSI;"
            "Database=LoperSlamdUNKDB;"
            "Trusted_Connection=yes;"
        )

        # Our main connection to the server. Use this variable to interact with it through queries.
        self.cursor = self.cnxn.cursor()

    def printContent(self):
        # Go through each row in the currently selected data and print it out.
        # We can move to something Tkinter based quite easily from here.
        for row in self.cursor:
            print('%r' % (row,))


    def getEvents(self):
        self.cursor = self.cnxn.cursor()
        self.cursor.execute('SELECT * FROM Events')

        self.printContent()

    def getMonthEvents(self, month, year):
        self.cursor = self.cnxn.cursor()
        self.cursor.execute(f"SELECT Name, Date FROM Events WHERE SUBSTRING(Date, 1, 2) = '{month:02d}' AND SUBSTRING(Date, 7, 4) = '{year}'")

        monthEvents = []
        for row in self.cursor:
            monthEvents.append(row)
       # self.printContent()
        return monthEvents
    def addEventQuery(self, name, date, team):
        self.cursor = self.cnxn.cursor()
        self.cursor.execute("INSERT INTO Events (Name, Date, TeamID) VALUES ('" + name + "','" + date + "', '" + str(
            team) + "'); COMMIT;")



#events = EventsController()
#events.addEvent("First meet of the season", "03/01/2004", 1)

#print("This shows all the rows of the Athletes table!:")
#events.getMonthEvents(2004, 3)
