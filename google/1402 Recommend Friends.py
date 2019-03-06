class Solution:
    """
    @param friends: people's friends
    @param user: the user's id
    @return: the person who most likely to know
    """
    def recommendFriends(self, friends, user):
        user_friends = friends[user]
        user_friends.append(user)
    
        unknown = list(set([i for i in range(len(friends))]) - set(user_friends))

        dic = collections.defaultdict(list)
    
        res = -1
        count = float('-inf')
    
        for i in unknown:
            tmp = list(set(friends[i]) & set(friends[user]))
            dic[i] = tmp
            if len(tmp) > count and tmp != []:
                res = i
                count = len(tmp)

        return res 
