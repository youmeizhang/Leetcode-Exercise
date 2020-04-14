## Leetcode

### Prefix Sum
* 525 Contiguous Array: [0,1,0]
  * replace 0 with -1, then if prefix sum equal to 0 we know the numbers of 0 and 1 are same
  * record the first index `i` that a prefix sum appears then when the same prefix sum happens again at `j`, sum between `j - i` must be 0
 
