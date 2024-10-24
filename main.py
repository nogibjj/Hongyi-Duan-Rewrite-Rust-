import time

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
    
x = [i for i in range(1, 1000000)]

start = time.time()
get_mean(x)
end = time.time()
print(f"Time taken for mean calculation: {10**6*(end - start)} microseconds")

start = time.time()
get_median(x)
end = time.time()
print(f"Time taken for median calculation: {10**6*(end - start)} microseconds")

start = time.time()
get_std(x)
end = time.time()
print(f"Time taken for standard deviation calculation: {10**6*(end - start)} microseconds")

