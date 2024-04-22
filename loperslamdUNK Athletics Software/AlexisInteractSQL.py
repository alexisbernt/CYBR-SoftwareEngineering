import pyodbc
from Table_Teams import TeamsController

# Establish a connection to the database
# DRIVER={SQL Server};SERVER=your_server;DATABASE=your_database;UID=username;PWD=password
# File location: "C:\Program Files (x86)\Microsoft SQL Server Management Studio 20\Common7\IDE\Ssms.exe"
# cnxn stands for the database connection object (which will allow queries and commands)
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=BERNTTOAST;Database=loperslamdUNK;Trusted_Connection=yes')

# Creating instance of the TeamsController class
teams_controller = TeamsController(cnxn)

# Call the addTeam method to insert a new team / the roster
title_name = "UNK Womens Basketball" # Uses apostrophe in SQL so that closes it out
roster = "Riley Jensen, Kia Wilson, Jordan Sears, Brinly Christensen, Macy Bryant"
success = teams_controller.addTeam(title_name, roster)

# print to terminal if the insertion was successful
# if success:
#     print("Team added successfully.")
# else:
#     print("Failed to add team.")

