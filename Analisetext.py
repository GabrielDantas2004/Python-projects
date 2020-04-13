print('                                                     ')
print('                                                     ')
print('\033[33m----------ANALISADOR DE TEXTO----------\033[m')
print('                                                     ')
print('\033[36mInsira o texto retirando as quebras de linha:\033[m')
text1 = str(input(''))
DIVIDIDO = text1.split()
quersaber = int(input('\033[36mVocê quer saber quantas vezes alguma palavra aparece? - (1 = sim; 2 = não). ---->\033[m  '))
if quersaber == 1:
    print('\033[36mQual a palavra você quer saber quantas vezes aparece?\033[m')
    word = str(input(''))
    tamanhoword = DIVIDIDO.count(word)
    if tamanhoword == 1:
        print('\033[4;31mA palavra {} aparece {} vez.\033[m'.format(word,tamanhoword))
    elif tamanhoword == 0:
        print('\033[4;31mA palavra inserida aparece nenhuma vez.\033[m')
    else:
        print('\033[4;31mA palavra {} aparece {} vezes.\033[m'.format(word,tamanhoword))
elif quersaber == 2:
    print('\033[4;31mOk!\033[m')
else:
    print('\033[4;31m😢 Ops, você não digitou um número válido...\033[m')
quersaber2 = int(input('\033[36mVocê quer saber se alguma palavra específica está no texto? - (1 = sim; 2 = não). ---->\033[m '))
if quersaber2 == 1:
    print('\033[36mQual é a palavra?\033[m')
    word2 = str(input(''))
    v = print(word2 in DIVIDIDO) 
elif quersaber2 == 2:
    print('\033[4;31mOk!\033[m')
else:
    print('\033[4;31m😢 Ops, você não digitou um número válido...\033[m')
print('                                                                                                                   ')
countA = text1.count('A')
counta = text1.count('a')
countÁ = text1.count('Á')
countá = text1.count('á')
countÀ = text1.count('À')
countà = text1.count('à')
countÂ = text1.count('Â')
countâ = text1.count('â')
countÃ = text1.count('Ã')
countã = text1.count('ã')
countB = text1.count('B')
countb = text1.count('b')
countC = text1.count('C')
countc = text1.count('c')
countD = text1.count('D')
countd = text1.count('d')
countE = text1.count('E')
counte = text1.count('e')
countÈ = text1.count('È')
countè = text1.count('è')
countÉ = text1.count('É')
counté = text1.count('é')
countÊ = text1.count('Ê')
countê = text1.count('ê')
countF = text1.count('F')
countf = text1.count('f')
countG = text1.count('G')
countg = text1.count('g')
countH = text1.count('H')
counth = text1.count('h')
countI = text1.count('I')
counti = text1.count('i')
countÌ = text1.count('Ì')
countì = text1.count('ì')
countÍ = text1.count('Í')
countí = text1.count('í')
countÎ = text1.count('Î')
countî = text1.count('î')
countJ = text1.count('J')
countj = text1.count('j')
countK = text1.count('K')
countk = text1.count('k')
countL = text1.count('L')
countl = text1.count('l')
countM = text1.count('M')
countm = text1.count('m')
countN = text1.count('N')
countn = text1.count('n')
countO = text1.count('O')
counto = text1.count('o')
countÓ = text1.count('Ó')
countó = text1.count('ó')
countÔ = text1.count('Ô')
countô = text1.count('ô')
countÒ = text1.count('Ò')
countò = text1.count('ò')
countÕ = text1.count('Õ')
countõ = text1.count('õ')
countP = text1.count('P')
countp = text1.count('p')
countQ = text1.count('Q')
countq = text1.count('q')
countR = text1.count('R')
countr = text1.count('r')
countS = text1.count('S')
counts = text1.count('s')
countT = text1.count('T')
countt = text1.count('t')
countU = text1.count('U')
countu = text1.count('u')
countÙ = text1.count('Ù')
countù = text1.count('ù')
countÚ = text1.count('Ú')
countú = text1.count('ú')
countÛ = text1.count('Û')
countû = text1.count('û')
countŨ = text1.count('Ũ')
countũ = text1.count('ũ')
countV = text1.count('V')
countv = text1.count('v')
countW = text1.count('W')
countw = text1.count('w')
countX = text1.count('X')
countx = text1.count('x')
countY = text1.count('Y')
county = text1.count('y')
countZ = text1.count('Z')
countz = text1.count('z')
letraa = countA+counta+countÁ+countá+countÀ+countà+countÂ+countâ+countÃ+countã
letrab = countB+countb
letrac = countC+countc
letrad = countD+countd
letrae = countE+counte+countÈ+countè+countÉ+counté+countÊ+countê
letraf = countF+countf
letrag = countG+countg
letrah = countH+counth
letrai = countI+counti+countÌ+countì+countÍ+countí+countÎ+countî
letraj = countJ+countj
letrak = countK+countk
letral = countL+countl
letram = countM+countm
letran = countN+countn
letrao = countO+counto+countÓ+countó+countÔ+countô+countÒ+countò+countÕ+countõ
letrap = countP+countp
letraq = countQ+countq
letrar = countR+countr
letras = countS+counts
letrat = countT+countt
letrau = countU+countu+countÙ+countù+countÚ+countú+countÛ+countû+countŨ+countũ
letrav = countV+countv
letraw = countW+countw
letrax = countX+countx
letray = countY+county
letraz = countZ+countz 
quersaber3 = int(input('\033[36mVocê quer saber a quantidade de cada letra no texto? - (1 = sim; 2 = não). ---->\033[m '))
if quersaber3 == 1:
    if letraa > 0:
        print('\033[4;31mSeu texto tem {} letras "A".\033[m'.format(letraa))
    if letrab > 0:
        print('\033[4;31mSeu texto tem {} letras "B".\033[m'.format(letrab))
    if letrac > 0:
        print('\033[4;31mSeu texto tem {} letras "C".\033[m'.format(letrac))
    if letrad > 0:
        print('\033[4;31mSeu texto tem {} letras "D".\033[m'.format(letrad))
    if letrae > 0:
        print('\033[4;31mSeu texto tem {} letras "E".\033[m'.format(letrae))
    if letraf > 0:
        print('\033[4;31mSeu texto tem {} letras "F".\033[m'.format(letraf))
    if letrag > 0:
        print('\033[4;31mSeu texto tem {} letras "G".\033[m'.format(letrag))
    if letrah > 0:
        print('\033[4;31mSeu texto tem {} letras "H".\033[m'.format(letrah))
    if letrai > 0:
        print('\033[4;31mSeu texto tem {} letras "I".\033[m'.format(letrai))
    if letraj > 0:
        print('\033[4;31mSeu texto tem {} letras "J".\033[m'.format(letraj))
    if letrak > 0:
        print('\033[4;31mSeu texto tem {} letras "K".\033[m'.format(letrak))
    if letral > 0:
        print('\033[4;31mSeu texto tem {} letras "L".\033[m'.format(letral))
    if letram > 0:
        print('\033[4;31mSeu texto tem {} letras "M".\033[m'.format(letram))
    if letran > 0:
        print('\033[4;31mSeu texto tem {} letras "N".\033[m'.format(letran))
    if letrao > 0:
        print('\033[4;31mSeu texto tem {} letras "O".\033[m'.format(letrao))
    if letrap > 0:
        print('\033[4;31mSeu texto tem {} letras "P".\033[m'.format(letrap))
    if letraq > 0:
        print('\033[4;31mSeu texto tem {} letras "Q".\033[m'.format(letraq))
    if letrar > 0:
        print('\033[4;31mSeu texto tem {} letras "R".\033[m'.format(letrar))
    if letras > 0:
        print('\033[4;31mSeu texto tem {} letras "S".\033[m'.format(letras))
    if letrat > 0:
        print('\033[4;31mSeu texto tem {} letras "T".\033[m'.format(letrat))
    if letrau > 0:
        print('\033[4;31mSeu texto tem {} letras "U".\033[m'.format(letrau))
    if letrav > 0:
        print('\033[4;31mSeu texto tem {} letras "V".\033[m'.format(letrav))
    if letraw > 0:
        print('\033[4;31mSeu texto tem {} letras "W".\033[m'.format(letraw))
    if letrax > 0:
        print('\033[4;31mSeu texto tem {} letras "X".\033[m'.format(letrax))
    if letray > 0:
        print('\033[4;31mSeu texto tem {} letras "Y".\033[m'.format(letray))
    if letraz > 0:
        print('\033[4;31mSeu texto tem {} letras "Z".\033[m'.format(letraz))
elif quersaber3 == 2:
    print('\033[4;31mOk!\033[m')
else:
    print('\033[4;31m😢 Ops, você não digitou um número válido...\033[m')
print('\033[4;31mSeu texto tem {} palavras.\033[m'.format(len(DIVIDIDO)))












































































