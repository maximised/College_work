injection.df <- read.table("P:\\ST2053\\Previous Exam Datasets\\18-19\\Injection.txt", header = T)

attach(injection.df)

injection.lm <- lm(Conc ~ Time+Dose+Weight+Age, data = injection.df)

injection.df
formula(injection.lm)

h <- lm.influence(injection.lm)$hat

plot(h, type='h',
     main="Plot of Leverage vs observation number",
     ylab="Leverage")

index()

match(max(h), h)
h[294]

injection.df[294, c("Time","Dose","Weight","Age")]
summary(injection.df$Time)
summary(injection.df$Dose)
summary(injection.df$Weight)
summary(injection.df$Age)

e <- resid(injection.lm)
s <- summary(injection.lm)$sigma
r <- e / (s*(1-h)^0.5)
summary(e)
summary(r)


plot(r, type="h",
     main="plot of Studentized Residuals vs observation number",
     ylab="Studentized Residuals", ylim=c(-4,4))
abline(h=0, lty=1)
abline(h=c(-2,2),lty=2)     

p <- length(coef(injection.lm))
d <- (1/p)*(h/(1-h))*r^2

plot(d, type='h',
     main="Plot of Cooks distance vs observation nnumber",
     ylab="Cooks distance")


coeffs.changes <- lm.influence(injection.lm)$coefficients

coeffs.changes[c(294),]

coef(injection.lm)

coefficients <- t(coef(injection.lm)-t(coeffs.changes))
coefficients
coefficients[294,]

e[1]

injection.df

sort(r[abs(r) > 2])

leverage_cutoff <- (2*p)/length(injection.df$Conc)

h[h > leverage_cutoff]


sort(d[c(15, 22, 45, 58, 128, 156, 158, 161, 174, 175, 212, 239, 250, 279)])
summary(d)
sort(d)

sort(h)


identify(r)

sort(d[d>4/300])

coefficients[294,]

e
