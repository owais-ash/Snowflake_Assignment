# python-assignment

# question and approach
https://leetcode.com/problems/surrounded-regions/solutions/3400240/python-simple-and-clean-beats-99-89/

After looking at the question, the following approach was taken:-

Naive Approach:-
We can traverse the entire matrix, for every position we check whether the O cell is surrounded by X or not. And for every position we will have to check the entire length of column and row to ensure that the cell is surrounded or not. Time Complexity: O(row * column)^2

Optimized Approach:-
Basically we will be searching in a matrix for certain positions satisfying certain conditions and hence searching algorithm DFS(depth first search) can be used.
First, we need to find all the regions that are surrounded by 'X' and mark them by flipping all their 'O's to 'X'. 
To identify the surrounding regions, we will traverse the board and mark all the 'O's that are not surrounded by 'X'. 
We can begin by visiting all the boundary cells that have 'O's and perform DFS to mark all the 'O's that are connected to them using some other letter, say ’k’. 
Once we have marked all the 'O's that are not surrounded by 'X', we can simply change the marked 'O's to 'X' and unmark them.
Then we finally can output our solved matrix.
Time Complexity: 2 x O(row * column) (since we traversing the board twice)

Solution:-
First inside our solve(board) function I create a function dfs(i, j) that takes the row and column index of a cell parameter and marks it as visited. The dfs function then calls itself recursively on all the neighboring cells of the current cell that have 'O' and are not already marked visited.
Then I traversed the board and called the dfs function on all the boundary cells that contain 'O's, marking all the 'O's that are not surrounded by 'X' as 'k' .
Finally traversed the board again to change all the marked 'k's to 'X' and unmark them.

