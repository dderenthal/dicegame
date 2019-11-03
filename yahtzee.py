import random as ra

class roll:

    def view(self):
        if self.num == 1 : print(' ______\n|      |\n|   *  |\n|______|')
        if self.num == 2 : print(' ______\n| *    |\n|      |\n|____*_|')
        if self.num == 3 : print(' ______\n| *    |\n|   *  |\n|_____*|')
        if self.num == 4 : print(' ______\n| *   *|\n|      |\n|_*___*|')
        if self.num == 5 : print(' ______\n| *   *|\n|   *  |\n|_*___*|')
        if self.num == 6 : print(' ______\n| *   *|\n| *   *|\n|_*___*|')

d1 = roll()
d2 = roll()
d3 = roll()
d4 = roll()
d5 = roll()
d6 = roll()

print('\n\nWelcome to Yahtzee!')

d1.num = 0
d2.num = 0
d3.num = 0
d4.num = 0
d5.num = 0

# upper scoring section
aces = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0
aces_use = ' '
twos_use = ' '
threes_use = ' '
fours_use = ' '
fives_use = ' '
sixes_use = ' '
up_bonus = 0


# lower scoring section
threekind = 0
fourkind = 0
fullhouse = 0
sm_str4 = 0
l_str5 = 0
yaht = 0
chance = 0
threekind_use = ' '
fourkind_use = ' '
fullhouse_use = ' '
sm_str4_use = ' '
l_str5_use = ' '
yaht_use = ' '
chance_use = ' '
yaht_b1 = 'no'
yaht_b2 = 'no'
yaht_b3 = 'no'
yaht_bonus_tot = 0

start = input('\n... press enter to start')
round = 1

while round < 14 :

    d1.num = ra.randint(1,6)
    d2.num = ra.randint(1,6)
    d3.num = ra.randint(1,6)
    d4.num = ra.randint(1,6)
    d5.num = ra.randint(1,6)

    print('\nROLL 1')
    d1.view()
    d2.view()
    d3.view()
    d4.view()
    d5.view()
    print('\ndie1: ', d1.num, '\tdie2: ', d2.num, '\tdie3: ', d3.num, '\tdice4: ', d4.num, '\tdice5: ', d5.num)
    print('\nSCORE SHEET')
    print('1- Aces (1 total): ', aces, aces_use)
    print('2- Twos (2 total): ', twos, twos_use)
    print('3- Threes (3 total): ', threes, threes_use)
    print('4- Fours (4 total): ', fours, fours_use)
    print('5- Fives (5 total): ', fives, fives_use)
    print('6- Sixes (6 total): ', sixes, sixes_use)
    print('7- 3 of a kind: ', threekind, threes_use)
    print('8- 4 of a kind: ', fourkind, fourkind_use)
    print('9- Full House (2 & 3 of a kind): ', fullhouse, fullhouse_use)
    print('10- Small Straight (4 in order): ', sm_str4, sm_str4_use)
    print('11- Long Straight (5 in order): ', l_str5, l_str5_use)
    print('12- Yahtzee (5 of a kind): ', yaht, yaht_use)
    print('13- Chance (any combo): ', chance, chance_use)

    print('\nChoose dice to roll again... (d for done)')
    choice1 = 0
    while choice1 != 'd' :
        choice1 = input('Enter die number: ')
        die_assign = 'd' + choice1
        if die_assign == 'd1' :
            d1.num = ra.randint(1,6)
        if die_assign == 'd2' :
            d2.num = ra.randint(1,6)
        if die_assign == 'd3' :
            d3.num = ra.randint(1,6)
        if die_assign == 'd4' :
            d4.num = ra.randint(1,6)
        if die_assign == 'd5' :
            d5.num = ra.randint(1,6)

    print('\nROLL 2')
    d1.view()
    d2.view()
    d3.view()
    d4.view()
    d5.view()
    print('\ndie1: ', d1.num, '\tdie2: ', d2.num, '\tdie3: ', d3.num, '\tdice4: ', d4.num, '\tdice5: ', d5.num)
    print('\nSCORE SHEET')
    print('1- Aces (1 total): ', aces, aces_use)
    print('2- Twos (2 total): ', twos, twos_use)
    print('3- Threes (3 total): ', threes, threes_use)
    print('4- Fours (4 total): ', fours, fours_use)
    print('5- Fives (5 total): ', fives, fives_use)
    print('6- Sixes (6 total): ', sixes, sixes_use)
    print('7- 3 of a kind: ', threekind, threes_use)
    print('8- 4 of a kind: ', fourkind, fourkind_use)
    print('9- Full House (2 & 3 of a kind): ', fullhouse, fullhouse_use)
    print('10- Small Straight (4 in order): ', sm_str4, sm_str4_use)
    print('11- Long Straight (5 in order): ', l_str5, l_str5_use)
    print('12- Yahtzee (5 of a kind): ', yaht, yaht_use)
    print('13- Chance (any combo): ', chance, chance_use)

    print('\nChoose dice to roll again... (d for done)')
    choice2 = 0
    while choice2 != 'd' :
        choice2 = input('Enter die number: ')
        die_assign = 'd' + choice2
        if die_assign == 'd1' :
            d1.num = ra.randint(1,6)
        if die_assign == 'd2' :
            d2.num = ra.randint(1,6)
        if die_assign == 'd3' :
            d3.num = ra.randint(1,6)
        if die_assign == 'd4' :
            d4.num = ra.randint(1,6)
        if die_assign == 'd5' :
            d5.num = ra.randint(1,6)

    print('\nROLL 3')
    d1.view()
    d2.view()
    d3.view()
    d4.view()
    d5.view()
    print('\ndie1: ', d1.num, '\tdie2: ', d2.num, '\tdie3: ', d3.num, '\tdie4: ', d4.num, '\tdie5: ', d5.num)

    print('\nChoose a scoring box for this round...')
    print('\nSCORE SHEET')
    print('1- Aces (1 total): ', aces, aces_use)
    print('2- Twos (2 total): ', twos, twos_use)
    print('3- Threes (3 total): ', threes, threes_use)
    print('4- Fours (4 total): ', fours, fours_use)
    print('5- Fives (5 total): ', fives, fives_use)
    print('6- Sixes (6 total): ', sixes, sixes_use)
    print('7- 3 of a kind: ', threekind, threes_use)
    print('8- 4 of a kind: ', fourkind, fourkind_use)
    print('9- Full House (2 & 3 of a kind): ', fullhouse, fullhouse_use)
    print('10- Small Straight (4 in order): ', sm_str4, sm_str4_use)
    print('11- Long Straight (5 in order): ', l_str5, l_str5_use)
    print('12- Yahtzee (5 of a kind): ', yaht, yaht_use)
    print('13- Chance (any combo): ', chance, chance_use)

    box = input('Enter box assignment number: ')

    if box == '1' :
        aces = 0
        if d1.num == 1 : aces += 1
        if d2.num == 1 : aces += 1
        if d3.num == 1 : aces += 1
        if d4.num == 1 : aces += 1
        if d5.num == 1 : aces += 1
        aces_use = '*'
    if box == '2' :
        twos = 0
        if d1.num == 2 : twos += 2
        if d2.num == 2 : twos += 2
        if d3.num == 2 : twos += 2
        if d4.num == 2 : twos += 2
        if d5.num == 2 : twos += 2
        twos_use = '*'
    if box == '3' :
        threes = 0
        if d1.num == 3 : threes += 3
        if d2.num == 3 : threes += 3
        if d3.num == 3 : threes += 3
        if d4.num == 3 : threes += 3
        if d5.num == 3 : threes += 3
        threes_use = '*'
    if box == '4' :
        fours = 0
        if d1.num == 4 : fours += 4
        if d2.num == 4 : fours += 4
        if d3.num == 4 : fours += 4
        if d4.num == 4 : fours += 4
        if d5.num == 4 : fours += 4
        fours_use = '*'
    if box == '5' :
        fives = 0
        if d1.num == 5 : fives += 5
        if d2.num == 5 : fives += 5
        if d3.num == 5 : fives += 5
        if d4.num == 5 : fives += 5
        if d5.num == 5 : fives += 5
        fives_use = '*'
    if box == '6' :
        sixes = 0
        if d1.num == 6 : sixes += 6
        if d2.num == 6 : sixes += 6
        if d3.num == 6 : sixes += 6
        if d4.num == 6 : sixes += 6
        if d5.num == 6 : sixes += 6
        sixes_use = '*'
    if box == '7' :
        threekind = 0
        if d1.num == d2.num == d3.num : threekind = d1.num + d2.num + d3.num + d4.num + d5.num
        if d2.num == d3.num == d4.num : threekind = d1.num + d2.num + d3.num + d4.num + d5.num
        if d3.num == d4.num == d5.num : threekind = d1.num + d2.num + d3.num + d4.num + d5.num
        if d1.num == d3.num == d4.num : threekind = d1.num + d2.num + d3.num + d4.num + d5.num
        if d1.num == d4.num == d5.num : threekind = d1.num + d2.num + d3.num + d4.num + d5.num
        if d2.num == d4.num == d5.num : threekind = d1.num + d2.num + d3.num + d4.num + d5.num
        if d1.num == d2.num == d4.num : threekind = d1.num + d2.num + d3.num + d4.num + d5.num
        if d1.num == d2.num == d5.num : threekind = d1.num + d2.num + d3.num + d4.num + d5.num
        if d1.num == d3.num == d5.num : threekind = d1.num + d2.num + d3.num + d4.num + d5.num
        if d2.num == d3.num == d5.num : threekind = d1.num + d2.num + d3.num + d4.num + d5.num
        threekind_use = '*'
    if box == '8' :
        fourkind = 0
        if d1.num == d2.num == d3.num == d4.num : fourkind = d1.num + d2.num + d3.num + d4.num + d5.num
        if d1.num == d2.num == d3.num == d5.num : fourkind = d1.num + d2.num + d3.num + d4.num + d5.num
        if d1.num == d2.num == d4.num == d5.num : fourkind = d1.num + d2.num + d3.num + d4.num + d5.num
        if d1.num == d3.num == d4.num == d5.num : fourkind = d1.num + d2.num + d3.num + d4.num + d5.num
        if d2.num == d3.num == d4.num == d5.num : fourkind = d1.num + d2.num + d3.num + d4.num + d5.num
        fourkind_use = '*'
    if box == '9' :
        fullhouse = 0
        if d1.num == d2.num == d3.num and d4.num == d5.num : fullhouse = 25
        if d2.num == d3.num == d4.num and d1.num == d5.num : fullhouse = 25
        if d3.num == d4.num == d5.num and d1.num == d2.num : fullhouse = 25
        if d1.num == d3.num == d4.num and d2.num == d5.num : fullhouse = 25
        if d1.num == d4.num == d5.num and d2.num == d3.num : fullhouse = 25
        if d2.num == d4.num == d5.num and d1.num == d3.num : fullhouse = 25
        if d1.num == d2.num == d4.num and d3.num == d5.num : fullhouse = 25
        if d1.num == d2.num == d5.num and d3.num == d4.num : fullhouse = 25
        if d1.num == d3.num == d5.num and d2.num == d4.num : fullhouse = 25
        if d2.num == d3.num == d5.num and d1.num == d4.num : fullhouse = 25
        fullhouse_use = '*'
    if box == '10' :
        sm_str4 = 0
        pot_str = [d1.num, d2.num, d3.num, d4.num, d5.num]
        unique = []
        for i in pot_str :
            if i not in unique:
                unique.append(i)
        sort_unique = sorted(unique)
        str4_a = [1, 2, 3, 4]
        str4_b = [2, 3, 4, 5]
        str4_c = [3, 4, 5, 6]
        if sort_unique == str4_a or sort_unique == str4_b or sort_unique == str4_c : sm_str4 = 30
        sm_str4_use = '*'
    if box == '11' :
        l_str5 = 0
        pot_str = [d1.num, d2.num, d3.num, d4.num, d5.num]
        unique = []
        for i in pot_str :
            if i not in unique:
                unique.append(i)
        sort_unique = sorted(unique)
        str5a = [1, 2, 3, 4, 5]
        str5b = [2, 3, 4, 5, 6]
        if sort_unique == str5a or sort_unique == str5b : l_str5 = 40
        l_str5_use = '*'
    if box == '12' :
        yaht = 0
        if d1.num == d2.num == d3.num == d4.num == d5.num : yaht = 50
        yaht_use = '*'
    if box == '13' :
        chance = d1.num + d2.num + d3.num + d4.num + d5.num
        chance_use = '*'

    box = 0

    round += 1

up_total = aces + twos + threes + fours + fives + sixes
if up_total >= 63 :
    up_bonus = 35
up_total_fin = up_total + up_bonus

if yaht_b1 == 'yes' : yaht_bonus_tot += 100
if yaht_b2 == 'yes' : yaht_bonus_tot += 100
if yaht_b3 == 'yes' : yaht_bonus_tot += 100

low_total = threekind + fourkind + fullhouse + sm_str4 + l_str5 + yaht + chance + yaht_bonus_tot
grand_total = up_total_fin + low_total

print('\nFinal Score...')
print('\nSCORE SHEET')
print('1- Aces (1 total): ', aces, aces_use)
print('2- Twos (2 total): ', twos, twos_use)
print('3- Threes (3 total): ', threes, threes_use)
print('4- Fours (4 total): ', fours, fours_use)
print('5- Fives (5 total): ', fives, fives_use)
print('6- Sixes (6 total): ', sixes, sixes_use)
print('7- 3 of a kind: ', threekind, threes_use)
print('8- 4 of a kind: ', fourkind, fourkind_use)
print('9- Full House (2 & 3 of a kind): ', fullhouse, fullhouse_use)
print('10- Small Straight (4 in order): ', sm_str4, sm_str4_use)
print('11- Long Straight (5 in order): ', l_str5, l_str5_use)
print('12- Yahtzee (5 of a kind): ', yaht, yaht_use)
print('13- Chance (any combo): ', chance, chance_use)
print('\nGRAND TOTAL: ', grand_total)
