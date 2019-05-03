server <- function(input, output, session){
  filteredData <- reactive({
    results <- data.frame("year" = input$yearChoice, "data" = input$dataChoice)
    return(results)
  })
  
  output$map <- renderLeaflet({
    m
  })
  
  observe({
    inputs <- filteredData()
    year <- inputs['year']
    print(inputs)
    
    mapProxy <- leafletProxy("map")
    
    switch(as.character(inputs$data), 
      "Growth" = {
        mypop <- paste0(cells$Growth)
        mapProxy %>%
          hideGroup("Fire") %>%
          hideGroup("Insect") %>%
          showGroup("Growth")
      }, 
      "Fire" = {
        mypop <- paste0(cells$Fire)
        mapProxy %>%
          hideGroup("Growth") %>%
          hideGroup("Insect") %>%
          showGroup("Fire")
      },
      "Insect" = {
        paste0(cells$Insect)
        mapProxy %>%
          hideGroup("Fire") %>%
          hideGroup("Growth") %>%
          showGroup("Insect")
      }
    )
    
    
     #leafletProxy("map") %>%
      # clearShapes()
      # addPolygons(
      #   data = cells,
      #   stroke = FALSE,
      #   fillOpacity = 0.7,
      #   fillColor = switch(as.character(inputs$data), 
      #                      "Growth" = ~Growthpal(Growth), 
      #                      "Fire" = ~Firepal(Fire),
      #                      "Insect" = ~Insectpal(Insect)
      #                      ),
      #   popup = mypop,
      #   layerId = ~Id
      # )
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



