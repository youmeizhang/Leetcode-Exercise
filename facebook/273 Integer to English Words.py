class Solution(object):
    def numberToWords(self, num):
        dic_1 = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
          "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        dic_2 = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        dic_3 = ["Hundred"]
        dic_4 = ["Thousand", "Million", "Billion"]

        words, digits = [], 0
        while num:
            token, num = num % 1000, num // 1000
            word = ""
            if token > 99:
                word += dic_1[token // 100] + ' ' + dic_3[0] + ' '
                token %= 100
            if token > 19:
                word += dic_2[token // 10 - 2] + ' '
                token %= 10
            if token > 0:
                word += dic_1[token] + ' '
            word = word.strip()
            if word:
                word += ' ' + dic_4[digits-1] if digits else ''
                words += word,
            digits += 1

        return ' '.join(words[::-1]) or "Zero"
