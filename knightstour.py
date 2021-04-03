size = 5
start = [0,0]
tours = 0

def jump(node): # This generates the L shapes moves
	array = []
	if node[0] - 1 in range(0,size) and node[1] - 2 in range(0,size):
		array.append([node[0] - 1, node[1] - 2])
	if node[0] + 1 in range(0,size) and node[1] - 2 in range(0,size):
		array.append([node[0] + 1, node[1] - 2])
	if node[0] - 1 in range(0,size) and node[1] + 2 in range(0,size):
		array.append([node[0] - 1, node[1] + 2])
	if node[0] + 1 in range(0,size) and node[1] + 2 in range(0,size):
		array.append([node[0] + 1, node[1] + 2])
	if node[1] - 1 in range(0,size) and node[0] - 2 in range(0,size):
		array.append([node[0] - 2, node[1] - 1])
	if node[1] + 1 in range(0,size) and node[0] - 2 in range(0,size):
		array.append([node[0] - 2, node[1] + 1])
	if node[1] - 1 in range(0,size) and node[0] + 2 in range(0,size):
		array.append([node[0] + 2, node[1] - 1])
	if node[1] + 1 in range(0,size) and node[0] + 2 in range(0,size):
		array.append([node[0] + 2, node[1] + 1])
	return array

def dfs(path):
	for i in jump(path[-1]):
		if i not in path:
			dfs(path+[i])
	# if path[-1] == start and len(path) == size**2:
	if len(path) == size**2:
		print(path)
		global tours
		tours += 1

dfs([start])
print(f"There are {tours} in total")