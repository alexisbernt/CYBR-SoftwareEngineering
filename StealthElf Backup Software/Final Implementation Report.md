## Final Implementation Report
* Main.java - Complete
  * main - calls the methods corresponding to the selection.
  * runningCheck - asks users if they want to continue or exit.
  * showMenu
    * shows available menu and takes user input for selection.
    * validates user input.
  * vaildateFileLocation - checks whether the file exists at the location user entered.
  * manualSelcetion - selects file to backup manually.
 
* Preset.java - Complete
  * showPresets - shows presets in CSV file.
  * getRow - reads a row from CSV file.
  * checkPreset - checks whether the preset exists.
  * newPreset - creates a new preset
  * loadPreset - loads an existing preset.
  * deletePreset - deletes an existing preset.
  * validatePresetLocation - checks whether the CSV file exists at the location user entered.
 
* Backup.java - Complete
  * copyFile - copies a file entered by the user to the destination path.
  * validateDestinationPath - checks whether the destination path is valid.
  * validateBackupPath - checks whether the backup path is valid for manualSelection.
