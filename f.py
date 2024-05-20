placa = input()

match placa:
    case placa if 6 > len(placa) > 2 and (placa[0] == 'A' or placa[0] == 'P') and placa[1:].isnumeric():
        print('Placa muito antiga')

    case placa if len(placa) < 7 and placa.isnumeric():
        print('Placa numerica')

    case placa if len(placa) == 6 and placa[:2].isalpha() and placa[2:].isnumeric():
        print('Placa AA-9999')

    case placa if len(placa) == 7 and placa[:3].isalpha() and placa[3:].isnumeric():
        print('Placa AAA-9999')

    case placa if len(placa) == 7 and placa[:2].isalpha() and placa[3].isnumeric() and placa[4].isalpha() and placa[5:].isnumeric():
        print('Placa Mercosul')

    case _:
        print('Placa invalida')