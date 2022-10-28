import copy

def array_test(board):
    safe = copy.deepcopy(board)
    safe[0][0] = "foo"
    return safe

board = [[0 for y in range(5)] for x in range(5)]
print(board)
foo = array_test(board)
print(board)
print(foo)