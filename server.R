server <- function(input, output, session){
  
  CreateCells <- function(){
    data <- data.frame("lat" = 38.9072, "lng" = -77.0369, "value" = 0.5, "color" = "#00000F")
    
    msg <- shiny:::toJSON(data)
    
    session$sendCustomMessage("cell-updated", msg);
  }
  observeEvent(input$simulate, CreateCells())
  
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



