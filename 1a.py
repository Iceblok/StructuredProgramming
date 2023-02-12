'''======Yunus Coskun======'''



'''Opdracht 1 - Piramide'''
def piramide_met_for_loops(omgekeerd=False):
    piramide = int(input('Hoe groot? '))
    if not omgekeerd:
        for i in range(1, piramide):
            print(i*'*')
        for i in range(piramide, 0, -1):
            print(i*'*')
    if omgekeerd:
        for i in range(piramide, 1, -1):
            string = f"{(i-1)*' '}*"
            if len(string) != piramide:
                string += '*' * (piramide-len(string))
            print(string)
        for i in range(0, piramide):
            string = f"{i*' '}*"
            if len(string) != piramide:
                string += '*' * (piramide-len(string))
            print(string)


# piramide_met_for_loops()
# piramide_met_for_loops(True)


def piramide_met_while_loops(omgekeerd=False):
    piramide = int(input('Hoe groot? '))
    if not omgekeerd:
        counter = 0
        while counter != piramide:
            counter += 1
            print(f"{counter*'*'}")
        counter = piramide
        while counter != 1:
            counter -= 1
            print(f"{counter*'*'}")
    if omgekeerd:
        counter = 0
        while counter != piramide-1:
            counter += 1
            string = f"{counter*'*'}"
            if len(string) != 5:
                string = ' '*(piramide-len(string)) + string
            print(string)
        counter = 0
        while counter != piramide:
            counter += 1
            string = f"{(counter-1)*' '}*"
            if len(string) != piramide:
                string += '*' * (piramide-len(string))
            print(string)



# piramide_met_while_loops()
# piramide_met_while_loops(True)


'''Opdracht 2 - Tekstcheck'''
def verschil_zoeken():
    eerste_string = input('Geef een string: ')
    tweede_string = input('Geef een string: ')
    if len(eerste_string) <= len(tweede_string):
        verschil_vanaf = [i for i in range(len(eerste_string)) if eerste_string[i] != tweede_string[i]]
        return verschil_vanaf[0]
    else:
        verschil_vanaf = [i for i in range(len(tweede_string)) if tweede_string[i] != eerste_string[i]]
        return verschil_vanaf[0]


# print(verschil_zoeken())


'''Opdracht 3 - Lijstcheck'''
def count(counterlist, count):
    lijst = counterlist
    counter = 0
    for i in lijst:
        if i == count:
            counter += 1
    return counter
    # aantal_geteld = lijst.count(count)
    # return aantal_geteld

# print(count([1,1,1,1,1], 1))

def biggest_difference(lst):
    lijst = lst
    verschillen = []
    for i in range(len(lijst)-1):
        verschil = lijst[i+1] - lijst[i]
        verschillen.append(verschil)
    return max(verschillen)


def check_list(lst):
    lijst = lst
    if count(lijst, 0) > 12:
        return 'Er mogen niet meer dan 12 nullen zijn.'
    return count(lijst, 1) > count(lijst, 0)


# print(check_list([1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))


'''Opdracht 4 - Palindroom'''
def palindroom1(woord):
    return "".join(reversed(woord)) == woord


# print(palindroom1('hallo'))

def palindroom2(woord):
    string = ''
    for i in woord:
        string = i + string
    return string == woord


# print(palindroom2('kok'))


'''Opdracht 5 - Sorteren'''
def sort(lst):
    lst_sorted = lst
    niet_klaar = True

    while niet_klaar:
        niet_klaar = False
        for i in range(len(lst_sorted) - 1):
            if lst_sorted[i] > lst_sorted[i + 1]:
                lst_sorted[i], lst_sorted[i + 1] = lst_sorted[i + 1], lst_sorted[i]
                niet_klaar = True
    return lst_sorted


# print(sort([2,1,6,7,3,0]))






