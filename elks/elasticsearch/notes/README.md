SECTION 1:
---------
    # What's Elasticsearch and why we use it?
        - Elastic Stack is a group of products that can reliably and securely take data from any source, in any format, then search, analyze, and visualize it in real-time.             
        - Elasticsearch is a distributed, RESTful search and analytics engine that can address a huge number of use cases. 
        - Elasticsearch also considered as the heart of the Elastic Stack.
        - It centrally stores user data for high-efficiency search, excellent   relevancy, and powerful analytics that is highly scalable.
        - Elasticsearch is a distributed and document-oriented database. It stores complex data structures into serialized JSON documents.
        - You can simply compare it with other NoSQL databases that use documents or documents inside a collection.
        - When storing data instead of in the traditional schema structure that uses tables, columns, and rows of a relational database.
        
SECTION 2:
---------
    # Deploying Elasticsearch using Dockers
        - First we have to create the Docker network to pull the Docker Elasticsearch image.

        - TO create Docker network
            docker network create <elastic>
        
        1. Pull the Elasticsearch Docker image
            docker pull docker.elastic.co/elasticsearch/elasticsearch:7.17.7

        2.  Now we can create a Docker container for Elasticsearch
            docker run --name <elasticsearch> --net<elastic> -p 9200:9200 docker.elastic.co/elasticsearch/elasticsearch:7.17.7

        - 9200 is default port number for Elasticsearch
        - Now we can access Elasticsearch UI using localhost:9200 or vmip:9200

SECTION 3:
---------
    # Deploying Elasticsearch using Kubernetes
        - First create the name space for elasticsearch

        - To create the name space
            kubectl create namespace <elastic>

        - To check the name space weather it is create or not by using below command
            kubectl get namespace

        1. Deployment spec
            - Create the deployment yml file for elasticsearch
                vi deploy.yml

            - To run the deployment
                kubectl create -f deploy.yml -n <elastic>  

            - Check the deployment by using below command
                kubectl get deployments -n <namespece> 

            - Check the pods by using below command   
                kubectl get pods -n <namespece>   

        2. Service spec
            - Create service yml file for elasticsearch
                vi serv.yml

            - To run the service
                kubectl create -f serv.yml -n <elastic> 

            - Check the svc by using below command
                kubectl get deployments -n <namespece> 

            - Check the pods by using below command   
                kubectl get pods -n <namespece>   

            - elasticsearch UI Access using localhost:port or VM_IP:9200
                     
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
    # Elasticsearch Deployment spec
             apiVersion: apps/v1
             kind: Deployment
             metadata:
              namespace: elk
              name: elasticsearch
             spec:
              selector:
               matchLabels:
                component: elasticsearch
              template:
                metadata:
             labels:
               component: elasticsearch
             spec:
             containers:
                name: elasticsearch
                image: docker.elastic.co/elasticsearch/elasticsearch:7.17.7
             ports:
              containerPort: 9200
              name: http
              protocol: TCP
              resources:
             limits:
              cpu: 100m
              memory: 1Gi
             requests:
              cpu: 100m
              memory: 1Gi
SECTION 5:
----------
    # Elasticsearch Service spec
             apiVersion: v1
             kind: Service
             metadata:
              namespace: elk
              name: elasticsearch
              labels:
               service: elasticsearch
             spec:
              type: NodePort
             selector:
              component: elasticsearch
             ports:
              port: 9200
              targetPort: 9200
SECTION 6:
----------
    # Verification post installation

        1.Access Elasticsearch in UI
            - we can access Elasticsearch in two ways
                - By using VMIP:ContainerPortNo (9200)
                - By using VMIP:NodePortNo

        2.CREATE/DELETE/UPDATE Indexes

            - What are indexes in Elasticsearch?
                - Elasticsearch index is a collection of related JSON documents.
                - An index is like a 'database' in a relational database. 
                - Elasticsearch => Indices => Types => JSON Documents with Properties

            - CREATE --> Create an index
                -  By using the PUT request to create a new index

            - UPDATE --> Update an index an index
                - Elasticsearch documents are immutable.
                - When you update an existing document a new document is created with an incremented_version the old document is marked for deletion

                    {
                    "doc": {
                        "title": "elasticsearch"     # Update the elasticsearch
                    }
                    } 
             
            - DELETE --> Delete an index
                - Once you have the index you wish to remove from Elasticsearch, use the DELETE request followed by the index name.
                     DELETE /index_name

        3. kubectl commands for Elasticsearch

            - Using below command we can see pod is available or not in required namespace
                kubectl get pod <pod-name> -n <namespace-name>

            - Using below command we can see service is available or not in required namespace
                kubectl get svc <svc-name> -n <namespace-name>  
       
          - Using below command we can see deployment is available or not in required namespace
                kubectl get deployment <deployment-name> -n <namespace-name>              
SECTION 7:
---------
     # Elasticsearch UI Access
        - http://10.74.190.111:9200

SECTION 8:
----------

    # REST API Commands for all CRUD
        - Create an Index in elasticsearch by using below command
        curl -XPUT "http://10.74.190.111:9200/emp_data" 

    - To verify Index created or not by using below command
        curl -XGET "http://10.74.190.111:9200/emp_data" 

    - Insert our date into our index by using below command
        curl -XPOST "http://10.74.190.111:9200/emp_data/_doc/1" -H 'Content-Type: application/json' -d' 
        {
        "Student_name": "Maneesh",
        "subects": "Maths","physics",
        "Age": 19,
        "Gender": "male",
        "Address": "Hyderabad"
        }'  

    - Update data in to our index by using below command
        curl -XPOST "http://10.74.190.111:9200/emp_data/_doc/1" -H 'Content-Type: application/json' -d'
        {
        "student_name": "Maneesh",
        "subjects": "Maths","Physics","chemistry"     # Update subjects
        "Age": 19,
        "Gender": "male",
        "Address": "Hyderabad"
        }' 

    - Delete in our index by using below command
        curl -XDELETE "http://10.74.190.111:9200/emp_data"  

    - Bulk API for Multiple Document Indexing and Modification
        - Create bulk indexes:
            curl -XPOST "http://10.74.190.111:9200/_bulk" -H 'Content-Type: application/json' -d' 
            {"create" : {"_index":"std_data", "_id":"1"}}
            {"name":"Ram", "std_id":"867", "dob":"2003","branch":"MPC", "address":"hyderabad", "age":"18"}
            {"create" : {"_index":"std_data", "_id":"2"}}
            {"name":"krishna", "std_id":"094", "dob":"2002","branch":"Bipc", "address":"hyderabad", "age":"17"}
            {"create" : {"_index":"std_data", "_id":"3"}}
            {"name":"Venkat", "std_id":"894", "dob":"1999","branch":"mechnical", "address":"guntur", "age":"22"}
            {"create" : {"_index":"std_data", "_id":"4"}}
            {"name":"Zenith", "std_id":"632", "dob":"1998","branch":"mechnical", "address":"chennai", "age":"21"}
            {"create" : {"_index":"std_data", "_id":"5"}}
            {"name":"Bharath", "std_id":"326", "dob":"1999","branch":"civil", "address":"chitoor", "age":"22"}
            {"create" : {"_index":"std_data", "_id":"6"}}
            {"name":"Kiran", "std_id":"789", "dob":"1997","branch":"cse", "address":"nellore", "age":"22"}

        - Update bulk indexes:
            curl -XPOST "http://10.74.190.111:9200/_bulk" -H 'Content-Type: application/json' -d' 
            {"update" : {"_index":"std_data", "_id":"3"}}
            {"doc": {"branch":"civil"}}
            {"update" : {"_index":"std_data", "_id":"5"}}
            {"doc": {"address":"nellore"}}
            {"update" : {"_index":"std_data", "_id":"6"}}
            {"doc": {"branch":"electronics"}}
            {"update" : {"_index":"std_data", "_id":"4"}}
            {"doc": {"age":"23"}}
            {"update" : {"_index":"std_data", "_id":"2"}}
            {"doc": {"dob":"2003"}}   

        - Delete bulk indexes:   
            curl -XPOST "http://10.74.190.111:9200/_bulk" -H 'Content-Type: application/json' -d'
            {"delete" : {"_index":"std_data", "_id":"1"}}
            {"delete" : {"_index":"std_data", "_id":"4"}}
            {"delete" : {"_index":"std_data", "_id":"6"}}
            {"delete" : {"_index":"std_data", "_id":"3"}}
            {"delete" : {"_index":"std_data", "_id":"2"}}
            {"delete" : {"_index":"std_data", "_id":"5"}}    

        - Search bulk indexes:
            curl -XGET "http://10.74.190.111:9200/_bulk" -H 'Content-Type: application/json' -d'
            {
                "query": {
                    "match_all": {}
            }
            }

    Performs multiple Indexing, Updating, Deleting operations in a single API call:
        curl -XPOST "http://10.74.190.111:9200/_bulk" -H 'Content-Type: application/json' -d'
        {"create":{"_index":"std_data", "_id":"6"}}
        {"name":"uday","branch":"civil"}
        {"delete":{"_index":"student", "_id":"3"}}
        {"update":{"_index":"std_data","_id":"4"}}
        {"name":"charan,"branch":"cse"}                          
SECTION 9:
----------
    # References 
        - https://linuxhint.com/elasticsearch-create-index/  
        - https://www.youtube.com/watch?v=Uo_Avtu_aY4 
        - https://dev.to/elastic/performing-crud-operations-with-elasticsearch-kibana-50ka                            
               