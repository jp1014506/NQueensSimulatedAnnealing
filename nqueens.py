import time
import random
import math

class Board():
    """An N-queens solution attempt."""
     
    def __init__(self, queens):
        """Instances differ by their queen placements."""
        self.queens = queens.copy() # No aliasing!

    def display(self):
        """Print the board."""
        for r in range(len(self.queens)):
            for c in range(len(self.queens)):
                if self.queens[c] == r:
                    print('Q', end='')
                else:
                    print('-', end='')
            print()
        print()
    
    def moves(self):
        """
        Return a list of possible moves given the current placements.
        Each possible move is of the tuple representation: (queen column, new row for queen).
        """
        n = len(self.queens)
        all_moves = []
        for col in range(n):
            current_row = self.queens[col]
            for row in range(n):
                if row != current_row:
                    all_moves.append((col, row))

        return all_moves

    def neighbor(self, move):
        """Return a Board instance like this one but with one move made."""
        col, new_row = move
        new_queens = self.queens.copy()
        new_queens[col] = new_row
        return Board(new_queens)

    def cost(self):
        """
        Compute the cost of this solution.
        Return number of attacking queens.
        """
        cost = 0
        n = len(self.queens) 
        for col1 in range(n):
            for col2 in range(col1 + 1, n):
                row1 = self.queens[col1]
                row2 = self.queens[col2]
                if row1 == row2 or abs(col1 - col2) == abs(row1 - row2):
                    cost += 2

        return cost

class Agent():
    """Knows how to solve an n-queens problem with simulated annealing."""

    def anneal(self, board):
        """Return a list of moves to adjust queen placements."""
        current = board
        t = 100.0
        decay = 0.95
        min_temp = 0.001
        path = []

        while t > min_temp:
            if current.cost() == 0:
                return path

            possible_moves = current.moves()
            move = random.choice(possible_moves)
            neighbor = current.neighbor(move)
            
            delta_cost = neighbor.cost() - current.cost()
            if delta_cost < 0:
                current = neighbor
                path.append(move)
                if current.cost() == 0:
                    return path
            else:
                probability = math.exp(-delta_cost / t)
                if random.random() < probability:
                    current = neighbor
                    path.append(move)
            t *= decay
        return path
   
def main():
    """Create a problem, solve it with simulated anealing, and console-animate."""

    queens = dict()
    for col in range(8):
        row = random.choice(range(8))
        queens[col] = row

    board = Board(queens)
    board.display()
    
    agent = Agent()
    path = agent.anneal(board)
    
    while path:
        move = path.pop(0)
        board = board.neighbor(move)
        time.sleep(0.1)
        board.display()

if __name__ == '__main__':
    main()