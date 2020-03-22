shortestPath = function(){
  n = 5                   #number of vectors
  y = 5                   #target vector
  
  x = 1                   #starting vector
  v = x
  
  V = c(1:5)
  E = list(c(2,3), c(3,1), c(4,2), c(5,4), c(1,4))
  G = list(V, E)               # Graph
  
  L = matrix(nrow = 5, ncol = 3)    # col 1: marks vector as done
                                    #col 2: moves to get to vector
                                    #col 3: last vector taken to get to current vector
  
  L[v, 2] = 0
  L[v, 3] = 0
  
  
  while(!is.na(v))
  {
    edges = L[v, 2] + 1
    for (pair in E)
    {
      if(v %in% pair)
      {
        j = pair[pair!=v]
        
        if(is.na(L[j, 2]))
        {
          L[j, 2] = edges
          L[j, 3] = v
          
          if(j == y)
          {
            return(L)       #second column of target vector is the number of turns it took
          }
        }
      }
    }
    L[v, 1] = 1 
    
    smallestLV2 = 1000000
    nextV = NA
    
    for (i in 1:5)
    {
      if(is.na(L[i, 1]) && !is.na(L[i, 2]))
      {
        if(L[i, 2] < smallestLV2)
        {
          nextV = i
          smallestLV2 = L[i, 2]
        }
      }
    }
    v = nextV
  }
  
  return(NA)
}

shortestPath()
