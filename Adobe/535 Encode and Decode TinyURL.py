import string, random

class Codec:
    def __init__(self):
        self.full_tiny = {}
        self.tiny_full = {}
        
    def encode(self, longUrl):   
        def gen():
            letters = string.ascii_letters + string.digits
            res = ''
            for i in range(6):
                res += letters[random.randint(0,10000)%62]
            return res
        
        u = "http://tinyurl.com/" + gen()
            
        if longUrl not in self.full_tiny:
            while u in self.tiny_full:
                u = "http://tinyurl.com/" + gen()
                
            self.full_tiny[longUrl] = u  
            self.tiny_full[u] = longUrl

        return u
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        
    def decode(self, shortUrl):
        if shortUrl in self.tiny_full:
            return self.tiny_full[shortUrl]
        else:
            return ''
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
