import string
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.split('\W+', paragraph)

        dic = collections.Counter(paragraph)


        dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

        for i, v in enumerate(dic):

            if v[0] in banned:
                continue
            else:
                return v[0]
