This is an universal script for parsing of RBS and\or RNC outputs recivied by AMOSBATCH utility.
For adding new functionality you need just to add additional arguments to amosbatch at start.sh file.
After that to develop new module *.py by using python (or any else) and include it to the start.sh
Do not forget to change the line below at smail.sh file:
SUBJECT="Ericson RBS data (licenses, e_tilt) report "
