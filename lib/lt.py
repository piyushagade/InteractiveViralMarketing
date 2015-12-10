def land(edge_in, seedlist):
        import pandas as pd
        import networkx as nx

        ic_seeds = pd.read_csv(seedlist, header=None)
        ic_seedlist = ic_seeds.values.tolist()

        seed_str=''
        for i in ic_seedlist:
            seed_str = seed_str+str(i[0])+" "

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
        ic_seedlist_int =  [int(i[0]) for i in ic_seedlist]
        for i in nodes_list:
            if ((i) in (ic_seedlist_int)):
                node1_str = node1_str+'{id: '+str(i)+', label: \''+str(i)+'\', color: \'#df23ee\'},\n'
            else:
                node1_str = node1_str+'{id: '+str(i)+', label: \''+str(i)+'\', color: \'#42dca3\'},\n'

        print node1_str

        return '''
<head>
<script type="text/javascript" src="VIS/dist/vis.js"></script>
<link href="VIS/dist/vis.css" rel="stylesheet" type="text/css" />
<link href="css/grayscale.css" rel="stylesheet" type="text/css" />
<style type="text/css">
    #mynetwork {            margin-left: auto;      margin-right: auto;      border: 0px solid lightgray;    }  </style>

<title>Linear Thresholding</title></head>

<body bgcolor="#000000">
<style type="text/css">
body {
    overflow:hidden;
}
</style>



<div  style="position: fixed; right: 20%; top: 70%; z-index:100;"><a href="lt_algo?edge_in='''+edge_in+'''&&seedlist='''+seedlist+'''" class="btn btn-default btn-lg" style="padding: 15px;">Proceed</a></div>
<div style="position: fixed; right: 20%; top: 78%; z-index:100;"><a href="index.html#about" class="btn btn-default btn-lg" style="padding: 15px;">Go Home</a></div>

<center>
<div style="position: fixed; border-style: dashed;    width:98%;    height:28%    border-width: 2px;    border-color:#42dca3;    margin-left:auto;    margin-right:auto;  align="center">
<div style="position: fixed; z-index: 9999; margin:50px"><h2><span style="color: #42dca3">Linear Thresholding</span></h2>
<font color="#FFF">Seeds selected: <a id="selectedseedlistdiv">'''+seed_str+'''</a></font>
<!--<br><font color="#FFF">Nodes Clicked: <a id="seedlistdiv"></a></font>-->
<br><br><br><br>
<div style="text-align:justify; padding:20px; border: dashed; width: 400px; z-index:100; border-color: #787; border-color: #787;"><p>This is the graph before execution of the algorithm. To execute the algorithm on this graph, click on 'Proceed'.</p></div><br><br>
<div style="text-align:justify; padding:20px; border: dashed; width: 400px;  z-index:100; border-color: #787;"><p>The edge weights are the thresholds for getting influenced by neighbours.</p></div>
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


def algo(edge_in, seedlist):
  import copy
  import networkx as nx
  import fileinput
  import random
  import sys
  import pandas as pd

  ic_seeds = pd.read_csv(seedlist, header=None)
  ic_seedlist = ic_seeds.values.tolist()

#  Seeds
  seed_str=''
  for i in ic_seedlist:
    seed_str = seed_str+str(i[0])+" "


# Edges
  edges = pd.read_csv(edge_in, sep=' ', header=None) #edges.csv_1 is with ,
  edges_list = edges.values.tolist()

  edge_str = ''
  for i in edges_list:
    edge_str = edge_str+'{from: '+str(i[0])+', to: '+str(i[1])+', arrows: {to:{scaleFactor:0.5}}, dashes:true, label: '+str(i[2])+'},\n'

  current_edges=edge_str

  def start_Influence(G, activated_Nodes):
    covered_edges = set()
    nodes_activated=[]
    #nodes_activated = copy.deepcopy(activated_Nodes)
    nodes_activated.extend([i for i in activated_Nodes])  # prevent side effect
    print(nodes_activated)
    no_activation = 0
    while True:
      (activated_Nodes, nodes_activated_this_time) = spread(G, activated_Nodes)
      if(nodes_activated_this_time):
        nodes_activated.extend(nodes_activated_this_time)

      print(nodes_activated_this_time)
      print(len(nodes_activated_this_time))
      if len(nodes_activated_this_time) == 0:
        no_activation += 1
      if (no_activation > 5):
        break
    return nodes_activated


  def spread(G, activated_Nodes):
    nodes_activated_this_time = set()
    edges_transversed_this_time = set()
    for each_node in activated_Nodes:

      for each_neighbor in G.successors(each_node):
        if each_neighbor in activated_Nodes:
          continue
        active_nodes_surrounding_this_neighbor = list(set(G.predecessors(each_neighbor)).intersection(set(activated_Nodes)))
        if calculate_collective_threshold(G,active_nodes_surrounding_this_neighbor,each_neighbor)>G.node[each_neighbor]['threshold']:
         nodes_activated_this_time.add(each_neighbor)
    nodes_activated_this_time = list(nodes_activated_this_time)
    activated_Nodes.extend(nodes_activated_this_time)
    return activated_Nodes, nodes_activated_this_time


  def calculate_collective_threshold(G, srcs, dest):
    influence_sum = 0.0
    for src in srcs:
      influence_sum += G[src][dest]['prob']
    return influence_sum


#Main Co# de

#create graph from file

  G = nx.read_edgelist(edge_in, nodetype=int, data=(('prob', float),))
  nodes_list = G.nodes()
        
  no_nodes = 0
  node_str = ''
  for i in nodes_list:
      node_str = node_str+'{id: '+str(i)+', label: \''+str(i)+'\', color: \'#42dca3\'},\n'
      no_nodes = no_nodes+1

  for each_node in G.nodes():
    nx.set_node_attributes(G,'threshold', 0.5)

  if not G.is_directed():
   DG = G.to_directed()
  else:
   DG = copy.deepcopy(G)

#Get the seed_List from file
  seed_List = [int(x) for x in open(seedlist).read().splitlines()]
  print(seed_List)
#validations
  for each_node in seed_List:
      if each_node not in G.nodes():
        raise Exception("seed", each_node, "is not in graph")


  activated_Nodes = copy.deepcopy(seed_List)

  influenced_nodes = (start_Influence(DG, activated_Nodes))
  #influenced_nodes_int =  [int(i) for i in influenced_nodes]

  influenced_nodes_int =  [int(i) for i in influenced_nodes]  

  node1_str=''          #node1_str is node_str with seeds colored differently
  for i in nodes_list:
      if ((i) in (influenced_nodes_int)):      
           node1_str = node1_str+'{id: '+str(i)+', label: \''+str(i)+'\', color: \'#df23ee\'},\n'
      else:
           node1_str = node1_str+'{id: '+str(i)+', label: \''+str(i)+'\', color: \'#42dca3\'},\n'
  return str(type(influenced_nodes))+'''

<head>
<script type="text/javascript" src="VIS/dist/vis.js"></script>
<link href="VIS/dist/vis.css" rel="stylesheet" type="text/css" />
<link href="css/grayscale.css" rel="stylesheet" type="text/css" />
<style type="text/css">
    #mynetwork {      width: 100%;      height: 100%;      margin-left: auto;      margin-right: auto;      border: 0px solid lightgray;    }  </style>

<title>Linear Thresholding</title></head>


<body bgcolor="#000000">
<style type="text/css">
body {
    overflow:hidden;
}
</style>
<div style="position: fixed; right: 20%; top: 70%; z-index:100;"><a href="lt_algo?edge_in='''+edge_in+'''&&seedlist='''+seedlist+'''" class="btn btn-default btn-lg" style="padding: 13px;">Rework</a></div>
<div style="position: fixed; right: 20%; top: 78%; z-index:100;"><a href="lt_land?edge_in='''+edge_in+'''&&seedlist='''+seedlist+'''" class="btn btn-default btn-lg" style="padding: 12px;">Go Back</a></div>
<div style="position: fixed; right: 20%; top: 62%; z-index:100;"><a href="index.html#about" class="btn btn-default btn-lg" style="padding: 12px;">Go Home</a></div>


<center>
<div style="position: fixed; border-style: dashed;    width:98%;    height:28%    border-width: 2px;    border-color:#42dca3;    margin-left:auto;    margin-right:auto;  align="center">
<div style="position: fixed; z-index: 9999; margin:50px"><h2><span style="color: #42dca3">Linear Thresholding</span></h2>
<font color="#FFF">Seeds selected: <a id="selectedseedlistdiv">'''+seed_str+'''</a></font>
<!--<br><font color="#FFF">Nodes Clicked: <a id="seedlistdiv"></a></font>-->
<br><br><br><br>
<div style="text-align:justify; padding:20px; border: dashed; width: 400px; border-color: #787;  z-index:100;"><p>The edge weights are the thresholds for getting influenced by neighbours.</p></div>
</div>

<div style="position: fixed; right: 100px; top: 50px; z-index:100;"><font color="#42dca3" size="+1"># of activated Nodes:</font><font color="#fff" size="+1"><br> '''+str(len(influenced_nodes))+'''</font></div>

<div style="position: fixed; left: 70px; bottom: 50px; z-index:100;"><img src="img/ic_legend.png"></div>

<div id="mynetwork"></div>

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