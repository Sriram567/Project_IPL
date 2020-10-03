import subprocess as sp
import pymysql
import pymysql.cursors


def option2():
    """
    Function to implement option 1
    """
    print("Not implemented")


def option3():
    """
    Function to implement option 2
    """
    print("Not implemented")


def option4():
    """
    Function to implement option 3
    """
    print("Not implemented")


def hireAnEmployee():
    """
    This is a sample function implemented for the refrence.
    This example is related to the Employee Database.
    In addition to taking input, you are required to handle domain errors as well
    For example: the SSN should be only 9 characters long
    Sex should be only M or F
    If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied
    HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
    """
    try:
        # Takes emplyee details as input
        row = {}
        print("Enter new employee's details: ")
        name = (input("Name (Fname Minit Lname): ")).split(' ')
        row["Fname"] = name[0]
        row["Minit"] = name[1]
        row["Lname"] = name[2]
        row["Ssn"] = input("SSN: ")
        row["Bdate"] = input("Birth Date (YYYY-MM-DD): ")
        row["Address"] = input("Address: ")
        row["Sex"] = input("Sex: ")
        row["Salary"] = float(input("Salary: "))
        row["Dno"] = int(input("Dno: "))

        query = "INSERT INTO EMPLOYEE(Fname, Minit, Lname, Ssn, Bdate, Address, Sex, Salary, Dno) VALUES('%s', '%c', '%s', '%s', '%s', '%s', '%c', %f, %d)" % (
            row["Fname"], row["Minit"], row["Lname"], row["Ssn"], row["Bdate"], row["Address"], row["Sex"], row["Salary"], row["Dno"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
def doprint():
    tmp = sp.call('clear', shell=True)
    print("1. Team")
    print("2. Player")
    print("3. Matches")
    print("4. Venue")
    print("5. Stage")
def routine():
    doprint()
    ch = int(input("Enter choice> "))
    tmp = sp.call('clear', shell=True)
    return ch 

def selection():
    ch = routine()
    return
     
def projection():
    ch = routine()
    return

def aggregation():
    ch = routine()
    return

def search():
    ch = routine()
    return
def modification_dispatcher(ch):
    return
def functionality_dispatcher(ch):
    if ch==1:
        selection()
    elif ch==2:
        projection()
    elif ch==3:
        aggregation()
    elif ch==4:
        search()
    else:
        print("Option given is invalid")
    return
    
def functionality():
    tmp = sp.call('clear', shell=True)
    # Here taking example of Employee Mini-world
    print("1. Selection")  # Hire an Employee
    print("2. Projection")  # Fire an Employee
    print("3. Aggregate")  # Promote Employee
    print("4. Search")
    ch = int(input("Enter choice> "))
    tmp = sp.call('clear', shell=True)
    functionality_dispatcher(ch)
    return 
def modification():
    tmp = sp.call('clear', shell=True)
    print("1. Insert")
    print("2. Delete")
    print("3. Update")
    ch = int(input("Enter choice> "))
    tmp = sp.call('clear', shell=True)
    modification_dispatcher(ch)
    return
def analysis():
    return
def dispatch(ch):
    
    if(ch == 1):
        functionality()
    elif(ch == 2):
        modification()
    elif(ch == 3):
        analysis()
    else:
        print("Error: Invalid Option")
    return

# Global
while(1):
    tmp = sp.call('clear', shell=True)
    
    # Can be skipped if you want to hard core username and password
    username = input("Username: ")
    password = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server 
        con = pymysql.connect(host='localhost',
                              user=username,
                              port=5005,
                              password=password,
                              db='IPLdb',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)
                # Here taking example of Employee Mini-world
                print("1. Functionalities")  # Hire an Employee
                print("2. Modification")  # Fire an Employee
                print("3. Analysis")  # Promote Employee
                print("4. Logout")
                try:
                    ch = int(input("Enter choice> "))
                    tmp = sp.call('clear', shell=True)
                    if ch == 4:
                        break
                    else:
                        dispatch(ch)
                        tmp = input("Enter any key to CONTINUE>")
                except:
                    print("Sorry the input is not a number")

    except:
        tmp = sp.call('clear', shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
