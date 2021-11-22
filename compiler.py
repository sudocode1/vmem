f = open('idx.is', 'r')
file = f.read()
f.close()

MEMORY = [] # 0-7
ERRORS = ['MEMORY_OVERLOAD', 'UNKNOWN_EXPRESSION', 'BIT_NOT_INITIALIZED', 'NO_BIT_SELECTED', 'BIT_ALREADY_INITIALIZED']
SELECTED = None
DEBUG = False

for line in file.split('\n'):
    splitter = line.split(' ')

    # error checking
    #print(len(MEMORY))
    if len(MEMORY) > 8:
        print(ERRORS[0] + ' WITH ' + str(MEMORY))
        break


    if line == 'CREATE BIT':
        # CREATE BIT
        MEMORY.append(None)
    elif line == 'CREATE BYTE':
        for x in range(8):
            MEMORY.append(None)
    elif line.startswith('SELECT'):
        if MEMORY[int(splitter[1])] == None:
            print(ERRORS[2] + ' WITH ' + str(MEMORY))
        SELECTED = int(splitter[1])

        if DEBUG:
            print(f"SELECTED BIT {SELECTED}")
    elif line.startswith('READ'):
        if splitter[1] == 'BIT':
            print(MEMORY[SELECTED])
        elif splitter[1] == 'BYTE':
            print(MEMORY)
    elif line.startswith('INIT'):
        MEMORY[int(splitter[1])] = 0
    elif line.startswith('SET'):
        if (SELECTED == None):
            print(ERRORS[3] + ' WITH ' + str(MEMORY))
            break
        MEMORY[SELECTED] = int(splitter[1])
        if DEBUG:
            print(f"SET BIT {SELECTED} to {splitter[1]}")
    elif line.startswith('RELEASE'):
        PREV = SELECTED
        MEMORY[SELECTED] = None
        SELECTED = None

        if DEBUG:
            print(f"RELEASED BIT {PREV}")
    elif line.startswith('CALCULATION'):
        if (SELECTED == None):
            print(ERRORS[3] + ' WITH ' + str(MEMORY))
            break
        # CALCULATION <CALC> <BIT> <BIT>
        if splitter[1] == 'ADD':
            MEMORY[SELECTED] = MEMORY[int(splitter[2])] + MEMORY[int(splitter[3])]
        elif splitter[1] == 'SUBTRACT':
            MEMORY[SELECTED] = MEMORY[int(splitter[2])] - MEMORY[int(splitter[3])]
        elif splitter[1] == 'MULTIPLY':
            MEMORY[SELECTED] = MEMORY[int(splitter[2])] * MEMORY[int(splitter[3])]
        elif splitter[1] == 'DIVIDE':
            MEMORY[SELECTED] = MEMORY[int(splitter[2])] / MEMORY[int(splitter[3])]
    elif line.startswith('COPY'):
        if (SELECTED == None):
            print(ERRORS[3] + ' WITH ' + str(MEMORY))
            break
        # copy value into another bit
        # COPY <BIT>

        if (MEMORY[int(splitter[1])] == None):
            MEMORY[int(splitter[1])] = MEMORY[SELECTED]
        else:
            print(ERRORS[4] + ' WITH ' + str(MEMORY))
            break

        if DEBUG:
            print(f"COPIED {SELECTED} INTO {splitter[1]}")
    elif line == 'DEBUG':
        if DEBUG:
            DEBUG = False
        else:
            DEBUG = True
    elif line.startswith('DESTROY'):
        if splitter[1] == 'MEMORY':
            SELECTED = None
            MEMORY = []
    elif line == 'INCREMENT':
        MEMORY[SELECTED] = MEMORY[SELECTED] + 1
    elif line == 'DECREMENT':
        MEMORY[SELECTED] = MEMORY[SELECTED] - 1
        
            

 
    if len(MEMORY) > 8:
        print(ERRORS[0] + ' WITH ' + str(MEMORY))
        break
   


print(MEMORY)
