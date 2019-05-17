library(shiny)
library(leaflet)
library(geojsonio)
library(rgdal)
library(sp)
library(rmapshaper)
library(shinyjs)
library(leaflet.extras)

shiny::addResourcePath("shinyjs", system.file("srcjs", package = "shinyjs"))

cat("Server Starting...\n\n")
cat("Loading Json...\n")
cells <- geojsonio::geojson_read("testdata/USCounties.json", what = "sp")
cat("Json Loaded!\n\n")
cat("Simplifying Json...\n")
cells <- ms_simplify(cells, keep = 0.01)
cat("Json Simplified!\n\n")

cat("Loading Growth Json...\n")
growthCells <- geojsonio::geojson_read("testdata/GrowthTestData.json", what = "sp")
cat("Growth Json Loaded!\n\n")
cat("Simplifying Growth Json...\n")
growthCells <- ms_simplify(growthCells, keep = 0.01)
cat("Growth Json Simplified!\n\n")

cat("Loading Fire Json...\n")
fireCells <- geojsonio::geojson_read("testdata/FireTestData.json", what = "sp")
cat("Fire Json Loaded!\n\n")
cat("Simplifying Fire Json...\n")
fireCells <- ms_simplify(fireCells, keep = 0.01)
cat("Fire Json Simplified!\n\n")

cat("Loading Insect Json...\n")
insectCells <- geojsonio::geojson_read("testdata/InsectTestData.json", what = "sp")
cat("Insect Json Loaded!\n\n")
cat("Simplifying Insect Json...\n")
insectCells <- ms_simplify(insectCells, keep = 0.01)
cat("Insect Json Simplified!\n\n")

cat("Creating Server Globals...\n")
currentYear <- 1
minYear <- 1
maxYear <- 4

growthYear <- 1
fireYear <- 1
insectYear <- 1

Growthpal <- colorNumeric("Greens", 0:1)
Firepal <- colorNumeric("Reds", 0:1)
Insectpal <- colorNumeric("Blues", 0:1)

growthPop <- paste0(cells$Growth)
firePop <- paste0(cells$Fire)
insectPop <- paste0(cells$Insect)

setCurrentYear <- function(year){
  currentYear <<- year
}

setGrowthYear <- function(year){
  growthYear <<- year
}

setFireYear <- function(year){
  fireYear <<- year
}

setInsectYear <- function(year){
  insectYear <<- year
}

compareCells <- function(cords){

  #print(cells$Id[1])
  cellArray <- c()
  minLat <- cords[[1]][[1]]
  minLong <- cords[[1]][[2]]
  maxLat <-cords[[2]][[1]]
  maxLong <- cords[[2]][[2]]
  counter <- 0
  #print(cells@polygons[[1]]@labpt)
  for(C in cells@polygons){
    counter <- counter + 1
    myCords <- C@Polygons[[1]]@coords
    for(P in 1:nrow(myCords)){
      if(minLat < myCords[P,1] && myCords[P,1] < maxLat && minLong < myCords[P, 2] && myCords[P,2] < maxLong){
        cellArray <- append(cellArray, counter)
        break
      }
    }
  }
  
  if(length(cellArray) == 0){
    cellResult <- GetRegionFromPoint(cords[[1]])
    cellArray[1] <- cellResult
  }
  return(cellArray)
}

GetRegionFromPoint <- function(point){
  counter <- 0
  cellArray <- c()
  
  x <- point[[1]]
  y <- point[[2]]
  
  for(C in cells@polygons){
    counter <- counter + 1
    myCords <- C@Polygons[[1]]@coords
    
    inside <- FALSE
    j <- nrow(myCords)
    for(i in 1:nrow(myCords)){
      xi <- myCords[i,1]
      yi <- myCords[i,2]
      xj <- myCords[j,1]
      yj <- myCords[j,2]
      
      doesIntersect <- ((yi > y) != (yj > y)) && (x < (xj - xi) * (y - yi) / (yj - yi) + xi)
      if(doesIntersect){
        inside <- !inside
      }
      
      j <- i  
    }
    
    if(inside){
      return(counter)
    }
  }
}
cat("Server Globals Created!\n\n")

cat("Creating Map...\n")
map <- leaflet(options = leafletOptions(zoomControl = FALSE)) %>%
  addTiles() %>%
  addDrawToolbar(
    targetGroup='draw',
    polylineOptions=FALSE,
    markerOptions = FALSE,
    circleOptions = FALSE,
    polygonOptions = FALSE,
    circleMarkerOptions = FALSE,
    rectangleOptions = FALSE,
    singleFeature = TRUE,
    position = 'topright') %>%
  addPolygons(
    data = growthCells,
    stroke = FALSE,
    fillOpacity = 0.7,
    fillColor = ~Growthpal(growthCells@data[[2]]), 
    popup = growthPop,
    group = "Growth"
  ) %>%
  hideGroup("Growth") %>%
  addPolygons(
    data = fireCells,
    stroke = FALSE,
    fillOpacity = 0.7,
    fillColor = ~Firepal(growthCells@data[[((currentYear - minYear) + 2)]]), 
    popup = firePop,
    group = "Fire"
  ) %>%
  hideGroup("Fire") %>%
  addPolygons(
    data = insectCells,
    stroke = FALSE,
    fillOpacity = 0.7,
    fillColor = ~Insectpal(growthCells@data[[((currentYear - minYear) + 2)]]), 
    popup = insectPop,
    group = "Insect"
  ) %>%
  hideGroup("Insect") %>%
  setView(lng = -98.583, lat = 39.833, zoom = 5)
cat("Map Created!\n\n")

cat("Server Ready!\n\n")