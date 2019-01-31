class Solution:
    def solveEquation(self, equation):
        left = equation.split("=")[0]
        right = equation.split("=")[1]

        left = left.split("+")
        right = right.split("+")


        def apart(old_left):
            left = []
            for element in old_left:
                if "-" in element:
                    idx_list = [i for i in range(len(element)) if element[i] == "-"]
                    if len(idx_list) > 1:
                        tmp = element.split("-")
                        for ele in tmp:
                            if ele != "":
                                left.append("-" + ele)
                    else:
                        idx = idx_list[0]
                        new_element = element[:idx] + "+" + element[idx:]
                        tmp = new_element.split("+")

                        for ele in tmp:
                            if ele != "":
                                left.append(ele)
                else:
                    left.append(element)
       
            left_x = []
            left_num = [0]
            for i in range(len(left)):
                if "x" in left[i]:
                    if len(left_x) == 0:
                        if left[i] == "x":
                            left_x.append("1x")
                        elif left[i] == "-x":
                            left_x.append("-1x")
                        else:
                            left_x.append(left[i])
                    else:
                        former = left[i][:-1]
                        if former == "":
                            former = 1
                        elif former[0] == "-":
                            if former == "-":
                                former = -1
                            else:

                                former = -1 * int(former[1:])
                        else:
                            former = int(former)

                        latter = left_x[-1][:-1]
                        if latter == "":
                            latter = 1
                        elif latter[0] == "-":
                            if latter == "-":
                                latter = -1
                            else:
                                latter = -1 * int(latter[1:])
                        else:
                            latter = int(latter)

                        left_x = ["1x"] if (former + latter) == 1 else [str(former + latter) + "x"]

                elif "-" in left[i]:
                    left_num = [left_num[-1] - int(left[i][1:])]
                else:
                    left_num = [int(left[i]) + int(left_num[-1])]

            return left_x, left_num

        left_x, left_num = apart(left)
        right_x, right_num = apart(right)

        if not left_x and not right_x:
            prefix = 0
        elif not left_x:
            prefix = int(right_x[0][:-1])
            num = left_num[0] - right_num[0]
        elif not right_x:
            prefix = int(left_x[0][:-1])
            num = right_num[0] - left_num[0]
        else:
            prefix = int(left_x[0][:-1]) - int(right_x[0][:-1])

            num = right_num[0] - left_num[0]

        if num == 0:
            if prefix == 0:
                return "Infinite solutions"
            elif prefix != 0:
                return "x=0"
            else:
                return "No solution"

        elif prefix == 0:
            return "No solution"
        else:
            return "x=" + str(int(num / prefix))
