## This is the Security Design Documentation

Our backup software will be capable of being opened through an icon that the user can click (visable on the user's computer screen).
When the icon is clicked, the software will open in terminal. 
Once in terminal, the user will be prompted:
  1. The user will be asked if they would like a preset. The user will be able to select from a numbered list. The numbered list will list the preset options (use pre-exsisting preset, create new, no preset/don't save).
  2. The program will then ask for the user's preset selection. This will also be entered by the user into the terminal as a number.
      Descriptions will be listed and assigned to numbers in the terminal. The user will then select a number.
  3. There will be a prompt for the user to enter a file path. The user will physically copy and paste a file path into the terminal.
      There will be two file paths that must be entered by the user. First, the source path. Second, the destination path.
  4. There will be a prompt to ask user if they want to save the preset they have used while using the program. This will be a yes/no prompt.
      If yes, the user will input a name for their preset. This user input will then be stored (along with the preset data) to a CSV document. 
  5. There will then be a restart or exit option. The user will be prompted to enter one of two options signaling for the program to run again or break.

  Between the user entering the file paths (source path and destination path), the backup functionality will be implemented. The user's files/folder
  given within the source path will be backed up to the given destination file path. There will not be a prompt for any of this though. This is the program's core functionality.
  The only instances of user input are designated within the 4 steps above.

Security Specifics:
  For Part 1.
    a. Security to ensure user input is a valid number. Determine valid number choices. Check to see if user entry is one of valid number choices.
  For Part 2. 
    b. Security to ensure user input is a valid number. Determine valid number choices. Check to see if user entry is one of valid number choices.
  For Part 3.
    c. User will enter a file path into terminal.
      i. Make sure file path exsists/ is valid
      ii. Make sure file path does not contain threats 
    c. Process to enter file path will occur x2. User must enter both source and destination file paths.
      i. Make sure file path exsists/ is valid
      ii. Make sure file path does not contain threats 
  For Part 4.
    d. Security to ensure user input is a valid choice. Either a "y" or a "n" option. 
      i. Additional security will be needed to secure CSV document. Only want user to be able to access CSV document that stores presets when "y" entered. 
          The only access the user should have to the CSV preset document is when they are writing preset data (for storage) to the CSV document. 
          Otherwise the user should have NO capability of accessing the preset data document. 
  For Part 5.
    e. Security to ensure user input is a valid option (either rerun or exit option). Rerun starts process over again. Exit breaks the program. 
