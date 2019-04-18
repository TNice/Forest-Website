import mysql.connector as mysql

#connect to database and returns the database cursor
def ConnectDB(host="localhost", user="root", passwd="", db="foresttest"):
    try:
        return mysql.connect(
            host=host,
            user=user,
            passwd=passwd,
            database=db
        )
    except:
        print("Unable to connect to database")
        return null

#takes in results form query and returns true if obj is found in it
def DoesExist(results, obj):
    for r in results:
        if r[0] == obj:
            return True

    return False

def SpeciesAttrToSQL(attrs):
    try:
        mydb = ConnectDB()
    except:
        print("Cannot Connect To Database")
        return
    
    mycursor = mydb.cursor()

    mycursor.execute("SELECT SpeciesName FROM speciestest")
    results = mycursor.fetchall()

    if DoesExist(results, attrs[0]) == False:
        sql = "INSERT INTO speciestest (SpeciesName, Longevity, Matur, Shade, Fire, EFFD, MaxD, VegP, MinVp, MaxVP, Rcls, Spt1, Spt2, MaxDBH, MaxSdi, TotSeed, Carbonco) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (attrs[0], int(attrs[1]), int(attrs[2]), int(attrs[3]), int(attrs[4]), int(attrs[5]), int(attrs[6]), float(attrs[7]), int(attrs[8]),
               int(attrs[9]), float(attrs[10]), int(attrs[11]), int(attrs[12]), int(attrs[13]), int(attrs[14]), int(attrs[15]), float(attrs[16]))
        mycursor.execute(sql, val)
        mydb.commit()
    
        
    print(attrs)