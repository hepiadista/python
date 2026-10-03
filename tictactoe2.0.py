import random
import time

def show_board(board):
	print(f'| {board[1]} | {board[2]} | {board[3]} |')
	print(f'| {board[4]} | {board[5]} | {board[6]} |')
	print(f'| {board[7]} | {board[8]} | {board[9]} |\n')
	


def players_turn(board, symbol, text):
	while True:
		try:
			number = int(input(f"Player {symbol}'s turn: "))
			time.sleep(1)
		
			if board[number] == ' ':
				board[number] = symbol
				print(f'\033[1;33m{text} {number}\033[0m')
				show_board(board)
				break
			
			else: 
				print('\033[1;31mPosition already occupied, try another one!\033[0m')
				show_board(board)
				
		except (ValueError, KeyError):
			print('\033[1;31mOnly numbers between 1 and 9 are allowed.\033[0m')
			show_board(board)

			
									
def computers_turn(board):
	random_pos = random.randint(1, 9)
	while True:
		if board[random_pos] != ' ':
			random_pos = random.randint(1, 9)
		elif board[random_pos] == ' ':
			break
			
	print("Computer's turn: ")
	time.sleep(1)
	board[random_pos] = 'O'
	print(f'\033[1;33mComputer chose position {random_pos}\033[0m')
	show_board(board)
	


def win_condition(board, symbol):
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
	
	
	
def header(title):
	print('-' * 36)
	print(title)
	print('-' * 36)
	print('\033[1;33mChoose one of the numbers to make a move.\033[0m')
	print(f'| 1 | 2 | 3 |')
	print(f'| 4 | 5 | 6 |')
	print(f'| 7 | 8 | 9 |')
		


def player_vs_computer():
	board = {1:' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
	
	header('Welcome to player vs computer mode')
	
	while True:
		
		players_turn(board, 'X', 'You chose position')
		
		if win_condition(board, 'X'):
			print('\033[1;32mCongratulations, you won!\n(the computer is dumb!)\033[0m\n')
			break
		
		if ' ' not in board.values():
			print('\033[1;29mThe game ended in a draw :/ \033[0m\n')
			break
		
		computers_turn(board)
			
		if win_condition(board, 'O'):
			print('\033[1;31mComputer won!\033[0m\n')
			break



def player_vs_player():
	board = {1:' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
	
	header('Welcome to player vs player mode')
	
	while True:
		players_turn(board, 'X', 'Player X chose position')
		
		if win_condition(board, 'X'):
			print('\033[1;32mCongratulations player X, you won!\033[0m\n')
			break
		
		if ' ' not in board.values():
			print('\033[1;29mThe game ended in a draw :/ \033[0m\n')
			break
			
		players_turn(board, 'O', 'Player O chose position')
		
		if win_condition(board, 'O'):
			print('\033[1;32mCongratulations player O, you won!\033[0m\n')
			break
			
			
			
def main():
	while True:
		print('[1] - Player vs player.\n[2] - Play against computer.\n[3] - Exit')
		
		choice = input('-: ')
		
		time.sleep(1)
		
		if choice == '1':
			player_vs_player()
			
		elif choice == '2':
			player_vs_computer()
			
		elif choice == '3':
			break
			
		else:
			print('\033[1;31mInvalid character!\033[0m')
	
	
	
if __name__ == '__main__':
	main()