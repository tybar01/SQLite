# Overview

This software generates a database of random employees and adds them to a table. It then takes from that employee table and schedules a number of those employees for a day of work. The day of work is another table. 

This software was built to understand the basics of SQLite and apply it in a way that could be used in a large scale buisnees scale. 

[Software Demo Video](https://youtu.be/p_DCvmLuXWQ)

# Relational Database

The database that I'm using is an employee that has an employee id. The employee has a first name, last name,
pay, job title, and an id.

The schedule class has a employee id, a number of hours worked that day, and a day they work on. The id is the common key between both 
tables and is used to link the data to the other table. 


# Development Environment

In this project I used visual studio code running SQLite to trim down on new programs runnings

In SQLite we use SQL commands that are executed in a python style environment. In order to manage
this we need to swap between the SQL syntax in strings for commands and python syntax. 
# Useful Websites

{Make a list of websites that you found helpful in this project}

- [sqlitetutorial](https://www.sqlitetutorial.net/)
- [Youtube tutorial](https://www.youtube.com/watch?v=pd-0G0MigUA&t=931s&ab_channel=CoreySchafer)

# Future Work

- Add more tables with key values.
- Impliment more python functions for easier readability
- Figure output for common full SQL programs. 
