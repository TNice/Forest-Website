ui <- fluidPage(
  tags$script(src = "leaflet.js"),
  tags$style(type = "text/css", "#map {height: 100vh !important; width: 100vw !important;}
             .container-fluid{padding:0px;}
             #control-container{pointer-events: none; margin-left: 0vw; margin-right: 0vw;}
             #controls{pointer-events: all; }
             h2{visibility: hidden; height: 0px; margin: 0px;}"),
  useShinyjs(),
  leafletOutput("map"),
  absolutePanel(
    id = "control-container",
    top = 0,
    bottom = 0,
    right = 'auto',
    left = 'auto',
    width = 'auto',
    sidebarLayout(
      titlePanel("Simulation Controls"),
      sidebarPanel(
        id = "controls",
        width = 200,
        sliderInput("yearChoice", "Year", minYear, maxYear, value = currentYear, sep = ""),
        selectInput("dataChoice","Simulation Data: ", choices = c("Growth", "Fire", "Insect")),
        actionButton(inputId = "drawRectangle", label = "Select Region"),
        actionButton(inputId = "clearSelection", label = "Clear Region")
      )
    )
  )
)