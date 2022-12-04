SECTION 1:
---------
    # What's Prometheus and why we use it?
        - Prometheus is a high-scalable open-source monitoring framework. 
        - It provides out of the box monitoring capabilities for the Kubernetes container orchestration platform. 
        - Prometheus requires an exposed HTTP endpoint. 
        - Once an endpoint is available,Prometheus can start scraping numerical data.
        - Prometheus comes with PromQL a very flexible query language that can be used to query the metrics in the Prometheus dashboard.
        - Also the PromQL query will be used by Prometheus UI and Grafana to visualize metrics. 
        - Prometheus Exporters are libraries that convert existing metrics from third-party apps to Prometheus metrics format. 
        - There are many official and community Prometheus exporters. 
        - One example is the Prometheus node exporter. 
        - It exposes all Linux system-level metrics in Prometheus format.
        - Prometheus uses TSDB (time-series database) for storing all the data efficiently.

SECTION 2:
---------
    # Deploying Prometheus using Dockers
        - First we have to create the Docker network to pull the Docker Prometheus image.

        - TO create Docker network
            docker network create <monitoring>
        
        1. Pull the Prometheus Docker image
            docker pull docker.prom.co/Prometheus/Prometheus:latestversion

        2.  Now we can create a Docker container for Prometheus
            docker run --name <Prometheus> --net<monitoring> -p 9090:9090 docker.prom.co/Prometheus/Prometheus:latestversion

        - 9090 is default port number for Prometheus
        - Now we can access Prometheus UI using localhost:9090 or vmip:9090

SECTION 3:
---------
    # Deploying Prometheus using Kubernetes
        - First create the name space for Prometheus

        - To create the name space
            kubectl create namespace <monitoring>

        - To check the name space weather it is create or not by using below command
            kubectl get namespace

        1. Deployment spec
            - Create the deployment yml file for Prometheus
                vi deploy.yml

            - To run the deployment
                kubectl create -f deploy.yml -n <namespace>  

            - Check the deployment by using below command
                kubectl get deployments -n <namespece> 

            - Check the pods by using below command   
                kubectl get pods -n <namespece>   

        2. Service spec
            - Create service yml file for Prometheus
                vi serv.yml

            - To run the service
                kubectl create -f serv.yml -n <namespace> 

            - Check the svc by using below command
                kubectl get deployments -n <namespece> 

            - Check the pods by using below command   
                kubectl get pods -n <namespece>   

            - Prometheus UI Access using localhost:port or VM_IP:9090
                     
        3. kubectl commands for debug 

             kubectl describe  pod <pod-name> -n <namespace-name>

            - Edit pod by using below command
                kubectl edit  pod <pod-name> -n <namespace-name>

            - Describe the service by using below command
                kubectl describe  svc <svc-name> -n <namespace-name>  

            - Edit Service by using below command
                kubectl edit  svc <svc-name> -n <namespace-name> 

SECTION 4:
----------
    # Prometheus Deployment spec

        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: prometheus
          namespace: monitoring
        spec:
          replicas: 1
          selector:
            matchLabels:
             app: prometheus
         template:
           metadata:
              labels:
                app: prometheus
         spec:
          containers:
          - name: prometheus
            image: prom/prometheus
            volumeMounts:
            - name: config-volume
              mountPath: /etc/prometheus/prometheus.yml
              subPath: prometheus.yml
            ports:
            - containerPort: 9090
            volumes:
            - name: config-volume
            configMap:
              name: prometheus-config
            serviceAccountName: monitor    

SECTION 5:
----------
    # Prometheus Service spec
    
        apiVersion: v1
        kind: Service
        metadata:
          name: prometheus
          namespace: monitoring
        spec:
          selector:
            app: prometheus
        ports:
        - name: promui
          nodePort: 39090
          protocol: TCP
          port: 9090
          targetPort: 9090
        type: NodePort   
        
SECTION 6:
----------
    # Verification post installation

        1.Access Prometheus in UI
            - we can access Prometheus in two ways
                - By using VMIP:ContainerPortNo (9090)
                - By using VMIP:NodePortNo    

        2.Deploying Sample metrics manually    
            - Prometheus uses a pull model to collect these metrics.
            - Prometheus scrapes HTTP endpoints that expose metrics. 
            - Those endpoints can be natively exposed by the component being monitored or exposed via one of the hundreds of Prometheus exporters built by the community.

        3. kubectl commands for Prometheus

            - Using below command we can see pod is available or not in required namespace
                kubectl get pod <pod-name> -n <namespace-name>

            - Using below command we can see service is available or not in required namespace
                kubectl get svc <svc-name> -n <namespace-name>  
       
          - Using below command we can see deployment is available or not in required namespace
                kubectl get deployment <deployment-name> -n <namespace-name> 

SECTION 7:
---------
     # Prometheus UI Access
        - http://10.74.190.111:9090

SECTION 8:
----------

    # REST APIs to interact with Prometheus                                                                            
    - Create an metrics in pometheus by using below command
        curl -XPUT "http://10.74.190.111:9090/emp_data" 

    - Verify metrics created or not by using below command
        curl -XGET "http://10.74.190.111:9090/emp_data"

        checkoutsTotal = new Prometheus.Counter({
        name: 'checkouts_total',
        help: 'Total number of checkouts',
        labelNames: ['payment_method']
        })

    - Update data in to our metrics by using below command
        curl -XPOST "http://10.74.190.111:9090/emp_data/_doc/1" -H 'Content-Type: application/json' -d' 

        checkoutsTotal.inc({
        payment_method: paymentMethod
        })   

    - Delete in our metrics by using below command
        - you need to delete a metric from all scrape job (if there were multiple).
            curl -X POST -g 'http://10.74.190.111:9090/api/v1/admin/tsdb/delete_series?match[]=prometheus_http_requests_total'

        - In case you need to delete a metric from a specific scrape job, you can mention the job label
            curl -X POST -g 'http://10.74.190.111:9090/api/v1/admin/tsdb/delete_series?match[]=prometheus_http_requests_total{job="prometheus"}'   

            
SECTION 9:
----------
    # References   
        - https://prometheus.io/docs/prometheus/latest/getting_started/          
        - https://faun.pub/how-to-drop-and-delete-metrics-in-prometheus-7f5e6911fb33  
        - https://www.npmjs.com/package/prometheus-api-metrics       
        