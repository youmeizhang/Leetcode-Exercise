# credit to: https://www.youtube.com/watch?v=IAet94C1FCc

class Solution(object):
    def nextClosestTime(self, time):
        s = set(time)
        hh = int(time[0:2])
        mm = int(time[3:5])
        while True:
            mm += 1
            if mm == 60:
                mm = 0
                if hh == 23:
                    hh = 0
                else:
                    hh += 1
            time = "%02d:%02d" % (hh, mm)
            if set(time) <= s:
                return time
        return time


                    
            
            
        """
        :type time: str
        :rtype: str
        """
        
