class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            'I':1,
            
            'V':5,
            
            'X':10,
            
            'L':50,

            'C':100,

            'D':500,

            'M':1000,
        }
        total = 0
        current = 0
        previous = 0
        for i in range(len(s)):
            current = dic[s[i]]
            if current>previous:
                total = total + current - 2 * previous           
            else:
                total += current
            previous = current
        return total
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
