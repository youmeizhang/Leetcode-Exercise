class Solution:
    def complexNumberMultiply(self, a, b):
        first_a, second_a = map(int, a[0:-1].split('+'))
        first_b, second_b = map(int, b[0:-1].split('+'))
        return str(first_a * first_b - second_a * second_b) + '+' + str(first_a * second_b + second_a * first_b) +'i'
  
#credit to: 夏洛的网
