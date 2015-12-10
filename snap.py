import random
import string
import pandas as pd
import cherrypy
import time
import re           # Sentence Replacement
import os           # Working Path
import sys
import unicodedata
from lib import ic, jmin, lt, p
     
path   = os.path.abspath(os.path.dirname(__file__))
WEB_ROOT = path+'/gui'
     
pathname = os.path.dirname(sys.argv[0])        
path =  os.path.abspath(pathname)
path = path.encode('utf8')
path = re.sub(r'\b\\\b', '/', path)

with open (WEB_ROOT+"/index.html", "r") as myfile:
    webpage=myfile.read()
    webpage = re.sub(r'\b(my_path)\b', WEB_ROOT, webpage)

current_nodes = ''
current_edges = ''
current_no_nodes = 0

#print no_nodes
#print node_str
#print edge_str
#print node_str[26+60]

class SocialNetworkProject(object):
    @cherrypy.expose
    def index(self):
        return webpage

#   Independent Cascading
    @cherrypy.expose
    def ic_land(self, edge_in='0', seedlist='0'):  
        wp = ic.land(edge_in, seedlist)
        return wp
       
    @cherrypy.expose
    def ic_algo(self, edge_in='0', seedlist='0'):
        wp = ic.algo(edge_in, seedlist)
        return wp

#   LT   
    @cherrypy.expose
    def lt_land(self, edge_in='0', seedlist='0'):  
        wp = lt.land(edge_in, seedlist)
        return wp
        
    @cherrypy.expose
    def lt_algo(self, edge_in='0', seedlist='0'):
        wp = lt.algo(edge_in, seedlist)
        return wp 

#   J-Min   
    @cherrypy.expose
    def jmin_land(self, edge_in='0', desiredNum=0):  
        wp = jmin.land(edge_in, desiredNum)
        return wp
        
    @cherrypy.expose
    def jmin_algo(self, edge_in='0', desiredNum=0):
        wp = jmin.algo(edge_in, desiredNum)
        return wp   

#   P  
    @cherrypy.expose
    def p_land(self, edge_in='0',  k=0):  
        wp = p.land(edge_in, k)
        return wp
        
    @cherrypy.expose
    def p_algo(self, edge_in='0', k=0):
        wp = p.algo(edge_in, k)
        return wp

if __name__ == '__main__':
                        
    conf = { '/':
  { 
    'tools.staticdir.on' : True,
    'tools.staticdir.dir' : WEB_ROOT,
    'tools.staticdir.index' : 'index.html' }
  }
    cherrypy.config.update({'server.socket_host': '127.0.0.1','server.socket_port': 8080}) 
    cherrypy.quickstart(SocialNetworkProject(), config = conf)