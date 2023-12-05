import sys

def Column(arr, col):
	st = set()
	for i in range(0, 9):
		if arr[i][col] in st:
			return False
		if arr[i][col] != '.':
			st.add(arr[i][col])
	return True
def Row(arr, row):
	st = set()
	for i in range(0, 9):
		if arr[row][i] in st:
			return False
		if arr[row][i] != '.':
			st.add(arr[row][i])
	return True
def Box(arr, startRow, startCol):
	st = set()
	for row in range(0, 3):
		for col in range(0, 3):
			curr = arr[row + startRow][col + startCol]
			if curr in st:
				return False
			if curr != '.':
				st.add(curr)
	return True
def Valid(arr, row, col):
	return (Row(arr, row) and Column(arr, col) and
			Box(arr, row - row % 3, col - col % 3))
def Check(arr, n):
	for i in range(0, n):
		for j in range(0, n):
			if not Valid(arr, i, j):
				return False
	return True
if __name__ == "__main__":
	board = []
	with open('Python-lab12 correct.txt','r') as file:
    	 for line in file:
        	 board.append(list(map(int,line.strip())))

	if Check(board, 9):
		print("YES")
	else:
		print("NO")
