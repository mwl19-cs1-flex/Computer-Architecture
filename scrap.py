import sys
# PRINT_MACK = 1
# HALT = 2
# SAVE_REG = 3 # save a value in a register
# PRINT_REG = 4 

# memory = [
#     PRINT_MACK, 
#     PRINT_MACK,
#     SAVE_REG, # SAVE_REG R0, 12. How do we do this?
#     0,
#     37, 
#     PRINT_REG,
#     0,
#     PRINT_MACK,
#     HALT 
# ]

# registers = [0,0,0,0,0,0,0,0] # named r0-r7

# halted = False

# pc = 0 # "Program Counter": Index into the memory array AKA a pointer, address, location

# while not halted:
#     instruction = memory[pc]

#     if instruction == PRINT_MACK:
#         print("Mack!")
#         pc += 1

#     elif instruction == SAVE_REG:
#         reg_num = memory[pc + 1]
#         value = memory[pc + 2]
#         registers[reg_num] = value 
#         pc += 3
#     elif instruction == PRINT_REG:
#         reg_num = memory[pc + 1]
#         print(registers[reg_num])
#         pc += 2
#     elif instruction == HALT:
#         halted = True
#     else:
#         print(f'Unknown instruction: {instruction} at address {pc}')
#         sys.exit(1)


# test_integer = {
#   "cat": "bob",
#   "dog": 23,
#   19: 18,
#   90: "fish"
# }

# def hashsum_function(tablehash):
#     total_sum = 0
#     for i in tablehash:
#         if type(tablehash[i]) == int:
#             total_sum += tablehash[i]
    
#     return total_sum

# print(hashsum_function(test_integer))

# PRINT_MACK = 1
# HALT = 2
# PRINT_NUM = 3
# SAVE = 4
# PRINT_REG = 5
# ADD = 6

# memory = [
#     PRINT_MACK,
#     SAVE,
#     65,
#     2,
#     SAVE,
#     20,
#     3,
#     ADD,
#     2,
#     3,
#     PRINT_REG,
#     2,
#     HALT,
# ]

# register = [0] * 8

# pc = 0
# running = True

# while running:
#     command = memory[pc]

#     if command == PRINT_MACK:
#         print("Mack!")
#         pc += 1
#     elif command == HALT:
#         print("Done!")
#         running = False
#     elif command == PRINT_NUM:
#         num = memory[pc+1]
#         print(num)
#         pc += 2
#     elif command == SAVE:
#         num = memory[pc+1]
#         reg = memory[pc+2]
#         register[reg] = num
#         pc += 3
    
#     elif command == PRINT_REG:
#         reg = memory[pc + 1]
#         print(register[reg])
#         pc += 2
    
#     elif command == ADD: 
#         reg_a = memory[pc+1]
#         reg_b = memory[pc+2]
#         register[reg_a] += register[reg_b]
#         pc += 3
#     else:
#         print(f"Unknown instruction: {command}")
#         sys.exit(1)
    
# print(register)