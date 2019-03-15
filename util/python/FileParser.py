import python.SqlHandler as sql


#checks is a string is a number
def is_number(s):
    try:
        x = float(s)    
    except ValueError:
        return False
    return True

#Parses The Species.dat file from user guide
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

                #combines the species name if it is more than 1 word   
                if is_number(attributes[i]) == False:
                    attributes[0] = attributes[0] + " " + attributes[i]
                    pops += 1
                    
                i += 1

            #removes redundent words that were combined
            for part in range(pops):
                attributes.pop(1)

            sql.SpeciesAttrToSQL(attributes)
          
    finally:
        f.close()
