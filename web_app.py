#!/usr/bin/env python
import cherrypy
import json
import os.path, os


from redis_storage import redis_data_store

class NiftyData(object):

	@cherrypy.expose
	def index(self):
		required_data1 = redis_data_store('https://www.nseindia.com/live_market/dynaContent/live_analysis/gainers/niftyGainers1.json')
		required_data2 = redis_data_store('https://www.nseindia.com/live_market/dynaContent/live_analysis/losers/niftyLosers1.json')
 		

		json_data1 = json.loads(required_data1)['data']
		json_data2 = json.loads(required_data2)['data']
		#json_data2 = json.loads(required_data1)
		#print json_data[0]['symbol']
		#print len(json_data)

		gainers = []
		for i in range(len(json_data1)):
			gainers.append(json_data1[i]['symbol'])

		losers = []
		for j in range(len(json_data2)):
			losers.append(json_data2[j]['symbol'])


		# return """<html>
  #         <head>

  #         	<script type="text/javascript" src=" + data.js + "></script>
  #           <script type="text/javascript" src="/static/jquery.min.js"></script>
  #           <script type="text/javascript" src="/static/data.js"></script>
  #           <link href="/static/style.css" rel="stylesheet">
  #         </head>
  #         <body>
  #           <p>this is to test css</p>
  #         </body>
  #       </html>""".format(**locals())




  # <script type="text/javascript" src="static/js/data.js"></script>
				
		# 	    <link href="/static/css/style.css" rel="stylesheet">


		return """ <!DOCTYPE html>
			<html lang="en">

			<head>
			    <title>Visualisation of NSE Data</title>
			    <!-- Bootstrap Core CSS -->
			    
			    <link href="/static/css/style.css" rel="stylesheet">
			    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
			    <script type="text/javascript" src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
			    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
			    
			</head>

			<body>

			    <!-- Page Content -->
			    <div class="container">

			        <!-- Page Heading -->
			        <div class="row">
			            <div class="col-lg-10">
			                <h1 class="page-header">TOP GAINERS</h1>
			            </div>
			        </div>
			        <!-- /.row -->

			        <!-- Projects Row -->
			        <div class="row">


			            <div class="col-md-2 portfolio-item" onclick='alert(\"HAHAHA\")'">
			                    <div class="well">
			                        <h4><span class="label pull-right"></span>{gainers[0]}</h4>
			                    </div>
			            </div>

			            <div class="col-md-2 portfolio-item">
			                    <div class="well">
			                        <h4><span class="label pull-right"></span>{gainers[1]}</h4>
			                    </div>
			            </div>

			            <div class="col-md-2 portfolio-item">
			                    <div class="well">
			                        <h4><span class="label pull-right"></span>{gainers[2]}</h4>
			                    </div>
			            </div>

			            <div class="col-md-2 portfolio-item">
			                    <div class="well">
			                        <h4><span class="label pull-right"></span>{gainers[3]}</h4>
			                    </div>
			            </div>

			            <div class="col-md-2 portfolio-item">
			                    <div class="well">
			                        <h4><span class="label pull-right"></span>{gainers[4]}</h4>
			                    </div>
			            </div>

			        </div>
			        <!-- /.row -->

			        <!-- Projects Row -->
			        <div class="row">
			            <div class="col-md-2 portfolio-item">
			                    <div class="well">
			                        <h4><span class="label pull-right"></span>{gainers[5]}</h4>
			                    </div>
			            </div>

			            <div class="col-md-2 portfolio-item">
			                    <div class="well">
			                        <h4><span class="label pull-right"></span>{gainers[6]}</h4>
			                    </div>
			            </div>

			            <div class="col-md-2 portfolio-item">
			                    <div class="well">
			                        <h4><span class="label pull-right"></span>{gainers[7]}</h4>
			                    </div>
			            </div>

			            <div class="col-md-2 portfolio-item">
			                    <div class="well">
			                        <h4><span class="label pull-right"></span>{gainers[8]}</h4>
			                    </div>
			            </div>

			            <div class="col-md-2 portfolio-item">
			                    <div class="well">
			                        <h4><span class="label pull-right"></span>{gainers[9]}</h4>
			                    </div>
			            </div>

			        </div>
			        <!-- /.row -->

			        <div class="row">
			            <div class="col-lg-10">
			                <h1 class="page-header">TOP LOSERS</h1>
			            </div>
			        </div>

			        <!-- Projects Row -->
			        <div class="row">
			            <div class="col-md-2 portfolio-item">
			                    <div class="well">
			                        <h4 class="text-danger"><span class="label pull-right"></span>{losers[0]}</h4>
			                    </div>
			            </div>

			            <div class="col-md-2 portfolio-item">
			                    <div class="well">
			                        <h4 class="text-danger"><span class="label pull-right"></span>{losers[1]}</h4>
			                    </div>
			            </div>

			            <div class="col-md-2 portfolio-item">
			                    <div class="well">
			                        <h4 class="text-danger"><span class="label pull-right"></span>{losers[2]}</h4>
			                    </div>
			            </div>

			            <div class="col-md-2 portfolio-item">
			                    <div class="well">
			                        <h4 class="text-danger"><span class="label pull-right"></span>{losers[3]}</h4>
			                    </div>
			            </div>

			            <div class="col-md-2 portfolio-item">
			                    <div class="well">
			                        <h4 class="text-danger"><span class="label pull-right"></span>{losers[4]}</h4>
			                    </div>
			            </div>

			        </div>
			        <!-- /.row -->

			        <div class="row">
			            <div class="col-md-2 portfolio-item">
			                    <div class="well">
			                        <h4 class="text-danger"><span class="label pull-right"></span>{losers[5]}</h4>
			                    </div>
			            </div>

			            <div class="col-md-2 portfolio-item">
			                    <div class="well">
			                        <h4 class="text-danger"><span class="label pull-right"></span>{losers[6]}</h4>
			                    </div>
			            </div>

			            <div class="col-md-2 portfolio-item">
			                    <div class="well">
			                        <h4 class="text-danger"><span class="label pull-right"></span>{losers[7]}</h4>
			                    </div>
			            </div>

			            <div class="col-md-2 portfolio-item">
			                    <div class="well">
			                        <h4 class="text-danger"><span class="label pull-right"></span>{losers[8]}</h4>
			                    </div>
			            </div>

			            <div class="col-md-2 portfolio-item">
			                    <div class="well">
			                        <h4 class="text-danger"><span class="label pull-right"></span>{losers[9]}</h4>
			                    </div>
			            </div>

			        </div>

			    </div>
			    <!-- /.container -->



			</body>

			</html>

 """.format(**locals())


	@cherrypy.expose
	def innerData(self):
		return "this is the detailed data..." 



if __name__ == '__main__':
	conf = {
	        '/': {
	            'tools.sessions.on': True,
	            'tools.staticdir.root': os.path.abspath(os.getcwd())
	        },
	        '/static': {
	            'tools.staticdir.on': True,
	            'tools.staticdir.dir': './public'
	        }
	    }

	cherrypy.quickstart(NiftyData(), '/', conf)
	#cherrypy.quickstart(NiftyData())
