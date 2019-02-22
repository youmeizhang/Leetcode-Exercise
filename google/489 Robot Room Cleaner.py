#credit to: https://www.cnblogs.com/lightwindy/p/9739158.html

class Solution(object):
    def cleanRoom(self, robot):
        
        def helper(robot):
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def dfs(pos, robot, d, visited):
            if pos in visited:
                return
            
            visited.add(pos)
            robot.clean()
            for _ in directions:
                if robot.move():
                    dfs((pos[0] + directions[d][0], pos[1] + directions[d][1]), robot, d, visited)
                    helper(robot)
                
                robot.turnRight()
                d = (d+1) % 4
                
        dfs((0, 0), robot, 0, set())
