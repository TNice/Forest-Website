ui <- fluidPage(
  tags$script(src = "leaflet.js"),
  tags$style(type = "text/css", "#map {height: 100vh !important; width: 100vw !important;}
             .container-fluid{padding:0px;}
             #control-container{pointer-events: none; margin-left: 1vw; margin-right: 0vw;}
             #controls{pointer-events: all; }"),
  useShinyjs(),
  leafletOutput("map"),
  absolutePanel(
    id = "control-container",
    top = 0,
    bottom = 0,
    right = 'auto',
    left = 'auto',
    width = 350,
    sidebarLayout(
      titlePanel(""),
      sidebarPanel(
        id = "controls",
        width = 250,
        sliderInput("yearChoice", "Year", minYear, maxYear, value = currentYear, sep = ""),
        selectInput("dataChoice","Simulation Data: ", choices = c("Growth", "Fire", "Insect")),
        actionButton(inputId = "drawRectangle", label = "test", class = "leaflet-draw-draw-rectangle")
      )
    )
  )
)