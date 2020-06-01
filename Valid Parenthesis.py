"""
class Solution:
    def isValid(self, s: str) -> bool:
        if len (s)== 0 or s=='*':
            return True
        if len (s)==1:
            return False
        
        leftBalance = 0
        for i in s:
        
       
            if i == ')':
                leftBalance-= 1
            else:
                leftBalance+=1
                
            if leftBalance<0:
                return False
                        
        if leftBalance == 0:
            return True
        
        rightBalance = 0
        
               
        for i in reversed(s):
            if i == '(':
                rightBalance-= 1
            else:
                 rightBalance+=1
                
            if  rightBalance<0:
                return False
            return True
        
        """
=============================================================================================================================================
"""
class Solution:
    def isValid(self, s: str) -> bool:
        
        Stack , Star_Stack = [],[]
        for index , char in  enumerate(s):
            if char =='*':
                Stack.append(index)
            elif char=='*':
                Star_Stack.append(index)
            elif char==')':
                if len (Stack)>0:
                    Stack.pop()
                elif len(Star_Stack)>0:
                    Star_Stack.pop()    
                else:
                    return False
        while Stack and Star_Stack:
            if Stack[-1]<Star_Stack[-1]:
                Stack.pop()
                Star_Stack.pop()
            else:
                break
        return len(Stack)==0        
                """
    ==========================================================================================================================================            

class Solution(object):
    # @return a boolean
    def isValid(self, s):
        stack, lookup = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in s:
            if parenthese in lookup:
                stack.append(parenthese)
            elif len(stack) == 0 or lookup[stack.pop()] != parenthese:
                return False
        return len(stack) == 0
