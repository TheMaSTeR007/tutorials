# 1. Depth First Search

sample_maze_map = [
    "111111111",
    "100010001",
    "1000100R1",
    "100000001",
    "100001001",
    "111001001",
    "111001111",
    "1100000D1",
    "111111111",
  ]

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
            if next_location == "1" :
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
            if next_location == "1" :
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
            if next_location == "1" :
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
            if next_location == "1" :
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
            child = Node(loc=moved_loc, parent=current_node, cost=current_node.cost + 1)
            children.append(child)
        except IndexError:
            continue

    return children

def dfs_main(map):
    start_loc, goal_loc = get_StartAndGoal(map)
    fringe = [Node(start_loc, None, 0)]

    while True:
        
        if not fringe:
            "Failure in finding plan"
        
        current_node = fringe.pop(0)
        
        if current_node.location == goal_loc:
            return funct_extractPlan(current_node)
        else:
          temp_lst = successor_funct(current_node, Bot(map))
          if len(fringe) ==0:
            fringe = temp_lst
          else:
            temp_lst += fringe
            fringe = temp_lst


def play_game():
  
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

# 2. Iterative Depening Search

routes = []

def goal_test(current_loc, goal_loc):
    if current_loc == goal_loc:
        return True
    return False


def get_moved_loc(x, y):
    if (x, y) == (1, 0):
        direction = "Down"
    elif (x, y) == (-1, 0):
        direction = "Up"
    elif (x, y) == (0, -1):
        direction = "Left"
    else:
        direction = "Right"
    return direction


def neighbours(robot_map, present_point, visited, x, y):
    n, m = len(robot_map), len(robot_map[0])
    temp_x, temp_y = x, y
    visited_temp = visited.copy()
    visited_node = False
    while 0 <= temp_x + present_point[0] < n and 0 <= temp_y + present_point[1] < m:
        if (temp_x + present_point[0], temp_y + present_point[1]) in visited_temp:
            visited_node = True
            break
        if robot_map[temp_x + present_point[0]][temp_y + present_point[1]]:
            temp_x -= x
            temp_y -= y
            break
        visited_temp.add(
            (temp_x + present_point[0], temp_y + present_point[1]))
        temp_x += x
        temp_y += y
    return (temp_x, temp_y, visited_node, visited_temp)


def get_child_nodes(present_point, robot_map, visited, previousPath, x, y):
    path = []
    n, m = len(robot_map), len(robot_map[0])
    temp_x, temp_y, visited_node, visited_temp = neighbours(robot_map, present_point, visited, x, y)
    if 0 > temp_x + present_point[0] or temp_x + present_point[0] >= n or 0 > temp_y + present_point[1] or temp_y + present_point[1] >= m:
        temp_x -= x
        temp_y -= y
    if not visited_node and (temp_x + present_point[0], temp_y + present_point[1]) != present_point:
        robot_direction = get_moved_loc(x, y)
        path.append(((temp_x + present_point[0], temp_y + present_point[1]), visited_temp, previousPath + robot_direction))
        return path


def check_nodes(robot_map, source, destination):
    if robot_map[source[0]][source[1]]:
        return "Invalid Source, Please enter right input"
    if robot_map[destination[0]][destination[1]]:
        return "Out of bounds"
    return True


def resolve(fringe, map, end_point, curr_depth):
    try:
        neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        global routes

        if goal_test(fringe[-1][0], end_point):
            routes.append(fringe[-1][2])
            return routes[0]
        if curr_depth <= 0:
            return
        present_position, visited, path = fringe[-1]

        for x, y in neighbours:
            possible_path = get_child_nodes(
                present_position, map, visited, path, x, y)
            if len(possible_path):
                resolve(fringe + possible_path, map,
                      ending_point, curr_depth - 1)
    except Exception as ex:
        return ex


def get_plan(starting_point, ending_point):
    sample_maze_map = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 0, 0, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
    corner_nodes = check_nodes(sample_maze_map, starting_point, ending_point)
    if corner_nodes == False:
        print(corner_nodes)
        return
    depth = 0
    while True:
        fringe = [[starting_point, {starting_point}, ""]]
        resolve(fringe, sample_maze_map, ending_point, depth)
        if len(routes):
            result = routes[0]
            print("Shortest plan from starting point to goal state is ", result)
            print("Total cost to reach goal state ", len(result))
            return
        depth = depth + 1


starting_point = (2, 7)
ending_point = (7, 7)
get_plan(starting_point, ending_point)
