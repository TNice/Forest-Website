ui <- fluidPage(
  tags$style(type = "text/css", "#map {height: 100vh !important; width: 100vw !important;} .container-fluid{padding:0px;}"),
  leafletOutput("map"),
  absolutePanel(
    top = 0,
    bottom = 0,
    right = 0,
    left = 0,
    width = 300,
    height = 150,
    sidebarLayout(
      titlePanel(""),
      sidebarPanel(
        width = 300,
        selectInput("dataChoice","Simulation Data: ", choices = c("Growth", "Fire", "Insect"))
      )
    )
  )
)