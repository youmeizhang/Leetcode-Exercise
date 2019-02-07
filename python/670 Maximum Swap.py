class Solution:
    def maximumSwap(self, num: 'int') -> 'int':
        new_num = [int(i) for i in str(num)]
        i = 0
        while(i < len(new_num)):
            max_value = max(new_num[i:])
            if max_value > new_num[i]:

                for j in range(i, len(new_num)):
                    if new_num[j] == max_value:
                        idx = j

                tmp = new_num[i]

                new_num[i] = max_value
                new_num[idx] = tmp
                break

            else:
                i += 1

        new_res = [str(i) for i in new_num] 
        return int(''.join(new_res))
