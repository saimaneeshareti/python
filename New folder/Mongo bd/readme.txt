# AIM: 
. Deploy MongoDB Deployment POD and a Service for that POD

# Pre-requisites
1. kubernetes Deployment
2. kubernetes Node-Port service

# Section 1:
*************
# What is MongoDB?
. MongoDB is a document-oriented NoSQL database used for high volume data storage.
. In MongoDB server you can start and then create multiple databases. 
. MongoDB makes use of collections and documents.
. Inside of the collection we have documents. 
. These documents contain the data we want to store in the MongoDB database.
. Documents consist of key-value pairs which are the basic unit of data in MongoDB.
. The data stored in the MongoDB is in the format of BSON documents. 
. BSON stands for Binary representation of JSON documents.

# Section 2:
*************
# What is Node-port K8s service and why we use it?
- Node-Port in k8s service:
**************************
. Node-Port is the port on the node where pod is running.We use this port along with node ip to access the app from your browser.
. Here we have 2-things 
  1.Node IP
  2.Node Port
. If we are defining the node port manually in the mainfest file
. Then make sure you define the node port in the range of 30000 to 32767
. Any number you can define outside of this range can not be node port.
. In case if you don't menction node port specifically in manifest file the k8s will assign unuse nodeport with in that range dynamically.  

- Uses of Node-Port:
*********************
. It is an open port on every node of your cluster. 
. Kubernetes transparently routes incoming traffic on the NodePort to your service,even if your application is running on a different node.

# Section 3:
*************
# Kubernetes Pod :
- Pod is a smallest object
- pod is create one or more Containers
- Inside the pod container is Running
- Mostly using single pod, single container
- Single node we can create the multi pods
- In siple words pod is nothing but replicas

# Kubernetes Deployments :
- Deployment nothing but configuration about your number of replicas, Name of images, Resources like cpu, ram, storage
- Deployment is managing of the our pods
- We will create number of pods to create create a single deployment by using the replica number.

# Section 4:
*************
- Create a deployment for mongodb
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
  app: mongo
  name: mongo
  namespace: mongodb
spec:
  replicas: 1
  selector:
   matchLabels:
    app: mongo
  template:
    metadata:
      labels:
        app: mongo
    spec:
      containers:
        - name: vude-mongo-c
          image: mongo:4.4.6
          env:
          - name: MONGO_INITDB_ROOT_USERNAME
            value: vudeadmin
          - name: MONGO_INITDB_ROOT_PASSWORD
            value: vudeshardis001
          - name: MONGO_INITDB_DATABASE
            value: admin
          imagePullPolicy: IfNotPresent
          ports:
            - containerPort: 27017
              name: httpm
              protocol: TCP
          volumeMounts:
             - mountPath: /data/db
               name: vude-mongo-v
      volumes:
        - name: vude-mongo-v
          hostPath:
             path: /opt/assignments/

# Create a svc.yaml file for the K8S Node-Port service for MongoDB:

apiversion: V1
kind: service
metadata:
   name: mongo
   labels:
     app: mongo
spec:
  selector:
    app: mongo
  type: NodePort
  ports:
   - nodeport: 31000
     targetport: 27017 
  
# Automation for Mongodb Deployment and Service :

function deployment() {

   echo "Bring up Deployment => START"

   kubectl apply -f /opt/assignments/mongo/specs/deployments/start.yml

   echo "Deployment ACTIVE => DONE"

}

function svc() {

   echo "Bring up Service => START"

   kubectl apply -f /opt/assignments/mongo/specs/svc/start.yml

   echo "Service ACTIVE  => DONE"

}

function main() {

#  namespace $1

  deployment

  svc

}

# Arguments :: $1 = namespace(mongodb)

main $1

# connect to Mongo shell :
***************************
. Once login to MongoDB pod enter mongo to connect mongoshell
  kubectl exec <pod name> -n <namespace> -- /bin/bash

> db - check the current database
> show dbs - check list of database to verify database exist or deleted already
> use <name of db> - select the db you want to deleted
> db.dropDatabase() - drop the database

. show collection (it will display all collections working in current db)
. insert your first document it's going to create collection automatically

> db.<collectionname>.insert() -- insert document
> db.<collectionname>.insertone() -- insert single document
> db.<collectionname>.insertmany() -- insert multiple documents


db.employee.insert(
{
  "EmployeeID": 125,
  "EmployeeName": "maneesh",
  "Age": 25,
  "Gender": "male",
  "Address": ["kphb", "hyd"]
}
)

db.employee.insert(
{
  "EmployeeID": 521,
  "EmployeeName": "rajashaker",
  "Age": 26,
  "Gender": "male",
  "Address": ["madhapur", "hyd"]
}
)


db.employee.insertmany(
{
  "EmployeeID": 478,
  "EmployeeName": "yeti",
  "Age": 27,
  "Gender": "male",
  "Address": "prakasham"
},
{
  "EmployeeID": 986,
  "EmployeeName": "bharath"
  "Age": 26,
  "Gender": "male",
  "Address": "tirupati"
},
{
  "EmployeeID": 076,
  "EmployeeName": "jagadeesh"
  "Age": 27,
  "Gender": "male",
  "Address": "nellore"
},
{
  "EmployeeID": 743,
  "EmployeeName": "charan",
  "Age": 26,
  "Gender": "male",
  "Address": ["anathapur", "andhra pradesh"]
}
)


> db.<collection name>.find() -- view document
> db.<collection name>.find().pretty() -- view document in json

# update document
******************
- Insert field 
- Delete field
- Update field

- Insert field
***************
. db.movies.update(
{""EmployeeID": 478}
{$set: {"language": "English"}}
)

- Delete field
***************
. db.<movies>.update(
{"EmployeeID": 478}
{$unset: {"language": "English"}}
)

- Update field
***************
. db.<movies>.update(
{"EmployeeID": 478}
{$set: {"language": "korean"}}
)

# Querying Document on fields:
*******************************

- equals, ne, gt, lt

. db.movies.find({"released": 1999}).pretty()

. db.movies.find({"director": "shankar"}).pretty()

. db.movies.find({"released": {$gt: 2000}}).pretty()

. db.movies.find({"released": {$lt: 2000}}).pretty()


# selecting specific fields in the query
*****************************************

. db.movies.find({}, {"_id": 0}).pretty()

. db.movies.find({}, {_"id": 0, "title":1, "released": 1, "language": 1}).pretty()

# Counting documents
*********************

. db.movies.count()

. db.movies.stats()

. db.movies.count({"releaed": {$lt: 2000}})

. db.movies.count({"releaed": {$gt: 2000}})

. db.movies.count({"language": "English"}) 

# Delete Documents
*******************
- selective
- all documents

. db.movies.delete

. db.movies.deleteMany(

. db.movies.deleteOne(

. db.movies.deleteMany({"language": "Tamil"})

. db.movies.deleteMany({})


# VERIFICATIONS :

1. Create Mongodb Deployment - Done
2. Create Mongodb Service - Done
3. Access the Mongodb UI - Done





























