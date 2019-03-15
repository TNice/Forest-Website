import sys, random, math
import matplotlib.pyplot as plt
import numpy as np
import RemoveFiles as rf
import python.FileParser as FileParser

timeInc = 2 #timestep for simulation

species = []

class Region:
    def __init__(self, area, speciesNum, treeNum)
        self.regionArea = area
        self.speciesArray = GenerateSpecies(self, speciesNum)
        self.numTree = treeNum
        self.trees = GenerateTrees()

    def GenerateSpecies(self, num):
        array = []
        for i in range(1, num):
            sindex = random.randint(0, num - 1)
            array.append(species[sindex])
        return array
    
    def GenerateTrees(self):
        array = []
        for s in self.speciesArray:
            numTreeInSpecies = random.randint(500, 900)
            for i in range(numTreeInSpecies):
                array.append(Tree(s, random.randint(0, int(s.Longevity)//timeInc)))

        return array

    #Calculates The Number of Trees in a diameter group (currently using the age cohort to group since DBH is determined by age)
    def NumberTreesInDiameterGroup(self, species, age, timestep):
        num = 0;
        for tree in trees:
            if tree.species == species:
                if tree.AgeCohort == age:
                    num += 1

        return self.DBH(age, timestep), num #returns the DBH of the group along with the number of trees in the group

    #DBH for species according to user guide formula
    def DBH(self, species, ageCohort, timestep, a = 1, k = 1.5):
        age = ageCohort * timestep
        #end constants
        return int(species.MaxDiameter) * math.exp(-a * math.exp(-k * (age / int(species.Longevity))))

    #GSO for a species according to user guide formula
    def GrowSpaceSpecies(self, species, timestep):
        result = 0
        for i in range(1, int(species.Longevity)//timestep):
            dbh, numberTrees = self.NumberTreesInDiameterGroup(i, species, timestep)
            result += ((dbh / 10) ** 1.605) * numberTrees * (1/(int(species.MaxStandDensity) * regionArea))
            
        #print(self.Name + ": " + str(result))
        return result

    #GSO for the region according to user guide formula. Also extracting species GSOs here for graphs
    def GSO(self, step):
        result = 0
        for s in self.speciesArray:
            grow = s.GrowSpace(step)
            result += grow
            
        return result

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
                
            speciesArray.append(Species(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7], parts[8],
                                     parts[9], parts[10], parts[11], parts[12], parts[13], parts[14], parts[15], parts[16]))
          
    finally:
        f.close()
    



LoadFile()
#transform: translateY(-100vh)

print("DONE")
