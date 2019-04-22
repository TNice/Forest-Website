ui <- fluidPage(
  tags$style(type = "text/css", "#map {height: 100vh !important; width: 100vw !important;} .container-fluid{padding:0px;}"),
  leafletOutput("map"),
  actionButton("button", "An action button")
  #htmlTemplate("./www/index.html")
)