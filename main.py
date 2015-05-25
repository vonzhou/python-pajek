#!/usr/bin/python

from igraph import *
from string import *
#import timeit

#start = timeit.default_timer()

fnode = open("nodes.data", "r")

g = Graph(directed=True)  # a directed graph

# Need to map from ids to vertex names (NB.)
maps = {}
index = 0
for line in fnode:
    nodeid = str(int(line))
    maps[nodeid] = index
    g.add_vertex(name=nodeid)
    index = index + 1

fnode.close()

'''
print(g)
1000080335
print(type(g.vs))
print(g.vs[0]['name'])
print(maps['1000080335'])
'''

fedge = open("edges.data", "r")
for line in fedge:
    line.strip()
    if line and line[0].isdigit():
    	#split by space
    	words = line.split(' ')
    	#print(words)
    	suid = str(int(words[0]))
    	tuid = str(int(words[1])) #this way to kill the last \n
    	#print("-"),
    	g.add_edges([(maps[suid],maps[tuid])])

#print(g)


fnet = open("/home/vonzhou/weibodb.net", "w")
g.write_pajek(fnet)

fedge.close()
fnet.close()

#stop = timeit.default_timer()
#print("Time Used :" ,(stop-start))


