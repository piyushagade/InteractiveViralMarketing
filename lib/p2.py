import copy
import time
import networkx as nx
import fileinput
import random
import sys
import queue
from plotly.graph_objs import *


def start_Influence(G, activated_Nodes):
  covered_edges = set()
  nodes_activated=[]
  #nodes_activated = copy.deepcopy(activated_Nodes)
  nodes_activated.append([i for i in activated_Nodes])  # prevent side effect

  no_activation = 0
  while True:
    (activated_Nodes, nodes_activated_this_time, edges_transversed_this_time) = spread(G, activated_Nodes, covered_edges)
    if(nodes_activated_this_time):
      nodes_activated.append(nodes_activated_this_time)
    covered_edges = covered_edges.union(edges_transversed_this_time)


    if len(nodes_activated_this_time) == 0:
      no_activation += 1
    if (no_activation > 3):
      break
  return nodes_activated


def spread(G, activated_Nodes, covered_edges):

  nodes_activated_this_time = set()
  edges_transversed_this_time = set()
  for each_node in activated_Nodes:
    for each_neighbor in G.successors(each_node):
      if each_neighbor in activated_Nodes or (each_node, each_neighbor) in covered_edges or (each_node, each_neighbor) in edges_transversed_this_time:
        continue
      if coin_flip(G, each_node, each_neighbor):
        nodes_activated_this_time.add(each_neighbor)
      edges_transversed_this_time.add((each_node, each_neighbor))
  nodes_activated_this_time = list(nodes_activated_this_time)
  activated_Nodes.extend(nodes_activated_this_time)
  return activated_Nodes, nodes_activated_this_time, edges_transversed_this_time

def coin_flip(G, src, dest):
  return random.random() <= G[src][dest]['probability']




def strongly_connected_components_path(vertices, edges):


    identified = set()
    stack = []
    index = {}
    boundaries = []

    def dfs(v):
        index[v] = len(stack)
        stack.append(v)
        boundaries.append(index[v])

        for w in edges[v]:
            if w not in index:

                # For Python >= 3.3, replace with "yield from dfs(w)"
                for scc in dfs(w):
                    yield scc
            elif w not in identified:
                while index[w] < boundaries[-1]:
                    boundaries.pop()

        if boundaries[-1] == index[v]:
            boundaries.pop()
            scc = set(stack[index[v]:])
            del stack[index[v]:]
            identified.update(scc)
            yield scc


    for v in vertices:
        if v not in index:
            # For Python >= 3.3, replace with "yield from dfs(v)"
            for scc in dfs(v):
                yield scc

def UPDATEDAG(i,t):
  #scc = scclist[i]

  L = copy.deepcopy(Hlist[i])
  latest=copy.deepcopy(latestlist[i])
  for v in L.nodes():
      latest[v] = 0
  if t in L.nodes() :
   L.remove_node(t)

def Gain(i,v,GR,S) :
  scc =scclist[i]
  sccset = set()
  for eachset in scc:
    for eachelement in eachset:
         if eachelement not in sccset:
              sccset.add(eachelement)
  H= copy.deepcopy(Hlist[i])
  latest=copy.deepcopy(latestlist[i])
  delta ={}
  if not sccset.issubset(H.nodes()):
    return 0
  if latest[v] == 1 :
    return delta[v]
  for each_node in latest :
    latest[each_node] =1
  if v in (ancList[i]) and len(S)==0 :
   delta[v] = Gain(i,hlist[i],GR,S)
  else :
   delta[v] = 0

  Q = queue.Queue()
  Q._put(v)
  X =set()
  X.add(v)
  r=0
  while not Q.empty():
   u= Q.get()
   if v in ancList[i] and u in (descList) and len(S)== 0 :
    continue
   delta[v]=delta[v]+ len(scc)
   for eachedge in H.edges():
    w=eachedge[1]
    if not w in X and  w in H.nodes():
     Q.put(w)
     X.add(w)
  deltalist.insert(i,delta)

  return delta[v]
#Main Code

#create graph from file

G = nx.read_edgelist(edge_in, nodetype=int, data=(('probability',float),))

#validations
live_edges =list()
R = 2
edges={}

edges = copy.copy(G.edges())

edgelist ={}
print(edges)
Seed_Set = list()
descList = list()
ancList =list()
Hlist =list()
hlist =list()
latestlist =list()
scclist =list()
edgeslist=list()
deltalist=list()

start_time = time.time()
print("Start time")
print(start_time)
print(len(G.nodes()))
print(len(G.edges()))
print(start_time)
for i in range(1,R+1) :

  edges=copy.copy(G.edges())
  for each_edge in G.edges() :
      if not (coin_flip(G,each_edge[0],each_edge[1])):
          edges.remove(each_edge)

  H = nx.Graph()
  H.add_edges_from(edges)

  Hlist.insert(i,H)
  sccs = list()
  for each_node in H.nodes():
     edgelist[each_node]=H.neighbors(each_node)
  for scc in strongly_connected_components_path(H.nodes(),edgelist):
      sccs.append(scc)

  templist =[]
  tempnode ={}
  j=0
  latest= {}
  for each_node in G.nodes():
      latest[each_node] = 0

  for each_node in H.nodes():

    templist.insert(j,H.degree(each_node))
    tempnode[H.degree(each_node)] = each_node
    j=j+1

  maxdegree = max(templist)
  maxdegreenode = tempnode[maxdegree]

  D = nx.descendants(H,maxdegreenode)
  A = nx.ancestors(H,maxdegreenode)
  hlist.insert(i,maxdegreenode)

  descList.insert(i,D)
  ancList.insert(i,A)
  latestlist.insert(i,latest)
  scclist.insert(i,sccs)
  edgeslist.insert(i,edges)


i=1
GSUM =0
nodes = G.nodes()

while len(Seed_Set) < k:
 gain = {}
 print("This takes time 1")
 gainlist = list()
 for j in range(1,R+1):
  H =Hlist[j]
  GSUM =0
  for v in H.nodes():
    GSUM = GSUM +Gain(i,v,H,Seed_Set)
    Avggain = GSUM/R
    gain[Avggain] = v
    gainlist.append(Avggain)
    print("This takes time node %d" %v)
 maxgain = max(gainlist)
 t = gain[maxgain]
 Seed_Set.append(t)
 print("Got Seeds %d: " %len(Seed_Set))

 for l in range(1,R+1):
  UPDATEDAG(l,t)


print("--- %s seconds ---" % (time.time () - start_time))
print("final seed set:")
print(Seed_Set)