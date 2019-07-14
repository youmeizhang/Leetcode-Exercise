class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        res = []
        n = len(cells)
        for i in range(14):
            tmp = [0] * n
            for j in range(1, n-1):            
                if cells[j+1] == cells[j-1]:
                    tmp[j] = 1
            cells = tmp
            res.append(tmp)

        return res[N % 14 - 1]
