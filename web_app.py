#!/usr/bin/env python
import cherrypy
import json
import os.path, os


from redis_storage import redis_data_store
#import redis_storage

class NiftyData(object):
#	r = redis.StrictRedis(host='localhost', port=6379, db=

	@cherrypy.expose
	def index(self):
		required_data1 = redis_data_store('https://www.nseindia.com/live_market/dynaContent/live_analysis/gainers/niftyGainers1.json')
		required_data2 = redis_data_store('https://www.nseindia.com/live_market/dynaContent/live_analysis/losers/niftyLosers1.json')
		#print required_data1
 

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


		return """ <!DOCTYPE html>
			<html lang="en">

			<head>
			    <title>Visualisation of NSE Data</title>
			    <!-- Bootstrap Core CSS -->
			    

			    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
			    <script type="text/javascript" src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
			    <script type="text/javascript" src="static/js/data.js"></script>
				
			    <link href="/static/css/style.css" rel="stylesheet">
			</head>

			<body>

			    <!-- Page Content -->
			    <div class="container">

			        <!-- Page Heading -->
			        <div class="row">
			            <div class="col-lg-12">
			                <h1 class="page-header">Top Gainers</h1>
			            </div>
			        </div>
			        <!-- /.row -->

			        <!-- Projects Row -->
			        <div class="row">


			            <div class="col-md-2 portfolio-item" onclick="alert('you clicked it');">
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
			            <div class="col-lg-12">
			                <h1 class="page-header">Top Losers</h1>
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

			    <!-- jQuery -->
			    <script src="js/jquery.js"></script>

			    <!-- Bootstrap Core JavaScript -->
			    <script src="js/bootstrap.min.js"></script>

			</body>

			</html>

 """.format(**locals())



# path   = os.path.abspath(os.path.dirname(__file__))
# config = {
#   'global' : {
#     'server.socket_host' : '127.0.0.1',
#     'server.socket_port' : 8080,
#     'server.thread_pool' : 8
#   },
#   '/js' : {
#     'tools.staticdir.on'  : True,
#     'tools.staticdir.dir' : os.path.join(path, 'js')
#   }
# }


if __name__ == '__main__':
	# current_dir = os.path.dirname(os.path.abspath(__file__)) + os.path.sep

	# '/' = {
	# 	'tools.staticdir.root': current_dir,
	# },

	config = {

		'/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        }
	}

	cherrypy.quickstart(NiftyData(), '/', config)
