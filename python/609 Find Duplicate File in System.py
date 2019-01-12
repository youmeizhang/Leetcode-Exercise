class Solution(object):
    def findDuplicate(self, paths):
        dic = {}
        res = []
        for path in paths:
            path_split = path.split(" ")
            for i in range(1, len(path_split)):
                content = path_split[i][path_split[i].find("(") + 1 : path_split[i].find(")")]
                if content in dic:
                    res_path = path_split[0] + '/' + path_split[i].replace("(" + content + ")","")
                    if res_path in dic[content]:
                        continue
                    else:
                        dic[content].append(res_path)
                else:
                    dic[content] = [path_split[0] + '/' + path_split[i].replace("(" + content + ")","")]
        res = []
        for i, j in enumerate(dic):
            if len(dic[j]) > 1:
                res.append(dic[j])
        return res
