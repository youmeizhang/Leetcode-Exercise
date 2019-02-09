class Solution:
    def nextClosestTime(self, time: 'str') -> 'str':
        hour, minu = time.split(":")[0], time.split(":")[1]
        digit = set()
        for ho in hour:
            digit.add(int(ho))
        for mi in minu:
            digit.add(int(mi))

        digit = list(sorted(digit))
        if len(digit) == 1:
            return time
        if digit.index(int(minu[-1])) < len(digit) - 1:
            #try to increase min[-1]
            new_minu = minu[0] + str(digit[digit.index(int(minu[-1])) + 1])
            return hour + ":" + new_minu

        elif digit.index(int(minu[-1])) == len(digit) - 1:
            if digit.index(int(minu[0])) < len(digit) - 1 and digit[digit.index(int(minu[0])) + 1] < 6:
                #minu[-1] equal the largest digit, if larger digit exists for minu[0], increase it
                new_minu = str(digit[digit.index(int(minu[0])) + 1]) + str(digit[0])
                return hour + ":" + new_minu
            else:
                #otherwise, just change to the minu to the smallest digit available
                new_minu = str(digit[0]) + str(digit[0])
                #then change the hour part, similar to the previous 
                if int(hour[0]) < 2:
                    #max value for hour[-1] coule be 9
                    if digit.index(int(hour[-1])) < len(digit) - 1:
                        new_hour = hour[0] + str(digit[digit.index(int(hour[-1])) + 1])
                        return new_hour + ":" + str(digit[0]) + str(digit[0])
                    else:
                        #no larger digit can can be chosen for hour[-1]
                        new_hour_0 = digit[digit.index(int(hour[0])) + 1]
                        if new_hour_0 == 2:
                            new_hour = str(2) + str(digit[0])
                        if new_hour_0 > 3:
                            new_hour = str(digit[0]) + str(digit[0])

                        else:
                            new_hour = str(new_hour_0) + hour[-1]

                        return new_hour + ":" + str(digit[0]) + str(digit[0])
                else:
                    #hour[0] is already 2
                    #max value for hour[-1] coule be 3
                    if digit.index(int(hour[-1])) < len(digit) - 1 and digit[digit.index(int(hour[-1])) + 1] < 4:
                        new_hour = str(2) + str(digit[digit.index(int(hour[-1])) + 1])
                    else:

                        new_hour = str(digit[0]) + str(digit[0])
                        minu = str(digit[0]) + str(digit[0])
                    return new_hour + ":" + str(digit[0]) + str(digit[0])
