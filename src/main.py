import graph as g
import haversine as hs
import kruskal as k
import json

def calcDistance(lat1:float, long1:float, lat2:float, long2:float):
    point1 = (lat1, long1)
    point2 = (lat2,long2)
    distanceKm = hs.haversine(point1,point2)
    return distanceKm

def readDataFile(path:str):
    with open('data/'+path,  encoding='utf-8') as dataFile:
        data = json.load(dataFile)
    dataFile.close()
    return data

def main():
    helipontosG = g.Graph()
    hpData = readDataFile('helipontos_MG.json')
    for heliponto in hpData:
        # CIAD (Código de Identificação do Aeródromo): identificador único de aeródromos civis
        helipontosG.addV(heliponto['CIAD'], float(heliponto['LATGEOPOINT']), float(heliponto['LONGEOPOINT']), heliponto['Nome'])
    aux = 1
    for i in hpData:
        for j in hpData[aux:]:
            lt1 = float(i['LATGEOPOINT'])
            lg1 = float(i['LONGEOPOINT'])
            lt2 = float(j['LATGEOPOINT'])
            lg2 = float(j['LONGEOPOINT'])
            km = calcDistance(lt1,lg1,lt2,lg2)
            helipontosG.addE(i['CIAD'],j['CIAD'],km)
        aux += 1
    
    s = k.kruskal(helipontosG)
    print(s.edges)
    del hpData
    del helipontosG
    del s

if __name__ == '__main__':
    main()