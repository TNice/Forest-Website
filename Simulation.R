MyObject <- setRefClass("MyObject",
                        fields = list(name = "character", age = "numeric"),
                        methods = list(
                          getPrinter = function() {
                            MyPrinter$new(obj=.self)
                          }
                        )
)
Cell <- setRefClass("Cell", 
                    fields = list(cellArea = "numeric", speciesArray, GenerateSpecies, numTree = "numeric", trees, lat = "numeric", long = "numeric"),
                    methods = list
                    (init = function(self, area, speciesNum, treeNum, lat, long){
                        MyCell$new(obj=.self)
                    },
                    GenerateSpecies = function(self, num){
                      
                    },
                    GenerateTrees = function(self){
                      
                    },
                    NumberTreesInDiameterGroup = function(self, species, age, timestep){
                      
                    },
                    DBH = function(self, species, ageCohort, timestep, a = 1, k = 1.5){
                      
                    },
                    GrowSpaceSpecies = function(self, species, timestep){
                      
                    },
                    GSO = function(self, step){
                      
                    },
                    AgeTrees = function(self){
                      
                    }
                      ))

Species <- setRefClass("Species", 
                    fields = list(Name, Longevity, MaturityAge, ShadeTolerance, FireTolerance, EffectiveSeedingDistance, MaxSeedingDistance, VegitativeProbability, MinResproutAge, MaxResproutAge, ReclassCoefficient, SpeciesType, BiomassType, MaxDiameter, MaxStandDensity, NumberSeeds, CarbonCoefficient)),
                    methods = list
                    (init = function(self, name, long, matur, shade, fire, effd, MaxD, veg_p, MinVp, MaxVp, rcls, spt1, spt2, MaxDbh, totseed, carbonco){
                      
                    },
                  
                    ))

Tree <- setRefClass("Tree", 
                       fields = list(Species, Age)),
                        methods = list
                        (init = function(self, species, age){
  
                        },
  
))

is_number <- function(s){
  
}

LoadFile <- function(){
  
}

GetCells <- function(){
  print("Cells")
  
  print("Cells Generated")
}

RunSimulation <- function(length = 1){
  
}
  