
while True:
    try:
        x = int(input('Enter a number: '))
        print(x)
        break
    except:
        print('Invalid input! \n')
    finally:
        print("Attempted input")
