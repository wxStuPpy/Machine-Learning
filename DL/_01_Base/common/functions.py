import numpy as np

def step_function(x):
    return np.array(x>0,dtype=int)

def sigmoid(x):
    return 1/(1+np.exp(-x))

def softmax(x):
    if x.ndim==2:
        exp_x = np.exp(x - np.max(x, axis=1, keepdims=True))
        y = exp_x / np.sum(exp_x, axis=1, keepdims=True)
        return y
    exp_x=np.exp(x-np.max(x))
    y=exp_x/np.sum(exp_x)
    return y

def identity(x):
    return x

def relu(x):
    return np.maximum(0,x)

if __name__=='__main__':
    arr = np.random.randint(low=-6, high=6, size=12)
    print(arr)
    print(step_function(arr))
    print(relu(arr))
    print(sigmoid(arr))
    print(softmax(arr))




