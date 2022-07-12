					PARKING PROBLEM
					project @ IV 
					SOFTWARE ENGINEERING

--------------------------------------------------------About_Project---------------------------------------------------------------------

Parking Problem :
	This project comeup with an idea to solve temporary parking problem. The project is all about managing parking within a specific
	area. The project needs are given under and implemented which can be understood by instructions.


Briefly:	
	--------+        ------------+		------------+		------------+		-------------------+
	tab 1		 tab 2			tab 3			tab 4			tab 5
	Booking    --->  User Details  ------>  confirmation	----->	Insert Data	---->	Graphical Represent
						(via SMS)		(Data Base)		(parking)
	--------+	 ------------+		------------+		------------+		-------------------+


---------------------------------------------------------instuctions!! -------------------------------------------------------------------
Requirements:
	1. Python(interpreter)
		install python interpreter by: 
		(https://www.python.org/downloads/)

		now install sql connector by applying following command in command prompt
		(pip install mysql-connector-python)

	2. Mysql Database (ORACLE)
		install Mysql Server by:
		(https://dev.mysql.com/downloads/file/?id=511553)
		**NOTE: Just Click on "No thanks, just start my download."**
		
		simply install MYSQL Community which will trace you to host and connectors customisations, select as per your own.
	
	3. Visual Studio Code (VS Code)  **OPTIONAL**
		install vs code simplay by :
		(https://code.visualstudio.com/Download) **As per your own OS select linux, Mac Ios ,windows**
		
		Add extensions(Ctrl + Shift + X) in VS code Named as :
		(Python by microsoft, Pylance by microsoft, SQL Bindings by microsoft, SQL Database Projects by microsoft, SQL Server 
		(mssql) by  microsoft, SQLTools by  Matheus Teixeira)
	
	4. Python_Libraries
		Twilio for SMS
		(pip install twilio)
		
		tkinter for User Interface
		(pip install tkinter) **mostly installed with interpreter**

		turtle for Graphical Representations
		(pip install turtle) **mostly Already intsalled with interpreter**


------------------------------------------------------------MYSQL-------------------------------------------------------------------------
Launch MySql Common Line - Unicode
Enter Your Password

#Apply these commands before adding sql to project

	1. CREATE DATABASE park;

	2. CREATE TABLE parking(
	Vehicle_Number varchar(12),
	Owner_Name varchar(24),
	Vehicle_Type int(1),
	Contact_Number varchar(10)   //**NOTE: '_' may give error corresponding to version of sql installed**//
	);

	**Do check if table is created or not by command:
	(show tables;)**
