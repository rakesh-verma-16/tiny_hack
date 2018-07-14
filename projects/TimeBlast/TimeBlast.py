import sys, select, os, time
from random import randint
limit = 6000
random_number = randint(0,9)
for i in range(limit, 1, -1):
    print("Your lucky number is ----> " + '\x1b[9;30;47m' + "   " + str(random_number) + "   " + '\x1b[0m', "Be very careful" )
    print("Timer has begin! Press ENTER to try your luck!!!" + '\x1b[1;30;47m' + "     " + str(i) + "    " + '\x1b[0m')
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        break;

    i += 1
    time.sleep(10/100)
    os.system('cls' if os.name == 'nt' else 'clear')

if i%10 == random_number:
    print('\x1b[3;35;44m' + "You are the hero they need but don't deserve" + '\x1b[0m')
else:
    print('\x1b[1;33;40m'+ "Not the fastest fish in the pond you are, I believe" + '\x1b[0m')



