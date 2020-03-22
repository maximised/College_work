house.df =  read.table("C:\\Users\\Maxim\\Downloads\\House Prices.txt", header = TRUE)
house.df

attach(house.df)

house.lm = lm(Price ~ Area, data = house.df)
summary(house.lm)

#(a) 100.898

#(b)
# R = 0.4539
# 45% of variance in y is explained by area
# find other variables that may further explain variability in Price

#(c)
# p = 1.207e-10 t = 7.573

2.0847 - 0.2753*(qt(0.975, 69))



predict(house.lm, data.frame(Area = 150), se.fit=T, interval="confidence", level=0.95)

2.0847 + 0.2753*qt(0.95, 69)

qt(0.95, 69)


-1.5085/0.2753

pt(-3, df = 69)




#2
house.lm = lm(Price ~ Area + Beds + Baths, data = house.df)

summary(house.lm)
#(a) 1.9282

qf(0.95, df1=3, df2=67)

#(c)
predict(house.lm, data.frame(Beds=3, Baths=3, Area=150), se.fit = T, interval = "confidence", level = 0.95)
house.lm1 = lm(Price ~ Area, data=house.df)

anova(house.lm, house.lm1)

#(e)

#(f)
1/(1-summary(lm(Area ~ Beds + Baths, data = house.df))$r.squared)


#3
e = resid(house.lm)
s = summary(house.lm)$sigma
h = lm.influence(house.lm)$hat
r = e/(s*(1-h)^0.5)
p =  length(coef(house.lm))
n = nrow(house.df)
d = (1/p)*(h/(1-h))*r^2

Diagnostics.df = data.frame(e, r, h, d)

summary(house.lm)
Diagnostics.df[1,]

Diagnostics.df[abs(Diagnostics.df$r) > 2, ]
Diagnostics.df[, r]

plot(d, type="h")
identify(d, n=1)
Diagnostics.df[40,]


#4
Q4.df =  read.table("P:\\ST2053\\Previous Exam Datasets\\17-18\\Q4.txt", header = TRUE)
Q4.df
attach(Q4.df)

Q4.lm1 = lm(Y ~ X, data=Q4.df)
Q4.lm2 = lm(sqrt(Y) ~ X, data=Q4.df)
Q4.lm3 = lm(Y ~ sqrt(X), data=Q4.df)


par(mfrow=c(2,2))
scatter.smooth(X, Y, main="Scatter smooth plot")
plot(fitted(Q4.lm1), resid(Q4.lm1), main = "Plot of fitted vs residual")
abline(h=0, lty=2)
hist(resid(Q4.lm1), main="jist of resids")
qqnorm(resid(Q4.lm1), main = "Normal prob plot of residuals")
qqline(resid(Q4.lm1))


par(mfrow=c(2,2))
scatter.smooth(X, sqrt(Y), main="Scatter smooth plot")
plot(fitted(Q4.lm2), resid(Q4.lm2), main = "Plot of fitted vs residual")
abline(h=0, lty=2)
hist(resid(Q4.lm2), main="jist of resids")
qqnorm(resid(Q4.lm2), main = "Normal prob plot of residuals")
qqline(resid(Q4.lm2))


par(mfrow=c(2,2))
scatter.smooth(sqrt(X), Y, main="Scatter smooth plot")
plot(fitted(Q4.lm3), resid(Q4.lm3), main = "Plot of fitted vs residual")
abline(h=0, lty=2)
hist(resid(Q4.lm3), main="jist of resids")
qqnorm(resid(Q4.lm3), main = "Normal prob plot of residuals")
qqline(resid(Q4.lm3))





# 5
house.lm = lm(Price ~ Beds, data=house.df)

summary(house.lm)
anova(house.lm)

qchisq(0.95, 69)
pchisq(87.97, df = 69)


house.aov = aov(Price ~ factor(Beds), data=house.df)
anova(house.lm, house.aov)


house.lm1 = lm(Price ~ Area + Type + Area:Type, data = house.df)
house.lm2 = lm(Price ~ Area, data = house.df)

anova(house.lm1, house.lm2)

summary(house.lm3)



travel.df = read.table("C:\\Users\\Maxim\\Downloads\\Travel.txt", header = TRUE)
travel.df

travel.lm1 = lm(Distance ~ Years + City + Years:City, data=travel.df)
travel.lm2 = lm(Distance ~ Years + City, data=travel.df)
travel.lm3 = lm(Distance ~ Years, data=travel.df)
summary(travel.lm2)
