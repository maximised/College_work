prim = function(){
  V = c(1:5)
  E = data.frame(vpairs = matrix(c(2,3,3,1,4,2,5,4,1,4), ncol = 2, byrow = T),
                 weights = c(5, 3, 2, 8, 1))
  
  G = list(V, E)
  T = c(1)
  F = c()
  
  for(i in 2:5)
  {
    min = 10000
    e = NULL
    
    for(c in 1:5)
    {
      if(length(intersect(c(E[c,1], E[c,2]), T))==1 && E[c,3] < min)
      {
        min = E[c,3]
        w = intersect(c(E[c,1], E[c,2]), T)
        y = c(E[c,1],E[c,2])[-w]
        
        e = list(w,y)
        
      }
    }
    
    F = union(F, e)
    T = union(T, y)
    
  }
  return(T)
  #~//###########################}
  
  
prim()
  
  