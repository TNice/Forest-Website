server <- function(input, output, session){
  filteredData <- reactive({
    results <- data.frame("year" = input$yearChoice, "data" = input$dataChoice)
    return(results)
  })
  
  output$map <- renderLeaflet({
    map
  })
  
  observe({
    inputs <- filteredData()
    year <- inputs$year
    updateYear <- FALSE
    
    print(currentYear)
    print(year)
    
    if(is.null(currentYear)){
      currentYear <- year
    }
    else if(currentYear != year){
      setCurrentYear(year)
      updateYear <- TRUE
    }
    
    mapProxy <- leafletProxy("map")
    
    switch(as.character(inputs$data), 
      "Growth" = {
        mypop <- paste0(cells$Growth)
        mapProxy %>%
          hideGroup("Fire") %>%
          hideGroup("Insect") %>%
          showGroup("Growth")
        if(updateYear == TRUE){
          setGrowthYear(year)
          mapProxy %>%
            clearGroup("Growth") %>%
            addPolygons(
              data = growthCells,
              stroke = FALSE,
              fillOpacity = 0.7,
              fillColor = ~Growthpal(growthCells@data[[((year - minYear) + 2)]]), 
              popup = growthPop,
              group = "Growth"
            )
        }else if(!is.null(session)){
          updateSliderInput(session = session, inputId = "yearChoice", value = growthYear)
          setCurrentYear(growthYear)
        }
      }, 
      "Fire" = {
        mypop <- paste0(cells$Fire)
        mapProxy %>%
          hideGroup("Growth") %>%
          hideGroup("Insect") %>%
          showGroup("Fire")
        if(updateYear == TRUE){
          setFireYear(year)
          mapProxy %>%
            clearGroup("Fire") %>%
            addPolygons(
              data = fireCells,
              stroke = FALSE,
              fillOpacity = 0.7,
              fillColor = ~Firepal(fireCells@data[[((year - minYear) + 2)]]), 
              popup = firePop,
              group = "Fire"
            )
        }else if(!is.null(session)){
          updateSliderInput(session = session, inputId = "yearChoice", value = fireYear)
          setCurrentYear(fireYear)
        }
      },
      "Insect" = {
        paste0(cells$Insect)
        mapProxy %>%
          hideGroup("Fire") %>%
          hideGroup("Growth") %>%
          showGroup("Insect")
        if(updateYear == TRUE){
          setInsectYear(year)
          mapProxy %>%
            clearGroup("Insect") %>%
            addPolygons(
              data = insectCells,
              stroke = FALSE,
              fillOpacity = 0.7,
              fillColor = ~Insectpal(insectCells@data[[((year - minYear) + 2)]]), 
              popup = insectPop,
              group = "Insect"
            )
        }
        else if(!is.null(session)){
          updateSliderInput(session = session, inputId = "yearChoice", value = insectYear)
          setCurrentYear(insectYear)
        }
      }
    )
  })
  
  #could be used to edit or see a single county
  observeEvent(input$map_shape_click, {
    id <- input$map_shape_click$id
    #print(id)
  })
  
  observeEvent(input$map_draw_new_feature, {
    feature_type <- input$map_draw_new_feature$properties$feature_type
    
    if(feature_type %in% c("rectangle")) {
      #get the coordinates of the polygon
      shapeBounds <- input$map_draw_new_feature$geometry$coordinates[[1]]
      cords = c(shapeBounds[1], shapeBounds[3])
      cellResults <- compareCells(cords)
      #print(cellResults)
    }
  })
  
  observeEvent(input$drawRectangle,{
    runjs("
      if (myMap == null) {
          myMap = mapsPlaceholder.pop();
      }
      let polygonDrawer = new L.Draw.Rectangle(myMap);
      
      console.log(window.shape);
      if(window.shape != null){
          console.log('Shape Removed');
          window.shape.remove();
      }

      // Assumming you have a Leaflet map accessible
      myMap.on('draw:created', function (e) {
          var type = e.layerType,
              layer = e.layer;
              
          window.shape = layer;
          layer.addTo(myMap);
      });
      
      polygonDrawer.enable();
    ")
  })
}



