# prometheus_code_examples


**Querying Prometheus:**

Starting at your graphana page:
https://cachai-dashboard.providentiaworldwide.com/d/Kn5xm-gZk2/enclave-rmq?orgId=1&refresh=15s

1)	Click on the metric you want to collect, and press the “e”  key:

 <img width="468" alt="image" src="https://github.com/biffsocko/prometheus_code_examples/assets/5352741/3b51eb7f-aee4-425a-8902-776bd22fd9f5">



2)	This screen will show the query that is needed :
 
<img width="468" alt="image" src="https://github.com/biffsocko/prometheus_code_examples/assets/5352741/cc4de348-27ae-46d5-bae5-df55c2d68d7f">

Note the namespace and the name of the rabbit-mq cluster.  These will be filled into the appropriate space in the query.

3)	For Python, you’ll need the prometheus_api_client:
pip3 install prometheus_api_client


Code examples can be downloaded here:
https://github.com/biffsocko/prometheus_code_examples

