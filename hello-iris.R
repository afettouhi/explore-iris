print('hello')
print('world')

print(head(iris,2))
summary(iris)

add_numbers<-function(a,b){
    return(a+b)
}

c<-add_numbers(23,45)
print(c)

plot(iris)

#.libPaths( c( "~/.R/libs" , .libPaths() ) )
.libPaths()

#install.packages("GGally", lib="~/.R/libs")
#library("GGally", lib.loc="~/.R/libs")

install.packages("GGally")
library("GGally")

ggpairs(iris, ggplot2::aes(colour=Species))
