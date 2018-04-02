import matplotlib.pyplot as plt

def main(): #functie die alles aanroept en de data uit het bestand verkrijgt
    file = open('percentages.txt')                                  #open het bestand
    perLijst = []                                                   #maak een lege lijst waar de gefilterde percentages in komen te staan
    for line in file.readlines():                                   #loop door het bestand...
        percentages = []                                            #maak een lege lijst voor de percentages
        line = line.split()                                         #split de line op elk aantal spaties
        del line[0]                                                 #verwijder het eerste element uit de lijst
        del line[0]                                                 #verwijder het eerste element uit de lijst
        if '-nan' in line:                                          #als er een -nan voorkomt in de lijst...
            x = line.count('-nan')                                  #tel het aantal keer dat -nan voorkomt in de lijst
            for i in range(0, x):                                   #zo lang i tussen 0 en waarde x zit...
                line.remove('-nan')                                 #verwijdert -nan uit de lijst (ik neem aan dat we die niet hoeven te tellen)
        for i in line:                                              #loop door de line
            i = float(i)                                            #zet het element om in een float
            i = round(i)                                            #rond het element af
            percentages.append(i)                                   #voeg het percentage toe aan de lijst met percentages
        perLijst.extend(percentages)                                #voeg de lijst met percentages toe aan de gefilterde lijst
    gebLijst = []                                                   #maak een lege lijst voor het aantal keren dat een percentage voorkomt
    for i in range(0,101):                                          #zo lang i in de range zit van 0 en 101...
        gebLijst.append(0)                                          #voeg een 0 toe aan de gebLijst
    for i in perLijst:                                              #zo lang i in de perLijst zit...
        gebLijst[i]+=1                                              #verhoog de positie van i in de gebLijst met 1
    plotten(gebLijst)                                               #roep de plotten functie aan en geef gebLijst mee

def plotten(gebLijst): #functie die de data in een bar plot zet
    print(gebLijst)                                         
    plt.bar(range(len(gebLijst)), gebLijst, align='center')
    plt.xticks(range(len(gebLijst)), size=7)
    plt.show()
    
main() #aanroep van main functie


