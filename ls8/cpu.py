"""CPU functionality."""

import sys

LDI = 0b10000010
PRN = 0b01000111
HLT = 0b00000001
MUL = 0b10100010

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.reg = [0] * 8
        self.pc = 0
        self.ram = [0] * 256
        self.running = True
        self.dispatch = {
            HLT: self.dis_hlt,
            LDI: self.dis_ldi,
            MUL: self.dis_mul,
            PRN: self.dis_prn,
        }

    def ram_read(self, MAR):
        return self.ram[MAR]

    def ram_write(self, MAR, MDR):
        self.ram[MAR] = MDR

    def load(self, program):
        """Load a program into memory."""

        address = 0

        with open(program) as f:
            for line in f:
                # what_is = line.split("#") # a list of items on that line
                # what_is_this = line.split("#")[0] # the first item of each line, lots of them blank spaces
                what_is_that = line.split("#")[0].strip() # first item, with first and last of chars removed!
                if what_is_that == '':
                    continue
                v = int(what_is_that, 2)
                self.ram_write(address, v)
                self.ram_read(address)
                address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op == "MUL":
            self.reg[reg_a] = (self.reg[reg_a] * self.reg[reg_b])
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        while self.running:
            reg_a = self.ram_read(self.pc + 1)
            reg_b = self.ram_read(self.pc + 2)

            ir = self.ram[self.pc]

            try:
                command = self.dispatch[ir](reg_a, reg_b)

                self.running = command[0]
                self.pc += command[1]
                ir = self.ram[self.pc]
            except:
                print(f'Failure to parse command')
                sys.exit(1)

### DISPATCH FUNCTIONS
    def dis_ldi(self, reg_a, reg_b):
        self.reg[reg_a] = reg_b
        return (True, 3)
    def dis_hlt(self, reg_a, reg_b):
        self.running = False
        return (False, 0)
    def dis_prn(self, reg_a, reg_b):
        print(self.reg[reg_a])
        return (True, 2)
    def dis_mul(self, reg_a, reg_b):
        self.alu('MUL', reg_a, reg_b)
        return (True, 3)

        


### LEGACY CODE
## DAY ONE

# Hash tables corresponding to address
        # item = {key is the address in memory and the value is the 'HLT'}
        # commands = {
        # 'hlt' = hlt
        # }
        # IR = self.pc
        # # setting memory to 0
        # for i in self.memory:
        #     self.memory[i] = 0
        # # setting registers to 0 and R7 to 0xF4
        # for i in self.registers:
        #     if i != 7:
        #         self.registers[i] = 0
        #     else:
        #         self.registers[i] = 0xF4
        # while IR not 'HLT':
        #     self.ram_read(self.pc)
        #     if self.registers[IR] == 'LDI':
        #        # run code
        #         pc += 1
        #     if self.registers[IR] == 'ADD':
        #         self.memory[IR+1] + self.memory[IR+2]
        #         pc += 1
             
        # while command is not HLT:
    # def load(self, program):
    #     """Load a program into memory."""

    #     address = 0

    #     # For now, we've just hardcoded a program:

    #     program = [
    #         # From print8.ls8
    #         LDI,
    #         0,
    #         8,
    #         PRN,
    #         0,
    #         HLT
    #         # 0b10000010, # LDI R0,8
    #         # 0b00000000,
    #         # 0b00001000,
    #         # 0b01000111, # PRN R0
    #         # 0b00000000,
    #         # 0b00000001, # HLT
    #     ]

    #     for instruction in program:
    #         self.ram_write(address, instruction)
    #         address += 1
    #     # print(self.ram)
    #     # for item in self.ram:
    #     #     if item == LDI:
    #     #         print('ldi')
    #     #         print(self.ram[0])
    #     #     elif item == PRN:
    #     #         print('prn')
    #     #         print(self.ram[3])
    #     #     elif item == HLT:
    #     #         print('hlt')
    #     #         print(self.ram[5])
    #     #     else:
    #     #         pass
        # def run(self):
        # """Run the CPU."""
        # global HLT
        # global PRN
        # global LDI

        # ir = self.ram[self.pc]
        # while self.running:
        #     if ir == LDI:
        #         regu = self.ram_read(self.pc + 1)
        #         num = self.ram_read(self.pc + 2)
        #         self.reg[regu] = num
        #         self.pc += 3
        #         ir = self.ram[self.pc]
        #     if ir == PRN:
        #         regu = self.ram[self.pc + 1]
        #         print(self.reg[regu])
        #         self.pc += 2
        #         ir = self.ram[self.pc]
        #     if ir == HLT:
        #         self.running = False
        # Hash tables corresponding to address
        # item = {key is the address in memory and the value is the 'HLT'}
        # commands = {
        # 'hlt' = hlt
        # }
        # IR = self.pc
        # # setting memory to 0
        # for i in self.memory:
        #     self.memory[i] = 0
        # # setting registers to 0 and R7 to 0xF4
        # for i in self.registers:
        #     if i != 7:
        #         self.registers[i] = 0
        #     else:
        #         self.registers[i] = 0xF4
        # while IR not 'HLT':
        #     self.ram_read(self.pc)
        #     if self.registers[IR] == 'LDI':
        #        # run code
        #         pc += 1
        #     if self.registers[IR] == 'ADD':
        #         self.memory[IR+1] + self.memory[IR+2]
        #         pc += 1
             
        # while command is not HLT:

