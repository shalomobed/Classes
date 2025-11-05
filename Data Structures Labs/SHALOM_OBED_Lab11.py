#Adjacency List represnting a graph
adj = [
        [1,3],
        [2], 
        [4],
        [],
        [0,3],
        [2] 
    ]
def extract_cycle(adj_list, start):
    visited = set() #keep count of visited nodes 
    path = [] 
    in_path = set() 
    found_cycle = [] #the output, store it if it found a cycle

    #Using Depth First Search
    def dfs(node):
        nonlocal found_cycle
        visited.add(node)
        path.append(node)
        in_path.add(node)

        for neighbor in adj_list[node]:
            if neighbor not in visited:
                dfs(neighbor)
                if found_cycle:
                    return
            elif neighbor in in_path:
                idx = path.index(neighbor)
                found_cycle = path[idx:] + [neighbor] #if neigbour = 1 [1, 2, 4, 0] +[1]
                return
        
        path.pop()
        in_path.remove(node)
    
    dfs(start)

    if found_cycle and start in found_cycle:
        return found_cycle
    return []
        

print(extract_cycle(adj, 0)) # Should print [0, 1, 2, 4, 0]
print(extract_cycle(adj, 1)) # Should print [1, 2, 4, 0, 1]
print(extract_cycle(adj, 3)) # Should print []