# Define the Romanian cities graph based on the image
graphmap = {
    'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
    'Zerind': ['Oradea', 'Arad'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Oradea', 'Fagaras', 'Rimnicu Vilcea', 'Arad'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Dobreta'],
    'Dobreta': ['Mehadia', 'Craiova'],
    'Craiova': ['Dobreta', 'Rimnicu Vilcea', 'Pitesti'],
    'Rimnicu Vilcea': ['Sibiu', 'Pitesti', 'Craiova'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}

def citymap(graphmap,startcity,endcity):
    opened=[startcity]
    closed=[]
    while opened:
        node = opened.pop(0)
        if node in endcity :
            closed.append(node)
            return closed
        else:
            opened = opened +[item for item in graphmap[node] if item not in opened and item not in closed]
            closed.append(node)
    return "Goal not found "


def citymapdfs(graphmap,startcity,endcity):
    opened=[startcity]
    closed=[]
    while opened:
        node = opened.pop(0)
        if node in endcity :
            closed.append(node)
            return closed
        else:
            opened = [item for item in graphmap[node] if item not in opened and item not in closed] +opened
            closed.append(node)
    return "Goal not found "

startcity = input("Enter the start city ")
endcity = input("Enter the end city ")

if startcity not in graphmap or endcity not in graphmap:
    print("enter correct city name ")
else:
    print("BFS ")
    bfspath = citymap(graphmap,startcity,endcity)
    print(bfspath)
    
    print("DFS ")
    bfspath = citymapdfs(graphmap,startcity,endcity)
    print(bfspath)

    
