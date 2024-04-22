# This will be the randomizer class
import tkinter as tk
from tkinter import Label, messagebox
import random
from functools import partial

class RandomClass:
    def __init__(self):
        self.on_screen = []
    def add_name(self, root):
        # To add names
        name_entry = tk.Entry(root, width=30)  # entry widget for name input
        name_entry.pack(pady=10)
        return name_entry
    def add_name_to_list(self, name_entry, name_list):
        # To add the name to a list that will be displayed on GUI
        # name_entry, name_list = self.add_name(self.window)
        if name_entry:
            name_list.insert(tk.END, name_entry.get())
            name_entry.delete(0, tk.END)
    def select_random_name(self, name_list, selected_name_var=None):
        # Function to generate a random name that is entered into the listbox
        selected_name_var = tk.StringVar()
        if name_list.size() > 0:
            random_name = random.choice(name_list.get(0, tk.END))
            selected_name_var.set(f"Selected Name: {random_name}")
            tk.messagebox.showinfo("Selected Random Name", f"The randomly selected name is: {random_name}")
        else:
            selected_name_var.set(f"Error. No names entered.")
            tk.messagebox.showinfo("Error Screen", "Error. Ensure names are entered")

RandomClass()

# CODE TRYING TO IMPORT NAMES -------------

# def names_library():
#     # a function to store remember names that were entered in the past
#     csv_file_path = "names.csv"
#     # Write the list to a CSV file
#     with open(csv_file_path, mode="w", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow(["Stored Names"])  # Optional: Write a header row
#         for name in name_list.get(0, tk.END):
#             writer.writerow([name])
#
#
# def get_names_library():
#     # Working here to get last stored names from csv file to display back on page
#     file = open('names.csv')
#     type(file)
#     rows = []
#     with (open('names.csv', mode="r", newline="") as file):
#         csvreader = csv.reader(file)
#         header = next(csvreader)  # Optional: Read the header row
#         for row in csvreader:
#             rows.append(row)
#             if row:  # display past list
#                 name_list.insert(tk.END, row)
#                 name_entry.delete(0, tk.END)
#     # getting header and row to display in the terminal
#     # print(header)
#     # print(rows)
#
#
# label = tk.Label(root, text="welcome to loper slam dUNK!", font=('Helvetica', 16), fg=('yellow'))
# label.pack(pady=20)  # to change the text color of the label use the fg (foreground) option

# spacing3.pack(pady=0.5)

# # "Clear Names" button
# clear_button = tk.Button(root, text="CLEAR NAMES ABOVE", command=clear_names)
# clear_button.pack()
# spacing4 = tk.Label(root, text=" ")
# spacing4.pack(pady=0.5)

# # Remembering the list entered to store into names_library
# remember_button = tk.Button(root, text="REMEMBER CURRENT LIST DISPLAYED", command=names_library)
# remember_button.pack()
# spacing1 = tk.Label(root, text=" ")
# spacing1.pack(pady=0.5)
# # Pull up past (the last stored) names_library entered names
# get_stored_button = tk.Button(root, text="GET LAST STORED NAMES", command=get_names_library)
# get_stored_button.pack()
# spacing2 = tk.Label(root, text=" ")
# spacing2.pack(pady=0.5)
# # Result variable
# result_var = StringVar()