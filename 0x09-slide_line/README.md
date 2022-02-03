# 0x09-slide_line
  
Given an array of integers, we want to be able to slide & merge it to the left or to the right. Identical numbers, if they are contiguous or separated by zeros, should be merged.

## Examples
```
alex@~/0x09-slide_line$ ./0-slide_line L 2 2 0 0
Line: 2, 2, 0, 0
Slide to the left
Line: 4, 0, 0, 0
alex@~/0x09-slide_line$ ./0-slide_line L 2 2 0 0 0 0 0 2 0 0 0 2 0 4
Line: 2, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 4
Slide to the left
Line: 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
alex@~/0x09-slide_line$ ./0-slide_line R 2 2 2 2
Line: 2, 2, 2, 2
Slide to the right
Line: 0, 0, 4, 4
alex@~/0x09-slide_line$ ./0-slide_line R 2 2 2 2 2
Line: 2, 2, 2, 2, 2
Slide to the right
Line: 0, 0, 2, 4, 4
alex@~/0x09-slide_line$ ./0-slide_line L 2 4 8 16
Line: 2, 4, 8, 16
Slide to the left
Line: 2, 4, 8, 16
alex@~/0x09-slide_line$ ./0-slide_line R 2 4 8 16
Line: 2, 4, 8, 16
Slide to the right
Line: 2, 4, 8, 16
alex@~/0x09-slide_line$ ./0-slide_line R 4 4 8 16
Line: 4, 4, 8, 16
Slide to the right
Line: 0, 8, 8, 16
```

## Thoughts
- How to determine if two numbers are identical?
- How to determine if two identical numbers are contiguous?
- How to determine if two identical numbers have zeros between them?
- What are all of the possible events?
  - How to handle all of the possible events?
    - Slide vs merge
    - Left vs right
    - Identical numbers seperated by zeros vs identical numbers not seperated by zeros
    - Where the identical numbers are in the array?


## Conclusive thoughts
- Events depend on user input, so split possible events into separate functions
- We will only ever have to slide or merge the array.
  - Sliding involves moving the numbers to the left or to the right.
  - Merging involves combining the numbers that are identical.
- If a number does not have an identical number to left or to the right, it is non mergeable but can still be slid.
- After numbers in array have been merged, one number will take double the value and the other will turn into zero.
- If array is odd in size, the last number is non mergeable and will stay in the array.
- If no slides or merges possible, return success.

