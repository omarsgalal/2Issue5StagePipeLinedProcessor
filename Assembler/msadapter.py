'''
This file is for adapting the assembly code generated from assembler to be loaded into the model sim RAM
'''

class MSAdapter:
    def __init__(self):
        pass

    def adaptToFile(self, code, outFileName):
        adapted = ""
        adapted += '''// memory data file (do not edit the following line - required for mem load use)
// instance=/tb_filereg/Fr/Ram/ram
// format=mti addressradix=d dataradix=b version=1.0 wordsperline=1
'''
        code = str(code)
        codeLines = code.splitlines(keepends=True)
        counter = 0
        for line in codeLines:
            orgAddress = self.orgAddress(line)
            if (orgAddress != None):
                counter = orgAddress
                continue
            adapted += f"{counter}: {line}"
            counter += 1
        outFile = open(f'{outFileName}.mem', 'w')
        outFile.write(adapted)
        return adapted        

    def orgAddress(self, instr):
        '''
            if the instrunction is ORG instrunction it should be like that ==> 'ORG100'
        '''
        markerSize = len(".ORG")
        if instr[:markerSize] == ".ORG":
            return int(instr[markerSize:], 16)