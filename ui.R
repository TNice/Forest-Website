ui <- fluidPage(
  tags$style(type = "text/css", "#map {height: 100vh !important; width: 100vw !important;} .container-fluid{padding:0px;}"),
  leafletOutput("map"),
  absolutePanel(
    top = 0,
    bottom = 0,
    right = 0,
    left = 0,
    sidebarLayout(
      titlePanel(""),
      sidebarPanel(
        selectInput("dataChoice", choices = c("test1", "test2"), label = "Simulation Data")
      )
    )
  )
)