data = read.csv('C:/Users/Maxim/Downloads/suicide-rates-overview-1985-to-2016/master.csv')

install.packages('dplyr')

data <- data %>% 
  rename(country = 'ï..country') %>%
  as.data.frame()

glimpse(data)

data <- data %>%
  filter(year != 2016) %>% # I therefore exclude 2016 data
  select(-country.year)


minimum_years <- data %>%
  group_by(i...country) %>%
  summarize(rows = n(), 
            years = rows / 12) %>%
  arrange(years)

data <- data %>%
  filter(!(country %in% head(minimum_years$country, 7)))


mapCountryData()
