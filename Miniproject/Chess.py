import chess

board = chess.Board()
user_color = input("Please input your colour, b or w: ")

# print(board.legal_moves)
# print(board)
#position values for certain peices
blackKing = [[ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    	[ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    	[ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    	[ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    	[ -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
    	[ -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
    	[  2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0 ],
    	[  2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0 ]]
king = blackKing[::-1]

queen = [[ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
		 [ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
    	 [ -1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
    	 [ -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
    	 [  0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
    	 [ -1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
    	 [ -1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0],
   	 	 [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]]

blackRook = [[  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
    	[  0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5],
    	[ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    	[ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    	[ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    	[ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    	[ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    	[  0.0,   0.0, 0.0,  0.5,  0.5,  0.0,  0.0,  0.0]]
rook = blackRook[::-1]

knight = [[-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
          [-4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0],
          [-3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0],
          [-3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0],
          [-3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0],
          [-3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0],
          [-4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0],
          [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]]

blackBishop = [[ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
		  [ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
   		  [ -1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0],
   		  [ -1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0],
   		  [ -1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0],
  		  [ -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0],
   		  [ -1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0],
   		  [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]]
bishop = blackBishop[::-1] #black and white players, not squares on the board.

blackPawn = [[0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
        [5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0],
        [1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0],
        [0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5],
        [0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0],
        [0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5],
        [0.5,  1.0, 1.0,  -2.0, -2.0,  1.0,  1.0,  0.5],
        [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]]
pawn = blackPawn[::-1]

def piecesEval(piece): #value of pieces still alive
	#piece is a chess object
	if piece == None:
		return 0
	if piece.piece_type == 1: #pawn
		if piece.color:
			return 10
		else:
			return -10
	elif piece.piece_type == 2: #knight
		if piece.color:
			return 40
		else:
			return -40
	elif piece.piece_type == 3: #bishop
		if piece.color:
			return 30
		else:
			return -30
	elif piece.piece_type == 4: #rook
		if piece.color:
			return 50
		else:
			return -50
	elif piece.piece_type == 5: #queen
		if piece.color:
			return 90
		else:
			return -90
	elif piece.piece_type == 6: #king
		if piece.color:
			return 900
		else:
			return -900

def positionEval(piece, squareName): #best position for a piece
	if piece == None:
		return 0
	#translating the square name to the index of the 2D array
	x = int (squareName[1])
	y = ord(squareName[0])-96
	#x represents the columns: a,b,c,d,e,f,g,h; need to convert to int
	#y represents the rows: 1,2,3,4,5,6,7,8
	value = 0
	if piece.piece_type == 1: #pawn
		if piece.color:
			value = pawn[y-1][x-1]
		else:
			value = blackPawn[y-1][x-1]
	elif piece.piece_type == 2: #knight
		value = knight[y-1][x-1]
	elif piece.piece_type == 3: #bishop
		if piece.color:
			value = bishop[y-1][x-1]
		else:
			value = blackBishop[y-1][x-1]
	elif piece.piece_type == 4: #rook
		if piece.color:
			value = rook[y-1][x-1]
		else:
			value = blackRook[y-1][x-1]
	elif piece.piece_type == 5: #queen
		value = queen[y-1][x-1]
	elif piece.piece_type == 6: #king
		if piece.color:
			value = king[y-1][x-1]
		else:
			value = blackKing[y-1][x-1]
	return value

def evaluateBoard(board): #not implemented yet
	total = 0
	for i in range(64):
		piece = board.piece_at(i)
		total = total + piecesEval(piece) + positionEval(piece, chess.square_name(i))
	return total

def minimaxStart(board, depth, maximizingPlayer):
	possibleMoves = list(board.legal_moves)
	bestMove = -9999
	worstMove = 9999
	bestMoveFound = "0000"

	for move in possibleMoves:
		board.push(move)
		value = minimax(board, depth-1, -10000, 10000, not maximizingPlayer)
		board.pop()
		if maximizingPlayer: #if comp playing as white (maximizing player)
			if value>=bestMove:
				bestMove = value
				bestMoveFound = move #move (string) and board (object) are different
		else: #if comp playing as black (minimizing player)
			if value<=worstMove:
				worstMove = value
				bestMoveFound = move #move (string) and board (object) are different
	return bestMoveFound

def minimax(board, depth, alpha, beta, maximizingPlayer):
	if depth == 0: #or gameOver in position
		value = evaluateBoard(board)
		return value  #make use of heuristic function here
	
	possibleMoves = list(board.legal_moves)
	if maximizingPlayer:
		maxEval = -9999
		for move in possibleMoves: #evaluating each possible moves
			board.push(move)
			eval = minimax(board, depth-1, alpha, beta, False)
			maxEval = max(maxEval, eval)
			board.pop()
			alpha = max(alpha, eval)
			if beta <= alpha:
				break
		return maxEval
 
	else:
		minEval = 9999
		for move in possibleMoves:
			board.push(move)
			eval = minimax(board, depth-1, alpha, beta, True)
			minEval = min(minEval, eval)
			board.pop()
			beta = min(beta, eval)
			if beta <= alpha:
				break
		return minEval

compGoFirst = True
blackwins = False
if user_color == 'b':
	compGoFirst = True
else:
	compGoFirst = False

illegalMoveCount = 0
while not board.is_game_over(claim_draw=True):
	if compGoFirst:
		if illegalMoveCount<1: #prevents AI from playing until player has made a legal move
			compMove = minimaxStart(board, 5, compGoFirst)
			print(compMove)
			board.push(compMove)
			print(board)
		legalMoves = list(board.legal_moves)
		print(legalMoves)
		playermove = input("Enter your move: ")
		pm = chess.Move.from_uci(playermove)
		if pm in legalMoves:
			board.push(pm)
			illegalMoveCount = 0
			print(board)
		else: 
			print("Illegal move, pls try again")
			illegalMoveCount = illegalMoveCount + 1
	else:
		legalMoves = list(board.legal_moves)
		print(legalMoves)
		playermove = input("Enter your move: ")
		pm = chess.Move.from_uci(playermove)
		if pm in legalMoves:
			board.push(pm)
			print(board)
			compMove = minimaxStart(board, 3, compGoFirst)
			print(compMove)
			board.push(compMove)
			print(board)
		else: 
			print("Illegal move, pls try again")
	
#Workout what happens when there is a checkmate.