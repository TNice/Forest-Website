server <- function(input, output, session){
  filteredData <- reactive({
    currentYear <-input$yearChoice
    print(currentYear)
    if(input$dataChoice == "Growth"){
      pal <- Growthpal
      return("Growth")
    }
    if(input$dataChoice == "Fire"){
      pal <- Firepal
      return("Fire")
    }
    if(input$dataChoice == "Insect"){
      pal <- Insectpal
      return("Insect")
    }
  })
  
  output$map <- renderLeaflet({
    m
  })
  
  observe({
    mypop <- paste0(switch(filteredData(), 
                           "Growth" = cells$Growth, 
                           "Fire" = cells$Fire,
                           "Insect" = cells$Insect)
                    )
    
    leafletProxy("map", data = cells) %>%
      addTiles() %>%
      clearShapes() %>%
      addPolygons(
        stroke = FALSE,
        fillOpacity = 0.7,
        fillColor = switch(filteredData(), 
                           "Growth" = ~Growthpal(Growth), 
                           "Fire" = ~Firepal(Fire),
                           "Insect" = ~Insectpal(Insect)
                           ),
        popup = mypop,
        layerId = ~Id
      )
  })
  
  #could be used to edit or see a single county
  observeEvent(input$map_shape_click, {
    id <- input$map_shape_click$id
    #print(id)
  })
  
  observeEvent(input$map_draw_new_feature, {
    print("New Feature")
    feature_type <- input$map_draw_new_feature$properties$feature_type
    
    if(feature_type %in% c("rectangle")) {
      #get the coordinates of the polygon
      shapeBounds <- input$map_draw_new_feature$geometry$coordinates[[1]]
      cords = c(shapeBounds[1], shapeBounds[3])
      cellResults <- compareCells(cords)
      print(cellResults)
    }
  })
}



