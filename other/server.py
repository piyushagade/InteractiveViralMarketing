import logging
import sys

from flask import Flask
from rocket import Rocket

import networkx as nx
import pandas as pd
from matplotlib.pylab import plt

app = Flask(__name__)
app.debug = True


@app.route("/")
def hello():
     return """
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Grayscale - Start Bootstrap Theme</title>

    <!-- Bootstrap Core CSS -->
    <link href="http://localhost/Greyscale/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom CSS -->
    <link href="http://localhost/Greyscale/css/grayscale.css" rel="stylesheet">

    <!-- Custom Fonts -->
    <link href="font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
    <link href="http://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic" rel="stylesheet" type="text/css">
    <link href="http://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->

</head>

<body id="page-top" data-spy="scroll" data-target=".navbar-fixed-top">

    <!-- Navigation -->
    <nav class="navbar navbar-custom navbar-fixed-top" role="navigation">
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-main-collapse">
                    <i class="fa fa-bars"></i>
                </button>
                <a class="navbar-brand page-scroll hidden" href="#page-top">
                    <i class="fa fa-play-circle"></i>  <span class="light">	Start</span> Bootstrap
                </a>
            </div>

            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse navbar-right navbar-main-collapse">
                <ul class="nav navbar-nav">
                    <!-- Hidden li included to remove active class from about link when scrolled up past about section -->
                    <li class="hidden">
                        <a href="#page-top"></a>
                    </li>
                    <li>
                        <a class="page-scroll" href="#about">Algorithms</a>
                    </li>
                    <li>
                        <a class="page-scroll" href="#download">About Project</a>
                    </li>
                    <li>
                        <a class="page-scroll" href="#contact">Group Info</a>
                    </li>
                </ul>
            </div>
            <!-- /.navbar-collapse -->
        </div>
        <!-- /.container -->
    </nav>

    <!-- Intro Header -->
    <header class="intro">
        <div class="intro-body">
            <div class="container">
                <div class="row">
                    <div class="col-md-8 col-md-offset-2">
                        <h1 class="brand-heading">Project Title</h1>
                        <p class="intro-text">Social Network Computing CIS6930 (2015)</p>
                        <a href="#about" class="btn btn-circle page-scroll">
                            <i class="fa fa-angle-double-down animated"></i>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </header>

    <!-- Algo Section -->
    <section id="about" class="container content-section text-center">
        <div class="row" id="algo_div">
          <div class="col-lg-8 col-lg-offset-2">
            <h2>Select an algorithm</h2>
            <p>Please select one amongst following algorithms to proceed.</p>
            <p><a class="btn btn-default btn-lg" id="jmin_button">J-MIN</a></p>
            <p><a id="p_button" class="btn btn-default btn-lg">Pruned</a></p>
            <p><a id="lt_button" class="btn btn-default btn-lg">Linear threshold</a></p>
            <p><a id="ic_button" class="btn btn-default btn-lg">Independent cascading</a></p>
            
    
            
             </div>
        </div>
        
        
           
<!-- JMin -->
<div id="jmin_div" class="row hidden">

<a  class="pageclose" id="allianzeclose" style="color: #ffffff">&nbsp;<i class="font-icon-remove"></i>&nbsp;</a>
<div class="pagecontainer">
  <table width="95%" border="0">

  <tr>
    <td width="60%"   style="font-size: 16px; vertical-align:text-top; color: #CCCCCC; text-align:justify"><br>
      <p><strong><font color="#42dca3" size="+3">Seed-set Minimization</font></strong><br>
         Here the objective as suggested by Cheng Long et al. is to <a>minimize </a>the <a>number of seeds</a> while at least <em>J</em> users are influenced. The problem is called <em>J</em>-MIN-Seed. Given a set <em>J</em> of seeds, we find the influence incurred by the seed.</p></td>
    <td rowspan="2" >&nbsp;</td>
    <td colspan="2" rowspan="2" valign="top">
      
      <div style="border-style: dashed;    border-width: 3px; border-color:#42dca3">
      <form name="form1" method="post" action="http://localhost/snap.py" ><br><br>
      <center>
      <input class="tb_input" name="file_src" type="text" id="file_src" size="30%" placeholder="Graph Input"><br><br>
      <input class="tb_input" name="file_src" type="text" id="min_inf_nodes" size="30%" placeholder="# of nodes to be influenced">
      <br><br>
      <a class="btn btn-default btn-lg">Process</a></center>
      </form>
      </div>
      </td>
  </tr>
  <tr>
    <td rowspan="2" ><center><a class="btn btn-default btn-lg" id="back_jmin">Go back</a></center></td>
  </tr>
  <tr>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td height="58" colspan="4"></p>
    </td>
    </tr>
  <tr>
    <td>&nbsp;</td>
    <td width="61">&nbsp;</td>
    <td width="161"><center>
    
    
      </center></td>
    <td width="15"></td>
  </tr>
  </table>

</div>
</div>


<!-- IC -->
<div id="ic_div" class="row hidden">

<div class="pagecontainer">
  <table width="95%" border="0">

  <tr>
    <td width="60%"   style="font-size: 16px; vertical-align:text-top; color: #CCCCCC; text-align:justify"><br>
      <p><strong><font color="#42dca3" size="+3">Independent Cascading</font></strong><br>
      In this algorithm for IC model, an active node tries to activate its neighbors with a given <a>probability</a>. Given a directed graph G = (V, E), a propagation probability function p: E → [0, 1], and a vertex set S ⊆ V called a seed set, we first activate vertices in S. Then the process unfolds in discrete steps according to the following randomized rule.
        </p></td>
    <td rowspan="2" >&nbsp;</td>
    <td colspan="2" rowspan="2" valign="top">
      
      <div style="border-style: dashed;    border-width: 3px; border-color:#42dca3">
      <form name="form1" method="post" action="" ><br><br>
      <center>
      <input class="tb_input" name="file_src" type="text" id="file_src" size="30%" placeholder="Graph Input">
      <br><br>
      <input class="tb_input" name="file_src" type="text" id="file_src" size="30%" placeholder="Seed-set size"><br><br>
      <a class="btn btn-default btn-lg">Process</a></center>
      </form>
      </div>
      </td>
  </tr>
  <tr>
    <td rowspan="2" ><center><a class="btn btn-default btn-lg" id="back_ic">Go back</a></center></td>
  </tr>
  <tr>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td height="58" colspan="4"></p>
    </td>
    </tr>
  <tr>
    <td>&nbsp;</td>
    <td width="61">&nbsp;</td>
    <td width="161"><center>
    
    
      </center></td>
    <td width="15"></td>
  </tr>
  </table>

</div>
</div>

<!-- P -->
<div id="p_div" class="row hidden">

<div class="pagecontainer">
  <table width="95%" border="0">

  <tr>
    <td width="60%"   style="font-size: 16px; vertical-align:text-top; color: #CCCCCC; text-align:justify"><br>
      <p><strong><font color="#42dca3" size="+3">Pruned</font></strong><br>
        In this algorithm as proposed by Ohsaka et al. we first generate <a>R</a> random graphs from G, then construct vertex-weighted directed acyclic graphs (DAGs) from these random graphs. The approximate value of marginal influence is then calculated by averaging the total weight of vertices reachable from a single vertex in each DAG.</p></td>
    <td rowspan="2" >&nbsp;</td>
    <td colspan="2" rowspan="2" valign="top">
      
      <div style="border-style: dashed;    border-width: 3px; border-color:#42dca3">
      <form name="form1" method="post" action="" ><br><br>
      <center>
      <input class="tb_input" name="file_src" type="text" id="file_src" size="30%" placeholder="Graph Input"><br><br>
      <input class="tb_input" name="file_src" type="text" id="file_src" size="30%" placeholder="Seed-set size"><br><br>
      <input class="tb_input" name="file_src" type="text" id="min_inf_nodes" size="30%" placeholder="Random graph size">
      <br><br>
      <a class="btn btn-default btn-lg">Process</a></center>
      </form>
      </div>
      </td>
  </tr>
  <tr>
    <td rowspan="2" ><center><a class="btn btn-default btn-lg" id="back_p">Go back</a></center></td>
  </tr>
  <tr>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td height="58" colspan="4"></p>
    </td>
    </tr>
  <tr>
    <td>&nbsp;</td>
    <td width="61">&nbsp;</td>
    <td width="161"><center>
    
    
      </center></td>
    <td width="15"></td>
  </tr>
  </table>

</div>
</div>

<!-- LT -->
<div id="lt_div" class="row hidden">

<div class="pagecontainer">
  <table width="95%" border="0">

  <tr>
    <td width="60%"   style="font-size: 16px; vertical-align:text-top; color: #CCCCCC; text-align:justify"><br>
      <p><strong><font color="#42dca3" size="+3">Linear Thresholding</font></strong><br>
        In LT model, a node is activated only if some portion of its neighbors are already active. An (LT) influence graph is a weighted graph G = (V, E, w), where V is a set of n vertices (nodes) and E ⊆ V × V is a set of m directed edges, and w : V × V → [0, 1] is a weight function such that w (u, v) = 0 if and only if (u, v) ∈ E, 1 P and u∈V w(u, v) ≤ 1.</p></td>
    <td rowspan="2" >&nbsp;</td>
    <td colspan="2" rowspan="2" valign="top">
      
      <div style="border-style: dashed;    border-width: 3px; border-color:#42dca3">
      <form name="form1" method="post" action="" ><br><br>
      <center>
      <input class="tb_input" name="file_src" type="text" id="file_src" size="30%" placeholder="Graph Input"><br><br>
      <input class="tb_input" name="file_src" type="text" id="file_src" size="30%" placeholder="Seed-set size"><br><br>
      <a class="btn btn-default btn-lg">Process</a></center>
      </form>
      </div>
      </td>
  </tr>
  <tr>
    <td rowspan="2" ><center><a class="btn btn-default btn-lg" id="back_lt">Go back</a></center></td>
  </tr>
  <tr>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td height="58" colspan="4"></p>
    </td>
    </tr>
  <tr>
    <td>&nbsp;</td>
    <td width="61">&nbsp;</td>
    <td width="161"><center>
    
    
      </center></td>
    <td width="15"></td>
  </tr>
  </table>

</div>
</div>
        
        
        
    </section>

    <!-- Download Section -->
    <section id="download" class="content-section text-center">
        <div class="download-section">
            <div class="container">
              <div class="col-lg-8 col-lg-offset-2">
                <h2>About the project</h2>
                <p>Grayscale is a free Bootstrap 3 theme created by Start Bootstrap. It can be yours right now, simply download the template on <a href="http://startbootstrap.com/template-overviews/grayscale/">the preview page</a>. The theme is open source, and you can use it for any purpose, personal or commercial.</p>
                <p>This theme features stock photos by <a href="http://gratisography.com/">Gratisography</a> along with a custom Google Maps skin courtesy of <a href="http://snazzymaps.com/">Snazzy Maps</a>.</p>
                <p>Grayscale includes full HTML, CSS, and custom JavaScript files along with LESS files for easy customization.</p>
              </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="container content-section text-center">
        <div class="row">
          <div class="col-lg-8 col-lg-offset-2">
            <h2><em>About the group</em></h2>
            <p><em>Group members include<br>
              <a href="mailto:feedback@startbootstrap.com">Swati Sisodia (<span style="color: #FFFFFF">04065889</span>)</a><br>
              <a href="mailto:feedback@startbootstrap.com">Maithili Gokhale (<span style="color: #FFFFFF">91353676</span>)</a><br>
              <a href="mailto:feedback@startbootstrap.com">Aman Chanana (<span style="color: #FFFFFF">35611337</span>)</a><br>
              <a href="mailto:feedback@startbootstrap.com">Piyush Agade (<span style="color: #FFFFFF">03108663</span>)</a></em>            </p>
            <ul class="list-inline banner-social-buttons">
              <li> <em><a href="https://twitter.com/SBootstrap" class="btn btn-default btn-lg"> <span class="network-name">Twitter</span></a> </em></li>
              <li> <em><a href="https://github.com/IronSummitMedia/startbootstrap" class="btn btn-default btn-lg"> <span class="network-name">Github</span></a> </em></li>
              <li> <em><a href="https://plus.google.com/+Startbootstrap/posts" class="btn btn-default btn-lg"> <span class="network-name">Google+</span></a> </em></li>
            </ul>
          </div>
        </div>
    </section>

    <!-- Map Section -->
    <div id="map"></div>

    <!-- Footer -->
    <footer>
        <div class="container text-center">
            <p>Group # 4, CIS 6930, Social Network Computing</p>
        </div>
    </footer>

    <!-- jQuery -->
    <script src="http://localhost/Greyscale/js/jquery.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="http://localhost/Greyscale/js/bootstrap.min.js"></script>

    <!-- Plugin JavaScript -->
    <script src="http://localhost/Greyscale/js/jquery.easing.min.js"></script>

    <!-- Google Maps API Key - Use your own API key to enable the map feature. More information on the Google Maps API can be found at https://developers.google.com/maps/ -->
    <script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCRngKslUGJTlibkQ3FkfTxj3Xss1UlZDA&sensor=false"></script>

    <!-- Custom Theme JavaScript -->
    <script src="http://localhost/Greyscale/js/grayscale.js"></script>
 
 
<script>
 
 $('#jmin_button1').click(function(){
 $.ajax({

    type: "POST",
    url: "http://localhost/snap.py",
    data: { param: " "}
    }).done(function( o ) {
        alert("OK");
});
});
 
 </script>
 
 
 

</body>

</html>


     """



def run_server():
    # Setup logging
    log = logging.getLogger('Rocket')
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler(sys.stdout))

    # Set the configuration of the web server
    server = Rocket(interfaces=('0.0.0.0', 5000), method='wsgi',
                    app_info={"wsgi_app": app})

    # Start the Rocket web server
    server.start()

if __name__ == "__main__":
    run_server()