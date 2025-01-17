import random
import os
import msvcrt

#Funkcja do obsługi pojedynczych klawiszy w Windows
def get_key():
    while True:
        key = msvcrt.getch()
        if key in [b'\x00', b'\xe0']:  #Strzałki
            key = msvcrt.getch()
            return key.decode()
        elif key == b'\r':  #Enter
            return "\n"

#Funkcja do wyboru opcji dialogowych
def dialogue_choice(options):
    selected = 0
    while True:
        os.system("cls")  #Wyczyść ekran na Windows
        print("Wybierz jedną z opcji dialogowych (strzałki ↑/↓ i Enter):")
        for i, option in enumerate(options):
            if i == selected:
                print(f"> {option}")  #Zaznaczona opcja
            else:
                print(f"  {option}")  #Niezaznaczona opcja

        key = get_key()  #Pobierz klawisz

        if key == "H":  #Strzałka w górę
            selected = (selected - 1) % len(options)
        elif key == "P":  #Strzałka w dół
            selected = (selected + 1) % len(options)
        elif key == "\n":  #Enter
            return selected

#Funkcja rzutu kostką
def diceThrow():
    options = ["Mag wody", "Mag ognia", "Mag ziemi", "Mag powietrza", "Mag 4 żywiołów"]
    return random.choice(options)

#Funkcja dla fabuły po rzucie kostką
def diceThrowMain():
    diceRoll = diceThrow()
    print(f"Kostka wylosowała: {diceRoll}")
    input("Naciśnij Enter, aby kontynuować...")
#Każdy rodzaj maga ma przypisaną oddzielną "drogę dialogową", np. mag wody ma coś typowego ale już mag powietrza ma np. wzmiankę o ojcu
    if diceRoll == "Mag wody": 
        print("Mag wody, intrygujące... Dawno nie było takiego w naszym kręgu...")
        input("Nacisnij Enter aby wybrać opcję dialogową...")
        options = [
            "*Odejdź od starca nic nie mowiąc.*",
            "I co ja teraz mam zrobić? Gdzie mam iść? Kim ja tak naprawdę jestem?!",
        ]
        choice = dialogue_choice(options)
        print(f"Wybrałeś: {options[choice]}")
        print(" ")
        if options[choice] == "*Odejdź od starca nic nie mowiąc.*":
            print("Wracasz do domu z karczmy. Niczego nieświadomy idziesz spać. W nocy budzi Cię przeraźliwy krzyk matki.")
            print("Zdenerwowany wybiegasz z domu i widzisz jak cała twoja wioska płonie a żołnierze w czarnych zbrojach zmierzają w twoim kierunku...")
            print(" ")
            print(" ")
            print("KONIEC GRY")
        elif options[choice] == "I co ja teraz mam zrobić? Gdzie mam iść? Kim ja tak naprawdę jestem?!":
            print("Musisz się przygotować na trening. Nie będzie łatwo to mogę ci zapewnić... - rzekł starzec")
            print("Za chwilę wybierzesz swoją decyzję dotyczącą treningu...")
            input("Nacisnij Enter aby wybrać opcję dialogową...")
            options = [
                    "Na żaden trening nie będę szedł, przestań bredzić *Odchodzisz od starca*",
                    "Gdzie będzie ten trening i jak szybko mam się tam udać?"
                ]
            choice = dialogue_choice(options)
            print(f"Wybrałeś: {options[choice]}")
            print(" ")
            if choice == 0:
                    print("Opuściłeś starca, nie przejmując się jego radami. Może popełniłeś błąd?")
                    print("Wracasz do domu z karczmy. Niczego nieświadomy idziesz spać. W nocy budzi Cię przeraźliwy krzyk matki.")
                    print("Zdenerwowany wybiegasz z domu i widzisz jak cała twoja wioska płonie a żołnierze w czarnych zbrojach zmierzają w twoim kierunku...")
                    print(" ")
                    print(" ")
                    print("KONIEC GRY")
            elif choice == 1:
                    print("Starzec opowiada Ci o tajemniczym miejscu, gdzie trening się odbędzie...")
                    print("Rozmowa zajeła dosłownie chwilę, bo musicie ruszać. Dowiadujesz się od starca, że twoja wioska zostanie nazajutrz spalona.")
                    print("Wracasz szybko do swojej chaty, aby zapakować najpotrzebniejsze rzeczy.")
                    print("Tłumaczysz swojej mamie, że musisz jechać, bo masz bardzo ważną misję do wypełnienia.")
                    print("Twoja matka zostaje odeskortowana do miasta daleko od twojej wioski tak, aby była bezpieczna, a ty wyruszasz w drogę.")
                    print("Razem ze starcem wsiadacie nie konie i wyruszacie na południe. Jesteś gotowy na to co przyniesie przyszłość, ale wewnętrznie odczuwasz lęk...")
                    print("Czy aby napewno sobie poradzę? Czy to własnie ja jestem tym ostatnim puzzlem układanki...?")
                    print(" ")
                    print("5 DNI PÓŹNIEJ")
                    print(" ")
                    print("Po pięciu dniach podróży przez pustynię i tropikalny las, w końcu docierasz na miejsce w którym ma zacząć się twój trening.")
                    print("Dostałeś komnatę w małym zamku nie opodal placu treningowego.")
                    print("Gdy rozpakowujesz rzeczy słyszysz pukanie do drzwi... *puk, puk*")
                    print("Kto tam? - pytasz zdziwiony.")
                    print("To ja Ferland. (imię starca, którego poznałeś w karczmie).")
                    print("Wejdź proszę! - krzyczysz z drugiego końca pokoju.")  
                    print("Jesteś gotowy na pierwszy trening Lobo?")
                    input("Nacisnij Enter aby wybrać opcję dialogową...")
                    options = [
                        "Urodziłem się gotowy starcze!",
                        "Napewno to ja mam wam pomóc? Jestem tylko zwykłym chłopakiem z wioski a nie zbawicielem"
                            ]   
                    choice = dialogue_choice(options)
                    print(f"Wybrałeś: {options[choice]}")
                    if options[choice] == "Urodziłem się gotowy starcze!":
                        print("To dobrze zbieraj się i idziemy.")
                        print(" ")
                        print("Na placu treningowym uczysz się jak opanować naturę wody.")
                        print("Szło Ci dobrze do momentu kiedy nie przyszło do przecinania skały wodą.")
                        print("Na tym momencie podłamałeś się, ale zdecydowałeś się że się nie poddasz.")
                        print(" ")
                        def rockCuttingTraining():
                            successes = 0
                            attempts = 0
                            print("Rozpoczynasz trening cięcia skał...")
                            #Pętla która działa na takiej zasadzie, że dopóki użytkownik nie będzie miał wyniku 3/3 cały czas się zapętla.
                            while successes < 3:
                                input("Naciśnij Enter, aby spróbować przeciąć skałę: ")
                                attempts += 1
                                rolled_number = random.randint(1, 10)
                                
                                if rolled_number % 2 == 0:  #Sukces, jeśli liczba parzysta
                                    successes += 1
                                    print(f"Udało ci się przeciąć skałę! ({successes}/3)")
                                else:  #Kolejna próba, jeśli liczba nieparzysta
                                    print(f"Próbuj dalej, wojowniku! ({successes}/3)")
                            
                            print(f"\nBrawo! Udało Ci się przeciąć skałę 3 razy w {attempts} próbach!")
                            print("Jesteś teraz gotowy, aby walczyć z Zgrobem!")
                            input("Wcisnij Enter aby przejść dalej...")
                            print("Parę ciężkich treningów potem...")
                            print("Jesteś gotowy Lobo, możemy iść pokonać twojego ojca... - rzekł starzec.")
                            print("Co mojego ojca? O czym ty mówisz??? *Serce zaczyna ci bić w nierównomiernym tempie*.")
                            print("Zgrob to tak naprawdę twój ojciec. Po tym jak dołączył do naszego zakonu ciemne siły chciały przejąć jego duszę i się im udało...")
                            print("Był on najpotężniejszym z nas i jedyne czego chciał to waszego dobra ale jego umysł był na to za słaby.")
                            print("Starał się z tym walczyć ale nie był w stanie...")
                            print("Nie, nie to nie może być prawda... - powiedział Lobo")
                            print("Zbieraj się musimy ruszać... - rzekł starzec.")
                            print(" ")
                            print("Droga zajęła długo, była wycieńczająca ale aby świat istniał Lobo musi pokonać Zgroba...")
                            print(" ")
                            print("Jesteśmy, oto Góra Zagłady. Wierzymy w Ciebie Lobo musisz pokonać ojca! - odparł starzec.")
                            print("Obiecuję, że was nie zawiodę! - odarpł Lobo.")
                            input("Wciśnij Enter, żeby walczyć z ojcem!")
                            def fightingFather():
                                successes = 0
                                attempts = 0
                                print("Rozpoczynasz walkę z ojcem...")
                                #Pętla która działa na takiej zasadzie, że dopóki użytkownik nie będzie miał wyniku 3/3 cały czas się zapętla.
                                while successes < 7:
                                    input("Naciśnij Enter, aby zadać cios: ")
                                    attempts += 1
                                    rolled_number = random.randint(1, 10)
                                
                                    if rolled_number % 2 == 0:  #Sukces, jeśli liczba parzysta
                                        successes += 1
                                        print(f"Cięcie wody! ({successes}/7)")
                                    else:  #Kolejna próba, jeśli liczba nieparzysta
                                        print(f"Nigdy mnie nie pokonasz *BUAHAHAHA*! ({successes}/7)")
                            fightingFather()
                            input("Wciśnij Enter, aby przejść dalej.")
                            print("*Ah,ah* Synu czy to ty?")
                            print("Ojcze... Naprawdę nie chciałem ale nie miałem innej opcji, inaczej zniszczył byś świat.")
                            print("Dziękuje Ci synu, pamiętaj że was kochałem...")
                            print("Ojciec umiera, a ty zostajesz bohaterem...")
                            print("Czasami myślisz czy była inna opcja? Czy musiałeś zabić ojca...?")
                            print("Nigdy jednak się tego nie dowiesz...")
                            print(" ")
                            print("Dziękuje za zagranie")
                            print("FIN")
                        rockCuttingTraining()
                    elif options[choice] == "Napewno to ja mam wam pomóc? Jestem tylko zwykłym chłopakiem z wioski a nie zbawicielem":
                        print("A myślisz ze zjawiłbym się w wiosce, o której nikt nawet nie wie i błagał Cię o to abyś ze mną poszedł?")
                        print("Masz to zapisane w kartach Lobo zaufaj mi... - rzekł starzec spokojnym tonem.")
                        print("Chyba masz rację... - odparł Lobo.")
                        print("Dobra dosyć tego gadania zabieraj się do treningu!")
                        def rockCuttingTraining():
                            successes = 0
                            attempts = 0
                            print("Rozpoczynasz trening cięcia skał...")
                            #Pętla która działa na takiej zasadzie, że dopóki użytkownik nie będzie miał wyniku 3/3 cały czas się zapętla.
                            while successes < 3:
                                input("Naciśnij Enter, aby spróbować przeciąć skałę: ")
                                attempts += 1
                                rolled_number = random.randint(1, 10)
                                
                                if rolled_number % 2 == 0:  #Sukces, jeśli liczba parzysta
                                    successes += 1
                                    print(f"Udało ci się przeciąć skałę! ({successes}/3)")
                                else:  #Kolejna próba, jeśli liczba nieparzysta
                                    print(f"Próbuj dalej, wojowniku! ({successes}/3)")
                            
                            print(f"\nBrawo! Udało Ci się przeciąć skałę 3 razy w {attempts} próbach!")
                            print("Jesteś teraz gotowy, aby walczyć z Zgrobem!")
                            input("Wcisnij Enter aby przejść dalej...")
                            print("Parę ciężkich treningów potem...")
                            print("Jesteś gotowy Lobo, możemy iść pokonać twojego ojca... - rzekł starzec.")
                            print("Co mojego ojca? O czym ty mówisz??? *Serce zaczyna ci bić w nierównomiernym tempie*.")
                            print("Zgrob to tak naprawdę twój ojciec. Po tym jak dołączył do naszego zakonu ciemne siły chciały przejąć jego duszę i się im udało...")
                            print("Był on najpotężniejszym z nas i jedyne czego chciał to waszego dobra ale jego umysł był na to za słaby.")
                            print("Starał się z tym walczyć ale nie był w stanie...")
                            print("Nie, nie to nie może być prawda... - powiedział Lobo")
                            print("Zbieraj się musimy ruszać... - rzekł starzec.")
                            print(" ")
                            print("Droga zajęła długo, była wycieńczająca ale aby świat istniał Lobo musi pokonać Zgroba...")
                            print(" ")
                            print("Jesteśmy, oto Góra Zagłady. Wierzymy w Ciebie Lobo musisz pokonać ojca! - odparł starzec.")
                            print("Obiecuję, że was nie zawiodę! - odarpł Lobo.")
                            input("Wciśnij Enter, żeby walczyć z ojcem!")
                            def fightingFather():
                                successes = 0
                                attempts = 0
                                print("Rozpoczynasz walkę z ojcem...")
                                
                                while successes < 7:
                                    input("Naciśnij Enter, aby zadać cios: ")
                                    attempts += 1
                                    rolled_number = random.randint(1, 10)
                                
                                    if rolled_number % 2 == 0:  #Sukces, jeśli liczba parzysta
                                        successes += 1
                                        print(f"Cięcie wody! ({successes}/7)")
                                    else:  #Kolejna próba, jeśli liczba nieparzysta
                                        print(f"Nigdy mnie nie pokonasz *BUAHAHAHA*! ({successes}/7)")
                            
                            fightingFather()
                            input("Wciśnij Enter, aby przejść dalej.")
                            print("*Ah,ah* Synu czy to ty?")
                            print("Ojcze... Naprawdę nie chciałem ale nie miałem innej opcji, inaczej zniszczył byś świat.")
                            print("Dziękuje Ci synu, pamiętaj że was kochałem...")
                            print("Ojciec umiera, a ty zostajesz bohaterem...")
                            print("Czasami myślisz czy była inna opcja? Czy musiałeś zabić ojca...?")
                            print("Nigdy jednak się tego nie dowiesz...")
                            print(" ")
                            print("Dziękuje za zagranie")
                            print("FIN")
                        rockCuttingTraining()
            


    elif diceRoll == "Mag ognia":
        print("Mag ognia... Ogień w twoich oczach to dobry znak. Przygotuj się na wielkie czyny.")
        input("Nacisnij Enter aby wybrać opcję dialogową...")
        options = [
            "*Odejdź od starca nic nie mowiąc.*",
            "I co ja teraz mam zrobić? Gdzie mam iść? Kim ja tak naprawdę jestem?!",
        ]
        choice = dialogue_choice(options)
        print(f"Wybrałeś: {options[choice]}")
        print(" ")
        if options[choice] == "*Odejdź od starca nic nie mowiąc.*":
            print("Wracasz do domu z karczmy. Niczego nieświadomy idziesz spać. W nocy budzi Cię przeraźliwy krzyk matki.")
            print("Zdenerwowany wybiegasz z domu i widzisz jak cała twoja wioska płonie a żołnierze w czarnych zbrojach zmierzają w twoim kierunku...")
            print(" ")
            print(" ")
            print("KONIEC GRY")
        elif options[choice] == "I co ja teraz mam zrobić? Gdzie mam iść? Kim ja tak naprawdę jestem?!":
            print("Musisz się przygotować na trening. Nie będzie łatwo to mogę Ci zapewnić... - rzekł starzec")
            print("Za chwilę wybierzesz swoją decyzję dotyczącą treningu...")
            input("Nacisnij Enter aby wybrać opcję dialogową...")
            options = [
                    "Na żaden trening nie będę szedł, przestań bredzić *Odchodzisz od starca*",
                    "Gdzie będzie ten trening i jak szybko mam się tam udać?"
                ]
            choice = dialogue_choice(options)
            print(f"Wybrałeś: {options[choice]}")
            print(" ")
            if choice == 0:
                    print("Opuściłeś starca, nie przejmując się jego radami. Może popełniłeś błąd?")
                    print("Wracasz do domu z karczmy. Niczego nieświadomy idziesz spać. W nocy budzi Cię przeraźliwy krzyk matki.")
                    print("Zdenerwowany wybiegasz z domu i widzisz jak cała twoja wioska płonie a żołnierze w czarnych zbrojach zmierzają w twoim kierunku...")
                    print(" ")
                    print(" ")
                    print("KONIEC GRY")
            elif choice == 1:
                    print("Starzec opowiada Ci o tajemniczym miejscu, gdzie trening się odbędzie...")
                    print("Rozmowa zajeła dosłownie chwilę, bo musicie ruszać. Dowiadujesz się od starca, że twoja wioska zostanie nazajutrz spalona.")
                    print("Wracasz szybko do swojej chaty, aby zapakować najpotrzebniejsze rzeczy.")
                    print("Tłumaczysz swojej mamie, że musisz jechać, bo masz bardzo ważną misję do wypełnienia.")
                    print("Twoja matka zostaje odeskortowana do miasta daleko od twojej wioski tak, aby była bezpieczna, a ty wyruszasz w drogę.")
                    print("Razem ze starcem wsiadacie nie konie i wyruszacie na południe. Jesteś gotowy na to co przyniesie przyszłość, ale wewnętrznie odczuwasz lęk...")
                    print("Czy aby napewno sobie poradzę? Czy to własnie ja jestem tym ostatnim puzzlem układanki...?")
                    print(" ")
                    print("5 DNI PÓŹNIEJ")
                    print(" ")
                    print("Po pięciu dniach podróży przez pustynię i tropikalny las, w końcu docierasz na miejsce w którym ma zacząć się twój trening.")
                    print("Dostałeś komnatę w małym zamku nie opodal placu treningowego.")
                    print("Gdy rozpakowujesz rzeczy słyszysz pukanie do drzwi... *puk, puk*")
                    print("Kto tam? - pytasz zdziwiony.")
                    print("To ja Ferland. (imię starca, którego poznałeś w karczmie).")
                    print("Wejdź proszę! - krzyczysz z drugiego końca pokoju.")  
                    print("Jesteś gotowy na pierwszy trening Lobo?")
                    input("Nacisnij Enter aby wybrać opcję dialogową...")
                    options = [
                        "Urodziłem się gotowy starcze!",
                        "Napewno to ja mam wam pomóc? Jestem tylko zwykłym chłopakiem z wioski a nie zbawicielem"
                            ]   
                    choice = dialogue_choice(options)
                    print(f"Wybrałeś: {options[choice]}")
                    if options[choice] == "Urodziłem się gotowy starcze!":
                        print("To dobrze zbieraj się i idziemy.")
                        print(" ")
                        print("Na placu treningowym uczysz się jak opanować naturę ognia.")
                        print("Szło Ci dobrze do momentu kiedy nie przyszło do kreacji smoka z ognia.")
                        print("Na tym momencie podłamałeś się, ale zdecydowałeś się że się nie poddasz.")
                        print(" ")
                        def dragonCreationTraining():
                            successes = 0
                            attempts = 0
                            print("Rozpoczynasz trening tworzenia smoka z ognia...")
                            #Pętla która działa na takiej zasadzie, że dopóki użytkownik nie będzie miał wyniku 3/3 cały czas się zapętla.
                            while successes < 3:
                                input("Naciśnij Enter, aby spróbować stworzyć smoka: ")
                                attempts += 1
                                rolled_number = random.randint(1, 10)
                                
                                if rolled_number % 2 == 0:  #Sukces, jeśli liczba parzysta
                                    successes += 1
                                    print(f"Udało ci się stworzyć smoka! ({successes}/3)")
                                else:  #Kolejna próba, jeśli liczba nieparzysta
                                    print(f"Próbuj dalej, wojowniku! ({successes}/3)")
                            
                            print(f"\nBrawo! Udało Ci się stworzyć smoka 3 razy w {attempts} próbach!")
                            print("Jesteś teraz gotowy, aby walczyć z Zgrobem!")
                            input("Wcisnij Enter aby przejść dalej...")
                            print("Parę ciężkich treningów potem...")
                            print("Jesteś gotowy Lobo, możemy iść pokonać twojego ojca... - rzekł starzec.")
                            print("Co mojego ojca? O czym ty mówisz??? *Serce zaczyna ci bić w nierównomiernym tempie*.")
                            print("Zgrob to tak naprawdę twój ojciec. Po tym jak dołączył do naszego zakonu ciemne siły chciały przejąć jego duszę i się im udało...")
                            print("Był on najpotężniejszym z nas i jedyne czego chciał to waszego dobra ale jego umysł był na to za słaby.")
                            print("Starał się z tym walczyć ale nie był w stanie...")
                            print("Nie, nie to nie może być prawda... - powiedział Lobo")
                            print("Zbieraj się musimy ruszać... - rzekł starzec.")
                            print(" ")
                            print("Droga zajęła długo, była wycieńczająca ale aby świat istniał Lobo musi pokonać Zgroba...")
                            print(" ")
                            print("Jesteśmy, oto Góra Zagłady. Wierzymy w Ciebie Lobo musisz pokonać ojca! - odparł starzec.")
                            print("Obiecuję, że was nie zawiodę! - odarpł Lobo.")
                            input("Wciśnij Enter, żeby walczyć z ojcem!")
                            def fightingFather():
                                successes = 0
                                attempts = 0
                                print("Rozpoczynasz walkę z ojcem...")
                            
                                while successes < 7:
                                    input("Naciśnij Enter, aby zadać cios: ")
                                    attempts += 1
                                    rolled_number = random.randint(1, 10)
                                
                                    if rolled_number % 2 == 0:  #Sukces, jeśli liczba parzysta
                                        successes += 1
                                        print(f"Ognisty smok! ({successes}/7)")
                                    else:  #Kolejna próba, jeśli liczba nieparzysta
                                        print(f"Nigdy mnie nie pokonasz *BUAHAHAHA*! ({successes}/7)")
                            
                            
                            fightingFather()
                            input("Wciśnij Enter, aby przejść dalej.")
                            print("*Ah,ah* Synu czy to ty?")
                            print("Ojcze... Naprawdę nie chciałem ale nie miałem innej opcji, inaczej zniszczył byś świat.")
                            print("Dziękuje Ci synu, pamiętaj że was kochałem...")
                            print("Ojciec umiera, a ty zostajesz bohaterem...")
                            print("Czasami myślisz czy była inna opcja? Czy musiałeś zabić ojca...?")
                            print("Nigdy jednak się tego nie dowiesz...")
                            print(" ")
                            print("Dziękuje za zagranie")
                            print("FIN")
                        dragonCreationTraining()
                    elif options[choice] == "Napewno to ja mam wam pomóc? Jestem tylko zwykłym chłopakiem z wioski a nie zbawicielem":
                        print("A myślisz ze zjawiłbym się w wiosce, o której nikt nawet nie wie i błagał Cię o to abyś ze mną poszedł?")
                        print("Masz to zapisane w kartach Lobo zaufaj mi... - rzekł starzec spokojnym tonem.")
                        print("Chyba masz rację... - odparł Lobo.")
                        print("Dobra dosyć tego gadania zabieraj się do treningu!")
                        def dragonCreationTraining():
                            successes = 0
                            attempts = 0
                            print("Rozpoczynasz trening tworzenia smoka z ognia...")
                            #Pętla która działa na takiej zasadzie, że dopóki użytkownik nie będzie miał wyniku 3/3 cały czas się zapętla.
                            while successes < 3:
                                input("Naciśnij Enter, aby spróbować stworzyć smoka: ")
                                attempts += 1
                                rolled_number = random.randint(1, 10)
                                
                                if rolled_number % 2 == 0:  #Sukces, jeśli liczba parzysta
                                    successes += 1
                                    print(f"Udało ci się stworzyć smoka! ({successes}/3)")
                                else:  #Kolejna próba, jeśli liczba nieparzysta
                                    print(f"Próbuj dalej, wojowniku! ({successes}/3)")
                            
                            print(f"\nBrawo! Udało Ci się stworzyć smoka 3 razy w {attempts} próbach!")
                            print("Jesteś teraz gotowy, aby walczyć z Zgrobem!")
                            input("Wcisnij Enter aby przejść dalej...")
                            print("Parę ciężkich treningów potem...")
                            print("Jesteś gotowy Lobo, możemy iść pokonać twojego ojca... - rzekł starzec.")
                            print("Co mojego ojca? O czym ty mówisz??? *Serce zaczyna ci bić w nierównomiernym tempie*.")
                            print("Zgrob to tak naprawdę twój ojciec. Po tym jak dołączył do naszego zakonu ciemne siły chciały przejąć jego duszę i się im udało...")
                            print("Był on najpotężniejszym z nas i jedyne czego chciał to waszego dobra ale jego umysł był na to za słaby.")
                            print("Starał się z tym walczyć ale nie był w stanie...")
                            print("Nie, nie to nie może być prawda... - powiedział Lobo")
                            print("Zbieraj się musimy ruszać... - rzekł starzec.")
                            print(" ")
                            print("Droga zajęła długo, była wycieńczająca ale aby świat istniał Lobo musi pokonać Zgroba...")
                            print(" ")
                            print("Jesteśmy, oto Góra Zagłady. Wierzymy w Ciebie Lobo musisz pokonać ojca! - odparł starzec.")
                            print("Obiecuję, że was nie zawiodę! - odarpł Lobo.")
                            input("Wciśnij Enter, żeby walczyć z ojcem!")
                            def fightingFather():
                                successes = 0
                                attempts = 0
                                print("Rozpoczynasz walkę z ojcem...")
                            
                                while successes < 7:
                                    input("Naciśnij Enter, aby zadać cios: ")
                                    attempts += 1
                                    rolled_number = random.randint(1, 10)
                                
                                    if rolled_number % 2 == 0:  #Sukces, jeśli liczba parzysta
                                        successes += 1
                                        print(f"Ognisty smok! ({successes}/7)")
                                    else:  #Kolejna próba, jeśli liczba nieparzysta
                                        print(f"Nigdy mnie nie pokonasz *BUAHAHAHA*! ({successes}/7)")
                            
                            
                            fightingFather()
                            input("Wciśnij Enter, aby przejść dalej.")
                            print("*Ah,ah* Synu czy to ty?")
                            print("Ojcze... Naprawdę nie chciałem ale nie miałem innej opcji, inaczej zniszczył byś świat.")
                            print("Dziękuje Ci synu, pamiętaj że was kochałem...")
                            print("Ojciec umiera, a ty zostajesz bohaterem...")
                            print("Czasami myślisz czy była inna opcja? Czy musiałeś zabić ojca...?")
                            print("Nigdy jednak się tego nie dowiesz...")
                            print(" ")
                            print("Dziękuje za zagranie")
                            print("FIN")
                        dragonCreationTraining()
            

    elif diceRoll == "Mag ziemi":
        print("Mag ziemi... Twoja siła będzie filarem dla twoich towarzyszy.")
        input("Nacisnij Enter aby wybrać opcję dialogową...")
        options = [
            "*Odejdź od starca nic nie mowiąc.*",
            "I co ja teraz mam zrobić? Gdzie mam iść? Kim ja tak naprawdę jestem?!",
        ]
        choice = dialogue_choice(options)
        print(f"Wybrałeś: {options[choice]}")
        print(" ")
        if options[choice] == "*Odejdź od starca nic nie mowiąc.*":
            print("Wracasz do domu z karczmy. Niczego nieświadomy idziesz spać. W nocy budzi Cię przeraźliwy krzyk matki.")
            print("Zdenerwowany wybiegasz z domu i widzisz jak cała twoja wioska płonie a żołnierze w czarnych zbrojach zmierzają w twoim kierunku...")
            print(" ")
            print(" ")
            print("KONIEC GRY")
        elif options[choice] == "I co ja teraz mam zrobić? Gdzie mam iść? Kim ja tak naprawdę jestem?!":
            print("Musisz się przygotować na trening. Nie będzie łatwo to mogę ci zapewnić... - rzekł starzec")
            print("Za chwilę wybierzesz swoją decyzję dotyczącą treningu...")
            input("Nacisnij Enter aby wybrać opcję dialogową...")
            options = [
                    "Na żaden trening nie będę szedł, przestań bredzić *Odchodzisz od starca*",
                    "Gdzie będzie ten trening i jak szybko mam się tam udać?"
                ]
            choice = dialogue_choice(options)
            print(f"Wybrałeś: {options[choice]}")
            print(" ")
            if choice == 0:
                    print("Opuściłeś starca, nie przejmując się jego radami. Może popełniłeś błąd?")
                    print("Wracasz do domu z karczmy. Niczego nieświadomy idziesz spać. W nocy budzi Cię przeraźliwy krzyk matki.")
                    print("Zdenerwowany wybiegasz z domu i widzisz jak cała twoja wioska płonie a żołnierze w czarnych zbrojach zmierzają w twoim kierunku...")
                    print(" ")
                    print(" ")
                    print("KONIEC GRY")
            
            elif choice == 1:
                    print("Starzec opowiada Ci o tajemniczym miejscu, gdzie trening się odbędzie...")
                    print("Rozmowa zajeła dosłownie chwilę, bo musicie ruszać. Dowiadujesz się od starca, że twoja wioska zostanie nazajutrz spalona.")
                    print("Wracasz szybko do swojej chaty, aby zapakować najpotrzebniejsze rzeczy.")
                    print("Tłumaczysz swojej mamie, że musisz jechać, bo masz bardzo ważną misję do wypełnienia.")
                    print("Twoja matka zostaje odeskortowana do miasta daleko od twojej wioski tak, aby była bezpieczna, a ty wyruszasz w drogę.")
                    print("Razem ze starcem wsiadacie nie konie i wyruszacie na południe. Jesteś gotowy na to co przyniesie przyszłość, ale wewnętrznie odczuwasz lęk...")
                    print("Czy aby napewno sobie poradzę? Czy to własnie ja jestem tym ostatnim puzzlem układanki...?")
                    print(" ")
                    print("5 DNI PÓŹNIEJ")
                    print(" ")
                    print("Po pięciu dniach podróży przez pustynię i tropikalny las, w końcu docierasz na miejsce w którym ma zacząć się twój trening.")
                    print("Dostałeś komnatę w małym zamku nie opodal placu treningowego.")
                    print("Gdy rozpakowujesz rzeczy słyszysz pukanie do drzwi... *puk, puk*")
                    print("Kto tam? - pytasz zdziwiony.")
                    print("To ja Ferland. (imię starca, którego poznałeś w karczmie).")
                    print("Wejdź proszę! - krzyczysz z drugiego końca pokoju.")  
                    print("Jesteś gotowy na pierwszy trening Lobo?")
                    input("Nacisnij Enter aby wybrać opcję dialogową...")
                    options = [
                        "Urodziłem się gotowy starcze!",
                        "Napewno to ja mam wam pomóc? Jestem tylko zwykłym chłopakiem z wioski a nie zbawicielem"
                            ]   
                    choice = dialogue_choice(options)
                    print(f"Wybrałeś: {options[choice]}")
                    if options[choice] == "Urodziłem się gotowy starcze!":
                        print("To dobrze zbieraj się i idziemy.")
                        print(" ")
                        print("Na placu treningowym uczysz się jak opanować naturę ziemi.")
                        print("Szło Ci dobrze do momentu kiedy nie przyszło do tworzenia kamienia z piasku.")
                        print("Na tym momencie podłamałeś się, ale zdecydowałeś się że się nie poddasz.")
                        print(" ")
                        def rockCreationTraining():
                            successes = 0
                            attempts = 0
                            print("Rozpoczynasz trening przemieniania piasku w kamień...")
                            #Pętla która działa na takiej zasadzie, że dopóki użytkownik nie będzie miał wyniku 3/3 cały czas się zapętla.
                            while successes < 3:
                                input("Naciśnij Enter, aby spróbować stworzyć kamień: ")
                                attempts += 1
                                rolled_number = random.randint(1, 10)
                                
                                if rolled_number % 2 == 0:  #Sukces, jeśli liczba parzysta
                                    successes += 1
                                    print(f"Udało ci się stworzyć kamień! ({successes}/3)")
                                else:  #Kolejna próba, jeśli liczba nieparzysta
                                    print(f"Próbuj dalej, wojowniku! ({successes}/3)")
                            
                            print(f"\nBrawo! Udało Ci się stworzyć kamień 3 razy w {attempts} próbach!")
                            print("Jesteś teraz gotowy, aby walczyć z Zgrobem!")
                            input("Wcisnij Enter aby przejść dalej...")
                            print("Parę ciężkich treningów potem...")
                            print("Jesteś gotowy Lobo, możemy iść pokonać twojego ojca... - rzekł starzec.")
                            print("Co mojego ojca? O czym ty mówisz??? *Serce zaczyna ci bić w nierównomiernym tempie*.")
                            print("Zgrob to tak naprawdę twój ojciec. Po tym jak dołączył do naszego zakonu ciemne siły chciały przejąć jego duszę i się im udało...")
                            print("Był on najpotężniejszym z nas i jedyne czego chciał to waszego dobra ale jego umysł był na to za słaby.")
                            print("Starał się z tym walczyć ale nie był w stanie...")
                            print("Nie, nie to nie może być prawda... - powiedział Lobo")
                            print("Zbieraj się musimy ruszać... - rzekł starzec.")
                            print(" ")
                            print("Droga zajęła długo, była wycieńczająca ale aby świat istniał Lobo musi pokonać Zgroba...")
                            print(" ")
                            print("Jesteśmy, oto Góra Zagłady. Wierzymy w Ciebie Lobo musisz pokonać ojca! - odparł starzec.")
                            print("Obiecuję, że was nie zawiodę! - odarpł Lobo.")
                            input("Wciśnij Enter, żeby walczyć z ojcem!")
                            def fightingFather():
                                successes = 0
                                attempts = 0
                                print("Rozpoczynasz walkę z ojcem...")
                            
                                while successes < 7:
                                    input("Naciśnij Enter, aby zadać cios: ")
                                    attempts += 1
                                    rolled_number = random.randint(1, 10)
                                
                                    if rolled_number % 2 == 0:  #Sukces, jeśli liczba parzysta
                                        successes += 1
                                        print(f"Zabójczy kamień! ({successes}/7)")
                                    else:  #Kolejna próba, jeśli liczba nieparzysta
                                        print(f"Nigdy mnie nie pokonasz *BUAHAHAHA*! ({successes}/7)")
                            
                            
                            fightingFather()
                            input("Wciśnij Enter, aby przejść dalej.")
                            print("*Ah,ah* Synu czy to ty?")
                            print("Ojcze... Naprawdę nie chciałem ale nie miałem innej opcji, inaczej zniszczył byś świat.")
                            print("Dziękuje Ci synu, pamiętaj że was kochałem...")
                            print("Ojciec umiera, a ty zostajesz bohaterem...")
                            print("Czasami myślisz czy była inna opcja? Czy musiałeś zabić ojca...?")
                            print("Nigdy jednak się tego nie dowiesz...")
                            print(" ")
                            print("Dziękuje za zagranie")
                            print("FIN")
                        rockCreationTraining()
                    elif options[choice] == "Napewno to ja mam wam pomóc? Jestem tylko zwykłym chłopakiem z wioski a nie zbawicielem":
                        print("A myślisz ze zjawiłbym się w wiosce, o której nikt nawet nie wie i błagał Cię o to abyś ze mną poszedł?")
                        print("Masz to zapisane w kartach Lobo zaufaj mi... - rzekł starzec spokojnym tonem.")
                        print("Chyba masz rację... - odparł Lobo.")
                        print("Dobra dosyć tego gadania zabieraj się do treningu!")
                        def rockCreationTraining():
                            successes = 0
                            attempts = 0
                            print("Rozpoczynasz trening przemieniania piasku w kamień...")
                            #Pętla która działa na takiej zasadzie, że dopóki użytkownik nie będzie miał wyniku 3/3 cały czas się zapętla.
                            while successes < 3:
                                input("Naciśnij Enter, aby spróbować stworzyć kamień: ")
                                attempts += 1
                                rolled_number = random.randint(1, 10)
                                
                                if rolled_number % 2 == 0:  #Sukces, jeśli liczba parzysta
                                    successes += 1
                                    print(f"Udało ci się stworzyć kamień! ({successes}/3)")
                                else:  #Kolejna próba, jeśli liczba nieparzysta
                                    print(f"Próbuj dalej, wojowniku! ({successes}/3)")
                            
                            print(f"\nBrawo! Udało Ci się stworzyć kamień 3 razy w {attempts} próbach!")
                            print("Jesteś teraz gotowy, aby walczyć z Zgrobem!")
                            input("Wcisnij Enter aby przejść dalej...")
                            print("Parę ciężkich treningów potem...")
                            print("Jesteś gotowy Lobo, możemy iść pokonać twojego ojca... - rzekł starzec.")
                            print("Co mojego ojca? O czym ty mówisz??? *Serce zaczyna ci bić w nierównomiernym tempie*.")
                            print("Zgrob to tak naprawdę twój ojciec. Po tym jak dołączył do naszego zakonu ciemne siły chciały przejąć jego duszę i się im udało...")
                            print("Był on najpotężniejszym z nas i jedyne czego chciał to waszego dobra ale jego umysł był na to za słaby.")
                            print("Starał się z tym walczyć ale nie był w stanie...")
                            print("Nie, nie to nie może być prawda... - powiedział Lobo")
                            print("Zbieraj się musimy ruszać... - rzekł starzec.")
                            print(" ")
                            print("Droga zajęła długo, była wycieńczająca ale aby świat istniał Lobo musi pokonać Zgroba...")
                            print(" ")
                            print("Jesteśmy, oto Góra Zagłady. Wierzymy w Ciebie Lobo musisz pokonać ojca! - odparł starzec.")
                            print("Obiecuję, że was nie zawiodę! - odarpł Lobo.")
                            input("Wciśnij Enter, żeby walczyć z ojcem!")
                            def fightingFather():
                                successes = 0
                                attempts = 0
                                print("Rozpoczynasz walkę z ojcem...")
                            
                                while successes < 7:
                                    input("Naciśnij Enter, aby zadać cios: ")
                                    attempts += 1
                                    rolled_number = random.randint(1, 10)
                                
                                    if rolled_number % 2 == 0:  #Sukces, jeśli liczba parzysta
                                        successes += 1
                                        print(f"Zabójczy kamień! ({successes}/7)")
                                    else:  #Kolejna próba, jeśli liczba nieparzysta
                                        print(f"Nigdy mnie nie pokonasz *BUAHAHAHA*! ({successes}/7)")
                            
                            
                            fightingFather()
                            input("Wciśnij Enter, aby przejść dalej.")
                            print("*Ah,ah* Synu czy to ty?")
                            print("Ojcze... Naprawdę nie chciałem ale nie miałem innej opcji, inaczej zniszczył byś świat.")
                            print("Dziękuje Ci synu, pamiętaj że was kochałem...")
                            print("Ojciec umiera, a ty zostajesz bohaterem...")
                            print("Czasami myślisz czy była inna opcja? Czy musiałeś zabić ojca...?")
                            print("Nigdy jednak się tego nie dowiesz...")
                            print(" ")
                            print("Dziękuje za zagranie")
                            print("FIN")

                        rockCreationTraining()
            

    elif diceRoll == "Mag powietrza":
        print("Mag powietrza... Tak samo jak ojciec... Intrygujące...")
        input("Nacisnij Enter aby wybrać opcję dialogową...")
        options = [
            "*Odejdź od starca nic nie mowiąc.*",
            "Tak samo jak mój ojciec? Przecież to zwykły pijak, ktory zostawił mnie i moją matkę samych na śmierć!"
        ]
        choice = dialogue_choice(options)
        print(f"Wybrałeś: {options[choice]}")
        print(" ")
        if options[choice] == "*Odejdź od starca nic nie mowiąc.*":
            print("Wracasz do domu z karczmy. Niczego nieświadomy idziesz spać. W nocy budzi Cię przeraźliwy krzyk matki.")
            print("Zdenerwowany wybiegasz z domu i widzisz jak cała twoja wioska płonie a żołnierze w czarnych zbrojach zmierzają w twoim kierunku...")
            print(" ")
            print(" ")
            print("KONIEC GRY")
        elif options[choice] == "Tak samo jak mój ojciec? Przecież to zwykły pijak, ktory zostawił mnie i moją matkę samych na śmierć!":
            print("On was nie opuścił z własnej woli. Zmusiliśmy go do tego aby nam pomógł. Zagroziliśmy że jeśli tego nie zrobi, zabijemy was... - odparł starzec.")
            print("Że co słucham? Ty chyba sobie żartujesz! - krzyczy Lobo")
            print("Zrozumiesz to w swoim czasie ale narazie musisz udać się na trening - rzekł dziwak")
            print("Za chwilę wybierzesz swoją decyzję dotyczącą treningu...")
            input("Nacisnij Enter aby wybrać opcję dialogową...")
            
            options = [
                    "*Zabij starca*",
                    "Jeżeli to mi pomoże dostać się do ojca i odpłacić za wszystkie jego grzechy to się zgadzam."
                ]
            choice = dialogue_choice(options)
            print(f"Wybrałeś: {options[choice]}")
            print(" ")
            if choice == 0:
                    print("Ze swojej kieszeni wyjmujesz sztylet i zwinnie niczym mysz podcinasz starcowi gardło.")
                    print("Ludzie w szoku patrzą na Ciebie, a ty wybiegasz z karczmy.")
                    print("Chowasz się w pobliskim lesie ale chwilę później łapią Cię stróże prawa i trafiasz do lochów.")
                    print("Następnego dnia czarno ubrani najeźdźcy równają z ziemią całą twoją wioskę.")
                    print("Szukająć Ciebie mordują każdą osobę po kolei, nawet twoją matkę, która nie chciała zdradzić twojej lokalizacji.")
                    print("W końcu jednak Ciebie znajdują i zabijają bez żadnych skrupółów krzycząc przy tym: Mukatīdātā mara gi'ā hai! (Wybawca nie żyje!)")
                    print(" ")
                    print(" ")
                    print("KONIEC GRY")
            elif choice == 1:
                    print("Starzec opowiada Ci o tajemniczym miejscu, gdzie trening się odbędzie...")
                    print("Rozmowa zajeła dosłownie chwilę, bo musicie ruszać. Dowiadujesz się od starca, że twoja wioska zostanie nazajutrz spalona.")
                    print("Wracasz szybko do swojej chaty, aby zapakować najpotrzebniejsze rzeczy.")
                    print("Tłumaczysz swojej mamie, że musisz jechać, bo masz bardzo ważną misję do wypełnienia.")
                    print("Twoja matka zostaje odeskortowana do miasta daleko od twojej wioski tak, aby była bezpieczna, a ty wyruszasz w drogę.")
                    print("Razem ze starcem wsiadacie nie konie i wyruszacie na południe. Jesteś gotowy na to co przyniesie przyszłość, ale wewnętrznie odczuwasz lęk...")
                    print("Czy aby napewno sobie poradzę? Czy to własnie ja jestem tym ostatnim puzzlem układanki...?")
                    print(" ")
                    print("5 DNI PÓŹNIEJ")
                    print(" ")
                    print("Po pięciu dniach podróży przez pustynię i tropikalny las, w końcu docierasz na miejsce w którym ma zacząć się twój trening.")
                    print("Dostałeś komnatę w małym zamku nie opodal placu treningowego.")
                    print("Gdy rozpakowujesz rzeczy słyszysz pukanie do drzwi... *puk, puk*")
                    print("Kto tam? - pytasz zdziwiony.")
                    print("To ja Ferland. (imię starca, którego poznałeś w karczmie).")
                    print("Wejdź proszę! - krzyczysz z drugiego końca pokoju.")  
                    print("Jesteś gotowy na pierwszy trening Lobo?")
                    input("Nacisnij Enter aby wybrać opcję dialogową...")
                    options = [
                        "Urodziłem się gotowy starcze!",
                        "Napewno to ja mam wam pomóc? Jestem tylko zwykłym chłopakiem z wioski a nie zbawicielem"
                            ]   
                    choice = dialogue_choice(options)
                    print(f"Wybrałeś: {options[choice]}")
                    if options[choice] == "Urodziłem się gotowy starcze!":
                        print("To dobrze zbieraj się i idziemy.")
                        print(" ")
                        print("Na placu treningowym uczysz się jak opanować naturę powietrza.")
                        print("Szło Ci dobrze do momentu kiedy nie przyszło do tworzenia kuli powietrza.")
                        print("Na tym momencie podłamałeś się, ale zdecydowałeś się że się nie poddasz.")
                        print(" ")
                        def airballCreationTraining():
                            successes = 0
                            attempts = 0
                            print("Rozpoczynasz trening tworzenia kuli powietrza...")
                            #Pętla która działa na takiej zasadzie, że dopóki użytkownik nie będzie miał wyniku 3/3 cały czas się zapętla.
                            while successes < 3:
                                input("Naciśnij Enter, aby spróbować stworzyć kulę: ")
                                attempts += 1
                                rolled_number = random.randint(1, 10)
                                
                                if rolled_number % 2 == 0:  #Sukces, jeśli liczba parzysta
                                    successes += 1
                                    print(f"Udało ci się stworzyć kulę! ({successes}/3)")
                                else:  #Kolejna próba, jeśli liczba nieparzysta
                                    print(f"Próbuj dalej, wojowniku! ({successes}/3)")
                            
                            print(f"\nBrawo! Udało Ci się stworzyć kulę 3 razy w {attempts} próbach!")
                            print("Jesteś teraz gotowy, aby walczyć z Zgrobem!")
                            input("Wcisnij Enter aby przejść dalej...")
                            print("Parę ciężkich treningów potem...")
                            print("Jesteś gotowy Lobo, możemy iść pokonać twojego ojca... - rzekł starzec.")
                            print("Co mojego ojca? O czym ty mówisz??? *Serce zaczyna ci bić w nierównomiernym tempie*.")
                            print("Zgrob to tak naprawdę twój ojciec. Po tym jak dołączył do naszego zakonu ciemne siły chciały przejąć jego duszę i się im udało...")
                            print("Był on najpotężniejszym z nas i jedyne czego chciał to waszego dobra ale jego umysł był na to za słaby.")
                            print("Starał się z tym walczyć ale nie był w stanie...")
                            print("Nie, nie to nie może być prawda... - powiedział Lobo")
                            print("Zbieraj się musimy ruszać... - rzekł starzec.")
                            print(" ")
                            print("Droga zajęła długo, była wycieńczająca ale aby świat istniał Lobo musi pokonać Zgroba...")
                            print(" ")
                            print("Jesteśmy, oto Góra Zagłady. Wierzymy w Ciebie Lobo musisz pokonać ojca! - odparł starzec.")
                            print("Obiecuję, że was nie zawiodę! - odarpł Lobo.")
                            input("Wciśnij Enter, żeby walczyć z ojcem!")
                            def fightingFather():
                                successes = 0
                                attempts = 0
                                print("Rozpoczynasz walkę z ojcem...")
                            
                                while successes < 7:
                                    input("Naciśnij Enter, aby zadać cios: ")
                                    attempts += 1
                                    rolled_number = random.randint(1, 10)
                                
                                    if rolled_number % 2 == 0:  #Sukces, jeśli liczba parzysta
                                        successes += 1
                                        print(f"Powietrzna kula! ({successes}/7)")
                                    else:  #Kolejna próba, jeśli liczba nieparzysta
                                        print(f"Nigdy mnie nie pokonasz *BUAHAHAHA*! ({successes}/7)")
                            
                            
                            fightingFather()
                            input("Wciśnij Enter, aby przejść dalej.")
                            print("*Ah,ah* Synu czy to ty?")
                            print("Ojcze... Naprawdę nie chciałem ale nie miałem innej opcji, inaczej zniszczył byś świat.")
                            print("Dziękuje Ci synu, pamiętaj że was kochałem...")
                            print("Ojciec umiera, a ty zostajesz bohaterem...")
                            print("Czasami myślisz czy była inna opcja? Czy musiałeś zabić ojca...?")
                            print("Nigdy jednak się tego nie dowiesz...")
                            print(" ")
                            print("Dziękuje za zagranie")
                            print("FIN")
                        airballCreationTraining()
                    elif options[choice] == "Napewno to ja mam wam pomóc? Jestem tylko zwykłym chłopakiem z wioski a nie zbawicielem":
                        print("A myślisz ze zjawiłbym się w wiosce, o której nikt nawet nie wie i błagał Cię o to abyś ze mną poszedł?")
                        print("Masz to zapisane w kartach Lobo zaufaj mi... - rzekł starzec spokojnym tonem.")
                        print("Chyba masz rację... - odparł Lobo.")
                        print("Dobra dosyć tego gadania zabieraj się do treningu!")
                        def airballCreationTraining():
                            successes = 0
                            attempts = 0
                            print("Rozpoczynasz trening tworzenia kuli powietrza...")
                            #Pętla która działa na takiej zasadzie, że dopóki użytkownik nie będzie miał wyniku 3/3 cały czas się zapętla.
                            while successes < 3:
                                input("Naciśnij Enter, aby spróbować stworzyć kulę: ")
                                attempts += 1
                                rolled_number = random.randint(1, 10)
                                
                                if rolled_number % 2 == 0:  #Sukces, jeśli liczba parzysta
                                    successes += 1
                                    print(f"Udało ci się stworzyć kulę! ({successes}/3)")
                                else:  #Kolejna próba, jeśli liczba nieparzysta
                                    print(f"Próbuj dalej, wojowniku! ({successes}/3)")
                            
                            print(f"\nBrawo! Udało Ci się stworzyć kulę 3 razy w {attempts} próbach!")
                            print("Jesteś teraz gotowy, aby walczyć z Zgrobem!")
                            input("Wcisnij Enter aby przejść dalej...")
                            print("Parę ciężkich treningów potem...")
                            print("Jesteś gotowy Lobo, możemy iść pokonać twojego ojca... - rzekł starzec.")
                            print("Co mojego ojca? O czym ty mówisz??? *Serce zaczyna ci bić w nierównomiernym tempie*.")
                            print("Zgrob to tak naprawdę twój ojciec. Po tym jak dołączył do naszego zakonu ciemne siły chciały przejąć jego duszę i się im udało...")
                            print("Był on najpotężniejszym z nas i jedyne czego chciał to waszego dobra ale jego umysł był na to za słaby.")
                            print("Starał się z tym walczyć ale nie był w stanie...")
                            print("Nie, nie to nie może być prawda... - powiedział Lobo")
                            print("Zbieraj się musimy ruszać... - rzekł starzec.")
                            print(" ")
                            print("Droga zajęła długo, była wycieńczająca ale aby świat istniał Lobo musi pokonać Zgroba...")
                            print(" ")
                            print("Jesteśmy, oto Góra Zagłady. Wierzymy w Ciebie Lobo musisz pokonać ojca! - odparł starzec.")
                            print("Obiecuję, że was nie zawiodę! - odarpł Lobo.")
                            input("Wciśnij Enter, żeby walczyć z ojcem!")
                            def fightingFather():
                                successes = 0
                                attempts = 0
                                print("Rozpoczynasz walkę z ojcem...")
                            
                                while successes < 7:
                                    input("Naciśnij Enter, aby zadać cios: ")
                                    attempts += 1
                                    rolled_number = random.randint(1, 10)
                                
                                    if rolled_number % 2 == 0:  #Sukces, jeśli liczba parzysta
                                        successes += 1
                                        print(f"Powietrzna kula! ({successes}/7)")
                                    else:  #Kolejna próba, jeśli liczba nieparzysta
                                        print(f"Nigdy mnie nie pokonasz *BUAHAHAHA*! ({successes}/7)")
                            
                            
                            fightingFather()
                            input("Wciśnij Enter, aby przejść dalej.")
                            print("*Ah,ah* Synu czy to ty?")
                            print("Ojcze... Naprawdę nie chciałem ale nie miałem innej opcji, inaczej zniszczył byś świat.")
                            print("Dziękuje Ci synu, pamiętaj że was kochałem...")
                            print("Ojciec umiera, a ty zostajesz bohaterem...")
                            print("Czasami myślisz czy była inna opcja? Czy musiałeś zabić ojca...?")
                            print("Nigdy jednak się tego nie dowiesz...")
                            print(" ")
                            print("Dziękuje za zagranie")
                            print("FIN")
                        airballCreationTraining()

    elif diceRoll == "Mag 4 żywiołów":
        print("*Kostka zaczyna się kręcić w niepowstrzymanej pętli*. Jesteś naszą ostatnią nadzieją!")
        input("Nacisnij Enter aby wybrać opcję dialogową...")
        options = [
            "*Odejdź od starca nic nie mowiąc.*",
            "Ostatnią nadzieją? O czym ty w ogóle mówisz?"
        ]
        choice = dialogue_choice(options)
        print(f"Wybrałeś: {options[choice]}")
        print(" ")
        if options[choice] == "*Odejdź od starca nic nie mowiąc.*":
            print("Wracasz do domu z karczmy. Niczego nieświadomy idziesz spać. W nocy budzi Cię przeraźliwy krzyk matki.")
            print("Zdenerwowany wybiegasz z domu i widzisz jak cała twoja wioska płonie a żołnierze w czarnych zbrojach zmierzają w twoim kierunku...")
            print(" ")
            print(" ")
            print("KONIEC GRY")
        elif options[choice] == "Ostatnią nadzieją? O czym ty w ogóle mówisz?":
            print("Nie mam teraz czasu żeby Ci to tłumaczyć. Błagam zaufaj mi, musimy wyjechać abyś zdążył z treningiem! - rzekł starzec")
            print("Za chwilę wybierzesz swoją decyzję dotyczącą treningu...")
            input("Nacisnij Enter aby wybrać opcję dialogową...")
            options = [
                    "Na żaden trening nie będę szedł, przestań bredzić *Odchodzisz od starca*",
                    "Powiedzmy że Ci ufam. Gdzie będzie ten trening i jak szybko mam się tam udać?"
                ]
            choice = dialogue_choice(options)
            print(f"Wybrałeś: {options[choice]}")
            print(" ")
            if choice == 0:
                    print("Opuściłeś starca, nie przejmując się jego radami.")
                    print("Wracasz do domu z karczmy. Niczego nieświadomy idziesz spać. W nocy budzi Cię przeraźliwy krzyk matki.")
                    print("Zdenerwowany wybiegasz z domu i widzisz jak cała twoja wioska płonie a żołnierze w czarnych zbrojach zmierzają w twoim kierunku...")
                    print(" ")
                    print(" ")
                    print("KONIEC GRY")
            elif choice == 1:
                    print("Starzec opowiada Ci o tajemniczym miejscu, gdzie trening się odbędzie...")
                    print("Rozmowa zajeła dosłownie chwilę, bo musicie ruszać. Dowiadujesz się od starca, że twoja wioska zostanie nazajutrz spalona.")
                    print("Wracasz szybko do swojej chaty, aby zapakować najpotrzebniejsze rzeczy.")
                    print("Tłumaczysz swojej mamie, że musisz jechać, bo masz bardzo ważną misję do wypełnienia.")
                    print("Twoja matka zostaje odeskortowana do miasta daleko od twojej wioski tak, aby była bezpieczna, a ty wyruszasz w drogę.")
                    print("Razem ze starcem wsiadacie nie konie i wyruszacie na południe. Jesteś gotowy na to co przyniesie przyszłość, ale wewnętrznie odczuwasz lęk...")
                    print("Czy aby napewno sobie poradzę? Czy to własnie ja jestem tym ostatnim puzzlem układanki...?")
                    print(" ")
                    print("5 DNI PÓŹNIEJ")
                    print(" ")
                    print("Po pięciu dniach podróży przez pustynię i tropikalny las, w końcu docierasz na miejsce w którym ma zacząć się twój trening.")
                    print("Dostałeś komnatę w małym zamku nie opodal placu treningowego.")
                    print("Gdy rozpakowujesz rzeczy słyszysz pukanie do drzwi... *puk, puk*")
                    print("Kto tam? - pytasz zdziwiony.")
                    print("To ja Ferland. (imię starca, którego poznałeś w karczmie).")
                    print("Wejdź proszę! - krzyczysz z drugiego końca pokoju.")  
                    print("Jesteś gotowy na pierwszy trening Lobo?")
                    input("Nacisnij Enter aby wybrać opcję dialogową...")
                    options = [
                        "Urodziłem się gotowy starcze!",
                        "Napewno to ja mam wam pomóc? Jestem tylko zwykłym chłopakiem z wioski a nie zbawicielem"
                            ]   
                    choice = dialogue_choice(options)
                    print(f"Wybrałeś: {options[choice]}")
                    if options[choice] == "Urodziłem się gotowy starcze!":
                        print("To dobrze zbieraj się i idziemy.")
                        print(" ")
                        print("Na placu treningowym uczysz się jak opanować naturę ziemi.")
                        print("Szło Ci dobrze do momentu kiedy nie przyszło do tworzenia golema 4 żywiołów.")
                        print("Na tym momencie podłamałeś się, ale zdecydowałeś się że się nie poddasz.")
                        print(" ")
                        def golemCreationTraining():
                            successes = 0
                            attempts = 0
                            print("Rozpoczynasz trening tworzenia golema 4 żywiołów...")
                            #Pętla która działa na takiej zasadzie, że dopóki użytkownik nie będzie miał wyniku 3/3 cały czas się zapętla.
                            while successes < 3:
                                input("Naciśnij Enter, aby spróbować stworzyć golema: ")
                                attempts += 1
                                rolled_number = random.randint(1, 10)
                                
                                if rolled_number % 2 == 0:  #Sukces, jeśli liczba parzysta
                                    successes += 1
                                    print(f"Udało ci się stworzyć golema! ({successes}/3)")
                                else:  #Kolejna próba, jeśli liczba nieparzysta
                                    print(f"Próbuj dalej, wojowniku! ({successes}/3)")
                            
                            print(f"\nBrawo! Udało Ci się stworzyć golema 3 razy w {attempts} próbach!")
                            print("Jesteś teraz gotowy, aby walczyć z Zgrobem!")
                            input("Wcisnij Enter aby przejść dalej...")
                            print("Parę ciężkich treningów potem...")
                            print("Jesteś gotowy Lobo, możemy iść pokonać twojego ojca... - rzekł starzec.")
                            print("Co mojego ojca? O czym ty mówisz??? *Serce zaczyna ci bić w nierównomiernym tempie*.")
                            print("Zgrob to tak naprawdę twój ojciec. Po tym jak dołączył do naszego zakonu ciemne siły chciały przejąć jego duszę i się im udało...")
                            print("Był on najpotężniejszym z nas i jedyne czego chciał to waszego dobra ale jego umysł był na to za słaby.")
                            print("Starał się z tym walczyć ale nie był w stanie...")
                            print("Nie, nie to nie może być prawda... - powiedział Lobo")
                            print("Zbieraj się musimy ruszać... - rzekł starzec.")
                            print(" ")
                            print("Droga zajęła długo, była wycieńczająca ale aby świat istniał Lobo musi pokonać Zgroba...")
                            print(" ")
                            print("Jesteśmy, oto Góra Zagłady. Wierzymy w Ciebie Lobo musisz pokonać ojca! - odparł starzec.")
                            print("Obiecuję, że was nie zawiodę! - odarpł Lobo.")
                            input("Wciśnij Enter, żeby walczyć z ojcem!")
                            def fightingFather():
                                successes = 0
                                attempts = 0
                                print("Rozpoczynasz walkę z ojcem...")
                            
                                while successes < 7:
                                    input("Naciśnij Enter, aby zadać cios: ")
                                    attempts += 1
                                    rolled_number = random.randint(1, 10)
                                
                                    if rolled_number % 2 == 0:  #Sukces, jeśli liczba parzysta
                                        successes += 1
                                        print(f"Uderzaj golemie! ({successes}/7)")
                                    else:  #Kolejna próba, jeśli liczba nieparzysta
                                        print(f"Nigdy mnie nie pokonasz *BUAHAHAHA*! ({successes}/7)")
                            
                            
                            fightingFather()
                            input("Wciśnij Enter, aby przejść dalej.")
                            print("*Ah,ah* Synu czy to ty?")
                            print("Ojcze... Naprawdę nie chciałem ale nie miałem innej opcji, inaczej zniszczył byś świat.")
                            print("Dziękuje Ci synu, pamiętaj że was kochałem...")
                            print("Ojciec umiera, a ty zostajesz bohaterem...")
                            print("Czasami myślisz czy była inna opcja? Czy musiałeś zabić ojca...?")
                            print("Nigdy jednak się tego nie dowiesz...")
                            print(" ")
                            print("Dziękuje za zagranie")
                            print("FIN")
                        golemCreationTraining()
                    elif options[choice] == "Napewno to ja mam wam pomóc? Jestem tylko zwykłym chłopakiem z wioski a nie zbawicielem":
                        print("A myślisz ze zjawiłbym się w wiosce, o której nikt nawet nie wie i błagał Cię o to abyś ze mną poszedł?")
                        print("Masz to zapisane w kartach Lobo zaufaj mi... - rzekł starzec spokojnym tonem.")
                        print("Chyba masz rację... - odparł Lobo.")
                        print("Dobra dosyć tego gadania zabieraj się do treningu!")
                        def golemCreationTraining():
                            successes = 0
                            attempts = 0
                            print("Rozpoczynasz trening tworzenia golema 4 żywiołów...")
                            #Pętla która działa na takiej zasadzie, że dopóki użytkownik nie będzie miał wyniku 3/3 cały czas się zapętla.
                            while successes < 3:
                                input("Naciśnij Enter, aby spróbować stworzyć golema: ")
                                attempts += 1
                                rolled_number = random.randint(1, 10)
                                
                                if rolled_number % 2 == 0:  #Sukces, jeśli liczba parzysta
                                    successes += 1
                                    print(f"Udało ci się stworzyć golema! ({successes}/3)")
                                else:  #Kolejna próba, jeśli liczba nieparzysta
                                    print(f"Próbuj dalej, wojowniku! ({successes}/3)")
                            
                            print(f"\nBrawo! Udało Ci się stworzyć golema  3 razy w {attempts} próbach!")
                            print("Jesteś teraz gotowy, aby walczyć z Zgrobem!")
                            input("Wcisnij Enter aby przejść dalej...")
                            print("Parę ciężkich treningów potem...")
                            print("Jesteś gotowy Lobo, możemy iść pokonać twojego ojca... - rzekł starzec.")
                            print("Co mojego ojca? O czym ty mówisz??? *Serce zaczyna ci bić w nierównomiernym tempie*.")
                            print("Zgrob to tak naprawdę twój ojciec. Po tym jak dołączył do naszego zakonu ciemne siły chciały przejąć jego duszę i się im udało...")
                            print("Był on najpotężniejszym z nas i jedyne czego chciał to waszego dobra ale jego umysł był na to za słaby.")
                            print("Starał się z tym walczyć ale nie był w stanie...")
                            print("Nie, nie to nie może być prawda... - powiedział Lobo")
                            print("Zbieraj się musimy ruszać... - rzekł starzec.")
                            print(" ")
                            print("Droga zajęła długo, była wycieńczająca ale aby świat istniał Lobo musi pokonać Zgroba...")
                            print(" ")
                            print("Jesteśmy, oto Góra Zagłady. Wierzymy w Ciebie Lobo musisz pokonać ojca! - odparł starzec.")
                            print("Obiecuję, że was nie zawiodę! - odarpł Lobo.")
                            input("Wciśnij Enter, żeby walczyć z ojcem!")
                            def fightingFather():
                                successes = 0
                                attempts = 0
                                print("Rozpoczynasz walkę z ojcem...")
                            
                                while successes < 7:
                                    input("Naciśnij Enter, aby zadać cios: ")
                                    attempts += 1
                                    rolled_number = random.randint(1, 10)
                                
                                    if rolled_number % 2 == 0:  #Sukces, jeśli liczba parzysta
                                        successes += 1
                                        print(f"Uderzaj golemie! ({successes}/7)")
                                    else:  #Kolejna próba, jeśli liczba nieparzysta
                                        print(f"Nigdy mnie nie pokonasz *BUAHAHAHA*! ({successes}/7)")
                            
                            
                            fightingFather()
                            input("Wciśnij Enter, aby przejść dalej.")
                            print("*Ah,ah* Synu czy to ty?")
                            print("Ojcze... Naprawdę nie chciałem ale nie miałem innej opcji, inaczej zniszczył byś świat.")
                            print("Dziękuje Ci synu, pamiętaj że was kochałem...")
                            print("Ojciec umiera, a ty zostajesz bohaterem...")
                            print("Czasami myślisz czy była inna opcja? Czy musiałeś zabić ojca...?")
                            print("Nigdy jednak się tego nie dowiesz...")
                            print(" ")
                            print("Dziękuje za zagranie")
                            print("FIN")
                        golemCreationTraining()
            
        
    else:
        print("Coś poszło nie tak...")

#Główna fabuła
def main():
    print("Przygody Lobo")
    print("Historia zaczyna się w odległej mieścinie Ofelpain, położonej w Nowej Zelandi - rok nieznany.")
    print("Główny bohater Lobo to zwyczajny chłopak, którego wychowywała samotna matka.")
    print("Nigdy nie miała za dużo pieniędzy. Jedni by powiedzieli, że to lenistwo, natomiast drudzy że nieszczęście w życiu doprowadziło ją do miejsca, w którym obecnie się znajduję.")
    print("Lobo cechował się wysoką inteligencją, jednakże jego praca pasterza nie pozwalała mu rozwijać ambicji.")
    print("Pewnego wieczoru w karczmie, gdzie jak co piątek siedział przy piwie i jadle, dosiadł się do niego tajemniczy nieznajomy.")
    print("Chłopak był do tego przyzwyczajony, bo już nie raz odganiał pijaczków z karczmy. Myślał, że w tym przypadku będzie tak samo, jednak nie wiedział jeszcze co go czeka.")
    print("Zakapturzony, starszy mężczyzna, który na oko wyglądał jak wszyscy dziwacy, którzy wierzyli w magię, głośno chrząknął tak, aby Lobo na niego spojrzał: ")
    print("Musisz rzucić tą kostką, zaufaj mi nic złego ci się nie stanie. - ze łzami w oczach powiedział dziwak.")
    input("Naciśnij Enter, aby rzucić kostką...")
    diceThrowMain()

main()




