"""CPU functionality."""

import sys

LDI = 0b10000010
PRN = 0b01000111
HLT = 0b00000001

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.reg = [0] * 8
        self.pc = 0
        self.ram = [0] * 256
        self.running = True

    def ram_read(self, MAR):
        # Need to turn MAR into decimal
        return self.ram[MAR] 

    def ram_write(self, MAR, MDR):
        self.ram[MAR] = MDR

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            LDI,
            0,
            8,
            PRN,
            0,
            HLT
            # 0b10000010, # LDI R0,8
            # 0b00000000,
            # 0b00001000,
            # 0b01000111, # PRN R0
            # 0b00000000,
            # 0b00000001, # HLT
        ]

        for instruction in program:
            self.ram_write(address, instruction)
            address += 1
        # print(self.ram)
        # for item in self.ram:
        #     if item == LDI:
        #         print('ldi')
        #         print(self.ram[0])
        #     elif item == PRN:
        #         print('prn')
        #         print(self.ram[3])
        #     elif item == HLT:
        #         print('hlt')
        #         print(self.ram[5])
        #     else:
        #         pass

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
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
        global HLT
        global PRN
        global LDI

        ir = self.ram[self.pc]
        while self.running:
            if ir == LDI:
                regu = self.ram_read(self.pc + 1)
                num = self.ram_read(self.pc + 2)
                self.reg[regu] = num
                self.pc += 3
                ir = self.ram[self.pc]
            if ir == PRN:
                regu = self.ram[self.pc + 1]
                print(self.reg[regu])
                self.pc += 2
                ir = self.ram[self.pc]
            if ir == HLT:
                self.running = False
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


