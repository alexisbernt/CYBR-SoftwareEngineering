## 4.3 - Requirements

**User Requirements**
-   In order for the users to use the system, they will need to have an understanding of (1) file paths and directories and (2) how to use a CLI interface. Additionally, they will need to provide a USB to be backed up.

**Hardware Requirements**
- Computer (the system will be written in Java, so it can be functional across a variety of machines)
- USB (user provided)

**Software Requirements**
- This software will be written in Java using Visual Studio.
- Deliverable will be an executable to run within a CLI interface.
- Writing to a .csv will be the method for storing system data initiated by the user. This will maintain a light, minimal system.
- Write a simple batch script to start the java program after clicking an icon

**Security Requirements**
- Use proven and popular Java libraries, try to avoid serialization.
- Hash user passwords, not logging sensitive information (for example not storing a user's documents/folders after process has completed).
- Prevent injection attack, watch for SQL injection opportunities.
- Make sure the file path given is valid.
source: https://www.guardrails.io/blog/12-java-security-best-practices/
- Watch out for user input (!!!) avoid user input when possible and protect against all user input. 
