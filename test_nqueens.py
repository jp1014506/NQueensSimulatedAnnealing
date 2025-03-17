from nqueens import *

# 4 x 4
queens_4a = {}
queens_4a[0] = 2
queens_4a[1] = 0
queens_4a[2] = 3
queens_4a[3] = 1

queens_4b = {}
queens_4b[0] = 0
queens_4b[1] = 0
queens_4b[2] = 3
queens_4b[3] = 3

queens_4c = {}
queens_4c[0] = 0
queens_4c[1] = 0
queens_4c[2] = 0
queens_4c[3] = 0

# 6 x 6
queens_6a = {}
queens_6a[0] = 2
queens_6a[1] = 0
queens_6a[2] = 3
queens_6a[3] = 1
queens_6a[4] = 1
queens_6a[5] = 5

# 8 x 8
queens_8a = {}
queens_8a[0] = 7
queens_8a[1] = 2
queens_8a[2] = 6
queens_8a[3] = 3
queens_8a[4] = 1
queens_8a[5] = 4
queens_8a[6] = 0
queens_8a[7] = 5

queens_8b = {}
queens_8b[0] = 4
queens_8b[1] = 5
queens_8b[2] = 6
queens_8b[3] = 3
queens_8b[4] = 4
queens_8b[5] = 5
queens_8b[6] = 6
queens_8b[7] = 5

def test_moves_4a():
    result = Board(queens_4a).moves()
    gold = [(0,0),(0,1),(0,3),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(3,0),(3,2),(3,3)]
    assert set(result) == set(gold)
    assert len(result) == len(gold)

def test_moves_4b():
    result = Board(queens_4b).moves()
    gold = [(0,1),(0,2),(0,3),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(3,0),(3,1),(3,2)]
    assert set(result) == set(gold)
    assert len(result) == len(gold)

def test_moves_4c():
    result = Board(queens_4c).moves()
    gold = [(0,1),(0,2),(0,3),(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3)]
    assert set(result) == set(gold)
    assert len(result) == len(gold)   

def test_moves_6a():
    result = Board(queens_6a).moves()
    gold = [(0,0),(0,1),(0,3),(0,4),(0,5),
            (1,1),(1,2),(1,3),(1,4),(1,5),
            (2,0),(2,1),(2,2),(2,4),(2,5),
            (3,0),(3,2),(3,3),(3,4),(3,5),
            (4,0),(4,2),(4,3),(4,4),(4,5),
            (5,0),(5,1),(5,2),(5,3),(5,4)]
    assert set(result) == set(gold)
    assert len(result) == len(gold)    

def test_neighbor_4a():
    b = Board(queens_4a)
    result = b.neighbor((0,3))   # move queen at col 0 from current row to row 3
    assert result.queens[0] == 3
    assert b.queens[0] == 2

def test_neighbor_6a():
    b = Board(queens_6a)
    result = b.neighbor((3,4))   # move queen at col 3 from current row to row 4
    assert result.queens[3] == 4
    assert b.queens[3] == 1

def test_cost_4a():
    assert Board(queens_4a).cost() == 0

def test_cost_4b():
    assert Board(queens_4b).cost() == 6

def test_cost_4c():
    assert Board(queens_4c).cost() == 12

def test_cost_6a():
    assert Board(queens_6a).cost() == 4    

def test_cost_8a():
    assert Board(queens_8a).cost() == 2   

def test_cost_8b():
    assert Board(queens_8b).cost() == 34  

def test_anneal_4b():
    board = Board(queens_4b)
    path = Agent().anneal(board)
    assert len(path) > 0
    while path:
        move = path.pop(0)
        board = board.neighbor(move)
    assert board.cost() == 0    

def test_anneal_6a():
    # give 5 tries for this attept to work, easy to get stuck in local minima
    
    attempts_remaining = 5
    while attempts_remaining > 0:
        attempts_remaining -= 1
    
        board = Board(queens_6a)
        path = Agent().anneal(board)
        assert len(path) > 0
        while path:
            move = path.pop(0)
            board = board.neighbor(move)
        if board.cost() == 0:
            break

def test_anneal_8b():
    # give 5 tries for this attept to work, easy to get stuck in local minima
    
    attempts_remaining = 5
    while attempts_remaining > 0:
        attempts_remaining -= 1
    
        board = Board(queens_8b)
        path = Agent().anneal(board)
        assert len(path) > 0
        while path:
            move = path.pop(0)
            board = board.neighbor(move)
        if board.cost() == 0:
            break

    assert board.cost() == 0              

