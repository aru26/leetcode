
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        """
            1. build a hashmap to record the frequenc of each letter
            2. Use heap, use min heap and keep the size as k
            
            Time: O(nlogk)
            Space: O(n)
        """
        
        # 1. build a hashmap to record the frequenc of each letter
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        print(dic)
        
        # top k most frequency words, [1,2], put the frequency into the heap
        heap = []
        for key, frequency in dic.items():
            heappush(heap, (frequency, key))
            if len(heap) > k:
                heappop(heap)
            
        result = []
        for _, element in heap:
            result.append(element)
        return result

========================================================================================================================================
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.
Solution
Approach 1: Heap
Let's start from the simple heap approach with \mathcal{O}(N \log k)O(Nlogk) time complexity. To ensure that \mathcal{O}(N \log k)O(Nlogk) is always less than \mathcal{O}(N \log N)O(NlogN), the particular case k = Nk=N could be considered separately and solved in \mathcal{O}(N)O(N) time.

Algorithm

The first step is to build a hash map element -> its frequency. In Java, we use the data structure HashMap. Python provides dictionary subclass Counter to initialize the hash map we need directly from the input array.
This step takes \mathcal{O}(N)O(N) time where N is a number of elements in the list.

The second step is to build a heap of size k using N elements. To add the first k elements takes a linear time \mathcal{O}(k)O(k) in the average case, and \mathcal{O}(\log 1 + \log 2 + ... + \log k) = \mathcal{O}(log k!) = \mathcal{O}(k \log k)O(log1+log2+...+logk)=O(logk!)=O(klogk) in the worst case. It's equivalent to heapify implementation in Python. After the first k elements we start to push and pop at each step, N - k steps in total. The time complexity of heap push/pop is \mathcal{O}(\log k)O(logk) and we do it N - k times that means \mathcal{O}((N - k)\log k)O((N−k)logk) time complexity. Adding both parts up, we get \mathcal{O}(N \log k)O(Nlogk) time complexity for the second step.

The third and the last step is to convert the heap into an output array. That could be done in \mathcal{O}(k \log k)O(klogk) time.

In Python, library heapq provides a method nlargest, which combines the last two steps under the hood and has the same \mathcal{O}(N \log k)O(Nlogk) time complexity.

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        # O(1) time 
        if k == len(nums):
            return nums
        
        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)   
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get) 
        
        Complexity Analysis

Time complexity : \mathcal{O}(N \log k)O(Nlogk) if k < Nk<N and \mathcal{O}(N)O(N) in the particular case of N = kN=k. That ensures time complexity to be better than \mathcal{O}(N \log N)O(NlogN).

Space complexity : \mathcal{O}(N + k)O(N+k) to store the hash map with not more NN elements and a heap with kk elements.

=====================================================================================================================================================
Approach 2: Quickselect
Hoare's selection algorithm

Quickselect is a textbook algorthm typically used to solve the problems "find kth something": kth smallest, kth largest, kth most frequent, kth less frequent, etc. Like quicksort, quickselect was developed by Tony Hoare, and also known as Hoare's selection algorithm.

It has \mathcal{O}(N)O(N) average time complexity and widely used in practice. It worth to note that its worth case time complexity is \mathcal{O}(N^2)O(N 
2
 ), although the probability of this worst-case is negligible.

The approach is the same as for quicksort.

One chooses a pivot and defines its position in a sorted array in a linear time using so-called partition algorithm.

As an output, we have an array where the pivot is on its perfect position in the ascending sorted array, sorted by the frequency. All elements on the left of the pivot are less frequent than the pivot, and all elements on the right are more frequent or have the same frequency.

Hence the array is now split into two parts. If by chance our pivot element took N - kth final position, then kk elements on the right are these top kk frequent we're looking for. If not, we can choose one more pivot and place it in its perfect position.
























