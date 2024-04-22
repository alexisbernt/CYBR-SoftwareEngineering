## Executive Design Document

* Classes
  * Preset
    * Check if a preset already exists
    * Create a new preset
    * Load a preset
    * Delete a preset
  * CSVStorage
    * Storage for preset files
  * Backup
    * Copy file(s) or folder(s) using presets and paste into destination
  * Main
    * Show menus and take user inputs
    * Call methods from Backup and Preset
    * Zip file(s) or folder(s) and store into USB
   
* Objects

![Object Diagram](https://github.com/jschnell13/StealthElf/blob/main/Diagrams/UML_Object_Diagram.png "Object Diagram")

* Data formats
  * User inputs - string
  * Presets - csv
  * Backup files - zip
 
* User interactions
  * Input for selection of menus
  * Input for path of source and destination
  * Create preset files
