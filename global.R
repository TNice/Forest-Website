library(shiny)
library(leaflet)
library(geojsonio)
library(rgdal)
library(sp)
library(rmapshaper)
library(shinyjs)

shiny::addResourcePath("shinyjs", system.file("srcjs", package = "shinyjs"))

print("Server Starting")
# cells <- geojsonio::geojson_read("testdata/us.json", what = "sp")
# cells <- ms_simplify(cells, keep = 0.01)

pal <- colorNumeric("Greens", 0:1)

# mypop <- paste0(cells$Value)

m <- leaflet(options = leafletOptions(zoomControl = FALSE)) %>% 
  addTiles() %>% 
  # addPolygons(
  #   stroke = FALSE, 
  #   fillOpacity = 0.7, 
  #   fillColor = ~pal(Value), 
  #   popup = mypop,
  #   layerId = ~Id) %>%
  setView(lng = -98.583, lat = 39.833, zoom = 5) %>%
  

print("Server Ready")