Approach 1: Brute Force
Algorithm

In this brute force approach we take all possible step combinations i.e. 1 and 2, at every step. At every step we are calling the function climbStairsclimbStairs for step 11 and 22, and return the sum of returned values of both functions.

climbStairs(i,n)=(i + 1, n) + climbStairs(i + 2, n)climbStairs(i,n)=(i+1,n)+climbStairs(i+2,n)

where ii defines the current step and nn defines the destination step.
Java Code:
public class Solution {
    public int climbStairs(int n) {
        return climb_Stairs(0, n);
    }
    public int climb_Stairs(int i, int n) {
        if (i > n) {
            return 0;
        }
        if (i == n) {
            return 1;
        }
        return climb_Stairs(i + 1, n) + climb_Stairs(i + 2, n);
    }
}
Complexity Analysis

Time complexity : O(2^n)O(2 
n
 ). Size of recursion tree will be 2^n2 
n
 .

Recursion tree for n=5 would be like this:

Climbing_Stairs

Space complexity : O(n)O(n). The depth of the recursion tree can go upto nn.

=====================================================================================
Approach 2: Recursion with Memoization
Algorithm

In the previous approach we are redundantly calculating the result for every step. Instead, we can store the result at each step in memomemo array and directly returning the result from the memo array whenever that function is called again.

In this way we are pruning recursion tree with the help of memomemo array and reducing the size of recursion tree upto nn.

Java Code:
public class Solution {
    public int climbStairs(int n) {
        int memo[] = new int[n + 1];
        return climb_Stairs(0, n, memo);
    }
    public int climb_Stairs(int 
    i, int n, int memo[]) {
        if (i > n) {
            return 0;
        }
        if (i == n) {
            return 1;
        }
        if (memo[i] > 0) {
            return memo[i];
        }
        memo[i] = climb_Stairs(i + 1, n, memo) + climb_Stairs(i + 2, n, memo);
        return memo[i];
    }
}

Complexity Analysis

Time complexity : O(n)O(n). Size of recursion tree can go upto nn.

Space complexity : O(n)O(n). The depth of recursion tree can go upto nn.
===========================================================================================================
Approach 3: Fibonacci Number
Algorithm

In the above approach we have used dpdp array where dp[i]=dp[i-1]+dp[i-2]dp[i]=dp[i−1]+dp[i−2]. It can be easily analysed that dp[i]dp[i] is nothing but i^{th}i 
th
  fibonacci number.

Fib(n)=Fib(n-1)+Fib(n-2)Fib(n)=Fib(n−1)+Fib(n−2)

Now we just have to find n^{th}n 
th
  number of the fibonacci series having 11 and 22 their first and second term respectively, i.e. Fib(1)=1Fib(1)=1 and Fib(2)=2Fib(2)=2.
Java Code:
public class Solution {
    public int climbStairs(int n) {
        if (n == 1) {
            return 1;
        }
        int first = 1;
        int second = 2;
        for (int i = 3; i <= n; i++) {
            int third = first + second;
            first = second;
            second = third;
        }
        return second;
    }
}

Complexity Analysis

Time complexity : O(n)O(n). Single loop upto nn is required to calculate n^{th}n 
th
  fibonacci number.

Space complexity : O(1)O(1). Constant space is used.
===================================================================================================================================






















