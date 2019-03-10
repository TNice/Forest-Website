import mysql.connector as mysql

#print(mydb)

mydb = ""

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

def is_number(s):
    try:
        x = float(s)    
    except ValueError:
        return False
    return True

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

def SpeciesAttr(file="uploads/species.dat"):
    try:
        f = open(file)
        for line in f:
            if '#' in line:
                continue

            attributes = line.split(' ')
            if '\n' in attributes:
                attributes.remove('\n')

            i = 0
            pops = 0
            for attr in attributes:
                if i == 0:
                    i += 1
                    continue
                    
                if is_number(attributes[i]) == False:
                    attributes[0] = attributes[0] + " " + attributes[i]
                    pops += 1
                    
                i += 1

            for part in range(pops):
                attributes.pop(1)
                
            SpeciesAttrToSQL(attributes)
          
    finally:
        f.close()
