import random
import time
board = {1:' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}

def show_board(board):
	print(f'| {board[1]} | {board[2]} | {board[3]} |')
	print(f'| {board[4]} | {board[5]} | {board[6]} |')
	print(f'| {board[7]} | {board[8]} | {board[9]} |\n')
	


def players_turn(board):
	while True:
		try:
			number = int(input('Sua vez: '))
			time.sleep(1)
		
			if board[number] == ' ':
				board[number] = 'X'
				print(f'\033[1;33mVocê escolheu a posição {number}\033[0m')
				show_board(board)
				break
			
			else: 
				print('\033[1;31mPosição já ocupada, tente outra!\033[0m')
				show_board(board)
				
		except (ValueError, KeyError):
			print('\033[1;31mApenas números entre 1 e 9 são permitidos.\033[0m')
			show_board(board)

			
									
def computers_turn(board):
	rand = random.randint(1, 9)
	while True:
		if board[rand] != ' ':
			rand = random.randint(1, 9)
		elif board[rand] == ' ':
			break
			
	print('Vez do computador: ')
	time.sleep(1)
	board[rand] = 'O'
	print(f'\033[1;33mComputador escolheu a posição {rand}\033[0m')
	show_board(board)
	


def victory(board, symbol):
	if board[1] == symbol and board[2] == symbol and board[3] == symbol:
		return True

	elif board[4] == symbol and board[5] == symbol and board[6] == symbol:
	    return True
	
	elif board[7] == symbol and board[8] == symbol and board[9] == symbol:
	    return True
	
	elif board[1] == symbol and board[4] == symbol and board[7] == symbol:
	    return True
	
	elif board[2] == symbol and board[5] == symbol and board[8] == symbol:
	    return True
	
	elif board[3] == symbol and board[6] == symbol and board[9] == symbol:
	    return True
	
	elif board[1] == symbol and board[5] == symbol and board[9] == symbol:
	    return True
	
	elif board[3] == symbol and board[5] == symbol and board[7] == symbol:
	    return True
	
	return False
		


def main():
	print('Escolha um dos números para fazer uma jogada.')
	print(f'| {1} | {2} | {3} |')
	print(f'| {4} | {5} | {6} |')
	print(f'| {7} | {8} | {9} |')
	while True:
		
		players_turn(board)
		
		if victory(board, 'X'):
			print('\033[1;32mParabéns você venceu!\n(o computador é burro!)\033[0m')
			print('')
			break
		
		if ' ' not in board.values():
			print('\033[1;244mEmpate\033[0m')
			break
		
		computers_turn(board)
			
		if victory(board, 'O'):
			print('\033[1;31mComputador venceu!\033[0m')
			break
			


if __name__ == '__main__':
	main()
