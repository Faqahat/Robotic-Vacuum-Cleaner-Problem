# Robotic Vacuum Cleaner Problem



![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)

 A small robot has been designed to automatically clean a room by picking up dirt from the floor.
Floor comprises of 'n' number of tiles of same size (e.g. 1 square foot each) making the room a grid of random size with equal length and width (e.g. 4x4, 8x8, 16x16 etc.). 
Each tile in the room represents a different location and is represented by a pair (x,y) where x is position on x-axis and y is position on y-axis making the tile (0,0) the bottom left corner of the room. 
Each tile has different amount of dirt lying on it. A sample room of size 4x4 is shown in Figure 1.0. 

Numbers like 5, 6, 2 etc. in the figure represent the amount of dirt lying on each tile.

| 5 | 6 | 2 | 1 |
|---|---|---|---|
| 2 | 0 | 7 | 5 |
| 9 | 1 | 8 | 6 |
| 3 | 0 | 3 | 4 |

### Input: 
The input consists of multiple test cases. The first line of the input is the number of test cases, N. 
Each of the following N lines contains 

1. the number of rows, r 
2. the number of columns, c 
3. a row-wise entry of the data.


### Output: 
For each test case, print a single line that says "Case i', where `i' is the test case number, followed by the starting point (top left tile), the top right tile, the bottom right tile ,the ending point (the bottom left tile) and the total amount of dirt lying in that area

##### Sample input 

```
1
445621207591863034 
```
##### Sample Output 
```Case 1: (2,2), (3,2), (3,1), (2,1), 26  ```
