server <- function(input, output){
  observeEvent(input$foo, {
    print(input$foo)
  })
}

