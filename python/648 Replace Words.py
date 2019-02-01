class Solution:
    def replaceWords(self, dic, sentence):
        sentence = sentence.split(" ")
    
        for i in range(len(sentence)):
            for word in dic:
                if word == sentence[i][:len(word)]:
                    if len(word) < len(sentence[i]):
                        sentence[i] = word
                    else:
                        continue
                else:
                    continue

        return " ".join(sentence)
