class Solution:
    def addToArrayForm(self, A: 'List[int]', K: 'int') -> 'List[int]':        
        K_str = str(K)
        if len(A) > len(K_str):
            K_list = [0 for _ in range(len(A) - len(K_str))] + [int(i) for i in K_str]
        else:
            A = [0 for _ in range(len(K_str) - len(A))] + A
            K_list = [int(i) for i in K_str]
        carry = 0
        res = [0 for _ in range(len(A))] 
        for i in range(len(K_list) - 1, -1, -1):
            total = K_list[i] + A[i] + carry
            res[i] = total % 10
            carry = total // 10
        if carry:
            res = [carry] + res
        return res
