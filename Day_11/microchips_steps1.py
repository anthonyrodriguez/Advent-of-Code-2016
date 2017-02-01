from __future__ import print_function
import copy

start_state = [ ['GA', 'MA', 'E'],
                ['GB', 'GC', 'GD', 'GE'],
                ['MB', 'MC', 'MD', 'ME'],
                [],
                0 ]

state_queue = []
state_queue.append(start_state)

visited_state_hash = {str(start_state): 1}

def is_valid_state(state):
    for i in range(4):
        if not is_valid_floor(state[i]):
            return False
    return True

def is_valid_floor(floor):
    for item in floor:
        if item[0] == 'G':
            for item in floor:
                if item[0] == 'M':
                    if 'G{}'.format(item[1]) not in floor:
                        return False
            return True
    return True

def is_end_state(state):
    #TODO note that the length of state[3] is hardcoded (10 items plus elevator)
    return (len(state[3]) == 11)

def print_state(state):
    print(state, end='\r')


# gonna try a BFS while remembering visited states.
# visited states currently don't keep track of equivalent permutations 
# therefore ['GA', 'MA'] is seen as different from ['MA', 'GA']
# fixing this would drastically cut down on total states
# took a nice month-long break from this problem but I think I got it now.
# Prof. Moshkovitz this one's for you

# ensure viable vertices remain in the queue
while state_queue:
    current_state = state_queue.pop(0)
    steps = current_state[-1] + 1
    
    elevator_floor = -1
    # find elevator floor
    for floor_num in range(4):
        if 'E' in current_state[floor_num]:
            elevator_floor = floor_num
            break

    # for each item on the floor, can also bring 0 or 1 other item
    for i in range(len(current_state[elevator_floor]) - 1):
        # just this item down a floor
        if elevator_floor > 0:
            # Deep copy of current_state, will use this method throughout
            new_state = copy.deepcopy(current_state)
            new_state[-1] = steps
            new_state[elevator_floor-1].append(new_state[elevator_floor].pop(i))
            # move elevator
            new_state[elevator_floor-1].append(new_state[elevator_floor].pop())
            if is_valid_state(new_state) and str(new_state) not in visited_state_hash:
                if is_end_state(new_state):
                    print(new_state)
                    print(steps)
                    exit()
                print_state(new_state)
                state_queue.append(new_state)
                visited_state_hash[str(new_state)] = 1

        # just this item up a floor
        if elevator_floor < 3:
            new_state = copy.deepcopy(current_state)
            new_state[-1] = steps
            new_state[elevator_floor+1].append(new_state[elevator_floor].pop(i))
            new_state[elevator_floor+1].append(new_state[elevator_floor].pop())
            if is_valid_state(new_state) and str(new_state) not in visited_state_hash:
                if is_end_state(new_state):
                    print(new_state)
                    print(steps)
                    exit()
                print_state(new_state)
                state_queue.append(new_state)
                visited_state_hash[str(new_state)] = 1


        # this item plus following items
        if i < len(current_state[elevator_floor])-2:
            for j in range(i+1, len(current_state[elevator_floor])-1):
                # move down a floor
                if elevator_floor > 0:
                    new_state = copy.deepcopy(current_state)
                    new_state[-1] = steps
                    new_state[elevator_floor-1].append(current_state[elevator_floor][i])
                    new_state[elevator_floor].remove(current_state[elevator_floor][i])
                    new_state[elevator_floor-1].append(current_state[elevator_floor][j])
                    new_state[elevator_floor].remove(current_state[elevator_floor][j])
                    new_state[elevator_floor-1].append(new_state[elevator_floor].pop())
                    if is_valid_state(new_state) and str(new_state) not in visited_state_hash:
                        if is_end_state(new_state):
                            print(new_state)
                            print(steps)
                            exit()
                        print_state(new_state)
                        state_queue.append(new_state)
                        visited_state_hash[str(new_state)] = 1

                # move up a floor
                if elevator_floor < 3:
                    new_state = copy.deepcopy(current_state)
                    new_state[-1] = steps
                    new_state[elevator_floor+1].append(current_state[elevator_floor][i])
                    new_state[elevator_floor].remove(current_state[elevator_floor][i])
                    new_state[elevator_floor+1].append(current_state[elevator_floor][j])
                    new_state[elevator_floor].remove(current_state[elevator_floor][j])
                    new_state[elevator_floor+1].append(new_state[elevator_floor].pop())
                    if is_valid_state(new_state) and str(new_state) not in visited_state_hash:
                        if is_end_state(new_state):
                            print(new_state)
                            print(steps)
                            exit()
                        print_state(new_state)
                        state_queue.append(new_state)
                        visited_state_hash[str(new_state)] = 1

