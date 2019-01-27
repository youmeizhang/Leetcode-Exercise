#credit to:	fuxuemingzhu
class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = collections.defaultdict(list)
        self.value = collections.defaultdict(list)
        self.max_ = collections.defaultdict(list)
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.time[key].append(timestamp)
        self.value[key].append(value)
        self.max_[key] = max(self.max_[key], timestamp)
        
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.time:
            return ""
        if timestamp > self.max_[key]:
            return self.value[key][-1]
        res = bisect.bisect_right(self.time[key], timestamp)
        if res:
            return self.value[key][res-1]
        return ""
        
#time limit: using binary search
class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key in self.dic:
            if timestamp > self.dic[key][1][0]:
                self.dic[key][0] = [value] + self.dic[key][0]
                self.dic[key][1] = [timestamp] + self.dic[key][1]
            else:
                self.dic[key][0].append(value)
                self.dic[key][1].append(timestamp)
            
        else:
            self.dic[key] = [[value], [timestamp]]
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        res_value = ""
        
        value_list = self.dic[key][0]
        timestamp_list = self.dic[key][1]
        
        
        def binsearch(timestamp_list, value_list, timestamp):            
            res_value = ""
            l = 0
            r = len(timestamp_list)

            while(l < r):
                mid = (l + r) // 2
                if timestamp_list[mid] == timestamp:
                    res_value = value_list[mid]
                    break
                elif timestamp_list[mid] > timestamp:
                    if mid == len(timestamp_list) - 1:
                        break
                    elif timestamp_list[mid + 1] <= timestamp:
                        res_value = value_list[mid + 1]
                        break
                    else:
                        l = mid + 1
                else:
                    if mid == 0:
                        break
                    elif timestamp_list[mid-1] >= timestamp: 
                        res_value = value_list[mid]
                        break
                    else:
                        r = mid - 1   
            return res_value
        
        if timestamp >= timestamp_list[0]:
            return value_list[0]
        else:
            return binsearch(timestamp_list, value_list, timestamp)
                
#time limit: using linear search
class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key in self.dic:
            if timestamp > self.dic[key][1][0]:
                self.dic[key][0] = [value] + self.dic[key][0]
                self.dic[key][1] = [timestamp] + self.dic[key][1]
            else:
                self.dic[key][0].append(value)
                self.dic[key][1].append(timestamp)
            
        else:
            self.dic[key] = [[value], [timestamp]]
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        res_value = ""
        res_timestamp = 0
        
        value_list = self.dic[key][0]
        timestamp_list = self.dic[key][1]
        
        for i in range(len(timestamp_list)):
            if timestamp_list[i] > timestamp:
                continue
            else:
                res_value = value_list[i]
                break
    
        return res_value
                
