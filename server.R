server <- function(input, output){
  
  CreateCells <- function(){
    data <- data.frame("lat" = 38.9072, "lng" = 77.0369, "value" = 0.5, "color" = '#00000F')
    
    msg <- shiny:::toJSON(data)
    
    return(msg)
  }
  
  observeEvent(input$simulate, {
    session$sendCustomMessage("CellUpdated", CreateCells())
  })
  
}



