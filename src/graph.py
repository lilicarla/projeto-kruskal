class Vertex:
    def __init__(self, initKey, initLat, initLong, initName):
        self.key = initKey
        self.lat = initLat
        self.long = initLong
        self.name = initName
        self.adj = {}
    
    def addAdj(self, ver, weight):
        try:
            self.adj[ver]
        except:
            self.adj[ver] = weight

class Graph:
    def __init__(self):
        self.size = 0
        self.g = {}
        self.edges = []

    def addV(self, key, lat, long, name):
        try:
            self.g[key]
        except:
            newV = Vertex(key, lat,long,name)
            self.g[key] = newV
            self.size +=1

    def addE(self, kOne, kTwo, weight):
        try:
            s = self.g[kOne]
            d = self.g[kTwo]
            s.addAdj(kTwo,weight)
            d.addAdj(kOne,weight)
            self.edges.append([weight,kOne,kTwo])
        except:
            pass
    
    def getVAdj(self, key):
        v = self.g[key]
        return v.adj # dict{'key':weight}

def dfs(g:Graph, v, marked:dict, rear:dict,d,found):
    marked[v] = True
    if not found[d]:
        found[d] = (v == d)
    if found[d]:
        return
    for u in g.getVAdj(v):
        try:
            marked[u]
        except:
            rear[u] = v
            dfs(g,u,marked,rear,d,found)

def depthFirstSearch(g:Graph, source,destiny):
    marked = {}
    rear = {}
    found = {destiny:False}
    dfs(g,source,marked,rear,destiny,found)
    del rear
    del marked
    return found[destiny]