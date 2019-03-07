import sys, random, math

timeInc = 2
regionArea = 900

class Species:
    trees = []
    
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

    def NumberTreesInDiameterGroup(self, age, timestep):
        num = 0;
        for tree in self.trees:
            if tree.AgeCohort == age:
                num += 1

        return self.DBH(age, timestep), num

    def GrowSpace(self, timestep):
        result = 0
        for i in range(1, int(self.Longevity)//timestep):
            dbh, numberTrees = self.NumberTreesInDiameterGroup(i, timestep)
            result += ((dbh / 10) ** 1.605) * numberTrees * (1/(int(self.MaxStandDensity) * regionArea))
            
        print(self.Name + ": " + str(result))
        return result

    def DBH(self, ageCohort, timestep):
        age = ageCohort * timestep
        a = 1
        k = 1.5
        return int(self.MaxDiameter) * math.exp(-a * math.exp( -k * (age / int(self.Longevity))))
        

class Tree:
    def __init__(self, species, age):
        self.Species = species
        self.AgeCohort = age
    

def GenerateTrees():
    for s in array:
        for i in range(random.randint(500, 900)):
            s.trees.append(Tree(s, random.randint(0, int(s.Longevity)//timeInc)))

array = []

def is_number(s):
    try:
        x = float(s)    
    except ValueError:
        return False
    return True

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
                
            array.append(Species(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7], parts[8],
                                     parts[9], parts[10], parts[11], parts[12], parts[13], parts[14], parts[15], parts[16]))
            
    finally:
        f.close()
    ##    for i in array:
    ##        print(i.Name + " " + i.MaxDiameter)
    

#species is an area of species
def GSO(step):
    result = 0
    for s in array:
        result += s.GrowSpace(step)

    return result

LoadFile()
GenerateTrees()
print("Total GSO = " + str(GSO(2)))
