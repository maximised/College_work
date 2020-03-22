library(shiny)

ui <- fluidPage(
  sliderInput(inputId = 'num',
              label = 'choose an num:',
              value = 25, max=100, min=1),
  plotOutput('hist'),
  plotOutput('plot'),
  verbatimTextOutput('stats'),
  
  textInput(inputId = 'text', label = 'favorite pony?',
            value = 'twilight'),
  actionButton(inputId = 'button', label='clicker')
)

server <- function(input, output, session) {
  data = reactive({
    rnorm(input$num)
  })
  
  pony = isolate(input$text)
  
  output$hist = renderPlot({
    hist(data(), main = isolate(input$text))
  })

  output$plot = renderPlot({
    plot(data())
  })
  
  output$stats = 
    renderPrint({
      summary(rnorm(input$num))
})
  
}

shinyApp(ui, server)