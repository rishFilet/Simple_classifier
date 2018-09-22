import numpy as np

# Write a function that takes as input a list of numbers (an Array), and returns
# the list of values given by the softmax function.
def softmax(L):
    y=[]
    for i in range(len(L)):
        y.append(np.exp(L[i])/np.sum(np.exp(L)))
    return y    
    pass
    
 #This is th sigmoid function which is only used when the number of classes is 2.
 def sigmoid(L):
     y=[]
     for i in range(len(L)):
         y.append(1/(1+np.exp(-L))
     return y    
