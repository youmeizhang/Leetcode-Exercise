class Solution(object):
    def isValid(self, code):
        tag_stack = []
        while code:
            if code.startswith("<![CDATA["):
                if not tag_stack: 
                    print("<!CDATA1")
                    return False
                nextIdx = code.find("]]>")
                if nextIdx == -1: 
                    print("<!CDATA2")
                    return False
                code = code[nextIdx + 3: ]

            elif code.startswith("</"):
                nextIdx = code.find(">")
                if nextIdx == -1: 
                    print("</1")
                    return False
                tag = code[2: nextIdx]
                if not tag_stack or tag != tag_stack.pop(): 
                    print("</2")
                    return False
                code = code[nextIdx + 1: ]
                if not tag_stack: return not code

            elif code.startswith("<"):
                nextIdx = code.find(">")
                if nextIdx == -1: 
                    print("<1")
                    return False
                tag = code[1:nextIdx]
                if not re.match('^[A-Z]{1,9}$', tag): 
                    print("<2")
                    return False
                tag_stack.append(tag)
                code = code[nextIdx + 1: ]

            elif not tag_stack: 
                print("tag_stack")
                return False

            else:
                code = code[1: ]

        return not tag_stack

credit to: 在线疯狂   
