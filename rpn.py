funcs = {'+' : lambda x,y:x+y,
		 '-' : lambda x,y:x-y,
		 '*' : lambda x,y:x*y,
		 '/' : lambda x,y:x/y if x*y>0 else -(-x/y),#-6/10 = -1 it's a bug!!
        }
class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
    	s = [0] * len(tokens)
    	head = 0
        for token in tokens:
        	func = funcs.get(token)
        	if func:
        		head -= 2
        		s[head] = func(s[head],s[head+1])
        		head += 1
        	else:
        		s[head] = int(token)
        		head += 1
        return s[head-1]

case1 = ["2", "1", "+", "3", "*"]
case2 = ["4", "13", "5", "/", "+"]
case3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
case4 = ["4","-2","/","2","-3","-","-"]
print -6/10
cases = [case1,case2]
cases = [case3,case4]

s = Solution()
for case in cases:
	print int(s.evalRPN(case))
