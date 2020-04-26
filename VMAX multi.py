import csv, os
from operator import itemgetter

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
for i, element in enumerate(os.listdir(chemin)):
    if element.endswith('-gps.csv'):
        kts = getVmax(element)
        tableau[i, 0] = element
        tableau[i, 1] = kts
        tableau[i, 2] = kts * 1.852

montri = list(sorted(tableau, key=itemgetter(1)))

[print(j, i) for i, j in montri]

with open(chemin + "vmax.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Vmax (knots)', 'filename'])
    for i, j in montri:
        writer.writerow([j, i])
