IR_OE =     0b00000000000000000000000000000001
IR_WE =     0b00000000000000000000000000000010  
PC_LODE =   0b00000000000000000000000000000100
PC_WE =     0b00000000000000000000000000001000
PC_OE =     0b00000000000000000000000000010000
AR_WE =     0b00000000000000000000000000100000
AR_OE =     0b00000000000000000000000001000000
INV_A =     0b00000000000000000000000010000000
INV_B =     0b00000000000000000000000100000000
CIN   =     0b00000000000000000000001000000000
SUM   =     0b00000000000000000000010000000000
AND   =     0b00000000000000000000100000000000
OR     =    0b00000000000000000001000000000000
FLG_WE =    0b00000000000000000010000000000000 
FLG_OE =    0b00000000000000000100000000000000
ER_WE =     0b00000000000000001000000000000000
ER_OE =     0b00000000000000010000000000000000
BR_WE =     0b00000000000000100000000000000000
BR_OE =     0b00000000000001000000000000000000
RAM_OE =    0b00000000000010000000000000000000
RAM_WE =    0b00000000000100000000000000000000
MAR_WE =    0b00000000001000000000000000000000
MAR_OE =    0b00000000010000000000000000000000
OUT_WE =    0b00000000100000000000000000000000
MAR_OB =    0b00000001000000000000000000000000

OPR_WE =    0b01000000000000000000000000000000
HLOP =      0b10000000000000000000000000000000


def hxfmt(num):
    b = str(hex(num))
    b = b[2:]
    return b


LDA = [ 
    PC_OE|MAR_WE,
    MAR_OE,
    IR_WE|RAM_OE,
    MAR_WE|OPR_WE|IR_OE|PC_WE,

    MAR_OE,
    RAM_OE|AR_WE,
    0,
    0
]

LDB = [ 
    PC_OE|MAR_WE,
    MAR_OE,
    IR_WE|RAM_OE,
    MAR_WE|OPR_WE|IR_OE|PC_WE,

    MAR_OE,
    RAM_OE|BR_WE,
    0,
    0
]

STA = [ 
    PC_OE|MAR_WE,
    MAR_OE,
    IR_WE|RAM_OE,
    MAR_WE|OPR_WE|IR_OE|PC_WE,
    
    MAR_OE,
    RAM_WE|AR_OE|MAR_OE,
    0,
    0
    ]

STB = [ 
    PC_OE|MAR_WE,
    MAR_OE,
    IR_WE|RAM_OE,
    MAR_WE|OPR_WE|IR_OE|PC_WE|MAR_OE,
    
    MAR_OE,
    RAM_WE|AR_OE,
    0,
    0
    ]

ADD = [ 
    PC_OE|MAR_WE,
    MAR_OE,
    IR_WE|RAM_OE,
    MAR_WE|OPR_WE|IR_OE|PC_WE,

    SUM|ER_WE|FLG_WE|FLG_WE,
    ER_OE|AR_WE,
    0,
    0
]

SUB = [ 
    PC_OE|MAR_WE,
    MAR_OE,
    IR_WE|RAM_OE,
    MAR_WE|OPR_WE|IR_OE|PC_WE,

    CIN|INV_B|SUM|ER_WE|FLG_WE,
    ER_OE|AR_WE,
    0,
    0
]

JMP = [ 
    PC_OE|MAR_WE,
    MAR_OE,
    IR_WE|RAM_OE,
    MAR_WE|OPR_WE|IR_OE|PC_WE,

    PC_LODE|IR_OE|PC_WE,
    0,
    0,
    0
]

#V = 0
#Z = 1
JZ = [ 
    PC_OE|MAR_WE,
    MAR_OE,
    IR_WE|RAM_OE,
    MAR_WE|OPR_WE|IR_OE|PC_WE,

    PC_LODE|IR_OE|PC_WE,
    0,
    0,
    0
]

OUT = [ 
    PC_OE|MAR_WE,
    MAR_OE,
    IR_WE|RAM_OE,
    MAR_WE|OPR_WE|IR_OE|PC_WE,

    MAR_OE,
    RAM_OE|OUT_WE,
    0,
    0
]
AND = [ 
    PC_OE|MAR_WE,
    MAR_OE,
    IR_WE|RAM_OE,
    MAR_WE|OPR_WE|IR_OE|PC_WE,

    AND|ER_WE|FLG_WE,
    ER_OE|AR_WE,
    0,
    0
]

OR = [ 
    PC_OE|MAR_WE,
    MAR_OE,
    IR_WE|RAM_OE,
    MAR_WE|OPR_WE|IR_OE|PC_WE,

    OR|ER_WE|FLG_WE,
    ER_OE|AR_WE,
    0,
    0
]

LDAL = [
    PC_OE|MAR_WE,
    MAR_OE,
    IR_WE|RAM_OE,
    MAR_WE|OPR_WE|IR_OE|PC_WE,

    MAR_OB|AR_WE,
    0,
    0,
    0
]

LDBL = [
    PC_OE|MAR_WE,
    MAR_OE,
    IR_WE|RAM_OE,
    MAR_WE|OPR_WE|IR_OE|PC_WE,

    MAR_OB|BR_WE,
    0,
    0,
    0
]

NOP = OR = [ 
    PC_OE|MAR_WE,
    MAR_OE,
    IR_WE|RAM_OE,
    MAR_WE|OPR_WE|IR_OE|PC_WE,

    0,
    0,
    0,
    0
]

JV  = [ 
    PC_OE|MAR_WE,
    MAR_OE,
    IR_WE|RAM_OE,
    MAR_WE|OPR_WE|IR_OE|PC_WE,

    PC_LODE|IR_OE|PC_WE,
    0,
    0,
    0
]

HLT = [HLOP, HLOP, HLOP, HLOP, HLOP, HLOP, HLOP ,HLOP]

def line(opCode):
    ret = ""
    for ele in opCode:
         ret = ret + hxfmt(ele) + " "

    return ret

file = open("ROM\ROM.HEX", "w")
file.writelines([    "v2.0 raw\r",
                     line(LDA)  + "\n",
                     line(LDB)  + "\n",
                     line(STA)  + "\n",
                     line(STB)  + "\n",
                     line(ADD)  + "\n",
                     line(SUB)  + "\n",
                     line(JMP)  + "\n",
                     line(NOP)  + "\n",
                     line(OUT)  + "\n",
                     line(AND)  + "\n",
                     line(OR)   + "\n",
                     line(LDAL) + "\n",
                     line(LDBL) + "\n",
                     line(NOP)  + "\n",
                     line(NOP)  + "\n",
                     line(HLT)  + "\n",
                     
                     line(LDA)  + "\n",
                     line(LDB)  + "\n",
                     line(STA)  + "\n",
                     line(STB)  + "\n",
                     line(ADD)  + "\n",
                     line(SUB)  + "\n",
                     line(JMP)  + "\n",
                     line(NOP)  + "\n",
                     line(OUT)  + "\n",
                     line(AND)  + "\n",
                     line(OR)   + "\n",
                     line(LDAL) + "\n",
                     line(LDBL) + "\n",
                     line(NOP)  + "\n",
                     line(JV)  + "\n",
                     line(HLT)  + "\n",
                     
                     line(LDA)  + "\n",
                     line(LDB)  + "\n",
                     line(STA)  + "\n",
                     line(STB)  + "\n",
                     line(ADD)  + "\n",
                     line(SUB)  + "\n",
                     line(JMP)  + "\n",
                     line(JZ)  + "\n",
                     line(OUT)  + "\n",
                     line(AND)  + "\n",
                     line(OR)   + "\n",
                     line(LDAL) + "\n",
                     line(LDBL) + "\n",
                     line(NOP)  + "\n",
                     line(NOP)  + "\n",
                     line(HLT)  + "\n",
                     
                     line(LDA)  + "\n",
                     line(LDB)  + "\n",
                     line(STA)  + "\n",
                     line(STB)  + "\n",
                     line(ADD)  + "\n",
                     line(SUB)  + "\n",
                     line(JMP)  + "\n",
                     line(JZ)  + "\n",
                     line(OUT)  + "\n",
                     line(AND)  + "\n",
                     line(OR)   + "\n",
                     line(LDAL) + "\n",
                     line(LDBL) + "\n",
                     line(NOP)  + "\n",
                     line(JV)  + "\n",
                     line(HLT)  + "\n",
                     ])

file.close()


