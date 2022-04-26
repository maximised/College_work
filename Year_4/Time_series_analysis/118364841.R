library(TSstudio)

# Prepare data
# from CSO - External Trade / External Trade / TSM04 - Exports of Cattle and Beef
fdat = read.csv("/Users/maximchomsikkvy/Documents/College_work/ST4064/CA/118364841.csv", sep=',', header = TRUE)
fdat = fdat[fdat$Month>="2006M01", ];# fdat = fdat[dat$Month<"1990M01", ]

fdat = ts(data = fdat$VALUE, start = 2006, frequency = 12)
test.length = 24
fdat.split <- ts_split(ts.obj = fdat, sample.out = test.length)
dat = dat.split$train; ndat = dat.split$test

#####################################
# plot the data
dev.off(); layout(mat=matrix(c(1,1,2,3),byrow=TRUE,ncol=2))
plot(dat, type = "l", main='Cattle Exports (1000s) by month', ylab= "Cattle Exports (1000s)", xlab='Date')
acf(dat, lag.max = 50) ; pacf(dat, lag.max = 50)


#  apply a transformation because variance is increasing
ldat = log(dat)
plot(ldat, main='log[ Cattle Exports (1000s) ] by time', ylab= "Log[ Cattle Exports (1000s) ]")
acf(ldat, lag.max = 50); pacf(ldat, lag.max = 50)


# visualise seasonality
dev.off(); layout(mat=matrix(c(1,1,2,3),byrow=TRUE,ncol=2))
Cattle = matrix(c(ldat), nrow = 12, byrow = FALSE) 
matplot(Cattle, type = "l")

Cattle = c(dat)
Month = c(cycle(dat))
boxplot(Cattle ~ Month, main='Boxplot of Cattle exports (1000s) in each month', ylab = 'Cattle (1000s)')
cpgram(ldat)
plot(decompose(ldat))
plot(stl(ldat, s.window = 12))


# differentiate data
Y = diff(ldat); Y = diff(Y, lag=12) # remove trend and seasonality

layout(matrix(c(1,1,2,3), 2, 2, byrow = TRUE))
plot(Y, ylab="",main =expression(Y[i]==(1-B)*(1-B^{12})*X[i]))
acf(Y, lag.max = 80); pacf(Y, lag.max = 80)


# select an ARIMA model
auto.arima(dat)
fit =  arima(ldat, order=c(2, 0, 0), seasonal = list(order=c(0, 1, 1), period=12)) # auto.arima
cpgram(residuals(fit), main= "SARIMA(0,1,0)x(0,1,1)")
tsdiag(fit)

fit1 =  arima(ldat, order=c(1, 0, 0), seasonal = list(order=c(0, 1 ,1), period=12)); fit1; BIC(fit1) # first guess
cpgram(residuals(fit1), main= "SARIMA(0,1,0)x(0,1,1)")
tsdiag(fit1)

fit2 =  arima(ldat, order=c(1, 0, 1), seasonal = list(order=c(0, 1 ,1), period=12)); fit2; BIC(fit2) # second guess
cpgram(residuals(fit2), main= "SARIMA(1,0,1)x(0,1,1)")
tsdiag(fit2)

fit = fit1 # fit1 is better


# forecast and predict data
dev.off()
ldat.pred = predict(fit, n.ahead = 24)
ldat.pred

plot(ldat, xlim = c(2015, 2022), ylim = c(0, 5),
     main="log[ Cattle Exports (1000's) ]", lwd=2)
lines(log(ndat),col="blue",lwd=2)
lines(ldat.pred$pred,col="red",lwd=2)
lines(ldat.pred$pred+2*ldat.pred$se,col="red",lty=3,lwd=2)
lines(ldat.pred$pred-2*ldat.pred$se,col="red",lty=3,lwd=2)


# forecast original data
plot(dat, xlim = c(2015, 2022), ylim = c(0, 90),
     main="Cattle Exports (1000s) by time", ylab='Cattle Exports (1000s)', lwd=2)
lines(ndat,col="blue", lwd=2)
lines(exp(ldat.pred$pred),col="red", lwd=2)
lines(exp(ldat.pred$pred+2*ldat.pred$se),col="red",lty=3, lwd=2)
lines(exp(ldat.pred$pred-2*ldat.pred$se),col="red",lty=3, lwd=2)
legend('topleft', legend=c("true values", "95% forecast interval"),
       col=c('blue','red'), lty=c(1,3), lwd=2, cex=1)


##############################################################################
# experiment
library(tseries)
plot(yield, type='l')
adf = adf.test()
adf

x <- arima.sim(list(order = c(0,1,0)),n = 1000)
plot(x, type='l')

Cattle = matrix(c(0,Y), nrow = 12, byrow = FALSE) 
matplot(Cattle, type = "l")

Cattle = c(Y)
Month = c(cycle(Y))
boxplot(Cattle ~ Month)
cpgram(Y)
plot(stl(Y, s.window = 12))

plot(stl(ldat, s.window = 12))
plot(decompose(ldat))

dev.off()
plot(ldat, type = "o")
lines(lowess(ldat, f=1/6), col="red", lwd=2)
