import sqlite3
import random
from employee import Employee
from schedule import Scheduled
ID_SLOT = 4
DAY = 'Monday'

NUM_MANAGERS = 3
NUM_CSR = 8
NUM_STOCKER = 4
NUM_CASHIER = 5


common_first_names = ['James', 'Robert', 'John', 'michael', 'David', 'William', 'Richard', 'Joseph', 'Thomas', 'Christopher',
                'Charles', 'Daniel', 'Matthew', 'Antony', 'Mark', 'Donald', 'Steven', 'Andrew', 'Paul', 'Joshua']
common_last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodrigez', 'Martinez',
                     'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin']
titles = ['Manager', 'CSR', 'Stocker', 'Cashier',]

#Connect to memory
conn = sqlite3.connect(':memory:')
c = conn.cursor()

#Create tables
c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer,
            title text,
            id integer
            )""")
c.execute("""CREATE TABLE schedule (
            id integer,
            hours interger,
            day text
            )""")


#Employee table commands
def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees Values (:first, :last, :pay, :title, :id)", 
                  {'first': emp.first, 'last': emp.last, 'pay': emp.pay, 'title': emp.title, 'id' : emp.id})

def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()
    
def get_emps_by_title(title):
    c.execute("SELECT * FROM employees WHERE title=:title", {'title': title})
    return c.fetchall()

def get_num_of_emps_by_title(title, num):
    c.execute("SELECT * FROM employees WHERE title=:title ORDER BY random()", {'title': title, 'num': num})
    return c.fetchmany(num)

def get_emps_by_id(id):
    c.execute("SELECT * FROM employees WHERE id=:id", {'id': id})
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay 
                    WHERE first = :first AND last = :last""",
                    {'first': emp.first, 'last' : emp.last, 'pay': pay})

def remove_emp(id):
    with conn:
        c.execute("DELETE from employees WHERE id = :id",
                  {'id': id})
        

#Schedule commands
def get_scheduled_by_day(day):
    c.execute("SELECT * FROM schedule WHERE day=:day", {'day': day})
    return c.fetchall()

def insert_scheduled(sch):
    with conn:
        c.execute("INSERT INTO schedule Values (:id, :hours, :day)", 
                  {'id' : sch.id, 'hours': sch.hours, 'day': sch.day})
        


#Generate employees 
for i in range(40):
    first = random.choice(common_first_names)
    last = random.choice(common_last_names)
    title = titles[i % 4]
    pay = random.randint(1000, 10000)
    emp = Employee(first, last, pay, title, i)
    insert_emp(emp)

#Schedule people for Monday
managers = get_num_of_emps_by_title('Manager', NUM_MANAGERS)
for i in range(NUM_MANAGERS):
    sch = Scheduled(managers[i][ID_SLOT], 10, DAY)
    insert_scheduled(sch)

#Remove an employee 
all_csr = get_emps_by_title('CSR')
print('CSR before: ', all_csr)
print('_____________________________________________________')
fired = get_num_of_emps_by_title('CSR', 1)
remove_emp(fired[0][ID_SLOT])
all_csr = get_emps_by_title('CSR')
print('CSR after: ', all_csr)
print('_____________________________________________________')

csr = get_num_of_emps_by_title('CSR', NUM_CSR)
for i in range(NUM_CSR):
    sch = Scheduled(csr[i][ID_SLOT], 6, DAY)
    insert_scheduled(sch)
cashiers = get_num_of_emps_by_title('Cashier', NUM_CSR)
for i in range(NUM_CASHIER):
    sch = Scheduled(cashiers[i][ID_SLOT], 6, DAY)
    insert_scheduled(sch)
stockers = get_num_of_emps_by_title('Stocker', NUM_CSR)
for i in range(NUM_STOCKER):
    sch = Scheduled(stockers[i][ID_SLOT], 6, DAY)
    insert_scheduled(sch)

monday = get_scheduled_by_day(DAY)

print(monday)
print('_____________________________________________________')

c.execute("""SELECT 
            schedule.id,
            first,
            last,
            pay,
            title,
            hours

            FROM employees INNER JOIN schedule
            ON employees.id = schedule.id
            """)

joined = c.fetchall()

print(joined)
print('_____________________________________________________')



conn.close()