# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 21:13:55 2019

@author: Kiooola
"""

import random


def import_graph(file):
    with open(file) as f:
        dataset = []
        for line in f:
            row = line.split()
            output = [int(x) for x in row]
            dataset.append(output)
        return dataset
    
dataset = import_graph("kargerMinCut.txt")
#dataset = import_graph("test.txt")    


def choose_edge(graph):
    u = random.randint(0,len(graph)-1)
    v = random.randint(1,len(graph[u])-1)
    return u,v



def merge_vertex(graph):
    
    """
    merges two vertices together
    """
    #create a list of all the vertices (first element of each line)
    #find the position of the second vertex in the graph
    u,v = choose_edge(graph)
    head_list = [item[0] for item in graph]
    v_val = graph[u][v]
    v_index =  head_list.index(v_val) 
#    print(graph,"\n")
#    print(graph[u][0],"u:")
#    print(graph[u])
#    print(graph[u][v],"v:")
#    print(graph[v_index])
    
    
    #delete self-loops by removing the second vertex from the list edges
    while v_val in graph[u]:
        graph[u].remove(v_val)
    

    # add edges of second vertex to first vertex (merge!)
    # and replace all instances of the second vertex in the rest of the graph
    for i in graph[v_index][1:]:
            if i != graph[u][0]:
                graph[u].append(i)
            
             
            replace_index = head_list.index(i)
            for i,r in enumerate(graph[replace_index]):
                if r == v_val:
                    graph[replace_index][i] = graph[u][0]
                
                    
    #delete second vertex info
    del graph[v_index]
#    print(graph)
    return graph
    


def min_cut(graph):
    i=0
    
    while len(graph)>2:
        u,v = choose_edge(graph)
        graph = merge_vertex(graph)
        i+=1
    
    count = len(graph[0])-1
    return count


def find_best(graph,iteration):
    
    cutz = []
    
    for i in range(0,iteration):
        cutz.append(min_cut(graph))
    
    return min(cutz)


#graph = merge_vertex(dataset)
#print(graph)        

print(find_best(dataset,len(dataset)**2))
    
    