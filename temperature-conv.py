def temperaturConverter():
    print('1.Celcius to Kelvin\n2.Kelvin to Celcius\n3.Fahrenheit to Celcius\n4.Celcius to Fahrenheit\n5.Fahrenheit to Kelvin\n6.Kelvin to Fahrenheit')

    type = int(input('Choose Conversion: '))
    again = True

    # celcius to kelvin
    if (type == 1):
        c = int(input('Input celcius: '))
        result = c + 273.15
        result = str(result)
        result = result + ' kelvin'
    # kelvin to celcius
    elif (type == 2):
        k = int(input('Input kelvin: '))
        result = k - 273.15
        result = str(result)
        result = result + ' celcius'
    # fahrenheit to celcius
    elif (type == 3):
        f = int(input('Input fahrenheit: '))
        result = (f - 32) * 5/9
        result = str(result)
        result = result + ' celcius'
    # celcius to fahrenheit
    elif (type == 4):
        c = int(input('Input celcius: '))
        result = (c * 9/5) + 32
        result = str(result)
        result = result + ' fahrenheit'
    # fahrenheit to kelvin
    elif (type == 5):
        f = int(input('Input fahrenheit: '))
        result = (f - 32) * 5/9 + 273.15
        result = str(result)
        result = result + ' kelvin'
    # kelvin to fahrenheit
    elif (type == 6):
        k = int(input('Input Kelvin: '))
        result = (k - 273.15) * 9/5 + 32
        result = str(result)
        result = result + ' fahrenheit'
    else:
        print('Erorr occured')

    print(result)

    ask = input('Do another conversion? y/n: ')
    if (ask != 'y'):
        again = False
    
    while(again):
        temperaturConverter()
    
print(temperaturConverter())
