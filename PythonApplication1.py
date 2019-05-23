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

def strtoint(str_list):
    int_list = [int(n) for n in str_list]
    return int_list

def solutie():
    mainarr = []
    f = open("File.txt", "r")
    lines = [line.rstrip('\n\r') for line in f]

    #aici creez un array lines cu fiecare linie pe care un loc
    #iau, pe rand, liniile si duc in mainarr elementul de la jumatea fiecarei linii
    x = 0
    for x in range (len(lines[x])):
        strtoint(lines[x])
        length = len(lines[x])
        mainarr[x] = lines[length/2]
        print(result)
        #print("\n")
        #mainarr[x] = lines[x]

    for x in range (len(mainarr[x])):
        print (mainarr[x])


def main():
    solutie()

if __name__ == "__main__":
    main()