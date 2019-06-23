class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        n = len(count)
        min_flag = False
        total = 0
        cnt = 0
        res = [0, 0, 0, 0, 0]
        mode_ = 0
        for i in range(n):
            if count[i] != 0:
                #max
                res[1] = float(i)

                #mode
                if count[i] > mode_:
                    res[4] = float(i)
                    mode_ = count[i]

                #min
                if not min_flag:
                    res[0] = float(i)
                    min_flag = True

                #mean
                total += count[i] * i
                cnt += count[i]


        sum_ = 0

        for j in range(n):
            if count[j] != 0:
                sum_ += count[j]
                if sum_ == cnt // 2:
                    if cnt % 2 != 0:
                        res[3] = float(j)
                        break
                    else:
                        for m in range(j+1, n):
                            if count[m] != 0:
                                res[3] = float((m + j) / 2)
                                break
                        break
                elif sum_ > cnt // 2:
                    res[3] = float(j)
                    break

        res[2] = float(total / cnt)
        return res


        
