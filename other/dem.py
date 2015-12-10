import networkx as nx
import pandas as pd
from matplotlib.pylab import plt
#%matplotlib inline
 
G = nx.Graph()
 
# Read csv for nodes and edges using pandas:
nodes = pd.read_csv("C:/nodes.csv")
edges = pd.read_csv("C:/edges.csv")
 
# Dataframe to list:
nodes_list = nodes.values.tolist()
edges_list = edges.values.tolist()

 
# Import id, name, and group into node of Networkx:
for i in nodes_list:
    G.add_node(i[0], name=i[1], group=i[2])
 
# Import source, target, and value into edges of Networkx:
for i in edges_list:
    G.add_edge(i[0],i[1], value=i[2])
 
pos=nx.random_layout(G)


# Visualize the network:
nx.draw_networkx(G)

#
                   
#nx.draw_networkx_edges(G,pos,
#                       edgelist=[(0,1),(1,2),(2,3),(3,0)],
#                       width=8,alpha=0.5,edge_color='b')
                       
