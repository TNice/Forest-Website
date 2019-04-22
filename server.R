server <- function(input, output, session){
  output$map <- renderLeaflet({
    m
  })
  
  observeEvent(input$map_shape_click, {
    id <- input$map_shape_click$id
    print(id)
    #poly <- cells[which(cells$Id == id)]
    #print(poly)
  })
    
  observeEvent(input$simulate, {
    print("Simulate")
  })
  
  observeEvent(input$randomizeCell, {
     info <- input$randomizeCell
     value <- runif(1, 0.25, .99)
     red <- sample(10:99, 1)
     green <- sample(10:99, 1)
     blue <- sample(10:99, 1)
     
     color <- paste("#", red, sep="")
     color <- paste(color, green, sep="")
     color <- paste(color, blue, sep="")
     
     print(color)
     data <- data.frame("lat" = info$lat, "lng" = info$lng, "value" = value, "color" = color)
  
     msg <- shiny:::toJSON(data)
     
     session$sendCustomMessage("cell-updated", msg);
  })
}



