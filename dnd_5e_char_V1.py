import random
import pdfrw
from pdfrw import PdfReader
from os import system, name

#template_pdf = pdfrw.Pdfreader("./charsheet_template.pdf")
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear()
print('Welcome to maxXxlos DnD 5e Character Creator Tool')
PlayerName = input('Enter YOUR Name:')
charname = input('Enter your CHARACTERS Name:')
charalignment = input('Whats your Characters alignment:')

clear()
charrace = int(input('''What Race is your Character?

Dwarf [1]          Gnome [6]
Elf [2]            Half-Elf [7]
Halfling [3]       Half-Orc [8]
Human [4]          Tieflin [9]
Dragonborn [5]

Enter your Characters Race:'''))

clear()
charclass = int(input('''What Class is your Character?

Barbarian [1]   Paladin [7]
Bard [2]        Ranger [8]
Cleric [3]      Rouge [9]
Druid [4]       Sorcerer [10]
Fighter [5]     Warlock [11]
Monk [6]        Wizard [12]

Enter your Characters Class:'''))
charlvl = 1
charXP = 0

clear()
statroll = input('Do do you want me to roll your stats for you? (y/n):')

clear()
# HIER WERDEN DIE 6 STATS GEMACHT
statnumbers = []
if statroll == 'Y' or statroll == 'y':
    for x in range(6):
        statnumbers.append(random.randint(3, 19))
    print('''These are the numbers: %s\n
Please assign them to your desired stats:''' % statnumbers)

    STR = int(input('Strength:'))
    DEX = int(input('Dexterity:'))
    CONS = int(input('Constitution:'))
    INT = int(input('Intelligence:'))
    WIS = int(input('Wisdom:'))
    CHAR = int(input('Charisma:'))

    print('''These are your stats:\n
STR: %s
DEX: %s
CONS: %s
INT: %s
WIS: %s
CHAR: %s''' % (STR, DEX, CONS, INT, WIS, CHAR))
else:
    STR = int(input('Strength:'))
    DEX = int(input('Dexterity:'))
    CONS = int(input('Constitution:'))
    INT = int(input('Intelligence:'))
    WIS = int(input('Wisdom:'))
    CHAR = int(input('Charisma:'))


def modifiercalculator(n):

    if 0 < n < 2:
        return -5
    if 1 < n < 3:
        return -4
    if 3 < n < 6:
        return -3
    if 5 < n < 8:
        return -2
    if 7 < n < 10:
        return -1
    if 9 < n < 12:
        return 0
    if 11 < n < 14:
        return 1
    if 13 < n < 16:
        return 2
    if 15 < n < 18:
        return 3
    if 17 < n < 20:
        return 4
    if 19 < n < 21:
        return 5
    else:
        print('ERROR')

STRmodifier = modifiercalculator(STR)
DEXmodifier = modifiercalculator(DEX)
CONSmodifier = modifiercalculator(CONS)
INTmodifier = modifiercalculator(INT)
WISmodifier = modifiercalculator(WIS)
CHARmodifier = modifiercalculator(CHAR)
#clear()

# JETZT KOMMEN DIE KLASSEN
if charclass == 1:
    text
if charclass == 2:
    text
if charclass == 2:
    text
if charclass == 3:
    text
if charclass == 4:
    text
if charclass == 5:
    text
if charclass == 6:
    text
if charclass == 7:
    text
if charclass == 8:
    text
if charclass == 9:
    text
if charclass == 10:
    text
if charclass == 11:
    text
if charclass == 12:
    text
else:
    print("Error")
