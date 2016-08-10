README:
------

How to Use:

1. Put sdextract.csv and landesk.csv in the directory (ensure that they are saved properly)
2. launch GUI.EXE
3. Enter parameters
	Note: Using a comma like "Project,Standard" will find all software with the words Project and Standard
	in their titles.
4. Generate the Report
5. Notice the progress on the console window
6. Open testOutput.html


Checking for Errors:

If you notice any oddities a quick rule to confirm the accuracy results is as follows:

Accurate Records + Problem Installs = # of LANDesk records in landesk.csv
Accurate Records + Unused Records   = # of Software Database records in sdextract.csv (that match your query of course)

Makes use of this sorting framework: http://www.kryogenix.org/code/browser/sorttable/
