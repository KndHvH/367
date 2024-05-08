data = [1,2,3,3,3,3,3,4,4,5,5,5]

class DP:
    def __init__(self, data):
        self.data = data
        self.mean = sum(data) / len(data)
        self.variance = sum((x - self.mean) ** 2 for x in data) / len(data)
        self.std_dev = self.variance ** 0.5

    def __repr__(self):
        return f"Mean: {self.mean}, Variance: {self.variance}, Standard Deviation: {self.std_dev}"
    
    
dp = DP(data)
print(dp)