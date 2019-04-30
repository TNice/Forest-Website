library(shiny)
library(leaflet)
library(geojsonio)
library(rgdal)
library(sp)
library(rmapshaper)
library(shinyjs)
library(leaflet.extras)

shiny::addResourcePath("shinyjs", system.file("srcjs", package = "shinyjs"))

print("Server Starting")
cells <- geojsonio::geojson_read("testdata/USCounties.json", what = "sp")
cells <- ms_simplify(cells, keep = 0.01)

Growthpal <- colorNumeric("Greens", 0:1)
Firepal <- colorNumeric("Reds", 0:1)
Insectpal <- colorNumeric("Blues", 0:1)

compareCells <- function(cords){

  print(cells$Id[1])
  cellArray <- c()
  minLat <- cords[[1]][[1]]
  minLong <- cords[[1]][[2]]
  maxLat <-cords[[2]][[1]]
  maxLong <- cords[[2]][[2]]
  counter <- 0
  print(cells@polygons[[1]]@labpt)
  for(C in cells@polygons){
    counter <- counter + 1
    myCords <- C@Polygons[[1]]@coords
    for(P in 1:nrow(myCords)){
      if(minLat < myCords[P,1] && myCords[P,1] < maxLat && minLong < myCords[P, 2] && myCords[P,2] < maxLong){
        
              append(cellArray, cells$Id[counter])
              print(cells$Id[counter])
              break;
      }
    }
  }
  
  if(length(cellArray) == 0){
    cellResult <- GetRegionFromPoint(cords[[1]])
    cellArray[1] <- cellResult
  }
  print(cellArray)
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
        print(inside)
      }
      
      j <- i  
    }
    
    if(inside){
      print(cells$Id[counter])
      return(cells$Id[counter])
    }
  }
}

m <- leaflet(options = leafletOptions(zoomControl = FALSE), data = cells) %>%
  addDrawToolbar(
    targetGroup='draw',
    polylineOptions=FALSE,
    markerOptions = FALSE,
    circleOptions = FALSE,
    polygonOptions = FALSE,
    circleMarkerOptions = FALSE,
    position = 'topright') %>%
  setView(lng = -98.583, lat = 39.833, zoom = 5)

print("Server Ready")