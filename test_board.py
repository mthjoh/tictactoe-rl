from board import Board

b = Board()
b.make_move(4,1) # X in the center
b.make_move(0,-1) # O in the top-left
b.show()
print("Winner:", b.check_winner())

