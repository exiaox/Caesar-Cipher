import sys
import os
                
class CaesarCipher:
    
    key = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


    def __init__(self):
        self.EncryptedText = ''
        self.DecryptedText = ''
        self.NewEncrypted = ''
        self.NewDecrypted = ''
        self.ShiftAmount = ''
        self.filename = ''
        self.filename
        self.DecryptedPlaceholder = ''
        self.EncryptedPlaceholder = ''
        self.SaveEncryptedPlaceholder = ''
        self.SaveDecryptedPlaceholder = ''
        self.CharacterList = []
        self.LowerCharacterList = []
        self.NumberList = []
        self.LowerNumberList = []
        self.dictionary = ''
        self.max1 = ''
        self.max2 = ''
        self.max3 = ''
        self.ord1 = ''
        self.ord2 = ''
        self.ord3 = ''
        self.charcount = ''
        self.upperdict = {}
        self.lowerdict = {}
        self.alldict = {}
        self.EncryptedTextTemp = ''
        self.DecryptedTextTemp = ''
    
    def ClearAll(self):
        self.EncryptedText = ''
        self.DecryptedText = ''
        #takes no parameters, clears both decrypted and encrypted text

    def PrintEncrypted(self):
        print(self.EncryptedText)
        #takes no parameters, prints encrypted text

    def PrintDecrypted(self):
        print(self.DecryptedText)
        #takes no parameters, prints decrypted text

    def Encrypt(self, ShiftAmount):
        self.ShiftAmount = int(ShiftAmount)
        if self.DecryptedText == '':
            return False
        else:
            if (self.ShiftAmount < 1 or self.ShiftAmount > 61) or (self.ShiftAmount == 26 or self.ShiftAmount == 36):
                return False
            else:
                if self.NewEncrypted != '':
                    self.NewEncrypted = ''
                for character in self.DecryptedText:
                    if character.isalpha() or character.isdigit():
                        position = (self.ShiftAmount + self.key.index(character)) % len(self.key)
                        ShiftLetter = self.key[position]
                        self.NewEncrypted += ShiftLetter
                    else:
                        self.NewEncrypted += character
                if self.EncryptedText != self.NewEncrypted:
                    self.EncryptedText = self.NewEncrypted
                else:
                    self.EncryptedText = self.EncryptedText 
                return True
        #takes shift_amount parameter, encrypts text

    def Decrypt(self, ShiftAmount):
        self.ShiftAmount = int(ShiftAmount)
        if self.EncryptedText == '':
            return False
        else:
            if self.ShiftAmount < 1 or self.ShiftAmount > 61:
                return False
            else:
                if self.NewDecrypted != '':
                    self.NewDecrypted = ''
                for character in self.EncryptedText:
                    if character.isalpha() or character.isdigit():
                        position = (self.key.index(character) - self.ShiftAmount) % len(self.key)
                        ShiftLetter = self.key[position]
                        self.NewDecrypted += ShiftLetter
                    else:
                        self.NewDecrypted += character
                if self.DecryptedText != self.NewDecrypted:
                    self.DecryptedText = self.NewDecrypted
                else:
                    self.DecryptedText = self.DecryptedText
                return True
            #takes shift_amount parameter, decrypts text

    def LoadEncryptedFile(self, filename):
        self.filename = filename
        self.DecryptedText = ''
        if os.path.exists(self.filename):
            self.EncryptedPlaceholder = open(filename,'r+')
            self.EncryptedText = self.EncryptedPlaceholder.read()
            self.EncryptedPlaceholder.close()
            return True
        elif (not os.path.exists(self.filename)) or filename == '':
            return False


    def LoadDecryptedFile(self, filename):
        self.filename = filename
        self.EncryptedText = ''
        if os.path.exists(self.filename):
            self.DecryptedPlaceholder = open(filename, 'r+')
            self.DecryptedText = self.DecryptedPlaceholder.read()
            self.DecryptedPlaceholder.close()
            return True
        elif (not os.path.exists(self.filename)) or filename == '':
            return False


    def SaveEncryptedFile(self, filename):
        self.filename = filename
        if type(filename) == int or type(filename) == float:
            filename = str(filename)
            self.filename = filename
        if self.EncryptedText == '':
            return False
        else:
            EncryptedFileOut = open(filename, 'w')
            EncryptedContent = self.EncryptedText
            EncryptedFileOut.write(EncryptedContent)
            EncryptedFileOut.close
            return True


    def SaveDecryptedFile(self, filename):
        self.filename = filename
        if type(filename) == int or type(filename) == float:
            filename = str(filename)
            self.filename = filename
        if self.DecryptedText == '':
            return False
        else:
            DecryptedFileOut = open(filename, 'w')
            DecryptedContent = self.DecryptedText
            DecryptedFileOut.write(DecryptedContent)
            DecryptedFileOut.close
            return True


    def DetermineShift(self):
        for character in self.EncryptedText:
            if character.isupper():
                if character not in self.CharacterList:
                    self.CharacterList.append(character)
                    self.charcount = self.EncryptedText.count(character)
                    self.NumberList.append(self.charcount)
                self.upperdict = dict(zip(self.CharacterList, self.NumberList))
            elif character.islower():
                if character not in self.LowerCharacterList:
                    self.LowerCharacterList.append(character)
                    self.charcount = self.EncryptedText.count(character)
                    self.LowerNumberList.append(self.charcount)
                self.lowerdict = dict(zip(self.LowerCharacterList, self.LowerNumberList))     
                self.alldict = dict(self.lowerdict, **self.upperdict)
                self.max1 = max(self.alldict, key=self.alldict.get)
                self.alldict.update({self.max1:0})
                self.max2 = max(self.alldict, key=self.alldict.get)
                self.alldict.update({self.max2:0})
                self.max3 = max(self.alldict, key=self.alldict.get)
                self.alldict.update({self.max3:0})
                
                self.ord1 = ord(self.max1) - ord('e')
                if self.ord1 < 0:
                    self.ord1 = self.ord1 + 62
                self.ord2 = ord(self.max2) - ord('t')
                if self.ord2 < 0:
                    self.ord2 = self.ord2 + 62
                self.ord3 = ord(self.max3) - ord('a')
                if self.ord3 < 0:
                    self.ord3 = self.ord3 + 62
                
        print('The three most likely shift values for this text are: ')
        print(self.ord1)
        print(self.ord2)
        print(self.ord3)    
        return True


caesar = CaesarCipher()

if __name__ == '__main__':
    Done = False
    if len(sys.argv) == 2:
        Done = True
        print('Invalid syntax: caesar shift infile [outfile]')
    elif len(sys.argv) == 3:
        Done = True
        try:
            sys.argv[1] = int(sys.argv[1])
            if type(sys.argv[1]) != int:
                print('Invalid syntax: caesar shift infile [outfile]')
            else:
                ShiftAmount = sys.argv[1]
                filename = sys.argv[2]
            if ShiftAmount < 0:
                ShiftAmount = abs(ShiftAmount)
                caesar.LoadEncryptedFile(filename)
                caesar.Decrypt(ShiftAmount)
                caesar.PrintDecrypted()

            elif ShiftAmount > 0:
                caesar.LoadDecryptedFile(filename)
                caesar.Encrypt(ShiftAmount)
                caesar.PrintEncrypted()

            elif ShiftAmount == 0:
                caesar.LoadEncryptedFile(filename)
                caesar.DetermineShift()
        except:
            print('Invalid syntax: caesar shift infile [outfile]')

    elif len(sys.argv) == 4:
        Done = True
        try:
            sys.argv[1] = int(sys.argv[1])
            if type(sys.argv[1]) != int:
                print('Invalid syntax: caesar shift infile [outfile]')
            else:     
                ShiftAmount = sys.argv[1]
                filename  = sys.argv[2]
            if ShiftAmount < 0:
                ShiftAmount = abs(ShiftAmount)
                caesar.LoadEncryptedFile(filename)
                caesar.Decrypt(ShiftAmount)
                filename = sys.argv[3]
                caesar.SaveDecryptedFile(filename)
            elif ShiftAmount > 0:
                caesar.LoadDecryptedFile(filename)
                caesar.Encrypt(ShiftAmount)
                filename = sys.argv[3]
                caesar.SaveEncryptedFile(filename)

            elif ShiftAmount == 0:
                caesar.LoadEncryptedFile(filename)
                caesar.DetermineShift()
        except:
            print('Invalid syntax: caesar shift infile[outfile]')
        
    while not Done:
        print('C Clear All')
        print('L Load Encrypted File')
        print('R Read Decrypted File')
        print('S Store Encrypted File')
        print('W Write Decrypted File')
        print('O Output Encrypted Text')
        print('P Print Decrypted Text')
        print('E Encrypt Decrypted Text')
        print('D Decrypted Encrypted Text')
        print('Q Quit')
        print('-' * 26)

        Input = ''
        while Input not in ['C', 'L', 'R', 'S', 'W', 'O', 'P', 'E', 'D', 'Q']:
            Input = input('Enter Choice> ').strip().upper()

        if Input == 'C':
            caesar.ClearAll()
        elif Input == 'L':
            filename = input('Enter Filename> ')
            caesar.LoadEncryptedFile(filename)
        elif Input == 'R':
            filename = input('Enter Filename> ')
            caesar.LoadDecryptedFile(filename)
        elif Input == 'S':
            filename = input('Enter Filename> ')
            caesar.SaveEncryptedFile(filename)
        elif Input == 'W':
            filename = input('Enter Filename> ')
            caesar.SaveDecryptedFile(filename)
        elif Input == 'O':
            caesar.PrintEncrypted()
        elif Input == 'P':
            caesar.PrintDecrypted()
        elif Input == 'E':
            ShiftAmount = input('Enter Shift Amount> ')
            caesar.Encrypt(ShiftAmount)
        elif Input == 'D':
            ShiftAmount = input('Enter Shift Amount> ')
            caesar.Decrypt(ShiftAmount)
        elif Input == 'Q':
            Done = True
            
            
            
