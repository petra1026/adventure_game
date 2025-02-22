import sys
import time

a=2
b=0.2
c=0.08

def intro():
    print()
    print("(EVERYTHING IS DARK)")
    time.sleep(a)
    print("teksts")
    time.sleep(a)
    print("teksts")
    time.sleep(a)
    print("teksts")
    time.sleep(a)
    print("teksts")
    time.sleep(a)
    print("teksts")
    time.sleep(a)

print()
question = '"teksts"'
for character in question:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(b)
    time.sleep(1.0)
    print()
    print()
    print("teksts")
    time.sleep(a)
    print("teksts")
    time.sleep(a)
    print()
    print("Path #1: teksts")
    time.sleep(a)
    print("Path #2: teksts")
    time.sleep(a)
    print("Path #3: teksts")
    time.sleep(a)
    print()
    firstPath = input("Which path will you choose? (1/2/3): ")
    if firstPath == '1':
        print()
        path1()
    elif firstPath == '2':
        print()
        path2()
    elif firstPath == '3':
        print()
        path3()
        def path1():
            print("teksts")
            time.sleep(a)
            print("teksts")
            time.sleep(a)
            print("teksts")
            time.sleep(a)
            print("teksts")
            time.sleep(a)
            print("teksts")
            time.sleep(a)
    print()
    s1 = '"Hello there!...'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    s2 = "...My name is APOLLO. I thought you were my sister, ARTEMIS..."
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s3 = "...Ah, now I remember you! Yes, you're looking for CHRONOS..."
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s4 = "...He's the one who trapped you in this time loop..."
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s5 = "...Yet, I cannot bring you to him..."
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s6 = "...Only HERMES can do that..."
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s7 = "...However, I have heard that CHRONOS dwells at the base of this mountain.\""
    for character in s7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)

    time.sleep(1)
    print()
    print()
    print("teksts:")
    time.sleep(a)
    print("Path #1: teksts")
    time.sleep(a)
    print("Path #2: teksts")
    time.sleep(a)
    print()
    secondPath = input("Which path will you choose? (1/2): ")
    if secondPath == '1':
        path1_1()
    elif secondPath == '2':
        path1_2()


def path1_1():
    print()
    print("teksts")
    time.sleep(a)
    print("teksts")
    time.sleep(a)
    print("teksts")
    time.sleep(a)
    s8 = '  "teksts"'
    for character in s8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('  --You think to yourself.')
    time.sleep(a)
    print("A boy calls out to you.")
    time.sleep(a)
    print()
    s1 = '"Hey! Wait up!...'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    s2 = "...My name is ARES. I was just coming down the mountain for some fresh air..."
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s3 = "...Mount OLYMPUS is the highest reaching mountain on Earth and the air is specially crisp..."
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s4 = "...Anyhow, I see you're searching for the correct path, as we all are..."
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s5 = "...It's not my place to tell you which path is correct..."
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s6 = "...However, I will tell you this..."
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    print()
    print()
    s7 = '..."ONLY THROUGH DARKNESS WILL FREEDOM BE ATTAINED"'
    for character in s7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    time.sleep(a)
    intro()


def path1_2():
    print()
    print("You begin scaling down the side of the mountain toward the bottom.")
    time.sleep(a)
    print("It's a long way down but you soon grow strong enough to appreciate the view.")
    time.sleep(a)
    print("Although you're still about halfway up the mountain, clouds surround you and the world seems small.")
    time.sleep(a)
    s1 = '  "I don\'t believe my eyes..."'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('  --You think to yourself')
    time.sleep(a)
    print()
    print("You continue down the mountain for days until you reach the bottom.")
    time.sleep(a)
    s2 = '  "Finally! I can face you, CHRONOS!"'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('--You yell, entering the base of Mount OLYMPUS through the largest red and black doors you\'ve ever seen')
    time.sleep(a)
    print("The darkness consumes you as you enter, unable to see a thing.")
    time.sleep(a)
    print("A thunderous voice calls out to you...")
    time.sleep(a)
    print()
    s3 = "Ah... I've been expecting you. But you're far too early..."
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s4 = "...It appears you've taken a fairly easy route..."
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s5 = "...You can see through the light, but not the DARKNESS..."
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s6 = "...You've developed some STRENGTH, but not enough..."
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s7 = "...There is more you need to grow..."
    for character in s7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s8 = "...More you need to LEARN"
    for character in s8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s9 = "...And learn you will"
    for character in s9:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s10 = "...In time..."
    for character in s10:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    intro()



    