import copy

start_state = [ ['GA', 'MA', 'GF', 'MF', 'GG', 'MG', 'E'],
                ['GB', 'GC', 'GD', 'GE'],
                ['MB', 'MC', 'MD', 'ME'],
                [],
                0 ]
"""
start_state = [ ['MA', 'MB', 'E'],
                ['GA'],
                ['GB'],
                [],
                0 ]
dup_state =   [ ['MB', 'MA', 'E'],
                ['GA'],
                ['GB'],
                [],
                2 ]
"""


state_queue = []
state_queue.append(start_state)
total_items = len(start_state[0]) + len(start_state[1]) + len(start_state[2]) + len(start_state[3])
# V2: format of hash is now elevator_floor, followed by num_pairs, num_gen, num_microchips for each floor
# therefore, hash of start state should be: 0100040004000

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
    return (len(state[3]) == total_items)

def print_state(state):
    print(state)

def hash_state(state):
    toReturn = ''
    for i in range(4):
        if state[i] and state[i][-1] == 'E':
            toReturn += str(i)
            break
    for i in range(4):
        num_pairs = 0
        num_gen = 0
        num_mic = 0
        floor_copy = copy.deepcopy(state[i])
        while floor_copy:
            if floor_copy[0][0] == 'M':
                if 'G{}'.format(floor_copy[0][1]) in floor_copy:
                    num_pairs += 1
                    floor_copy.remove('G'+floor_copy[0][1])
                else:
                    num_mic += 1
                floor_copy.remove(floor_copy[0])
            elif floor_copy[0][0] == 'G':
                if 'M{}'.format(floor_copy[0][1]) in floor_copy:
                    num_pairs += 1
                    floor_copy.remove('M'+floor_copy[0][1])
                else:
                    num_gen += 1
                floor_copy.remove(floor_copy[0])
            else:
                floor_copy.pop(0)
        toReturn += str(num_pairs)
        toReturn += str(num_gen)
        toReturn += str(num_mic)
    return int(toReturn)


# gonna try a BFS while remembering visited states.
# visited states currently don't keep track of equivalent permutations 
# therefore ['GA', 'MA'] is seen as different from ['MA', 'GA']
# fixing this would drastically cut down on total states
# took a nice month-long break from this problem but I think I got it now.
# Prof. Moshkovitz this one's for you

#pdb.set_trace()
visited_state_hash = {hash_state(start_state): 1}

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
            if is_valid_state(new_state) and hash_state(new_state) not in visited_state_hash:
                if is_end_state(new_state):
                    print(new_state)
                    print(steps)
                    exit()
                state_queue.append(new_state)
                visited_state_hash[hash_state(new_state)] = 1

        # just this item up a floor
        if elevator_floor < 3:
            new_state = copy.deepcopy(current_state)
            new_state[-1] = steps
            new_state[elevator_floor+1].append(new_state[elevator_floor].pop(i))
            new_state[elevator_floor+1].append(new_state[elevator_floor].pop())
            if is_valid_state(new_state) and hash_state(new_state) not in visited_state_hash:
                if is_end_state(new_state):
                    print(new_state)
                    print(steps)
                    exit()
                state_queue.append(new_state)
                visited_state_hash[hash_state(new_state)] = 1


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
                    if is_valid_state(new_state) and hash_state(new_state) not in visited_state_hash:
                        if is_end_state(new_state):
                            print(new_state)
                            print(steps)
                            exit()
                        state_queue.append(new_state)
                        visited_state_hash[hash_state(new_state)] = 1

                # move up a floor
                if elevator_floor < 3:
                    new_state = copy.deepcopy(current_state)
                    new_state[-1] = steps
                    new_state[elevator_floor+1].append(current_state[elevator_floor][i])
                    new_state[elevator_floor].remove(current_state[elevator_floor][i])
                    new_state[elevator_floor+1].append(current_state[elevator_floor][j])
                    new_state[elevator_floor].remove(current_state[elevator_floor][j])
                    new_state[elevator_floor+1].append(new_state[elevator_floor].pop())
                    if is_valid_state(new_state) and hash_state(new_state) not in visited_state_hash:
                        if is_end_state(new_state):
                            print(new_state)
                            print(steps)
                            exit()
                        state_queue.append(new_state)
                        visited_state_hash[hash_state(new_state)] = 1

print(state_queue)
