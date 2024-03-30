# prometheus_code_examples

Word Document with pictures: https://drop.biffsocko.com/monitoring/Querying_Prometheus.docx


Querying Prometheus:
Starting at:
https://cachai-dashboard.providentiaworldwide.com/d/Kn5xm-gZk2/enclave-rmq?orgId=1&refresh=15s

1)	Click on the metric you want to collect, and press the “e”  key:

 


2)	This screen will show the query that is needed :
 

Note the namespace and the name of the rabbit-mq cluster.  These will be filled into the appropriate space in the query.

3)	For Python, you’ll need the prometheus_api_client:
pip3 install prometheus_api_client


Code examples can be downloaded here:
https://github.com/biffsocko/prometheus_code_examples

![image](https://github.com/biffsocko/prometheus_code_examples/assets/5352741/146df825-c98c-480f-b965-0d7993f02e74)
