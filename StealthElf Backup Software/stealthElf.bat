@ECHO OFF
set CLASSPATH=.
::Change path to location of StealthElf.jar on whatever computer is being used
set CLASSPATH=%CLASSPATH%;C:\Users\Jordan\IdeaProjects\StealthElf\out\artifacts\StealthElf_jar\StealthElf.jar

start cmd /k ""%JAVA_HOME%\bin\java" -Xms128m -Xmx384m -Xnoclassgc Main"