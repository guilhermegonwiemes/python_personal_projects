import random
import heapq

def roll_attribute():
    contador = 0
    while contador < 6:
        dice = [random.randint(1,6)for _ in range(5)]
        print ("\033[31m{}\033[m".format(sum(heapq.nlargest(3, dice,))))
        print(dice,'\n')
        contador += 1
print('\n=== D&D Attribute Roller ===\n')
print('Attributes to distribute:\n')
roll_attribute()
