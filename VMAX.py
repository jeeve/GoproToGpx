import csv, os

chemin = './exports/'

def getVmax(fichier):

    vmax = 0

    with open(chemin + fichier, newline='') as f:
        reader = csv.reader(f)
        for index, row in enumerate(reader):
            if index > 0:
                v = float(row[4]) * 1.94384
                if v > vmax:
                    vmax = v

    return vmax

tableau = {}
for element in os.listdir(chemin):
    if element.endswith('-gps.csv'):
        tableau[element] = getVmax(element)

mavar = tableau.items()
montri = sorted(mavar, key=lambda x: x[1], reverse=True)

[print(j, i) for i, j in montri]

with open(chemin + "vmax.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Vmax (knots)', 'filename'])
    for i, j in montri:
        writer.writerow([j, i])
