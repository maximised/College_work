library(shiny)

ui <- fluidPage(

)

server <- function(input, output, session) {
  
}

shinyApp(ui, server)





crimes = read.csv('C:/Users/Maxim/Downloads/crimes-in-boston/crime.csv')

summary(crimes)
crimes
head(crimes)
colnames(crimes)
row.names(crimes)

summary(crimes)
length(crimes$OFFENSE_CODE)

offenses = read.csv('C:/Users/Maxim/Downloads/crimes-in-boston/offense_codes.csv')

summary(offenses)
colnames(offenses)
unique(offenses$NAME)
length(offenses$NAME)

offenses
max(count(crimes$OFFENSE_CODE))


library(plyr)

factor(crimes$OFFENSE_CODE)
counted_crime = count(crimes$OFFENSE_CODE)
max(counted_crime)
counted_crime
