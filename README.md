# 8_puzzle_search

This project is part of a programming assignment for the Artificial Intelligence course taught at Trinity College-Hartford.

We were tasked to implement two search algorithms for the 8-puzzle problem and analyze their relative performance.

I chose to implement BFS and A* Search with two different heuristics. 

## Analysis/Writeup

Using the three algorithms was insightful and practical in the context of understanding the importance of efficiency
and usability in Artificial Intelligence.

### Breadth First Search:
  
  This search algorithm took the longest (in time of execution) compared to the other search
algorithms. It is quite noticeable that it had the highest number of search tree nodes explored
before arriving at a solution. What is interesting, though, is that it also had the shortest length to a
solution compared to A Star. It took the longest, but it also came across the shortest path compared
to both A Star algorithms that finished upon finding one solution. To note, at times running BFS took
a rather long time (due to linear search of reached nodes) and I would have to restart the program
and run with another random configuration. I assumed that this behavior is natural since there is a
large state space and due to the nature of the algorithm. Evaluation function here is the depth of
the node so we are able to find an optimal (in terms of path length) solution compared to the
lengthy paths that A star generates (on both heuristics).

### A Star Misplaced Tiles Heuristic:

  This search algorithm with the first heuristic was the second fastest. It explored notably less nodes
than in BFS but had a much larger solution length compared to BFS. This heuristic was less
efficient than the Manhattan heuristic used in the following explanation.

### A Star Manhattan Heuristic:

  This search algorithm was the quickest out of all the searches. It consistently provided me with a
quick (time-wise) solution to the puzzle no matter how ‘difficult’ it may have been. It is noticeably
quicker than the misplaced tiles heuristic and extremely faster than BFS ever was on any initial
state. Again, it is quite noticeable that as the number of search tree nodes decreases, the length of
the solution increases compared to BFS. Since it is an informed search algorithm, this is
understandable since it will always find a solution if one exists, however, it is not the most optimal
solution (path distance wise) because BFS always gives a shorter path. This heuristic, however,
gave a shorter path compared to the misplaced tiles heuristic since this took the euclidean distance
of tiles from their goal positions. To note, there are instances where Manhattan had a longer path
than Misplaced alongside having the same path length as BFS. There are a couple of examples
below where this is the case, however, the general trend still holds that as the number of search
tree nodes decreases, the length of the solution increases (varies on heuristic). It depends on the
initial state, but the majority of them follow this pattern.
