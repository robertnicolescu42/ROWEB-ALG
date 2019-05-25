import math


def isprime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True



def solutie():
    answer = input("a/b/c?")
    f = open("File.txt", "r")
    lines = [line.rstrip('\n\r') for line in f]

#aici creez un array lines cu fiecare linie pe care un loc
#iau, pe rand, liniile si duc in mainarr elementul de la jumatea fiecarei linii

    mainintarr = []
    mainarr = []
    length = len(lines)-1
    temparr = []
    nrprime = []
    cuvant = ''
    x=0

    for line in lines:
        if(x<=length):
            temparr = lines[x].split(' ')
            x+=1
#acum in temparr am o linie din fisier, urmeaza
#sa o convertesc in int
        mainarr.append(temparr[int(len(temparr)/2)])

    for x in range (len(mainarr)):
        mainintarr.append(int(mainarr[x]))
    
    if (answer == 'a'):
        print(mainintarr)

    for x in range (len(mainintarr)):
        if(isprime(mainintarr[x])):
            nrprime.append(mainintarr[x])

    if (answer == 'b'):
        print(nrprime)

    if (answer == 'c'):
        for x in range(len(nrprime)):
            cuvant = cuvant + chr(nrprime[x])
        print (cuvant)

def main():
    solutie()

if __name__ == "__main__":
    main()