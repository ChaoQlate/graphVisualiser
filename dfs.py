import api
from queue import Queue

def dfs(g, n, s, q):
    visited = {}
    for key in g.getNodes():
        visited[key] = False
    return dfsR(g, n, s, visited, q)

def dfsR(g, n, s, visited, q):
    q.put(n)
    if n == s:
        return True
    visited[n] = True
    for e in g.getEdges(n):
        if e[0] != n and not visited[e[0]]:
            r = dfsR(g, e[0], s, visited, q)
            if r == True:
                return True
    return False


if __name__ == '__main__':
    g = api.newGraph()
    '''
    api.addNode("a")
    api.addNode("b")
    api.addNode("c")
    api.addNode("d")
    api.addNode("e")

    api.addEdge("a", "b")
    api.addEdge("a", "c")
    api.addEdge("b", "c")
    api.addEdge("a", "e")
    api.addEdge("b", "d")
    '''

    g = api.newGraph()

    api.addNode("Pazzi")
    api.addNode("Salviati")
    api.addNode("Acciaiuolli")
    api.addNode("Medici")
    api.addNode("Barbadori")
    api.addNode("Casteliani")
    api.addNode("Strozzi")
    api.addNode("Peruzzi")
    api.addNode("Bischeri")
    api.addNode("Ridolfi")
    api.addNode("Tornabiouni")
    api.addNode("Guadagini")
    api.addNode("Albizzi")
    api.addNode("Ginori")
    api.addNode("Lamberteschi")

    api.addEdge("Pazzi", "Salviati")
    api.addEdge("Salviati", "Medici")
    api.addEdge("Acciaiuolli", "Medici")
    api.addEdge("Medici", "Barbadori")
    api.addEdge("Barbadori", "Casteliani")
    api.addEdge("Casteliani", "Strozzi")
    api.addEdge("Casteliani", "Peruzzi")
    api.addEdge("Peruzzi", "Bischeri")
    api.addEdge("Peruzzi", "Strozzi")
    api.addEdge("Strozzi", "Bischeri")
    api.addEdge("Strozzi", "Ridolfi")
    api.addEdge("Ridolfi", "Medici")
    api.addEdge("Tornabiouni", "Medici")
    api.addEdge("Tornabiouni", "Ridolfi")
    api.addEdge("Medici", "Albizzi")
    api.addEdge("Albizzi", "Ginori")
    api.addEdge("Albizzi", "Guadagini")
    api.addEdge("Guadagini", "Lamberteschi")
    api.addEdge("Guadagini", "Tornabiouni")
    api.addEdge("Guadagini", "Bischeri")

    q = Queue(len(g.getNodes()))

    dfs(g, "Medici", "Ridolfi", q)

    api.setNodeQueue(q)

    api.showGraph()
    api.run()