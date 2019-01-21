class Solution(object):
    def distance(self, a, b, c):
        x1 = a.x - b.x
        y1 = a.y - b.y
        x2 = a.x - c.x
        y2 = a.y - c.y
        
        res1 = x1 * x1 + y1 * y1
        res2 = x2 * x2 + y2 * y2
        
        if res1 == res2:
            return 0
        elif res1 < res2:
            return -1
        else:
            return 1
        
    def crossproduct(self, a, b, c):
        x1 = a.x - b.x
        y1 = a.y - b.y
        x2 = a.x - c.x
        y2 = a.y - c.y
        return y2 * x1 - y1 * x2
        
    def outerTrees(self, points):
        start = points[0]
        for i in range(1, len(points)):
            if points[i].x < start.x:
                start = points[i]
                
        result = set() 
        result.add(start)
        current = start
        colinear = []
        
        while(True):
            next_target = points[0]
            for i in range(1, len(points)):
                if points[i] == current:
                    continue
                val = self.crossproduct(current, next_target, points[i])
                if val == 0:
                    #collinear point, pick the closer one to colinear, next target becomes the further one
                    if self.distance(current, next_target, points[i]) < 0:
                        colinear.append(next_target)
                        next_target = points[i]
                    else:
                        colinear.append(points[i])
                elif val > 0:
                    #rightmost
                    next_target = points[i]
                    colinear = []                    
                    
            for point in colinear:
                result.add(point)
                
            if next_target == start:
                break
                
            result.add(next_target)
            current = next_target

        return list(result)
