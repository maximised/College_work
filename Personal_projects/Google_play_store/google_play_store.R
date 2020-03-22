
google_data = read.csv('C:/Users/Maxim/Downloads/google-play-store-apps/googleplaystore.csv')
reviews = read.csv('C:/Users/Maxim/Downloads/google-play-store-apps/googleplaystore_user_reviews.csv')
glimpse(google_data)
glimpse(reviews)


levels(google_data$Content.Rating)

library(plyr)

google_data$Content.Rating = revalue(google_data$Content.Rating, c('Adults only 18+'='18+',
                       'Everyone'='E',
                       'Everyone 10+'='10+',
                       'Mature 17+'='17+',
                       'Teen'='T',
                       'Unrated'='U'))
google_data$Content.Rating = factor(google_data$Content.Rating,
                                    ordered = T,
                                    levels = c('E',
                                               '10+',
                                               'T',
                                               '17+',
                                               '18+',
                                               'U'))

plot(google_data$Content.Rating)
sum(google_data$Content.Rating == 'U')
sum(is.na(google_data$Content.Rating))
google_data[is.na(google_data$Content.Rating)]

google_data %>%
  filter(App == 'Tinder')

plot = ggplot(google_data, aes(x = Rating, y = Reviews)) +
  geom_point()

plot

mean(google_data$Rating[!is.nan(google_data$Rating)])

google_data = na.omit(google_data)

length(google_data$App)
google_data = unique(google_data)
google_data = google_data[!duplicated(google_data$App),]

google_data = google_data %>%
  gsub('Varies with device', 'NaN', Size)
google_data$Size = gsub('Varies with device', 'NaN', google_data$Size)

google_data$Installs = gsub(',', '', google_data$Installs)
google_data$Installs = sub('+', '', google_data$Installs)
google_data$Installs = as.integer(google_data$Installs)
google_data$Installs
substr('afdgsd', 1, nchar('afdgsd'))
'dsaf'[-1]
gsub(pl, '', 'ddasa+')
google_data$Installs = substr(google_data$Installs, 1, nchar(google_data$Installs)-1)


google_data$Size = gsub(',', '', google_data$Size)
google_data$Size = ifelse('k' %in% google_data$Size, as.integer(gsub('k', '', google_data$Size))/1000, as.integer(google_data$Size))

pie(google_data$Category)

t.test(google_data$Rating)
