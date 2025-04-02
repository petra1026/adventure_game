import time
import sys

a = 1 # sekundes starp katru rindkopu
b = 0.05 # sekundes starp katru rindkopu
c = 0.1 # sekundes starp katru rindkopu

def intro():
    print("")
    time.sleep(a)
    print("")
    time.sleep(a)
    print("")
    time.sleep(a)
    print("")
    time.sleep(a)
    print("")
    time.sleep(a)
    print()
    s1 = "...."
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    time.sleep(a)

    print("")
    time.sleep(a)
    print("")
    time.sleep(a)
    print("")
    time.sleep(a)

    s2 = "...."
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    time.sleep(a)

    print("")
    time.sleep(a)
    print("")
    print("")
    time.sleep(a)

    choice = input("Ko tu izvēlēsies? (1/2): ")

    if choice == "1":
        explore_riga()
    elif choice == "2":
        stay_home()
    else: 
        print("")  
        intro()

def explore_riga():
    print()
    print("")
    time.sleep(a)
    print("")
    time.sleep(a)
    print("")
    time.sleep(a)
    print("")
    time.sleep(a)

    print("")
    time.sleep(a)

    s3 = ' "" '
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    time.sleep(a)

    print("")
    time.sleep(a)
    print("")
    time.sleep(a)
    print("")
    print("")

    choice = input("Ko tu izvēlēsies? (1/2): ")

    if choice == "1":
        find_ally()
    elif choice == "2":
        listen_speech()
    else: 
        print("")  
        explore_riga()