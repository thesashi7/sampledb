import MySQLdb
from warnings import filterwarnings

### THIS IS TO REMOVE WARNINGS FROM "CREATE ___ IF NOT EXISTS"
filterwarnings('ignore', category = MySQLdb.Warning)

connection = MySQLdb.connect(host="localhost", user="root", passwd="thapaliya")

cursor = connection.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS ARTBASE;')

cursor.execute('USE ARTBASE;')

def createTables():
    sql_command = """
    CREATE TABLE IF NOT EXISTS ARTIST (
    AName VARCHAR(30) NOT NULL,
    Birthplace VARCHAR(40),
    Age INTEGER,
    Style VARCHAR(15),
    PRIMARY KEY (AName)
    );"""

    cursor.execute(sql_command)

    sql_command = """
    CREATE TABLE IF NOT EXISTS ARTWORK (
    Title VARCHAR(30),
    Year INTEGER,
    Type VARCHAR(20),
    Price INTEGER,
    AName VARCHAR(30),
    PRIMARY KEY (Title),
    FOREIGN KEY (AName) REFERENCES ARTIST (AName)
    );"""

    cursor.execute(sql_command)

    sql_command = """
    CREATE TABLE IF NOT EXISTS CUSTOMER (
    CustID INTEGER,
    CName VARCHAR(30),
    Address VARCHAR(40),
    Amount INTEGER,
    PRIMARY KEY (CustID)
    );"""

    cursor.execute(sql_command)

    sql_command = """
    CREATE TABLE IF NOT EXISTS GROUPS (
    GName VARCHAR(30),
    PRIMARY KEY (GName)
    );"""

    cursor.execute(sql_command)

    sql_command = """
    CREATE TABLE IF NOT EXISTS CLASSIFY (
    Title VARCHAR(30),
    GName VARCHAR(30),
    PRIMARY KEY (Title, GName),
    FOREIGN KEY (Title) REFERENCES ARTWORK (Title),
    FOREIGN KEY (GName) REFERENCES GROUPS (GName)
    );"""

    cursor.execute(sql_command)

    sql_command = """
    CREATE TABLE IF NOT EXISTS LIKE_GROUP (
    CustID INTEGER,
    GName VARCHAR(30),
    PRIMARY KEY (CustID, GName),
    FOREIGN KEY (CustID) REFERENCES CUSTOMER (CustId),
    FOREIGN KEY (GName) REFERENCES GROUPS (GName)
    );"""

    cursor.execute(sql_command)

    sql_command = """
    CREATE TABLE IF NOT EXISTS LIKE_ARTIST (
    CustID INTEGER,
    AName VARCHAR(30),
    PRIMARY KEY (CustID, AName),
    FOREIGN KEY (CustID) REFERENCES CUSTOMER (CustId),
    FOREIGN KEY (AName) REFERENCES ARTIST (AName)
    );"""

    cursor.execute(sql_command)

def deleteTables():
    '''Use this in case we need to reset our tables'''


    cursor.execute('DROP TABLE CLASSIFY;')
    cursor.execute('DROP TABLE LIKE_GROUP;')
    cursor.execute('DROP TABLE LIKE_ARTIST;')
    cursor.execute('DROP TABLE ARTWORK;')
    cursor.execute('DROP TABLE ARTIST;')
    cursor.execute('DROP TABLE CUSTOMER;')
    cursor.execute('DROP TABLE GROUPS;')


def addArtist(AName, Birthplace, Age, Style):
    cursor.execute('INSERT INTO ARTIST (AName, Birthplace, Age, Style) VALUES (%s,%s,%s,%s)', (AName, Birthplace, Age, Style))
    connection.commit()

def addCustomer(CName, Address, Amount):
    cursor.execute('INSERT INTO CUSTOMER (CName, Address, Amount) VALUES (%s,%s,%s,%s)', (CName, Address, Amount))
    connection.commit()


def addArtwork(Title, Year, Type, Price, AName):
    # need to check if the artist exists
    cursor.execute('INSERT INTO ARTWORK (Title, Year, Type, Price, AName) VALUES (%s,%s,%s,%s,%s)', (Title, Year, Type, Price, AName))

    connection.commit()

def addGroup(GName):
    cursor.execute('INSERT INTO GROUP (GName) VALUES (%s)', (GName))
    connection.commit()

def addClassify(Title, GName):
    cursor.execute('INSERT INTO ARTWORK (Title, GName) VALUES (%s,%s)', (Title, GName))
    connection.commit()

def addLikeGroup(CustID, GName):
    cursor.execute('INSERT INTO LIKE_GROUP (CustID, GName) VALUES (%s,%s)', (CustID, GName))
    connection.commit()

def addLikeArtist(CustID, AName):
    cursor.execute('INSERT INTO LIKE_ARTIST (CustID, AName) VALUES (%s,%s)', (CustID, AName))
    connection.commit()

def updateArtist():
    print "Updating Artist"
    aname = raw_input("Enter the name of the artist : ")
    style = raw_input("Enter the updated style:")
    #call update


def getArtists():
    query = "SELECT * FROM ARTIST"

    cursor.execute(query)

    results = cursor.fetchall()
    for r in results:
        print(r)


def getCustomers():
    query = "SELECT * FROM CUSTOMER"

    cursor.execute(query)

    results = cursor.fetchall()
    for r in results:
        print(r)


def getArtworks():
    query = "SELECT * FROM ARTWORK"

    cursor.execute(query)

    results = cursor.fetchall()
    for r in results:
        print(r)


def getGroups():
    query = "SELECT * FROM GROUPS"

    cursor.execute(query)

    results = cursor.fetchall()
    for r in results:
        print(r)


def getClassifies():
    query = "SELECT * FROM CLASSIFY"

    cursor.execute(query)

    results = cursor.fetchall()
    for r in results:
        print(r)


def getLikeGroups():
    query = "SELECT * FROM LIKE_GROUP"

    cursor.execute(query)

    results = cursor.fetchall()
    for r in results:
        print(r)


def getLikeArtists():
    query = "SELECT * FROM LIKE_ARTIST"

    cursor.execute(query)

    results = cursor.fetchall()
    for r in results:
        print(r)

def artist():
    print "\t\tAdding Artist"
    artist_name =  raw_input("Enter Aritst Name: ")
    birthplace = raw_input("Enter Birthplace: ")
    age = raw_input("Enter age: ")
    style = raw_input("Enter Style: ")
    addArtist(artist_name, birthplace, age, style)

def customer():
    print "\t\tAdding Customer"
    cname = raw_input("Enter Customer Name: ")
    address = raw_input("Enter Address: ")
    amount = raw_input("Enter amount: ")
    addCustomer(cname, address, amount)

def artwork():
    print "\t\tAdding Artwork"
    title = raw_input("Enter Title: ")
    year = raw_input("Enter Year: ")
    price = raw_input("Enter Price: ")
    tp = raw_input("Enter Type: ")
    aname = raw_input("Enter artist name: ")
    gnmae = raw_input("Enter group name: ")
    addArtwork(Title, Year, Type, Price, AName)
    #if group does not exist
    addGroup(gname)
    addClassify(title,gname)

def groupLike():
    print "\t\tAdding Group Like"
    custId = raw_input("Enter customer Id: ")
    gname = raw_input("Enter group name: ")
""" - if it doesn't exist
 - get all the titles (classifies) of that GName from classify
     - use the titles to returive the artist names of those titles
     - create entries in like artist with the customer id and artist names
     - create entry in the like group with cust id and gname"""

def retreive():
    print "\\tRetrieving records"
    print "\tEnter 1 to retrieve all Artists"
    print "\tEnter 2 to retrieve all Customers"
    print "\tEnter 3 to retrieve all Artwork"
    print "\tEnter 4 to retrieve all Group Likes"
    print "\tEnter 5 to retrieve all Artist Likes"
    print "\tEnter 6 to retrieve all Classify"
    user_inp = raw_input()
    if (user_inp == str(1)):
        getArtists()
    elif (user_inp == str(2)):
        getCustomers()
    elif (user_inp == str(3)):
        getArtworks()
    elif (user_inp == str(4)):
        getLikeGroups()
    elif (user_inp == str(5)):
        getLikeArtists()
    elif (user_inp == str(6)):
        getClassifies()

def promptUserInput():
    print "\nWELCOME to ArtBase by hype@2018\n"
    while True:
        print "\tEnter 1 to add an Artist"
        print "\tEnter 2 to add Customer"
        print "\tEnter 3 to add ArtWork"
        print "\tEnter 4 to add Group Like"
        print "\tEnter 5 to update style of an artist"
        print "\tEnter 6 to retrieve records"
        print "\tEnter 7 to exit"
        user_inp = raw_input()
        if (user_inp == str(7)):
            exit()
        elif (user_inp == str(1)):
            artist()
        elif (user_inp == str(2)):
            customer()
        elif (user_inp == str(3)):
            artwork()
        elif (user_inp == str(4)):
            groupLike()
        elif (user_inp == str(5)):
            updateArtist()
        elif (user_inp == str(6)):
            retreive()




def main():
    createTables()
    promptUserInput()


if __name__ == "__main__":
    main()

    ### THIS IS A BASIC TEST
    '''
    createTables()
    addArtist("Test Test", "San Diego, CA", 24, "Test2 Test2")
    getArtists()
    deleteTables()
    '''
