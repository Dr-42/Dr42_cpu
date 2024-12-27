ci = []

#for i in range(0,16):
#    y = input(str(i)+" >>")
#   ci.append(y)
name = input("Enter file name : ")

def asmToMach(argument):
    commands = {
        "LDA"   :  "0",
        "LDB"   :  "1",
        "STA"   :  "2",
        "STB"   :  "3",
        "ADD"   :  "4",
        "SUB"   :  "5",
        "JMP"   :  "6",
        "JZ"   :  "7",
        "OUT"   :  "8",
        "AND"   :  "9",
        "OR "   :  "A",
        "LDAL"  :  "B",
        "LDBL"  :  "C",
        "NOP"   :  "D",
        "JV"   :  "E",
        "HLT"   :  "F",
        "0"     :  "0",
        "1"     :  "1",
        "2"     :  "2",
        "3"     :  "3",
        "4"     :  "4",
        "5"     :  "5",
        "6"     :  "6",
        "7"     :  "7",
        "8"     :  "8",
        "9"     :  "9",
        "10"     :  "A",
        "11"     :  "B",
        "12"     :  "C",
        "13"     :  "D",
        "14"     :  "E",
        "15"     :  "F"
    }

    return commands.get(argument, "0")



def funBod(codeInput):
    output = ""
    for e in codeInput:
        E = e.split()
        if len(E) == 2:
            m = hex(int(E[1]))
            m = m[2:]
            o = asmToMach(E[0]) + m + " "
        elif len(E) == 1:
            o = hex(int(E[0]))
            o = o[2:] + " "
        else:
            o = "0 "
        
        output += o
    

    return output
    
e = open("RAM/" + name, "r")
ci = e.readlines()
e.close()

f = open("RAM/RAM.HEX", "w")
f.writelines([    
                "v2.0 raw\r",
                funBod(ci)
            ])
f.close()
