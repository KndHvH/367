mtcars 
#cars dataset

weight <- mtcars$wt
#select weight column

mean <- mean(weight)
#mean

sd(weight)
#desvio padrao

total <- sum(weight)
count <- nrow(mtcars)

total/count == mean

weight
mean
diff <- weight - mean
diff <- diff^2

diff <- sum(diff)

diff <- diff/count

diff <- sqrt(diff)

diff

diff == sd(weight)



