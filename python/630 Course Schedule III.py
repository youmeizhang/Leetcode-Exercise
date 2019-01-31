class Solution(object):
    def scheduleCourse(self, courses):
        courses.sort(key=lambda x: x[1])
        longest = [-1]
        start = 0
        for i in range(len(courses)):
            start = courses[i][0] + start
            if  start <= courses[i][1]:
                longest.append(courses[i][0])

            elif start > courses[i][1]:
                max_value = max(longest)
                if max_value == -1:
                    start -= courses[i][0]
                elif max_value <= courses[i][0]:
                    #delete current course
                    start -= courses[i][0]
                else:
                    #delete previous longese course
                    start -= max_value
                    longest.remove(max_value)
                    longest.append(courses[i][0])
        return len(longest) - 1
            
