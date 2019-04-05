import sys, random, math
import RemoveFiles as rf
import Constants as const
#mport python.FileParser as FileParser
import json, Cells

species = []
cells = []

class Cell:
    def __init__(self, area, speciesNum, treeNum, lat, long):
        self.cellArea = area
        self.speciesArray = self.GenerateSpecies(speciesNum)
        self.numTree = treeNum
        self.trees = self.GenerateTrees()
        self.lat = lat
        self.long = long

    def GenerateSpecies(self, num):
        array = []
        for i in range(1, num):
            sindex = random.randint(0, len(species) - 1)
            while species[sindex] in array:
                sindex = random.randint(0, num - 1)
            array.append(species[sindex])
        return array
    
    def GenerateTrees(self):
        array = []
        treesLeft = self.numTree
        treeDispersalConst = 2
        i = 0
        for s in self.speciesArray:
            numTreeInSpecies = random.randint(self.numTree // (len(self.speciesArray) + treeDispersalConst), self.numTree // len(self.speciesArray))
            if numTreeInSpecies > treesLeft or i >= len(self.speciesArray):
                numTreeInSpecies = treesLeft
                        
            for i in range(numTreeInSpecies):
                array.append(Tree(s, random.randint(0, int(s.Longevity)//timestep)))
            
            i += 1

        return array

    #Calculates The Number of Trees in a diameter group (currently using the age cohort to group since DBH is determined by age)
    def NumberTreesInDiameterGroup(self, species, age, timestep):
        num = 0;
        for tree in self.trees:
            if tree.Species.Name == species.Name:
                if tree.AgeCohort == age:
                    num += 1
        
        return self.DBH(species, age, timestep), num #returns the DBH of the group along with the number of trees in the group

    #DBH for species according to user guide formula
    def DBH(self, species, ageCohort, timestep, a = 1, k = 1.5):
        age = ageCohort * timestep
        #end constants
        return int(species.MaxDiameter) * math.exp(-a * math.exp(-k * (age / int(species.Longevity))))

    #GSO for a species according to user guide formula
    def GrowSpaceSpecies(self, species, timestep):
        result = 0
        for i in range(1, int(species.Longevity)//timestep):
            dbh, numberTrees = self.NumberTreesInDiameterGroup(species, i, timestep)
            #print(numberTrees)
            result += ((dbh / 10) ** 1.605) * numberTrees * (1/(int(species.MaxStandDensity) * self.cellArea))
            
        #print(species.Name + ": " + str(result))
        return result

    #GSO for the cell according to user guide formula. Also extracting species GSOs here for graphs
    def GSO(self, step):
        result = 0
        for s in self.speciesArray:
            grow = self.GrowSpaceSpecies(s, step)
            result += grow
            
        return result
    
    def AgeTrees(self):
        for tree in self.trees:
            tree.AgeCohort += 1

class Species: 
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
        

class Tree:
    def __init__(self, species, age):
        self.Species = species
        self.AgeCohort = age


timestep = 0
size = 0
variance = 0
nwLat = 0
nwLng = 0
seLat = 0
seLng = 0                        


#checks if string is a number
def is_number(s):
    try:
        x = float(s)    
    except ValueError:
        return False
    return True

#parses the SpeciesAttrInput file format into the species array. (will modify for database once the database is ready)
def LoadFile():
    #FileParser.SpeciesAttr to be used once algorithums are refactored for the database
    #FileParser.SpeciesAttr()
    try:
        f = open("uploads/species.dat")
            
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
                
            species.append(Species(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7], parts[8],
                                     parts[9], parts[10], parts[11], parts[12], parts[13], parts[14], parts[15], parts[16]))
          
    finally:
        f.close()

def GetCells():
    cellResults = Cells.GetCellsInSelectedRegion(nwLat, nwLng, seLat,seLng, size, variance)
    area = cellResults['northSide'] * cellResults['westSide']
    center = Cells.GetCellCenter()

    for cell in cellResults['cells']:
        cells.append(Cell(area, random.randint(2, 5), random.randint(7000, 9000), center[0], center[1]))

def RunSimulation(length=1):
    year = 1
    data = {}
    data['max'] = 1
    data['data'] = []
    while year <= length:
        i = 0;
        #print("Creating Json For Year " + str(year) + "...")
        for c in cells:
            gso = c.GSO(timestep)
            data['data'].append({
                'lat': c.lat,
                'lng': c.long,
                'gso': gso
            })
            string = "..." + str(int((i / len(cells)) * 100)) + "%" 
            #print(string)
            i += 1
        
        with open("results/gsoData" + str(year) +".json", 'w') as outfile:
            print("Writing: results/gsoData.json")
            json.dump(data, outfile)
            #print("JSON COMPLETE")

        for c in cells:
            c.AgeTrees()
        year += 1
    
if len(sys.argv) == 8:
    timestep = sys.argv[1]
    size = sys.argv[2]
    variance = sys.argv[3]
    nwLat = sys.argv[4]
    nwLng = sys.argv[5]
    seLat = sys.argv[6]
    seLng = sys.argv[7]
    GetCells()
    RunSimulation()
    print("Done")

else:
    print("Invalid Arguments")
