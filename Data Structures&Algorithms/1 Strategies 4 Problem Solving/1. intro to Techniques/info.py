''' 
These strategies / techniques aren't algorithms, rather they are ways to think about problems
Do check how backtracking, heuristics, and dynamic programming work in real life python coding.
Do think of a grid, braeak the problem into smaller bits in the comlumn headings
Then, the items in the row section
'''
# From Dynamic Programming, use imaginary or 1d grids to divide a problem into sub problems
'''
Making the grid (diving into sub problem)
What does the grid for this problem look like? You need to answer these 
questions:
• What are the values of the cells?
• How do you divide this problem into subproblems?
• What are the axes of the grid?

Filling in the grid
Now you have a good idea of what the grid should look like. What's the formula for filling in each cell of the grid? You can cheat a little, 
because you already know what the solution should be—hish and fish have a substring of length 3 in common: ish. But that still doesn't tell 
you the formula to use. Computer scientists sometimes joke about using the Feynman algorithm. The Feynman algorithm is named after the famous 
physicist Richard Feynman, and it works like this: 
1. Write down the problem. 
2. Think real hard. 
3. Write down the solution.
The truth is, there's no easy way to calculate the formula here. You have to experiment and try to find something that works. Sometimes, 
algorithms aren't an exact recipe. They're a framework that you build your idea on top of (so the first code I write shouldn't be the final
code but rather a blueprint for me to build on)
Try to come up with a solution to this problem yourself.
'''