import sys

'''
    Usage:
        CommandLine ~ $ python3 CaesarCipher.py [language] [cipher] [key] [text]

      Parameters' Explanation:
      
        #[language]="en" or [language]="tr"
        #[cipher]="enc" or [cipher]="dec"
        #[key]=1 to 29 for Turkish   or  [key]=1 to 26 for English
                                    OR
        #If you don't know the key. You can use "bf" value for the key parameter.
        #"bf" means Brute Force.
         
        Example:
            CommandLine ~ $ python3 CaesarCipher.py en dec 2 "map"
            Decrypted Text: ['ocr']
            
            CommandLine ~ $ python3 CaesarCipher.py en enc 2 "ocr"
            Encrypted Text: ['map']

        !!!Text is the must be enclosed in quotation marks.Others are optional.!!!

        Example for Brute Force:
        
            CommandLine ~ $ python3 sezar.py en dec bf "ywivreqi"
            Key =  1 ['zxjwsfrj']
            Key =  2 ['aykxtgsk']
            Key =  3 ['bzlyuhtl']
            Key =  4 ['camzvium']
            Key =  5 ['dbnawjvn']
            Key =  6 ['ecobxkwo']
            Key =  7 ['fdpcylxp']
            Key =  8 ['geqdzmyq']
            Key =  9 ['hfreanzr']
            Key =  10 ['igsfboas']
            Key =  11 ['jhtgcpbt']
            Key =  12 ['kiuhdqcu']
            Key =  13 ['ljvierdv']
            Key =  14 ['mkwjfsew']
            Key =  15 ['nlxkgtfx']
            Key =  16 ['omylhugy']
            Key =  17 ['pnzmivhz']
            Key =  18 ['qoanjwia']
            Key =  19 ['rpbokxjb']
            Key =  20 ['sqcplykc']
            Key =  21 ['trdqmzld']
            Key =  22 ['username']
            Key =  23 ['vtfsobnf']
            Key =  24 ['wugtpcog']
            Key =  25 ['xvhuqdph']


'''
alphabetTr=list("abcçdefgğhıijklmnoöprsştuüvyz")
alphabetEn=list("abcdefghijklmnopqrstuvwxyz")

lang=sys.argv[1]
cipher=sys.argv[2]
    
if(sys.argv[3]!="bf"):#Brute Force özelliği  yoksa yani sayı girilmişse.
    key=int(sys.argv[3])
else:#Brute force özelliği var ise int'e çevirmeye gerek yok.
    key=sys.argv[3]
    
text=str(sys.argv[4:])#Text, tırnak koyulmadan yazılırsa herbir kelimeyi
                         #bir liste elemanıymış gibi davranarak şifresini çözer.


def CaesarEn(text):#Şİfreli ingilizce metni çözer.
    decText=""
    text=text.lower()#Tüm metin küçük harflere çevrildi.
    for i in text:
        if(i==" "):
            decText += " "
        if(i not in alphabetEn):
            decText += i
        if(i in alphabetEn):   
            index=alphabetEn.index(i)
            decText += alphabetEn[(index+key) % 26]#Alfabede kaydırma yapılır.
    print("Decrypted Text:",decText)
    
def CaesarTr(text):#Şifreli Türkçe metni çözer.
    decText=""
    text=text.lower()#Tüm metin küçük harflere çevrildi.
    for i in text:
        if(i==" "):
            decText += " "
        if(i not in alphabetTr):
            decText += i
        if(i in alphabetTr):
            index=alphabetTr.index(i)           
            decText += alphabetTr[(index+key) % 29]
    print("Decrypted Text:",decText)

def CaesarEnEncrypt(text):#Metin şifrelenir.
    encText=""
    text=text.lower()
    for i in text:
        if(i==" "):
            encText += " "
        if(i not in alphabetEn):
            encText += i
        if(i in alphabetEn):
            index=alphabetEn.index(i)           
            encText += alphabetEn[(index-key) % 29]
    print("Encrypted Text:",encText)
    
def CaesarTrEncrypt(text):#Metin şifrelenir.
    encText=""
    text=text.lower()#Tüm metin küçük harflere çevrildi.
    for i in text:
        if(i==" "):
            encText += " "
        if(i not in alphabetTr):
            encText += i
        if(i in alphabetTr):
            index=alphabetTr.index(i)           
            encText += alphabetTr[(index-key) % 29]
    print("Encrypted Text:",encText)


def CaesarBruteForceEn(text):#İngilizce için Brute Force ile metnin şifresi çözülür.
    decText=""
    text=text.lower()#Tüm metin küçük harflere çevrildi.
    key=1
    while key < 26:
        for i in text:
            if(i==" "):
                decText += " "
            if(i not in alphabetEn):
                decText += i
            if(i in alphabetEn):   
                index=alphabetEn.index(i)
                decText += alphabetEn[(index+key) % 26]#Alfabede kaydırma yapılır.       
        print("Key = ",key,decText)
        decText=""
        key+=1 

def CaesarBruteForceTr(text):
    decText=""
    text=text.lower()#Tüm metin küçük harflere çevrildi.
    key=1
    while key < 29:
        for i in text:
            if(i==" "):
                decText += " "
            if(i not in alphabetTr):
                decText += i
            if(i in alphabetTr):
                index=alphabetTr.index(i)           
                decText += alphabetTr[(index+key) % 29]
        print("Key = ",key,decText)
        key+=1
        decText=""
        
if(lang.lower()=="en"):
    if(key=="bf"):
        cipher=="dec"
        CaesarBruteForceEn(text)
    elif(cipher=="dec"):
        CaesarEn(text)
    elif(cipher=="enc"):
        CaesarEnEncrypt(text)

elif(lang.lower()=="tr"):
    if(key=="bf"):
        cipher=="dec"
        CaesarBruteForceTr(text)
    elif(cipher=="dec"):
        CaesarTr(text)
    elif(cipher=="enc"):
        CaesarTrEncrypt(text)

else:
    print("One of the parameters is incorrect")
