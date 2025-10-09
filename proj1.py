
'''
Name: Jennifer Cha
UMID: 2781 2800
email: jennycha@umich.edu

'''

import csv #using penguins dataset


def read_penguin_data(filename):
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.apend(row)
    return data

def avg_bodymass(data):
    results = []
    totals = {}
    counts = {}

    for i in range(1, data):
        row = data[i]
        species = row[0]
        sex = row[i+1]
        body_mass = row[i-1]

        if body_mass == '' or sex == '':

