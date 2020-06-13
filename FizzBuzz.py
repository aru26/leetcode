class Solution(object):
    def fizzBuzz(self, n):
        """
        if (input % 3 == 0)and (input % 5 == 0):
            return "FizzBuzz"
        if(input % 3 == 0):
            return "Fizz"
        if(input % 5 == 0):
            return "Buzz"
        return input
        """
    
        
        
        
        """
        :type n: int
        :rtype: List[str]
        """
    
        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]
        
