import sys, random, math
import matplotlib.pyplot as plt
import numpy as np

timeInc = 2 #timestep for simulation
regionArea = 900 #region area of our single cell test space (30m x 30m)
speciesArray = [] #array of species
numTree = 0 #number of trees

#variables for matplotlib graphs
pieFile = "graphs/pie.png"
barFile = "graphs/bar.png"
pieLabels = 'Pine', 'Cedar', 'Red Oak', 'White Oak', 'Hickory', 'Maple', 'Elm','Pseudosp'
barLabels = 'Pine', 'Cedar', 'Red Oak', 'White Oak', 'Hickory', 'Maple', 'Elm','Pseudosp', 'Region'
values = []
explode = (0, 0, 0, 0, 0, 0, 0, 0)
N = 9
GSOValues = []
ind = np.arange(N)
width = 0.5
#end matplotlib

class Species:
    trees = [] #array of all trees in species 
    #all attributes are from SpeciesAttrInput file in the user guide
    def __init__(self, name, long, matur, shade, fire, effd, MaxD, veg_p, MinVp, MaxVp, rcls, spt1, spt2, MaxDbh, MaxSdi, totseed, carbonco):
        self.Name = name
        self.Longevity = long
        self.MaturityAge = matur
        self.ShadeTolerance = shade
        self.FireTolerance = fire
        self.EffectiveSeedingDistance = effd
        self.MaxSeedingDistance = MaxD
        self.VegitativeProbability = veg_p
        self.MinResproutAge = MinVp
        self.MaxResproutAge = MaxVp
        self.ReclassCoefficient = rcls
        self.SpeciesType = spt1
        self.BiomassType = spt2
        self.MaxDiameter = MaxDbh
        self.MaxStandDensity = MaxSdi
        self.NumberSeeds = totseed
        self.CarbonCoeffiecent = carbonco

    #Calculates The Number of Trees in a diameter group (currently using the age cohort to group since DBH is determined by age)
    def NumberTreesInDiameterGroup(self, age, timestep):
        num = 0;
        for tree in self.trees:
            if tree.AgeCohort == age:
                num += 1

        return self.DBH(age, timestep), num #returns the DBH of the group along with the number of trees in the group

    #GSO for a species according to user guide formula
    def GrowSpace(self, timestep):
        result = 0
        for i in range(1, int(self.Longevity)//timestep):
            dbh, numberTrees = self.NumberTreesInDiameterGroup(i, timestep)
            result += ((dbh / 10) ** 1.605) * numberTrees * (1/(int(self.MaxStandDensity) * regionArea))
            
        #print(self.Name + ": " + str(result))
        return result

    #DBH for species according to user guide formula
    def DBH(self, ageCohort, timestep):
        age = ageCohort * timestep
        #constants of the DBH equasion. User guided didnt have any values or say where they came froms so these are placeholder values
        a = 1 
        k = 1.5
        #end constants
        return int(self.MaxDiameter) * math.exp(-a * math.exp( -k * (age / int(self.Longevity))))
        

class Tree:
    def __init__(self, species, age):
        self.Species = species
        self.AgeCohort = age
    
#generates a some what randomized tree set for each species to test simulation
def GenerateTrees():
    for s in speciesArray:
        numTree = random.randint(500, 900)
        values.append(numTree)
        for i in range(numTree):
            s.trees.append(Tree(s, random.randint(0, int(s.Longevity)//timeInc)))

#checks if string is a number
def is_number(s):
    try:
        x = float(s)    
    except ValueError:
        return False
    return True

#parses the SpeciesAttrInput file format into the species array. (will modify for database once the database is ready)
def LoadFile():
    try:
        f = open("uploads/test.txt")
            
        for line in f:
            if '#' in line:
                continue

            parts = line.split(' ')
            if '\n' in parts:
                parts.remove('\n')

            i = 0
            pops = 0
            for part in parts:
                if i == 0:
                    i += 1
                    continue
                    
                if is_number(parts[i]) == False:
                    parts[0] = parts[0] + " " + parts[i]
                    pops += 1
                    
                i += 1

            for part in range(pops):
                parts.pop(1)

            #print(parts)
                
            speciesArray.append(Species(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7], parts[8],
                                     parts[9], parts[10], parts[11], parts[12], parts[13], parts[14], parts[15], parts[16]))
          
    finally:
        f.close()
    

#GSO for the region according to user guide formula. Also extracting species GSOs here for graphs
def GSO(step):
    result = 0
    for s in speciesArray:
        grow = s.GrowSpace(step)
        GSOValues.append(grow)
        result += grow

    GSOValues.append(result)
    return result

LoadFile()
GenerateTrees()
gsoResult = GSO(2)

if len(sys.argv) == 2:
    pieFile = "graphs/pie" + sys.argv[1] + ".png"
    barFile = "graphs/bar" + sys.argv[1] + ".png"

#creates .png files of the graphs
fig1, ax1 = plt.subplots()
ax1.pie(values, explode=explode, labels=pieLabels, autopct='%1.1f%%', shadow=False, startangle=90)
ax1.axis('equal')
plt.savefig(pieFile)

fig1, ax1 = plt.subplots()
plot = plt.bar(ind,GSOValues, width)

plt.title('Title')
plt.xticks(ind, (barLabels))
plt.yticks(np.arange(0, 1, .05))
fig1.autofmt_xdate()
plt.savefig(barFile)

print("DONE")
