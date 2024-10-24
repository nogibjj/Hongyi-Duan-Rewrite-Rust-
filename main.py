import matplotlib.pyplot as plt

def get_mean(x):
    mean = 0
    for i in x:
        mean += i
    mean = mean / len(x)
    return mean
        
def get_median(x):
    mid = int(len(x) / 2)
    x = sorted(x)
    if len(x) % 2 == 0:
        return (x[mid-1] + x[mid]) / 2
    else:
        return x[mid]

def get_std(x):
    std = 0
    mean = get_mean(x)
    for i in x:
        std += (i - mean)**2
    std = (std / (len(x) - 1))**0.5
    return std
    
def get_plot(x):
    plt.plot(x)
    plt.title(x.name)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
    
