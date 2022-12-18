
def AddName(name,file):
    with open(file,'a') as f:
        f.write(name + '\n')

def ReadNames(file):
    with open(file,'r') as f:
        print('Names in file: ')
        for name in f:
            print(name,end='')

def ReplaceName(old,new,file):
    names = ReadNames(file)
    with open(file,'w') as f:
        for name in names:
            if name == old:
                f.write(new + '\n')
            else:
                f.write(name + '\n')

def SearchName(name,file):
    with open(file,'r') as f:
        for line in f:
            if name == line:
                return True
        return False
def SortName(file):
    names = ReadNames(file)
    with open(file,'w') as f:
        for name in names:
            f.write(name + '\n')

def main():
    file = input('Enter file name: ')
    while True:
        print('1. Add name')
        print('2. Replace name')
        print('3. Read names')
        print('4. Search name')
        print('5. Sort Name')
        print('6. Exit')
        choice = int(input('Enter choice: '))
        if choice == 1:
            name = input('Enter name: ')
            AddName(name,file)
        elif choice == 2:
            old = input('Enter old name: ')
            new = input('Enter new name: ')
            ReplaceName(old,new,file)
        elif choice == 3:
            ReadNames(file)
        elif choice == 4:
            name = input('Enter name: ')
            if SearchName(name,file):
                print('Name found')
            else:
                print('Name not found')
        elif choice == 6:
            break
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()

