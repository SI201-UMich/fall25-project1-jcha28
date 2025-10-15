
'''
Name: Jennifer Cha
UMID: 2781 2800
email: jennycha@umich.edu

'''

import csv #using penguins dataset


def read_penguin_data(file_name): #reads/analyzes penguin data from csv file
    data = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def get_data(data): #gets data of columns, sample row, and total rows
    if len(data) > 0:
        columns = list(data[0].keys())
        sample = data[0]
    else:
        columns = []
        sample = {}

    total_rows = len(data)
    return columns, sample, total_rows


def avg_bodymass(data): #calculation 1: what's the average body mass by species and sex

    all_animals = {}

    for row in data: #itterate through each row of data
        species = row['species']
        sex = row['sex']
        body_mass = row['body_mass']

        if species and sex and body_mass != 'NA': #checks existance of data
            body_mass = float(body_mass)
            key = (species, sex)
            if key not in all_animals:
                all_animals[key] = {'total_mass': 0, 'count': 0}
            all_animals[key]['total_mass'] += body_mass
            all_animals[key]['count'] += 1

        averages = {} #calculates the averages
        for key, value in all_animals.items():
            averages[key] = float(f'{value['total_mass'] / value['count']:.2f}')
        return averages

    pass

def flipper_length_over200(data): #calculation 2: what % of penquins have a flipper length over 200mm
    total_count = 0
    over200_count = 0

    for row in data:
        flipper = row['flipper length']
        if flipper != 'NA':
            flipper_value = float(flipper)
            total_count += 1
            if flipper_value > 200:
                over200_count += 1

    if total_count == 0:
        return 0.0
    
    percentage = (over200_count / total_count) * 100
    return float(f'{percentage:.2f}')


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


