# This will be the communication class
# Dylan will begin coding the communication
import tkinter as tk
from tkinter import Label

import os
import pyodbc
#--- Standard table imports we will all be using...
from Table_Athletes import AthletesController
from Table_Coaches import CoachesController
# from Table_Events import EventsController
from Table_MessagesCtoA import MessagesCtoAController
from Table_MessagesCtoT import MessagesCtoTController
from Table_Teams import TeamsController
#---

# Blake note: We will need different behavior for athletes and coaches. Let's assume we're working with a coach for now.
# Let's hardcode some variables in here so we can actually send messages to the SQL server. We really need an Authentication controller or something.
# If you run this, make sure to put some entries manually into the SQL Server if necessary.

class Communication:
    def __init__(self):
        #--- Hard-coded variables to allow sending of announcements
        self.authType = 2                   # 1 for athlete, 2 for coach
        self.userId = 1                     # ID 1 being the first ID in the coach table
        #---
        #--- Stuff for connecting with the SQL Server
        # change settings to my own
        # change to try to get to work with .env file
        driverStr = os.environ.get('DRIVER') or "{SQL Server}"
        serverStr = os.environ.get('SERVER') or "BERNTTOAST"
        databaseStr = os.environ.get('DATABASE') or "loperslamdUNK"
        trustedConStr = os.environ.get('TRUSTED_CONNECTION') or "yes"
        print("Driver="+driverStr+";")
        print("Server="+serverStr+";")
        print("Database="+databaseStr+";")
        print("Trusted_Connection="+trustedConStr+";")
        self.cnxn = pyodbc.connect(
            "Driver="+driverStr+";"
            "Server="+serverStr+";"
            "Database="+databaseStr+";"
            "Trusted_Connection="+trustedConStr+";"
        )
        # self.cursor = self.cnxn.cursor()
        #---
        self.window = tk.Tk()
        self.on_screen = []
        self.announcement_list = []
        self.window.title("Communication")
        self.window.geometry(f'{self.window.winfo_screenwidth() // 4}x{self.window.winfo_screenheight() // 3:.0f}')

    def reset_for_communicate(self):
        # Clear The Screen_________
        for item in self.on_screen:
            item.pack_forget()
        self.on_screen = []
        # Title____________________________________________________________
        communication_title = Label(self.window, text="COMMUNICATE", font=("litera", 25), pady=10)
        self.on_screen.append(communication_title)
        communication_title.pack()

        # Adds textbox to comm page, sends it to the SQL server
        comm_textbox = tk.Entry(self.window, width=40)
        self.on_screen.append(comm_textbox)
        comm_textbox.pack()
        send_button = tk.Button(self.window, text="Send announcement",
                                command=lambda: self.send_announcement(comm_textbox))
        self.on_screen.append(send_button)
        send_button.pack()

    def send_announcement(self, comm_textbox):
        announce = comm_textbox.get()
        if announce:
            # Code to communicate with SQL server
            if self.authType == 2:
                coachController = CoachesController(cnxn=self.cnxn)
                teamController = TeamsController(cnxn=self.cnxn)
                msgController = MessagesCtoTController(cnxn=self.cnxn)
                
                # - If there are no coaches, create one.
                coaches = coachController.getCoaches()
                if not coaches:
                    coachController.addCoach("First Coach", "Example description")

                CoachID = coachController.getCoaches()[0][0]
                print(CoachID)
                # - If there are no teams, create one.
                teams = teamController.getTeams()
                if not teams:
                    teamController.addTeam("First Team", "Example description")

                TeamID = teamController.getTeams()[0][0]
                print(TeamID)
                # - If there is no connection between the first coach and the first team, create one.
                teams = coachController.getTeams(CoachID)
                if not teams:
                    coachController.attachTeam(CoachID, TeamID) # change this value to something that works for you...

                # ---
                
                # Teams = coachController.getTeams(CoachID)
                # if Teams:
                # TeamID = coachController.getTeams(CoachID)[0] # will give an error if you don't have entry in CoachesTeams pivot table...
                # print("Team ID is:")
                # print(TeamID)

                result = msgController.addMessageCtoT(announce,announce,CoachID,TeamID)
                print(result)
                if not result:
                    print("uh oh, something went wrong with inserting.")
                else:
                    print("Successfully added new record to MessagesCtoT table. Coach ID: "+str(CoachID)+", Team ID: "+str(TeamID))
            # ---
            self.announcement_list.append(announce)
            comm_textbox.delete(0, tk.END)
            print("Announcement sent: ", announce)

# run_com_instance = Communication()
# run_com_instance.reset_for_communicate()
