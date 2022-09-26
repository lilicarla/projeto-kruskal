import graph as g
import heap as h

def kruskal(graph: g.Graph):
    marked = {}
    s = g.Graph()
    edges = [[-1,'','']]
    edges+= graph.edges

    minHeap = h.buildMinHeap(edges)

    while s.size < graph.size:
        minE,minHeap = h.heapExtractMin(minHeap)
        newPointS = False
        newPointD = False

        weight = minE[0]
        keyOne = minE[1]
        keyTwo = minE[2]

        try:
            marked[keyOne]
        except:
            marked[keyOne] = True
            newPointS = True
            v1 = graph.g[keyOne]
            s.addV(keyOne,v1.lat,v1.long,v1.name)

        try:
            marked[keyTwo]
        except:
            marked[keyTwo] = True
            newPointD = True
            v2 = graph.g[keyOne]
            s.addV(keyTwo,v2.lat,v2.long,v2.name)
        
        if not newPointS and not newPointD:
            cycle = g.depthFirstSearch(s,source=keyOne,destiny=keyTwo)
            if not cycle:
                s.addE(keyOne,keyTwo,weight)
        else:
            s.addE(keyOne,keyTwo,weight)

    return s