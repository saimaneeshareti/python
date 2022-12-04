# AIM: 
. Deploy MongoDB Deployment POD and a Service for that POD
. Run a Python Script to connect to that Mongo and CRUD(Create, Update & Delete Records)

# Pre-requisites:
1. Kubernetes secrets
2. Kubernetes storage classes
1. kubernetes deployment
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
# How to deploy mongodb on kubernetes?

# Step 1:
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

#step 2:
# Create a StatefulSet for mongodb

apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: mongodb-standalone
  namespace: mongodb
spec:
  serviceName: database
  replicas: 1
  selector:
    matchLabels:
      app: database
  template:
    metadata:
      labels:
        app: database
        selector: mongodb-standalone
    spec:
      containers:
      - name: mongodb-standalone
        image: mongo:4.0.8
        env:
          - name: MONGO_INITDB_ROOT_USERNAME
            value: admin
          - name: MONGO_INITDB_ROOT_PASSWORD
            value: password
      nodeSelector:
        kubernetes.io/hostname: mongodb-node

# Step 3:
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

# Run a Python Script to connect to that Mongo and CRUD:

# What Does CRUD Mean in MongoDB?
. A CRUD operation in MongoDB describes a user interface that allows users to view, search, and modify data in a database.

. CRUD stands for Create,Read,Update and Delete.
- Create inserts new documents into the MongoDB database.
- Read operation is used to retrieve documents from a database.
- Update operation modifies existing documents in the database.
- Delete operation removes documents from a database.

# Prerequisites for Setting Up MongoDB CRUD Operations in Python:
. The latest version of Python.
. MongoDB database.
. PyMongo MongoDB driver installation.

# Section 1:
*************
- Setting Up MongoDB CRUD Operations in Python:
. MongoDB provides its users a python distribution called PyMongo that contains tools for working with MongoDB databases.
. To install PyMongo for communicating with MongoDB.

. In your command prompt run the below command to install PyMongo.
   pip install pymongo

. Now to perform MongoDB CRUD operations in Python  

. you need to establish a connection using Mongo client. Type the below command
   >>> from pymongo import MongoClient
   >>> client = MongoClient('localhost',27017)  # 27017 is the default port number for mongodb

. Above MongoClient is used to connect the MongoDB server. 

. Next connect to your test database
   db = client.test

. Retrieve the collection from the database
   col = db.person    

# Section 2:
*************
- Using MongoDB CRUD Operations in Python:

# C-Create Operation
. Data is stored in MongoDB as JSON objects. 
. The records for a collection in MongoDB are referred to as documents.

- There are two ways you can add documents to a MongoDB collection.

. db.collection.insert_one()
. db.collection.insert_many()

- insert_one():
***************** 
. insert_one() facilitates the insertion of a single document into a collection. 
. we are working with a collection called SalesDB in this example.   

 db.SalesDB.insert_one({
    name: "Linda",
    orderdate: "6/10/2021",
    species: "Dog",
    ownerAddress: "380 W. Fir Ave",
    chipped: true
 })

. Above successful completion of the create operation a new document is created.
. The function will return an object whose "acknowledged" attribute is "true" and whose "insertedID" attribute is the newly created "ObjectId."

 db.SalesDB.insert_one({
    name: "Linda",
    orderdate: "6/10/2021",
    species: "Dog",
    ownerAddress: "380 W. Fir Ave",
    chipped: true
 })
{
        "acknowledged" : true,
        "insertedId" : ObjectId("5fd989674e6b9ceb8665c57d")
}

- insert_many():
*****************
. Using the insert_many() method on a collection it is possible to insert multiple documents at the same time.

db.SalesDB.insert_many([{
    name: "Linda",
    orderdate: "6/10/2021",
    species: "Dog",
    ownerAddress: "380 W. Fir Ave",
    chipped: true},
      {name: "Kitana", 
      orderdate: "6/10/2021", 
      species: "Cat", 
      ownerAddress: "521 E. Cortland", 
      chipped: true}])

db.SalesDB.insert_many([{ name: "Linda", orderdate: "6/11/2021", species: "Dog", 
ownerAddress: "380 W. Fir Ave", chipped: true}, {name: "Kitana", orderdate: "6/11/2021", 
species: "Cat", ownerAddress: "521 E. Cortland", chipped: true}])
{
        "acknowledged" : true,
        "insertedIds" : [
                ObjectId("5fd98ea9ce6e8850d88270b4"),
                ObjectId("5fd98ea9ce6e8850d88270b5")
        ]
}

# R-Read Operation:
. There are two ways to read documents from a collection in MongoDB:

. db.collection.find()
. db.collection.find_one()

- find():
**********
. On a collection to get all the documents within it.
. Using the find() method without any arguments will return all records in the collection.

db.SalesDB.find():
*******************
{ "_id" : ObjectId("5fd98ea9ce6e8850d88270b5"), "name" : "Kitana", "orderdate" : "6/10/2021", "species" : "Cat", "ownerAddress" : "521 E. Cortland", "chipped" : true }
{ "_id" : ObjectId("5fd993a2ce6e8850d88270b7"), "name" : "Marsh", "orderdate" : "6/10/2021", "species" : "Dog", "ownerAddress" : "380 W. Fir Ave", "chipped" : true }

. The "ObjectId" assigned to every record is mapped to the "_id" key.
. When performing a read operation you can use filtering criteria to narrow your search to a desired subsection of the records.
. Searching by value is one of the most common ways to filter the results.

db.SalesDB.find({"species":"Cat"})
{ "_id" : ObjectId("5fd98ea9ce6e8850d88270b5"), "name" : "Kitana", "orderdate" : "6/10/2021", "species" : "Cat", "ownerAddress" : "521 E. Cortland", "chipped" : true }

- find_one():
**************
. If we only want one document that meets the search criteria then we can use the find_one() method on the collection

db.{collection}.find_one({query}, {projection})

# U-Update Operation
. update operations operate on a single collection. 
. Filters and criteria are used to select the documents to be updated in an update operation.
. Document updates are permanent and cannot be rolled back. 
. Be careful when updating documents. This also applies to deleting documents.

- MongoDB CRUD allows users to update documents in three different ways:
. db.collection.update_one()
. db.collection.update_many()
. db.collection.replace_one()

- update_one():
****************
. By performing an update_one() operation, we can change a single document and update a record. 
. To update a document two arguments need to be provided an update filter and an update action.
. Update filters specify which items should be updated, and update actions specify how to do so.

db.SalesDB.update_one({name: "Marsh"}, {$set:{ownerAddress: "451 W. Coffee St. A204"}})

{ "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }

{ "_id" : ObjectId("5fd993a2ce6e8850d88270b7"), "name" : "Marsh", "orderdate" : "6/10/2021", "species" : "Dog", "ownerAddress" : "451 W. Coffee St. A204", "chipped" : true }

- update_many():
*****************
. The update_many() function allows us to update multiple documents by passing in a list of items.just as we did when we inserted multiple items.

db.SalesDB.update_many({species:"Dog"}, {$set: {age: "5"}})

{ "acknowledged" : true, "matchedCount" : 3, "modifiedCount" : 3 }

 db.SalesDB.find()
{ "_id" : ObjectId("5fd98ea9ce6e8850d88270b5"), "name" : "Kitana", "orderdate" : "6/10/2021", "species" : "Cat", "ownerAddress" : "521 E. Cortland", "chipped" : true }
{ "_id" : ObjectId("5fd993a2ce6e8850d88270b7"), "name" : "Marsh", "orderdate" : "6/10/2021", "species" : "Dog", "ownerAddress" : "451 W. Coffee St. A204", "chipped" : true }

- replace_one():
*****************
. The replace_one() method replaces a single document in a collection.
. The replace_one() method replaces a document's entire contents,so fields not found in the new document will be lost.

db.SalesDB.replace_one({name: "Kevin"}, {name: "Maki"})

{ "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }

 db.SalesDB.find()
{ "_id" : ObjectId("5fd98ea9ce6e8850d88270b5"), "name" : "Kitana", "orderdate" : "6/10/2021", "species" : "Cat", "ownerAddress" : "521 E. Cortland", "chipped" : true }
{ "_id" : ObjectId("5fd993a2ce6e8850d88270b7"), "name" : "Marsh", "orderdate" : "6/10/2021", "species" : "Dog", "ownerAddress" : "451 W. Coffee St. A204", "chipped" : true }

# D-Delete Operation:
. The delete operation operates on a single collection like the update and create operations. 
. Deletes are also atomic for a single document. 

- There are two ways to delete records from a collection in MongoDB:
. db.collection.delete_one()
. db.collection.delete_many()

. delete_one()
***************
. The delete_one() method is used to remove a document from a MongoDB collection. 
. The document to be deleted is specified by a filter. Only records matching the specified filter are deleted.

db.SalesDB.delete_one({name:"Maki"})

{ "acknowledged" : true, "deletedCount" : 1 }

 db.SalesDB.find()
{ "_id" : ObjectId("5fd98ea9ce6e8850d88270b5"), "name" : "Kitana", "orderdate" : "6/10/2021", "species" : "Cat", "ownerAddress" : "521 E. Cortland", "chipped" : true }
{ "_id" : ObjectId("5fd993a2ce6e8850d88270b7"), "name" : "Marsh", "orderdate" : "6/10/2021", "species" : "Dog", "ownerAddress" : "451 W. Coffee St. A204", "chipped" : true }
{ "_id" : ObjectId("5fd993f3ce6e8850d88270b8"), "name" : "Loo", "orderdate" : "7/10/2021", "species" : "Dog", "ownerAddress" : "380 W. Fir Ave", "chipped" : true }

- delete_many()
****************
. A single delete operation is used to delete multiple documents from a desired collection with delete_many(). 

db.SalesDB.delete_many({species:"Dog"})

{ "acknowledged" : true, "deletedCount" : 2 }

 db.SalesDB.find()
{ "_id" : ObjectId("5fd98ea9ce6e8850d88270b5"), "name" : "Kitana", "orderdate" : "6/10/2021", "species" : "Cat", "ownerAddress" : "521 E. Cortland", "chipped" : true }

# Referance:
*************
. https://hevodata.com/learn/mongodb-crud-operations-in-python/






























