from nqueens import *

# 5 x 5
queens_5a = {}
queens_5a[0] = 0
queens_5a[1] = 0
queens_5a[2] = 0
queens_5a[3] = 0
queens_5a[4] = 0


def test_moves_5a():
    result = Board(queens_5a).moves()
    gold = [(0,1),(0,2),(0,3),(0,4),(1,1),(1,2),(1,3),(1,4),(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3),(3,4),(4,1),(4,2),(4,3),(4,4)]
    assert set(result) == set(gold)
    assert len(result) == len(gold)

def test_neighbor_5a():
    b = Board(queens_5a)
    result = b.neighbor((0,3))   # move queen at col 0 from current row to row 3
    assert result.queens[0] == 3
    assert b.queens[0] == 0


def test_cost_5a():
    assert Board(queens_5a).cost() == 20
  

def test_anneal_5a():
    # give 5 tries for this attept to work, easy to get stuck in local minima
    
    attempts_remaining = 5
    while attempts_remaining > 0:
        attempts_remaining -= 1
    
        board = Board(queens_5a)
        path = Agent().anneal(board)
        assert len(path) > 0
        while path:
            move = path.pop(0)
            board = board.neighbor(move)
        if board.cost() == 0:
            break

           

