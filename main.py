from Class.menu import Menu

def main():
    print("Running...")
    print("Chose program:")
    print("1 for NetScan")
    print("2 for Dirb Apache")
    program = int(input())
    Menu(program)

if __name__ == '__main__':
    main()