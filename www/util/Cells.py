import math
import Constants as const
import json
import time
import random as r


#Input lat and long at the center of the cell and area in m^2 (default is 900m^2). Output the corner boundries of the cell.
def GetCellBoundries(lat, long, area=900):
    sideLength = math.sqrt(area)
    latOffset = sideLength / const.RADIUS_EARTH
    longOffset = sideLength / (const.RADIUS_EARTH * math.cos(math.pi * lat / 180))

    cords={}
    cords['NW'] = []
    latNW = lat + (latOffset * 180 / math.pi / 2)
    longNW = long + (longOffset * 180 / math.pi / 2)
    cords['NW'].append(latNW)
    cords['NW'].append(longNW)
    
    cords['NE'] = []
    latNE = lat + (latOffset * 180 / math.pi / 2)
    longNE = long - (longOffset * 180 / math.pi / 2)
    cords['NE'].append(latNE)
    cords['NE'].append(longNE)

    cords['SW'] = []
    latSW = lat - (latOffset * 180 / math.pi / 2)
    longSW = long + (longOffset * 180 / math.pi / 2)
    cords['SW'].append(latSW)
    cords['SW'].append(longSW)
    
    cords['SE'] = []
    latSE = lat - (latOffset * 180 / math.pi / 2)
    longSE = long - (longOffset * 180 / math.pi / 2)
    cords['SE'].append(latSE)
    cords['SE'].append(longSE)
    
    return cords

def GetCellCenter():
    lat = (seLat - nwLat) / 2
    lng = (seLng - nwLng) / 2
    return (lat, lng)

def GetCellsInDrawnRegion(nwLat, nwLng, seLat, seLng):
    return 0
    #no idea how to start. Needs to generate the cells of the region in the drawn polly gone 

#Returns dictionary{northSide, westSide, cells},  size(side length) and varience are in meters
def GetCellsInSelectedRegion(latNW, longNW, latSE, longSE, size=10000, varience=5):
    print("\nStart cell generation\n")
    start = time.time() #get start time for timing
    
    #Sets desiered lat and long offset for cells
    latOffset = size / const.RADIUS_EARTH
    longOffset = size / (const.RADIUS_EARTH * math.cos(math.pi * latNW / 180))
    print("test")
    #Sets desired varience for lat and long offset (determins how strict the size is for upper end)
    #lower end has no varience since the region is divided into whole number cells of same size
    longVarience = varience / (const.RADIUS_EARTH * math.cos(math.pi * latNW / 180))
    latVarience = varience / const.RADIUS_EARTH

    #long step
    northSideLength = longNW - longSE
    #lat step
    westSideLength = latNW - latSE

    #determins side lengths
    if northSideLength > (longOffset + longVarience):
        i = 2
        temp = northSideLength
        while temp > (longOffset + longVarience):
            temp = northSideLength / i
            i += 1

        northSideLength = temp

    if westSideLength > (latOffset + latVarience):
        j = 2
        temp = westSideLength
        while temp > (latOffset + latVarience):
            temp = westSideLength / j
            j += 1

        westSideLength = temp

    #divids regions into cells
    #NE cell is 0 and SW cell is number of cells - 1
    cells = {}
    cellNum = 0
    currentLat = latNW
    currentLong = longNW
    print("GENERATING CELLS.....")
    cells['lat'] = []
    cells['long'] = []
    cells['value1'] = []
    cells['value2'] = []
    cells['value3'] = []
    r.seed()
    while currentLat > latSE:
        currentLong = longNW
        while currentLong > longSE:
            #print(currentLat)
##            cells['lat'].append(currentLat - (westSideLength / 2))
##            cells['long'].append(currentLong - (northSideLength / 2))
##            cells['value1'].append(r.random())
##            cells['value2'].append(r.random())
##            cells['value3'].append(r.random())
##            cells[str(cellNum)] = {}
##            cells[str(cellNum)]['N'] = {
##                'lat':  currentLat,
##            }
##            cells[str(cellNum)]['W'] = {
##                'long': currentLong
##            }
##            cells[str(cellNum)]['E'] = {
##                'long': currentLong - (northSideLength / 2)
##            }

            cellNum += 1
            currentLong -= northSideLength
        #print(currentLat)
        currentLat -= westSideLength
        
    end = time.time()
    print(str(end - start) + "s to generate cells")

    #print(cells)
##    print("Saving JSON")
##    with open('results/cellsGenerated.json', 'w') as outfile:  
##        json.dump(cells, outfile)

##    end = time.time()
##    print(str(end - start) + "s Total time")
    print(cellNum + 1)

GetCellsInSelectedRegion(49.90257419738858, -66.07710900000001, 24.777976425842812, -128.12789025)
