Q = np.zeros((100,100))
x,y=np.meshgrid(np.arange(-50,50,1),np.arange(-50,50,1))
Q[x**2+y**2<25**2]=1
Q = Q*10/np.sum(Q)      # [W]
  
