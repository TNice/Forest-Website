ui <- fluidPage(
  tags$style(type = "text/css", "#map {height: 100vh !important; width: 100vw !important;} .container-fluid{padding:0px;}"),
  leafletOutput("map"),
  absolutePanel(
    top = 0,
    bottom = 'auto',
    right = 'auto',
    left = 0,
    sidebarLayout(
      titlePanel(""),
      sidebarPanel(
        selectInput("dataChoice","Simulateion Data: ", choices = c("Growth", "Fire", "Insect"))
      )
    )
  )
)