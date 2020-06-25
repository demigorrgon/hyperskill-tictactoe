cells = []
for item in range(9):
	cells.append(' ')

col_amount = 3  # columns of matrix
matrix = [cells[item:item + col_amount] for item in range(0, len(cells), col_amount)]
lines_horizontal = '-'*9

# final_matrix = [list(matrix[0]), list(matrix[1]), list(matrix[2])]
final_matrix = [[cells[6], cells[3], cells[0]], [cells[7], cells[4], cells[1]], [cells[8], cells[5], cells[2]]]


def battlefield():
	print(lines_horizontal)
	print(f"| {final_matrix[0][2]} {final_matrix[1][2]} {final_matrix[2][2]} |")
	print(f"| {final_matrix[0][1]} {final_matrix[1][1]} {final_matrix[2][1]} |")
	print(f"| {final_matrix[0][0]} {final_matrix[1][0]} {final_matrix[2][0]} |")
	print(lines_horizontal)


def victory_check(field):
	print(field)
	finding_blank = [symbol for array in field for symbol in array]  # to check if draw

	# vertical verification
	if all([cell if cell == 'X' else False for cell in field[0]]) \
		or all([cell if cell == 'O' else False for cell in field[0]]):
		print(f'{field[0][0]} wins')
		return True
	if all([cell if cell == 'X' else False for cell in field[1]]) \
		or all([cell if cell == 'O' else False for cell in field[1]]):
		print(f'{field[1][0]} wins')
		return True
	if all([cell if cell == 'X' else False for cell in field[2]]) \
		or all([cell if cell == 'O' else False for cell in field[2]]):
		print(f'{field[2][0]} wins')
		return True

	# horizontal verification
	transposed_field = list(zip(*field))
	print(transposed_field)
	if all([cell if cell == 'X' else False for cell in transposed_field[0]]) \
		or all([cell if cell == 'O' else False for cell in transposed_field[0]]):
		print(f'{transposed_field[0][0]} wins')
		return True
	if all([cell if cell == 'X' else False for cell in transposed_field[1]]) \
		or all([cell if cell == 'O' else False for cell in transposed_field[1]]):
		print(f'{transposed_field[1][0]} wins')
		return True
	if all([cell if cell == 'X' else False for cell in transposed_field[2]]) \
		or all([cell if cell == 'O' else False for cell in transposed_field[2]]):
		print(f'{transposed_field[2][0]} wins')
		return True

	if field[0][0] == field[1][1] == field[2][2] and field[0][0] != ' ':
		print(f'{field[0][0]} wins')
		return True
	if field[0][2] == field[1][1] == field[2][0] and field[0][2] != ' ':
		print(f'{field[0][2]} wins')
		return True

	elif ' ' not in finding_blank:
		print('Draw')
		return True
	else:
		return False


battlefield()
turns = 1
while True:
	user_input = input("Enter the coordinates: ").split()
	if user_input[0].isdecimal() and user_input[1].isdecimal():
		if int(user_input[0]) > 3 or int(user_input[1]) > 3:
			print("Coordinates should be from 1 to 3!")
		elif final_matrix[int(user_input[0]) - 1][int(user_input[1]) - 1] in ("X", "O"):
			print("This cell is occupied! Choose another one!")
		else:
			if (turns % 2) != 0:
				if turns >= 5:
					if victory_check(final_matrix):
						break
					else:
						final_matrix[int(user_input[0]) - 1][int(user_input[1]) - 1] = "X"
						turns += 1
						battlefield()
						if victory_check(final_matrix):
							break
						continue
				final_matrix[int(user_input[0]) - 1][int(user_input[1]) - 1] = "X"
				turns += 1
				battlefield()
				continue

			elif (turns % 2) == 0:
				if turns >= 5:
					battlefield()
					if victory_check(final_matrix):
						break
					else:
						final_matrix[int(user_input[0]) - 1][int(user_input[1]) - 1] = "O"
						turns += 1
						battlefield()
						if victory_check(final_matrix):
							break
						continue
				final_matrix[int(user_input[0]) - 1][int(user_input[1]) - 1] = "O"
				turns += 1
				battlefield()
				continue

	else:
		print("You should enter numbers!")
