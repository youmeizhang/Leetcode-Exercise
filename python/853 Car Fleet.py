class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #position = sorted(position)
        cars = [(pos, spd) for pos, spd in zip(position, speed)]
        sorted_car = sorted(cars, reverse = True)
        
        time = []
        for i in range(len(sorted_car)):
            t = (target - sorted_car[i][0]) / sorted_car[i][1]
            time.append(t)
            
        stack = []

        for i in range(len(time)):
            if not stack:
                stack.append(time[i])
            else:
                if time[i] > stack[-1]:
                    stack.append(time[i])
        return len(stack)
        
        
