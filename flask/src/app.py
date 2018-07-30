from flask import Flask,request,render_template
import json
import logging 
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch([{'host': 'elasticsearch', 'port': 9200}])

@app.route('/hello',methods=["GET","POST"])
def hello():
	if request.method=='POST':
		p = json.dumps(request.json)
		print (p)
		c = "clientip"
		ans = es.search(index='tomcat-2018.07.29',doc_type='doc',body={"_source": { "includes": ["clientip","date"]},"query": {"match": {'clientip':'172.18.0.1'}},"filter": [{"range": {"@timestamp": {"from":"now-30s"}}}]})
		logging.info(ans)
		return "p"

if __name__ == '__main__':
	logging.basicConfig(filename='/src/Applog.log',format='%(asctime)s %(message)s', level=logging.INFO)
	app.run(host='0.0.0.0',port=5000,debug=True)

