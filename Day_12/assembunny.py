input = """cpy 1 a
cpy 1 b
cpy 26 d
jnz c 2
jnz 1 5
cpy 7 c
inc d
dec c
jnz c -2
cpy a c
inc a
dec b
jnz b -2
cpy c b
dec d
jnz d -6
cpy 13 c
cpy 14 d
inc a
dec d
jnz d -2
dec c
jnz c -5"""

"""input = cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a"""

inst_list = input.splitlines()
pc = 0
reg = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
while(pc < len(inst_list)):
    inst = inst_list[pc].split()
    if inst[0] == 'cpy':
        if inst[1] in reg:
            reg[inst[2]] = reg[inst[1]]
        else:
            reg[inst[2]] = int(inst[1])
        pc += 1
    elif inst[0] == 'inc':
        reg[inst[1]] += 1
        pc += 1
    elif inst[0] == 'dec':
        reg[inst[1]] -= 1
        pc += 1 
    elif inst[0] == 'jnz':
        if inst[1] in reg:
            if reg[inst[1]] != 0:
                pc += int(inst[2])
            else:
                pc += 1
        else:
            if inst[1] != '0':
                pc += int(inst[2])
            else:
                pc += 1
    else:
        print('Not an instruction: {}'.format(inst))

print(reg)
