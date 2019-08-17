class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        row = len(image)
        col = len(image[0])
        original_color = image[sr][sc]
        
        def dfs(x, y):
            for dx, dy in zip([0,1,0,-1],[1,0,-1,0]):
                new_x = dx + x
                new_y = dy + y
                if new_x in range(row) and new_y in range(col) and not self.visited[new_x][new_y] and image[new_x][new_y] == original_color:
                    image[new_x][new_y] = newColor
                    self.visited[new_x][new_y] = True
                    dfs(new_x, new_y)
                    
        self.visited = [[False] * col for _ in range(row)]

        image[sr][sc] = newColor
        dfs(sr, sc)
        return image
        
