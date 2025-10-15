
'''
Name: Jennifer Cha
UMID: 2781 2800
email: jennycha@umich.edu

'''

import csv #using penguins dataset


def read_penguin_data(filename): #reads/analyzes penguin data from csv file
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def avg_bodymass(data): #calculation 1: what's the average body mass by species and sex
    results = []
    totals = {}
    counts = {}

    for i in range(1, data):
        row = data[i]
        species = row[0]
        sex = row[i+1]
        body_mass = row[i-1]

        if species and sex and body_mass != 'NA':
            body_mass = float(body_mass)




    return results

    pass


def test_calc1(): #test case for calculation 1 (avg boddy mass)
    #gen1
    data = [
        {'species': 'Adelie', 'sex': "male", 'body_mass': '4000'},
        {'species': 'Adelie', 'sex': "male", 'body_mass': '6000'}
    ]
    result = avg_bodymass(data)
    expected = 5000.00
    if result.get(('Adelie', 'male')) == expected:
        print('calc_avg_bodymass test passed')

    else:
        print(f'calc_avg_bodymass test failed: {result}')


    #gen2
    data = [
        {'species': 'Adelie', 'sex': 'male', 'body_mass': '4000'},
        {'species': 'Adelie', 'sex': 'female', 'body_mass': '3000'},
        {'species': 'Gentoo', 'sex': 'male', 'body_mass': '5000'}
    ]
    result = avg_bodymass(data)
    if (result.get(('Adelie', 'male')) == 4000.00 and
        result.get(('Adelie', 'female')) == 3000.00 and
        result.get(('Gentoo', 'male')) == 5000.00):
        print('calc_avg_bodymass test passed')
    else:
        print(f'calc_avg_bodymass test failed: {result}')


    #edge1
    data = [
        {'species': 'Adelie', 'sex': 'male', 'body_mass': 'NA'},
        {'species': 'Adelie', 'sex': 'male', 'body_mass': '5000'}
    ]
    result = avg_bodymass(data)
    if result.get(('Adelie', 'male')) == 5000.00:
        print('calc_avg_bodymass test passed')
    else:
        print(f'calc_avg_bodymass test failed: {result}')


    #edge2
    data = [
        {'species': 'Adelie', 'sex': 'male', 'body_mass': 'NA'},
    ]
    result = avg_bodymass(data)
    if result == {}:
        print('calc_avg_bodymass test passed')
    else:
        print(f'calc_avg_bodymass test failed: {result}')

def test_calc2(): #test case for calculation 2 (flipper length > 200mm)
    #gen1
    data = [
        {'flipper length': '210'},
        {'flipper length': '190'}
    ]
    result = flipper_length_over200(data)
    if result == 50.00:
        print('flipper length test passed')
    else:
        print(f'flipper length test failed: {result}')

    #gen2
    data = [
        {'flipper length': '210'},
        {'flipper length': '220'}
    ]
    result = flipper_length_over200(data)
    if result == 100.00:
        print('flipper length test passed')
    else:
        print(f'flipper length test failed: {result}')

    

def main():


if __name__ == '__main__':
    main()


