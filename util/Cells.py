import math
import Constants as const
import json
import time

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

def GetCellsInDrawnRegion():
    return 0
    #no idea how to start. Needs to generate the cells of the region in the drawn polly gone 

#size(side length) and varience are in meters
def GetCellsInSelectedRegion(latNW, longNW, latSE, longSE, size=3, varience=5):
    start = time.time() #get start time for timing
    
    #Sets desiered lat and long offset for cells
    latOffset = size / const.RADIUS_EARTH
    longOffset = size / (const.RADIUS_EARTH * math.cos(math.pi * latNW / 180))

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
    while currentLat > latSE:
        while currentLong > longSE:
            cells[str(cellNum)] = {}
            cells[str(cellNum)]['NW'] = {
                'lat':  currentLat,
                'long': currentLong
            }
            #cells[str(cellNum)]['NW'].append({"lat", currentLat})
            #cells[str(cellNum)]['NW'].append({"long", currentLong})

            cells[str(cellNum)]['NE'] = {
                'lat':  currentLat,
                'long': currentLong - northSideLength
            }
            #cells[str(cellNum)]['NE'].append({"lat", currentLat})
            #cells[str(cellNum)]['NE'].append({"long", currentLong - northSideLength})

            cells[str(cellNum)]['SW'] = {
                'lat':  currentLat - westSideLength,
                'long': currentLong
            }
            #cells[str(cellNum)]['SW'].append({"lat", currentLat - westSideLength})
            #cells[str(cellNum)]['SW'].append({"long", currentLong})

            cells[str(cellNum)]['SE'] = {
                'lat':  currentLat - westSideLength,
                'long': currentLong - northSideLength
            }
            #cells[str(cellNum)]['SE'].append({"lat", currentLat - westSideLength})
            #cells[str(cellNum)]['SE'].append({"long", currentLong - northSideLength})

            cellNum += 1
            currentLong -= northSideLength
        currentLat -= westSideLength

    with open('results/cellsGenerated.json', 'w') as outfile:  
        json.dump(cells, outfile)

    end = time.time()
    print(end - start)
    print(cellNum + 1)
##    try:
##        f = open("results/cellsGenerated", 'w')
##        f.write(str(cells))
##    finally:
##        f.close()

GetCellsInSelectedRegion(50, 50, 45, 45)

