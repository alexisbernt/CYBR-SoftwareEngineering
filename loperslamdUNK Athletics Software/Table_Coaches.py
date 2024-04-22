class CoachesController:
    def __init__(self,cnxn):
        self.cnxn = cnxn
        self.cursor = self.cnxn.cursor()

    def printContent(self):
        # Go through each row in the currently selected data and print it out.
        # We can move to something Tkinter based quite easily from here.
        for row in self.cursor:
            print('row = %r' % (row,))


    def getCoaches(self):
        self.cursor = self.cnxn.cursor()
        self.cursor.execute('SELECT * FROM Coaches')
        return self.cursor.fetchall()

    def getCoach(self, id):
        self.cursor = self.cnxn.cursor()
        self.cursor.execute("SELECT * FROM Coaches where CoachID = '"+str(id)+"'")
        return self.cursor.fetchall()

    def addCoach(self, name, description):
        self.cursor = self.cnxn.cursor()
        try:
            self.cursor.execute("INSERT INTO Coaches (Name, Description) VALUES ('"+str(name)+"', '"+str(description)+"'); COMMIT;")
        except:
            return False
        else:
            return True

    def removeCoach(self, id):
        self.cursor = self.cnxn.cursor()
        try:
            self.cursor.execute("DELETE FROM Coaches where CoachID = '"+str(id)+"'; COMMIT;")
        except:
            return False
        else:
            return True
        
    def attachTeam(self, coach, team):
        self.cursor = self.cnxn.cursor()
        try:
            self.cursor.execute("INSERT INTO CoachesTeams (CoachID, TeamID) VALUES ('"+str(coach)+"', '"+str(team)+"'); COMMIT;")
        except:
            return False
        else:
            return True

    def detachTeam(self, coach, team):
        self.cursor = self.cnxn.cursor()
        try:
            self.cursor.execute("DELETE FROM CoachesTeams where CoachID = '"+str(coach)+"' and TeamID = '"+str(team)+"'; COMMIT;")
        except:
            return False
        else:
            return True
    
    def getTeams(self, coach):
        self.cursor = self.cnxn.cursor()
        self.cursor.execute("SELECT * FROM CoachesTeams where CoachID = '"+str(coach)+"'")
        return self.cursor.fetchall()
        
    def updateCoach(self, id, colNames = [], colVals = []):
        if len(colNames) != len(colVals):
            return "Column name / value mismatch. Ensure same # of values for both!"
        self.cursor = self.cnxn.cursor()
        try:
            updateString = "UPDATE Coaches "
            setString = ""
            whereString = " WHERE CoachID = '"+id+"'"
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