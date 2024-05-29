"""
Python Data Structures - A Game-Based Approach
BFS maze solver.
Robin Andrews - https://compucademy.net/
The queue contains positions as (row, column) tuples. Predecessors are kept in a dictionary.
"""

from helpers import get_path, offsets, is_legal_pos, read_maze
from queue_ll import Queue


def bfs(maze, start, goal):
    my_queue= Queue()
    my_queue.enqueue(start)
    path={start: None}
    maze[start[0]][start[1]]='*'
    while my_queue.size():
        i,j = my_queue.dequeue()
        if((i,j)==goal):
            return get_path(path, start, goal)
        neighbors = [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]
        for neighbor in neighbors:
            if(is_legal_pos(maze, neighbor)):
                my_queue.enqueue(neighbor)
                maze[i][j]='*'
                path[neighbor] = (i,j)
    return None
if __name__ == "__main__":
    # Test 1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = bfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]

    # Test 2
    maze = read_maze("mazes/mini_maze_bfs.txt")
    # for row in maze:
    #     print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = bfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]

    # Test 3
    maze = read_maze("mazes/mini_maze_bfs.txt")
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = bfs(maze, start_pos, goal_pos)
    assert result is None
