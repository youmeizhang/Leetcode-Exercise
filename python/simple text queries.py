def textQueries(sentences, queries):
    # Write your code here
    for j in range(len(queries)):
        res = []
        for i in range(len(sentences)):
            sen = sentences[i].split(" ")
            que = queries[j].split(" ")
            tmp = set(sen) - (set(sen) - set(que))
            if list(sorted(list(tmp))) == list(sorted(que)):
                res.append(i)
                
        if res == []:
            print(-1)
        else:
            for i in res:
                print(i, end = " ")
            print("")
