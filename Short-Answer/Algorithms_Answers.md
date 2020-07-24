#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - As input size n increases, so does the runtime. Although you are cubing n in the while loop, you are adding n^2 to a, so it would reduce to linear runtime. 


b) O(n log n) - The initial for loop would have an O(n) runtime because as n increases, so does the amount of operations that need to run. The while loop, on the other hand, is doubling j each time it runs, essentially halving the amount of times it'll need to run, which would be an O(log n) runtime. To get the runtime for the entire snippet, I'd multiply O(n) * O(log n) to get O(n log n).


c) O(n) - The amount of times the recursive function will run is directly related to the input size bunnies.

## Exercise II

I would use a binary search tree model to help solve this problem as follows: 

mid_floor = n // 2

throw egg off the building at mid_floor

if the egg breaks, find the floor between the floor you just threw the egg from and the bottom of the building. Throw the egg again. 

if the egg does not break, find the floor between the floor you just threw the egg from and the n (top) floor of the building. Throw the egg again. 

Repeat this process until you are moving by just one floor. If the egg breaks and you move down one floor and the egg doesn't break, the previous floor is floor f. If the egg does not break and you move up one floor and the egg breaks, your current floor is floor f. 

The runtime complexity of this solution would be O(log n), as it is based on binary search and you are essentially halving the amount of floors you need to search to find floor f each time you throw an egg. 
