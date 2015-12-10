def land(edge_in, k):
        import pandas as pd
        import networkx as nx

        # Nodes
        G = nx.read_edgelist(edge_in, nodetype=int, data=(('prob',float),))
        nodes_list = G.nodes()
        
        no_nodes = 0
        node_str = ''
        for i in nodes_list:
            node_str = node_str+'{id: '+str(i)+', label: \''+str(i)+'\', color: \'#42dca3\'},\n'
            no_nodes = no_nodes+1

        # Edges
        edges = pd.read_csv(edge_in, sep=' ', header=None) #edges.csv_1 is with ,
        edges_list = edges.values.tolist()     
        
        edge_str = ''
        for i in edges_list:
            edge_str = edge_str+'{from: '+str(i[0])+', to: '+str(i[1])+', arrows: {to:{scaleFactor:0.5}}, dashes:true, label: '+str(i[2])+'},\n'

        current_edges=edge_str

        node1_str=''          #node1_str is node_str with seeds colored differently
#        ic_seedlist_int =  [int(i[0]) for i in ic_seedlist]
#        for i in nodes_list:
#            if ((i[0]) in (ic_seedlist_int)):
#                node1_str = node1_str+'{id: '+str(i[0])+', label: \''+str(i[0])+'\', color: \'#df23ee\'},\n'
#            else:
#                node1_str = node1_str+'{id: '+str(i[0])+', label: \''+str(i[0])+'\', color: \'#42dca3\'},\n'
#
#        print node1_str
        node1_str = node_str
        return '''
<head>
<script type="text/javascript" src="VIS/dist/vis.js"></script>
<link href="VIS/dist/vis.css" rel="stylesheet" type="text/css" />
<link href="css/grayscale.css" rel="stylesheet" type="text/css" />
<style type="text/css">
    #mynetwork {            margin-left: auto;      margin-right: auto;      border: 0px solid lightgray;    }  </style>

<title>Seed-Set Selection</title></head>

<body bgcolor="#000000">
<style type="text/css">
body {
    overflow:hidden;
}
</style>

<div  style="position: fixed; right: 20%; top: 70%; z-index:100;"><a href="p_algo?edge_in='''+edge_in+'''&&k='''+str(k)+'''" class="btn btn-default btn-lg" style="padding: 15px;">Proceed</a></div>
<div style="position: fixed; right: 20%; top: 78%; z-index:100;"><a href="index.html#about" class="btn btn-default btn-lg" style="padding: 15px;">Go Home</a></div>

<center>
<div style="position: fixed; border-style: dashed;    width:98%;    height:28%    border-width: 2px;    border-color:#42dca3;    margin-left:auto;    margin-right:auto;  align="center">
<div style="position: fixed; z-index: 9999; margin:50px"><h2><span style="color: #42dca3">Seed-Set Selection</span></h2>
<font color="#FFF">Required # of seeds: <a id="selectedseedlistdiv">'''+str(k)+'''</a></font>
<!--<br><font color="#FFF">Nodes Clicked: <a id="seedlistdiv"></a></font>-->
<br><br><br><br>
<div style="text-align:justify; padding:20px; border: dashed; width: 400px; z-index:100; border-color: #787; border-color: #787;"><p>This is the graph before execution of the algorithm. To execute the algorithm on this graph, click on 'Proceed'.</p></div><br><br>
</div>

<div id="mynetwork"></div>

<script type="text/javascript">
      document.getElementById("selectedseedlistdiv").innerHTML = ic_seedlist.toString();
</script>

<script type="text/javascript">
  // create an array with nodes
  var nodes = new vis.DataSet([
    '''+node1_str+'''
  ]);

  // create an array with edges
  var edges = new vis.DataSet([
     '''+edge_str+'''
  ]);

  // create a network
  var container = document.getElementById('mynetwork');
  var data = {
    nodes: nodes,
    edges: edges
  };
   var options = {
        nodes: {
            size: 20,
            font: {
                size: 22,
                color: '#ffffff'
            },
            borderWidth: 2
        },
        edges: {
            width: 2,
            font: {
                size: 12,
                color: '#ffffff',
                align: 'top'
                }

        }
    };

  var network = new vis.Network(container, data, options);
  var seedlist = "";
  var seedlistarr = []
  for(i='''+str(no_nodes)+'''-1;i>=0;i--){
      seedlistarr[i]="0";
  }
  var noinsnodes=0

  network.on("click", function (params) {
        params.event = "[original event]";
        text = JSON.stringify(params, null, 4);
        obj = JSON.parse(text);

        if(noinsnodes<'''+str(no_nodes)+''')
         {
             if(obj.nodes.length!=0){
                 seedlistarr[noinsnodes]=obj.nodes;
                 noinsnodes=noinsnodes+1;
                 document.getElementById("seedlistdiv").innerHTML = seedlistarr.toString();
                 }
         }

        if(obj.nodes.length!=0)
            {
            if(seedlist.length!=0){
                seedlist=seedlist+", "+obj.nodes
                }
            else{
                seedlist=obj.nodes
               }
            }
        document.getElementById("eventSpan").innerHTML = seedlist;

    });
</script>
<font color="#ffffff"><pre id="eventSpan"></pre></font>

</body>
        '''
k_global=0

def algo(edge_in, k):
  import copy
  import networkx as nx
  import fileinput
  import random
  import sys
  import pandas as pd
  import copy
  import time
  import Queue as queue
  k=int(k)
  
# Edges
  edges = pd.read_csv(edge_in, sep=' ', header=None) #edges.csv_1 is with ,
  edges_list = edges.values.tolist()     
        

  edge_str = ''
  for i in edges_list:
    edge_str = edge_str+'{from: '+str(i[0])+', to: '+str(i[1])+', arrows: {to:{scaleFactor:0.5}}, dashes:true, label: '+str(i[2])+'},\n'

  current_edges=edge_str

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
    Q.put(v)
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
  nodes_list = G.nodes()
        
  no_nodes = 0
  node_str = ''
  for i in nodes_list:
      node_str = node_str+'{id: '+str(i)+', label: \''+str(i)+'\', color: \'#42dca3\'},\n'
      no_nodes = no_nodes+1

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
   for j in range(1,R):
    H =Hlist[j]
    GSUM =0
    for v in H.nodes():
        if v not in Seed_Set:
         GSUM = GSUM +Gain(i,v,H,Seed_Set)
         Avggain = GSUM/R
         gain[Avggain] = v
         gainlist.append(Avggain)
#         print("The node %d" %v)
   maxgain = max(gainlist)
   t = gain[maxgain]
   Seed_Set.append(t)
   print("Got Seeds %d: " %len(Seed_Set))

   for l in range(1,R):
    UPDATEDAG(l,t)


  print("--- %s seconds ---" % (time.time () - start_time))
  print("final seed set:")
  print(Seed_Set)
  
  influenced_nodes = Seed_Set
  influenced_nodes_int =  [int(i) for i in influenced_nodes]  

  node1_str=''          #node1_str is node_str with seeds colored differently
  for i in nodes_list:
      if ((i) in (influenced_nodes_int)):      
          node1_str = node1_str+'{id: '+str(i)+', label: \''+str(i)+'\', color: \'#df23ee\'},\n'
      else:
          node1_str = node1_str+'{id: '+str(i)+', label: \''+str(i)+'\', color: \'#42dca3\'},\n'
  return str(type(Seed_Set))+'''

<head>
<script type="text/javascript" src="VIS/dist/vis.js"></script>
<link href="VIS/dist/vis.css" rel="stylesheet" type="text/css" />
<link href="css/grayscale.css" rel="stylesheet" type="text/css" />
<style type="text/css">
    #mynetwork {      width: 100%;      height: 100%;      margin-left: auto;      margin-right: auto;      border: 0px solid lightgray;    }  </style>

<title>Seed-Set Selection</title></head>


<body bgcolor="#000000">
<style type="text/css">
body {
    overflow:hidden;
}
</style>
<div style="position: fixed; right: 20%; top: 70%; z-index:100;"><a href="p_algo?edge_in='''+edge_in+'''&&k='''+str(k)+'''" class="btn btn-default btn-lg" style="padding: 13px;">Rework</a></div>
<div style="position: fixed; right: 20%; top: 78%; z-index:100;"><a href="p_land?edge_in='''+edge_in+'''&&k='''+str(k)+'''" class="btn btn-default btn-lg" style="padding: 12px;">Go Back</a></div>
<div style="position: fixed; right: 20%; top: 62%; z-index:100;"><a href="index.html#about" class="btn btn-default btn-lg" style="padding: 12px;">Go Home</a></div>

<center>
<div style="position: fixed; border-style: dashed;    width:98%;    height:28%    border-width: 2px;    border-color:#42dca3;    margin-left:auto;    margin-right:auto;  align="center">
<div style="position: fixed; z-index: 9999; margin:50px"><h2><span style="color: #42dca3">Seed-Set Selection</span></h2>
<font color="#FFF">Desired # of seeds: <a id="selectedseedlistdiv">'''+str(k)+'''</a></font>
<!--<br><font color="#FFF">Nodes Clicked: <a id="seedlistdiv"></a></font>-->
<br><br><br><br>
<div style="text-align:justify; padding:20px; border: dashed; width: 400px; border-color: #787;  z-index:100;"><p>This is the graph after the execution of the algorithm. </p></div>
</div>

<div style="position: fixed; right: 100px; top: 50px; z-index:100;"><font color="#42dca3" size="+1">Target Seeds:</font><font color="#fff" size="+1"><br> '''+str(influenced_nodes)+'''</font></div>

<div style="position: fixed; left: 70px; bottom: 50px; z-index:100;"><img src="img/ic_legend.png"></div>


<div id="mynetwork"></div>

<script type="text/javascript">
  // create an array with nodes
  var nodes = new vis.DataSet([
    '''+str(node1_str)+'''
  ]);

  // create an array with edges
  var edges = new vis.DataSet([
    '''+str(edge_str)+'''
  ]);

  // create a network
  var container = document.getElementById('mynetwork');
  var data = {
    nodes: nodes,
    edges: edges
  };
   var options = {
        nodes: {
            size: 20,
            font: {
                size: 22,
                color: '#ffffff'
            },
            borderWidth: 2
        },
        edges: {
            width: 2,
            font: {
                size: 16,
                color: '#ffffff'
                }
        }
    };
  var network = new vis.Network(container, data, options);
  var seedlist = "";
  var seedlistarr = []
  for(i='''+str(no_nodes)+'''-1;i>=0;i--){
      seedlistarr[i]="0";    // Initialize the set with 0
  }
  var noinsnodes=0          // Number of Inserted Nodes

  network.on("click", function (params) {
        params.event = "[original event]";
        text = JSON.stringify(params, null, 4);
        obj = JSON.parse(text);

        if(noinsnodes<'''+str(no_nodes)+''')
         {
             if(obj.nodes.length!=0){
                 seedlistarr[noinsnodes]=obj.nodes;
                 noinsnodes=noinsnodes+1;
                 document.getElementById("seedlistdiv").innerHTML = seedlistarr.toString();
                 }
         }

        if(obj.nodes.length!=0)
            {
            if(seedlist.length!=0){
                seedlist=seedlist+", "+obj.nodes
                }
            else{
                seedlist=obj.nodes
               }
            }
        document.getElementById("eventSpan").innerHTML = seedlist;
    });
</script>
<!--<font color="#ffffff"><pre id="eventSpan"></pre></font>-->

</body>'''