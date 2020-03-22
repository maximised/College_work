#Q1
#read.csv
wolf=read.csv('wolf_hormone_data_for_dryad.csv')

# make a wolf.sub only populations 1 and 2
#(1) check population first
wolf$Population
#(2)
wolf.sub=subset(wolf,Population!=3)
#(3) check again
wolf.sub$Population

# make a new factor called 'hunting', set population 1 light and population 2 heavy
wolf.sub$Hunting='Heavy'
wolf.sub$Hunting[wolf.sub$Population==1]='Light'
wolf.sub$Hunting=as.factor(wolf.sub$Hunting)
wolf.sub$Hunting

# get rid of the empty 'U' factor for Sex using
# check first
wolf.sub$Sex
wolf.sub=droplevels(subset(wolf.sub,Sex!='U'))
# check again
wolf.sub$Sex

# set up variables
Sex=wolf.sub$Sex
Population=wolf.sub$Population
Colour=wolf.sub$Colour
Cpgmg=wolf.sub$Cpgmg
Hunting=wolf.sub$Hunting

#Q2
par(mfrow=c(1,2))
hist(Cpgmg[Hunting=='Light'],main='Cortisol in Wolves',xlab='Light')
hist(Cpgmg[Hunting=='Heavy'],main='Cortisol in Wolves',xlab='Heavy')

#Q3
col=wolf.sub$Colour
table(col)

boxplot(Cpgmg~Sex+col)
boxplot(Cpgmg~Sex+col,names=c('F-Dark','M-Dark','F-light','M-light'))

Sex_new=ordered(Sex,levels=c('M','F'))
boxplot(Cpgmg~Sex+col) 
boxplot(Cpgmg~Sex_new+col)


