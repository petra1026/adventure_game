import time
import sys

a = 1 # sekundes starp katru rindkopu
b = 0.05 # sekundes starp katru rindkopu
c = 0.1 # sekundes starp katru rindkopu

def intro():
    print("Tu pamosties no skaļa tramvaja zvana aiz loga.")
    time.sleep(a)
    print("Pavēries apkārt – istaba izskatās citādi nekā ierasts.")
    time.sleep(a)
    print("Nav televizora, nav datora... Tikai vecs radio uz koka galds.")
    time.sleep(a)
    print("Caur logu tu redzi ielu, kas izskatās neparasti – cilvēki ģērbti vecmodīgi, un automašīnas ir senlaicīgas.")
    time.sleep(a)
    print("Pie mājas stūra avīžu zēns piedāvā 'Jaunākās Ziņas', un uz avīzes vāka ir raksts par... prezidentu Kārli Ulmani?!")
    time.sleep(a)
    print()
    s1 = "Kur es esmu? Kāpēc Rīga izskatās tā, it kā būtu 1930. gadi?"
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    time.sleep(a)

    print("Tu piecelies un pieej pie loga.")
    time.sleep(a)
    print("Pilsēta ir dzīva – uz ielām pastaigājas dāmas elegantos mēteļos un kungi ar platmalēm.")
    time.sleep(a)
    print("Kādā brīdī kāds tev uzliek roku uz pleca...")
    time.sleep(a)

    s2 = '"Jūs esat pamodies... Laiks ir svarīgs, un jums jāpieņem lēmums."'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    time.sleep(a)

    print("Tev ir divas izvēles:")
    time.sleep(a)
    print("1) Iet laukā uz ielas un izpētīt, kas notiek Rīgā.")
    print("2) Palikt mājās un mēģināt saprast, kā tu šeit nokļuvi.")
    time.sleep(a)

    choice = input("Ko tu izvēlēsies? (1/2): ")

    if choice == "1":
        explore_riga()
    elif choice == "2":
        stay_home()
    else: 
        print("Nepareiza izvēle. Mēģini vēlreiz.")  
        intro()

def explore_riga():
    print()
    print("Tu nolem iet ārā un iepazīt šo neparasto Rīgu.")
    time.sleep(a)
    print("Pa ielu brauc veci tramvaji, cilvēki sarunājas, un avīžu kioski piedāvā laikrakstus par notikumiem, kas tev šķiet kā no vēstures grāmatām.")
    time.sleep(a)
    print("Tu dzirdi, ka netālu pie Brīvības pieminekļa notiek runa.")
    time.sleep(a)
    print("Ziņkārības vadīts, tu dodies turp.")
    time.sleep(a)

    print("Cilvēku pūlis ir sapulcējies, un uz nelielas tribīnes stāv vīrietis, kuru tu tūlīt atpazīsti no bildēm – Kārlis Ulmanis!")
    time.sleep(a)

    s3 = ' "Latvija ir stipra! Tauta ir vienota!" '
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    time.sleep(a)

    print("Tu saproti, ka šī nav tikai ilūzija vai sapnis – tu patiešām esi pagātnē.")
    time.sleep(a)
    print("Tagad tev ir divas izvēles:")
    time.sleep(a)
    print("1) Mēģināt atrast kādu, kurš varētu tev izskaidrot, kas notiek.")
    print("2) Saplūst ar pūli un klausīties Ulmaņa runu.")

    choice = input("Ko tu izvēlēsies? (1/2): ")

    if choice == "1":
        find_ally()
    elif choice == "2":
        listen_speech()
    else: 
        print("Nepareiza izvēle. Mēģini vēlreiz.")  
        explore_riga()