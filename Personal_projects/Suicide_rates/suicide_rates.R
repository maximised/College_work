install.packages('caTools')
library(caTools)
data()

mydata = read.csv("https://stats.idre.ucla.edu/stat/data/binary.csv")

set.seed(88)

split = sample.split(mydata$admit, SplitRatio = 0.75)
split

dressdata = subset(mydata, split == T)
dresstest = subset(mydata, split == F)

dressdata

suicides = read.csv('C:/Users/Maxim/Downloads/suicide-rates-overview-1985-to-2016/master.csv', header = T)
summary(suicides)
head(suicides)


barplot(suicides$ï..country)

counts = table(suicides$ï..country)
counts

barplot(counts[10:20], las = 2)
count_country_year = table(suicides$country.year)
UN_years = count_country_year[substring(names(count_country_year), 1, 13)=='United States']
count_country_year
substring(count_country_year[1], 1, 3)
substring(names(count_country_year[1]), 1, 8)
names(count_country_year)
UN_years 
substring('United Stateswgfgfi', 1, 13)

barplot(UN_years)

install.packages(ggplot2)
library(ggplot)

sum(suicides$suicides_no[suicides$country=='United States19'])

UN_years = table(sum(suicides$suicides_no[substring(names(count_country_year), 1, 13)=='United States']))
ggplot()

paste(2, 'da', sep='')

typeof(suicides)

summary(test)
test = lm(suicides_no ~ population, data = suicides)
summary(tab = table(suicides$country.year,suicides$suicides_no)

tab = tab[substring(names(tab), 1, 13)=='United States']
tab
(UN_years)
ls = suicides$country.year[substring(suicides$country.year, 1, 13)=='United States']
ls = unique(ls)
ls = as.table(ls)

tab = table('United States1985' = 2)







tab = table(NULL)

for (i in 1985:2015)
{
  year = paste('Italy', i, sep='')
  
  tab[year] = 100 * sum(suicides$suicides_no[suicides$country.year==year])/sum(suicides$population[suicides$country.year==year])

  
}
barplot(as.array(tab))

-------------------------------------------
s  
  
countries = unique(suicides$ï..country)

countries2014 = table(NULL)
  
for(c in countries)
{
  year = paste(c, 2014, sep='')
  
  countries2015[year] = 100 * sum(suicides$suicides_no[suicides$country.year==year])/sum(suicides$population[suicides$country.year==year])
  
}
  
  
plot = barplot(as.array(countries2015), las = 2, cex.names = 0.5, line = -1)
plot = 

max(as.array(countries2015))
is.na(countries2015[1])

countries2014 = countries2014[!is.na(countries2015)]

pdf(file="example.pdf", width=3, height=4)
print(plot)
dev.off()







tab
tab[, 2:=NULL]
remove(tab['2'])
plot(tab)
tab = as.table(tab)
tab[0]
pop_tab = table('2'==1)
barplot(table('2'==2))
for (i in 2:32)
{
  
}

tab = tab[-1]
barplot(height = tab)
tab[1]
print(tab[['United States1985']])
typeof(tab)
tab[[]]
barplot(as.array(tab))
as.array(tab)[1]
group_by(age)

grep('gf', 'i wgfant a g')
cor(suicides$gdp_per_capita.... , suicides$year)


aov(suicides_no ~ suicides_no, data = suicides)
t.test(suicides$year, suicides$population)

cor(suicides$suicides_no, suicides$year
    )












install.packages('tidyverse')
vb
library(tidyverse)



theme_set(theme_light())


