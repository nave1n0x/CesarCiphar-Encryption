Caesar Cipher
Usage: CommandLine ~ $ python3 CaesarCipher.py [language] [cipher] [key] [text]

  Parameters' Explanation:
  
    #[language]="en" or [language]="tr"
    #[cipher]="enc" or [cipher]="dec"
     enc=encryption    dec=decryption
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
    
        CommandLine ~ $ python3 CaesarCipher.py en dec bf "ywivreqi"
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
