class Solution:
    def plusOne(self, digits: 'List[int]') -> 'List[int]':
        carry = 1
        i = len(digits) - 1
        while carry and i > -1:
            new_digit = digits[i] + carry
            carry = new_digit // 10
            digits[i] = new_digit % 10
            #print(new_digit)
            i -= 1
        if carry:
            digits = [carry] + digits
        return digits
