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


def stay_home():
    print()
    print("Tu paliec mājās un mēģini saprast, kas notiek.")
    time.sleep(a)
    print("Tu apskati istabu un atrodi dažus vecus dokumentus ar datumiem no 1930. gadiem.")
    time.sleep(a)
    print("Kāda liekama sajūta tev saka, ka šie papīri varētu būt svarīgi.")
    time.sleep(a)
    print("Pēkšņi uz radio sāk runāt ziņu diktors.")
    time.sleep(a)
    
    s4 = '"Šodien, 1939. gada 23. augustā, Maskavā tika parakstīts līgums starp Vāciju un PSRS..."'
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    time.sleep(a)
    
    print("Tava sirds sāk sisties straujāk – tu zini, ko nozīmē šis datums.")
    time.sleep(a)
    print("Tu esi nokļuvis brīdī, kad Latvijas nākotne vēl ir neskaidra.")
    time.sleep(a)
    
    print("Tagad tev jāizlemj:")
    time.sleep(a)
    print("1) Meklēt atbildes ielās un runāt ar cilvēkiem.")
    print("2) Palikt istabā un mēģināt atrast vēl vairāk informācijas.")
    
    choice = input("Ko tu izvēlēsies? (1/2): ")
    
    if choice == "1":
        explore_riga()
    elif choice == "2":
        investigate_home()
    else:
        print("Nepareiza izvēle. Mēģini vēlreiz.")
        stay_home()

def investigate_home():
    print()
    print("Tu izvēlies palikt un rūpīgāk izpētīt māju.")
    time.sleep(a)
    print("Zem grīdas dēļiem tu atrodi slepenu nodalījumu.")
    time.sleep(a)
    print("Tajā ir vecs dienasgrāmatas žurnāls un fotogrāfija, kurā redzams cilvēks līdzīgs tev pašam...")
    time.sleep(a)
    
    s9 = '"Ja tu lasi šo, tas nozīmē, ka laiks atkal ir salūzis..."'
    for character in s9:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    time.sleep(a)
    
    print("Tu sāc apjaust, ka tava klātbūtne šeit nav nejauša.")
    time.sleep(a)
    print("Ir iespējams, ka esi bijis šeit jau iepriekš, varbūt pat vairākas reizes.")
    time.sleep(a)
    
    print("Pēkšņi pie durvīm kāds klauvē. Tu tuvojies uzmanīgi...")
    time.sleep(a)
    print("* TURPINĀJUMS SEKOS *")


def listen_speech():
    print()
    print("Tu esi vēstures epicentrā, bet vai vari to mainīt?")
    time.sleep(a)
    print("Tu sāc saprast, ka tava klātbūtne šeit var būt nozīmīgāka, nekā šķiet.")
    time.sleep(a)
    
    print("Tagad tev jāizlemj:")
    time.sleep(a)
    print("1) Iedzert kafiju un mēģināt iegūt vairāk informācijas no Edvarda.")
    print("2) Aiziet prom no kafejnīcas.")
    
    choice = input("Ko tu izvēlēsies? (1/2): ")
    
    if choice == "1":
        drink_coffee()
    elif choice == "2":
        leave_cafe()
    else:
        print("Nepareiza izvēle. Mēģini vēlreiz.")
        listen_speech()



def find_ally():
    print()
    print("Tu nolem meklēt kādu, kas varētu tev palīdzēt saprast situāciju.")
    time.sleep(a)
    print("Ejot pa ielu, tu pamani vīrieti ar pelēku uzvalku, kurš uzmanīgi vēro apkārtni.")
    time.sleep(a)
    print("Kad tavs skatiens sastopas ar viņa, viņš pietuvojas un klusi saka:")
    time.sleep(a)
    
    s5 = '"Tu neizskaties kā vietējais... Man liekas, ka mums ir jāparunā."'
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    time.sleep(a)
    
    print("Kas ir šis cilvēks? Vai viņš var tev palīdzēt?")
    time.sleep(a)
    print("Tu seko viņam mazā kafejnīcā, un sākas jauns piedzīvojums...")
    time.sleep(a)
    
    print("* TURPINĀJUMS SEKOS *")
    time.sleep(5)

    print("Tu esi vēstures epicentrā, bet vai vari to mainīt?")
    time.sleep(a)
    print("Tu sāc saprast, ka tava klātbūtne šeit var būt nozīmīgāka, nekā šķiet.")
    time.sleep(a)
    
    print("Tagad tev jāizlemj:")
    time.sleep(a)
    print("1) Iedzert kafiju un mēģināt iegūt vairāk informācijas no Edvarda.")
    print("2) Aiziet prom no kafejnīcas.")
    
    choice = input("Ko tu izvēlēsies? (1/2): ")
    
    if choice == "1":
        drink_coffee()
    elif choice == "2":
        leave_cafe()
    else:
        print("Nepareiza izvēle. Mēģini vēlreiz.")
        listen_speech()
        
def drink_coffee():
    print()
    print("Tu piesardzīgi noliek savu telefonu uz galda, lai pierādītu Edvardam, ka neesi drauds.")
    time.sleep(a)
    print("Viņš skatās uz tevi, pēc tam uz telefonu, un viegli pasmaida.")
    time.sleep(a)
    
    s6 = '"Gudrs lēmums," viņš saka. "Tas nozīmē, ka mēs varam runāt atklātāk."'
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    time.sleep(a)
    
    print("Viņš uzaicina tevi pasēdēt pie galda un pasūta divas kafijas.")
    time.sleep(a)
    print("Tu centies saprast, kāpēc viņš šķiet tik neparasts – viņa mati ir neparasti krāsaini šajā laikmetā, un tehnoloģijas viņam šķiet aizdomīgas.")
    time.sleep(a)
    
    print("Kad kafija tiek atnesta, Edvards skatās, kā tu iedzer pirmo malku.")
    time.sleep(a)
    print("Dzēriens ir silts, bet pēc brīža tu sajūti vieglu reiboni. Galva kļūst smaga, un redze sāk migloties.")
    time.sleep(a)
    
    print("Pirms tu pilnībā zaudē samaņu, tu dzirdi Edvarda balsi:")
    time.sleep(a)
    
    s7 = '"Tev tiešām nevajadzēja šeit atrasties. Piedod, bet tev nāksies palikt pagātnē..."'
    for character in s7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    time.sleep(a)
    
    print("Tavs ķermenis kļūst vājš, un pēdējais, ko tu redzi, ir Edvarda noslēpumainais smaids.")
    time.sleep(a)
    
    print("SPĒLES BEIGAS... vai tomēr turpinājums sekos?")
    time.sleep(a)

def leave_cafe():
    print()
    print("Tu pieceļies un pamāj ar galvu, atvainojies un dodies prom.")
    time.sleep(a)
    print("Edvards tikai nopūšas un saka:")
    time.sleep(a)
    s8 = '"Reizēm vislabākais lēmums ir neiesaistīties."'
    for character in s8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    time.sleep(a)
    print("Tu iznāc ārā un domā – kas patiesībā bija šis cilvēks un kā viņš zināja par tevi?")
    time.sleep(a)
    print("Tu ej tālāk pa ielu, mēģinot saprast, kā atgriezties mājās.")
    time.sleep(a)
    print("* SPĒLES BEIGAS – Bet pasaule joprojām gaida atbildes... *")