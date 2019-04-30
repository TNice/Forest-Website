library(shiny)
library(leaflet)
library(geojsonio)
library(rgdal)
library(sp)
library(rmapshaper)
library(shinyjs)

shiny::addResourcePath("shinyjs", system.file("srcjs", package = "shinyjs"))

print("Server Starting")
cells <- geojsonio::geojson_read("testdata/USCounties.json", what = "sp")
cells <- ms_simplify(cells, keep = 0.01)

Growthpal <- colorNumeric("Greens", 0:1)
Firepal <- colorNumeric("Reds", 0:1)
Insectpal <- colorNumeric("Blues", 0:1)

pal <- Firepal

m <- leaflet(options = leafletOptions(zoomControl = FALSE), data = cells) %>%
  setView(lng = -98.583, lat = 39.833, zoom = 5)
print("Server Ready")