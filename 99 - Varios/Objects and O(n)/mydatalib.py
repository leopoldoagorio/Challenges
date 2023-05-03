'''
DataStats class for saving the time series statistics. Constructed with DataCapture's build_stats() method
Attributes:
    freqs: int list containing frequency of ocurrence of each int from 0..n in the time series
    csum: cummulative sum (occurrences less or equal than index)
Methods:
    less: returns ocurrences less than value
    between: returns ocurrences between min and max value
    greater: returns ocurrences greater than value
'''
class DataStats():
    def __init__(self,n = 1000):
        self.freqs = [0]*(n+1) #se esperan numeros entre 0...n (n+1 nums en total)
        self.csum = [0]*(n+1)
        self.n = n
    def less(self, num):
        if(not isinstance(num,int)): #https://stackoverflow.com/questions/152580/whats-the-canonical-way-to-check-for-type-in-python
            raise ValueError('Can\'t check stats for non int data') #https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python
        return self.csum[num-1]
    def between(self,min,max):
        if (not isinstance(min, int) or not isinstance(max,int)):
            raise ValueError('Can\'t check stats for non int data')
        if (not (min<=max)):
            raise ValueError('max should be greater than min')
        return self.csum[max]-self.csum[min-1]
    def greater(self,num):
        if (not isinstance(num, int)):
            raise ValueError('Can\'t check stats for non int data')
        return self.csum[-1]-self.csum[num]

'''
DataCapture class for saving the time series and calculating statistics.
Attributes:
    time_series: saves in list all data added through the .add method
Methods:
    add: adds a data element to the time_series. Must be an integer.
    build_stats: generates stats for current time_series and returns a DataStats object.
'''
class DataCapture():
    def __init__(self): #https://www.programiz.com/python-programming/class#:~:text=An%20object%20is%20simply%20a,%2C%20doors%2C%20windows%2C%20etc.
        self.time_series = []
    def reset(self):
        self.time_series = []
    def add(self, data): #append is O(1) as per following link
        if(isinstance(data,int)):
            self.time_series.append(data) #https://stackoverflow.com/questions/252703/what-is-the-difference-between-pythons-list-methods-append-and-extend?rq=1
        else:
            raise ValueError('Can\'t add non integer data to time series')
    def build_stats(self): #is O(n) because of second for loop, where n is max expected int value in DataCapture.
        l = len(self.time_series)
        if(l == 0):
            raise ValueError('Can\'t build stats if there is no time series.')
        stats = DataStats()
        for i in range(l): #https://www.geeksforgeeks.org/count-frequencies-elements-array-o1-extra-space-time/amp/
            stats.freqs[self.time_series[i]]+=1
        stats.csum = stats.freqs.copy()
        #print(l)
        for i in range(1,stats.n+1): #https://stackoverflow.com/questions/15889131/how-to-find-the-cumulative-sum-of-numbers-in-a-list
            #print(i)
            stats.csum[i] += stats.csum[i-1]
        return stats