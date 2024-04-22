class MessagesCtoAController:
    def __init__(self,cnxn):
        self.cnxn = cnxn
        self.cursor = self.cnxn.cursor()

    def printContent(self):
        # Go through each row in the currently selected data and print it out.
        # We can move to something Tkinter based quite easily from here.
        for row in self.cursor:
            print('row = %r' % (row,))


    def getMessagesCtoA(self):
        self.cursor = self.cnxn.cursor()
        self.cursor.execute('SELECT * FROM MessagesCtoA')
        return self.cursor.fetchall()

    def getMessageCtoA(self, id):
        self.cursor = self.cnxn.cursor()
        self.cursor.execute("SELECT * FROM MessagesCtoA where MessageID = '"+str(id)+"'")
        return self.cursor.fetchall()

    def addMessageCtoA(self, subject, description, coachId, athlete):
        self.cursor = self.cnxn.cursor()
        try:
            self.cursor.execute(
                "INSERT INTO MessageCtoA (Subject, Description, CoachID, AthleteID) VALUES "+
                "('"+subject+"', '"+description+"', '"+str(coachId)+"', '"+str(athlete)+"'); COMMIT;"
            )
        except:
            return False
        else:
            return True
    def removeMessageCtoA(self, id):
        self.cursor = self.cnxn.cursor()
        try:
            self.cursor.execute("DELETE FROM MessagesCtoA where MessageID = '"+str(id)+"'; COMMIT;")
        except:
            return False
        else:
            return True
        
    def updateMessageCtoA(self, id, colNames = [], colVals = []):
        if len(colNames) != len(colVals):
            return "Column name / value mismatch. Ensure same # of values for both!"
        self.cursor = self.cnxn.cursor()
        try:
            updateString = "UPDATE MessagesCtoA "
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