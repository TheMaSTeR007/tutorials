class Node:
    def __init__(self, loc, parent, cost):
        self.cost = cost
        self.parent = parent
        self.location = loc

class Bot:
    def __init__(self, map):
        self.map = map
        self.map_height = len(map)
        self.map_width = len(map[0])

    def left(self, current_loc):
        x = current_loc[0]
        y = current_loc[1]
        x_moved = current_loc[0]

        for i in range(x - 1, -1, -1):
            next_location = self.map[y][i]
            if next_location == "1":
                break
            x_moved = i

        if x == x_moved:
            raise IndexError
        return (x_moved, y)

    def right(self, current_loc):
        x = current_loc[0]
        y = current_loc[1]
        x_moved = current_loc[0]

        for i in range(x + 1, self.map_width):
            next_location = self.map[y][i]
            if next_location == "1":
                break
            x_moved = i

        if x == x_moved:
            raise IndexError
        return (x_moved, y)

    def up(self, current_loc):
        x = current_loc[0]
        y = current_loc[1]
        y_moved = current_loc[1]

        for i in range(y - 1, -1, -1):
            next_location = self.map[i][x]
            if next_location == "1":
                break
            y_moved = i

        if y == y_moved:
            raise IndexError
        return (x, y_moved)

    def down(self, current_loc):
        x = current_loc[0]
        y = current_loc[1]
        y_moved = current_loc[1]

        for i in range(y + 1, self.map_height):
            next_location = self.map[i][x]
            if next_location == "1":
                break
            y_moved = i

        if y == y_moved:
            raise IndexError
        return (x, y_moved)

def get_StartAndGoal(map):
    start = "R"
    goal = "D"
    start_loc = None
    goal_loc = None

    for indx, row in enumerate(map):
        if start_loc == None and start in row:
            start_loc = (row.find(start), indx)
        if goal_loc == None and goal in row:
            goal_loc = (row.find(goal), indx)
        if start_loc != None and goal_loc != None:
            break

    return start_loc, goal_loc

def funct_extractPlan(goal_node):
     current_node = goal_node
     temp_path = []

     while True:
         temp_path.append(current_node.location)
         current_node = current_node.parent
         if current_node is None:
            break

     result_path = [temp_path.pop() for i in range(len(temp_path))]
     return result_path, goal_node.cost

def successor_funct(current_node, robot):
    functions = [robot.up, robot.down, robot.left, robot.right]
    children = []

    for f in functions:
        try:
            moved_loc = f(current_node.location)
        except IndexError:
            continue

        child = Node(loc=moved_loc, parent=current_node, cost=current_node.cost + 1)
        children.append(child)
    return children

def dfs_main(map):
    start_loc, goal_loc = get_StartAndGoal(map)
    fringe = [Node(start_loc, None, 0)]

    while True:
        
        if not fringe:
            "Failure in finding plan"
        
        current_node = fringe.pop()
        
        if current_node.location == goal_loc:
            return funct_extractPlan(current_node)
        else:
            fringe += successor_funct(current_node, Bot(map))


def play_game():
  sample_maze_map = [
    "111111111",
    "1D00R0001",
    "100000011",
    "100000001",
    "100001001",
    "111001001",
    "111001111",
    "110000001",
    "111111111",
  ]
  result = dfs_main(sample_maze_map)
  if isinstance(result, tuple):
    final_res = []
    x = 0
    y = 0
    plan =result[0]
    for i in range(len(plan)):
      if plan[i][0]<x and plan[i][1]==y:
        final_res.append("Left")
      elif plan[i][0]>x and plan[i][1]==y:
        final_res.append("Right")
      elif plan[i][1]<y and plan[i][0]==x:
        final_res.append("Up")
      elif plan[i][1]>y and plan[i][0]==x:
        final_res.append("Down")
      
      x = plan[i][0]
      y = plan[i][1]

    print("Cost ", result[1])
    print("Plan ", result[0])
      
    return '->'.join(final_res)
 

play_game()
