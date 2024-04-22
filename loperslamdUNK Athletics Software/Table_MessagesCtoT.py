class MessagesCtoTController:
    def __init__(self,cnxn):
        self.cnxn = cnxn
        self.cursor = self.cnxn.cursor()

    def printContent(self):
        # Go through each row in the currently selected data and print it out.
        # We can move to something Tkinter based quite easily from here.
        for row in self.cursor:
            print('row = %r' % (row,))


    def getMessagesCtoT(self):
        self.cursor = self.cnxn.cursor()
        self.cursor.execute('SELECT * FROM MessagesCtoT')
        return self.cursor.fetchall()

    def getMessageCtoT(self, id):
        self.cursor = self.cnxn.cursor()
        self.cursor.execute("SELECT * FROM MessagesCtoT where MessageID = '"+str(id)+"'")
        return self.cursor.fetchall()

    def addMessageCtoT(self, subject, description, coach, team):
        self.cursor = self.cnxn.cursor()
        try:
            self.cursor.execute(
                "INSERT INTO MessagesCtoT (Subject, Description, CoachID, TeamID) VALUES "+
                "('"+subject+"', '"+description+"', '"+str(coach)+"', '"+str(team)+"'); COMMIT;"
            )
        except:
            return False
        else:
            return True
    def removeMessageCtoT(self, id):
        self.cursor = self.cnxn.cursor()
        try:
            self.cursor.execute("DELETE FROM MessagesCtoT where MessageID = '"+str(id)+"'; COMMIT;")
        except:
            return False
        else:
            return True
        
    def updateMessageCtoT(self, id, colNames = [], colVals = []):
        if len(colNames) != len(colVals):
            return "Column name / value mismatch. Ensure same # of values for both!"
        self.cursor = self.cnxn.cursor()
        try:
            updateString = "UPDATE MessagesCtoT "
            setString = ""
            whereString = " WHERE MessageID = '"+id+"'"
            x = 0
            setString += "SET "+colNames[0]+" = "+colVals[0]
            colVals.pop(0)
            colNames.pop(0)
            for col in colNames:
                setString += ", SET "+col+" = "+colVals[x]
                x+=1
            self.cursor.execute(updateString+setString+whereString)
        except:
            return False
        else:
            return True