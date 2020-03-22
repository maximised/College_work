injection.df <- read.table("P:\\ST2053\\Previous Exam Datasets\\18-19\\Injection.txt", header = T)

summary(injection.df)

attach(injection.df)

cor(injection.df[-5])


############################################


injection.df.lm = lm(Conc ~ Time + Dose + Weight + Age, data=injection.df)
summary(injection.df.lm)


######################################


F = 805.8 on 4 and 295 DF, p value < 2.2e-16
Reject H0, at least one is modelled


##########################################

injection.df2.lm <- lm(Conc ~ Time + Dose, data = injection.df)
anova(injection.df2.lm, injection.df.lm)

anova 


###########################################

injection.df3.lm <- lm(Conc ~ Time + Dose + Weight, data = injection.df)
injection.df4.lm <- lm(Conc ~ Time + Dose + Age, data = injection.df)

anova(injection.df3.lm, injection.df.lm)
anova(injection.df4.lm, injection.df.lm)
