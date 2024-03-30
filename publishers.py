#!/usr/bin/env python3

from prometheus_api_client import PrometheusConnect

# Replace this URL with the actual URL of your Prometheus server
prometheus_url = 'http://enclave-prometheus.upscale.providentiaworldwide.com:9090/'

# Initialize the Prometheus connection
prom = PrometheusConnect(url=prometheus_url, disable_ssl=True)

# Variables to be used in the query
rabbitmq_cluster = "rabbitmq.devA"  # Replace with your actual RabbitMQ cluster name
namespace = "enclave-rmq"  # Replace with your actual namespace

# Your Prometheus query
query =f"""
sum(rabbitmq_global_publishers * on(instance) group_left(rabbitmq_cluster) rabbitmq_identity_info{{rabbitmq_cluster="rabbitmq.devA", namespace="enclave-rmq"}})
"""


# Execute the query
result = prom.custom_query(query=query)

# Print the results
print(result)

