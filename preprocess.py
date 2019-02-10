import csv
from shutil import copyfile

def age(val):
    return round(int(val), -1)

def size(val):
    if int(val) < 40:
        return 20
    if int(val) < 80:
        return 60
    if int(val) < 120:
        return 100
    if int(val) < 200:
        return 160
    return 260

def beautyscore(val):
    return round(float(val))

def evalscore(val):
    return round(float(val))

def courseval(val):
    if float(val) < 4:
        return "bad"
    return "good"

options = { 4: age,
            5: size,
            7: beautyscore,
            8: evalscore,
            #Comment out this line if you don't want the target attribute to be categorical.
            #9: courseval
}

with open('StudentEvaluations.csv', newline='') as data:
    output = []
    dreader = csv.reader(data, delimiter=',')
    for row, line in enumerate(dreader):
        if row == 0:
            continue
        output.append(list(line))
        for column, word in enumerate(line):
            if column in options:
                output[row-1][column] = options[column](word)

with open('processed.csv', 'w', newline='') as processed:
    dwriter = csv.writer(processed)
    dwriter.writerows(output)