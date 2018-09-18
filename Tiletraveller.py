#Player start at 1,1
#After each move selected by player
#Print the players travel options - if there is a open wall that direction is written as possible direction

#1,1 => N
#1,2 => N and E and S
#1,3 => S and E
#2,1 => N
#2,2 => S and W
#2,3 => E and W
#3,1 => N
#3,2 => N and S
#3,3 => S and W

#If invalid direction is entered print "Not a valid direction"

#Tile 3,1 is victory location: When entered player is notified of their victory and quit running

#a = fyrri talan og b = seinni talan

#n => a + 0 
#n => b + 1
#e => a + 1
#e => b + 0
#s => a - 0
#s => b - 1
#w => a - 1
#w => b - 0 

north = '(N)orth'
east = '(E)ast'
west = '(W)est'
south = '(S)outh'
travel = 'You can travel: '

a = 1
b = 1
start = (a,b)
while a < 4:
    while b < 4:
        location = str(a) + str(b)
        
        if location == '11':
            print(travel + north + '.')
            direction = str(input("Direction: "))
            if direction in 'nN':
                b = 2
            else:
                print("Not a valid direction!")
                direction = str(input("Direction: "))
                if direction in 'nN':
                    b = 2
                else:
                    print("Not a valid direction!")
        elif location == '12':
            print(travel + north + ' or ' + east + ' or ' + south + '.')
            direction = str(input("Direction: "))
            if direction in 'nN':
                b = 3 
            elif direction in 'sS':
                b = 1
            elif direction in 'eE':
                a = 2
            else:
                print("Not a valid direction!")
                direction = str(input("Direction: "))
                if direction in 'nN':
                    b = 3 
                elif direction in 'sS':
                    b = 1
                elif direction in 'eE':
                    a = 2
                else:
                    print("Not a valid direction!")
        elif location == '13':
            print(travel + east + ' or ' + south + '.')
            direction = str(input("Direction: "))
            if direction in 'eE':
                a = 2
            elif direction in 'sS':
                b = 2
            else:
                print("Not a valid direction!")
                direction = str(input("Direction: "))
                if direction in 'eE':
                    a = 2
                elif direction in 'sS':
                    b = 2
                else:
                    print("Not a valid direction!")
        elif location == '21':
            print(travel + north + '.')
            direction = str(input("Direction: "))
            if direction in 'nN':
                b = 2
            else:
                print("Not a valid direction!")
                direction = str(input("Direction: "))
                if direction in 'nN':
                    b = 2
                else:
                    print("Not a valid direction!")
        elif location == '22':
            print(travel + south + ' or ' + west + '.')
            direction = str(input("Direction: "))
            if direction in 'sS':
                b = 1
            elif direction in 'wW':
                a = 1
            else:
                print("Not a valid direction!")
                direction = str(input("Direction: "))
                if direction in 'sS':
                    b = 1
                elif direction in 'wW':
                    a = 1
                else:
                    print("Not a valid direction!")
        elif location == '23':
            print(travel + east + ' or ' + west + '.')
            direction = str(input("Direction: "))
            if direction in 'eE':
                a = 3
            elif direction in 'wW':
                a = 1
            else:
                print("Not a valid direction!")
                direction = str(input("Direction: "))
                if direction in 'eE':
                    a = 3
                elif direction in 'wW':
                    a = 1
                else:
                    print("Not a valid direction!")
        elif location == '33':
            print(travel + south + ' or ' + west + '.')
            direction = str(input("Direction: "))
            if direction in 'sS':
                b = 2
            elif direction in 'wW':
                a = 2
            else:
                print("Not a valid direction!")
                direction = str(input("Direction: "))
                if direction in 'sS':
                    b = 2
                elif direction in 'wW':
                    a = 2
                else:
                    print("Not a valid direction!")
        elif location == '32':
            print(travel + north + ' or ' + south + '.')
            direction = str(input("Direction: "))
            if direction in 'sS':
                b = 1
            elif direction in 'nN':
                b = 3
            else:
                print("Not a valid direction!")
                direction = str(input("Direction: "))
                if direction in 'sS':
                    b = 1
                elif direction in 'nN':
                    b = 3
                else:
                    print("Not a valid direction!")
                
        else:
            print('Victory!')
            b = 5
            a = 5






 