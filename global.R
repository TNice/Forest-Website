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
  
  print("Test")
  print(minLat)
  
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


  # cellArray <- c()
  # print(cells, 1:5)
  # for (F in cells$Polygons){
  #   for(point in F$Polygon$coords){
  #     if(minLat < point[0] && point[0] < maxLat && minLong < points[1] && points[1] < maxLong){
  #       append(cellArray, F$Id)
  #       print(F$Id)
  #       break;
  #     }
  #   }
  # }
  # return(cellArray)
}

m <- leaflet(options = leafletOptions(zoomControl = FALSE), data = cells) %>%
  addDrawToolbar(
    targetGroup='draw',
    polylineOptions=FALSE,
    markerOptions = FALSE,
    circleOptions = TRUE,
    position = 'topright') %>%
  setView(lng = -98.583, lat = 39.833, zoom = 5)

print("Server Ready")