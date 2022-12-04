# Aim: 
. Build a simple python flask web-app with Mongo as database.

# What is python flask web-app?
. Flask is a lightweight Python web framework.
. That provides useful tools and features for creating web applications in the Python Language.
. It gives developers flexibility and is an accessible framework for new developers. 
. Because you can build a web application quickly using only a single Python file. 

# What is MongoDB?
. MongoDB is a document-oriented NoSQL database used for high volume data storage.
. In MongoDB server you can start and then create multiple databases. 
. MongoDB makes use of collections and documents.
. Inside of the collection we have documents. 
. These documents contain the data we want to store in the MongoDB database.
. Documents consist of key-value pairs which are the basic unit of data in MongoDB.
. The data stored in the MongoDB is in the format of BSON documents. 
. BSON stands for Binary representation of JSON documents.

# How to deploy flask web-app in K8S?

. Create a Deployment and Service for the Flask app.

apiVersion: apps/v1
kind: Deployment
metadata:
  name: flask-deployment
spec:
  selector:
    matchLabels:
      app: flask
      namespace: mongo
  replicas: 1
  template:
    metadata:
      labels:
        app: flask
    spec:
      containers:
      - name: flask
        image: flask-image
        ports:
          - containerPort: 80

. To create the above deploymet file
   kubectl apply -f <filename> -n <namespace> 

apiVersion: v1
kind: Service
metadata:
  name: flask-service
spec:
  ports:
  - port: 80
    targetPort: 80
    name: http
  selector:
    app: flask

. To create above svc file
   kubectl apply -f <filename> -n <namespace>

# How to deploy MongoDB in K8S?

. Create a Deployment and Service for the MongoDB.

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

. To create the above deploymet file
   kubectl apply -f <filename> -n <namespace> 

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

. To create the above svc file
   kubectl apply -f <filename> -n <namespace> 

# How to Create MongoDB cluster ?

. Login to MongoDB and go to Atlas. Click on Build a cluster.
. Under shared clusters, click on create a cluster.
. Click on create cluster button.Wait till the cluster is being created.
. MongoDB will create three replicas of the database for the high availability of the data and provide fault tolerance.

# How to Create a database user for MongoDB ?

. Click on Database Access from the options in the left pane. 
. Now, click on Add New Database User button.
. I will be selecting the authentication method as a Password.
. Enter the username and I will generate a password by clicking the Autogenerate Secure Password
. This will generate a secure password.
. This passowrd is very important and if you lose it, you will be not able to access this database later
. Click on Add User button. This will add a new user, in my case.   
   
# How to Get a URL for connecting to the MongoDB cluster ?
. Click on the Clusters option from the left pane.
. Now, in the cluster sandbox, click on CONNECT button. 
. This will open up one pop-up window. Select Connect your application option.
. Select Python as a driver and appropriate version of python.
. Copy the connection URL and replace <password> with the password of the admin
. User that we have created a pass word in the previous step.   
. Now, we have the MongoDB database ready to use.
. Let’s create a Flask application for using this MongoDB database.

# Create REST APIs in Python using Flask

. REST APIs play a major role as a communication channel between different services. 

# What is a REST API?
**********************
. REST stands for Representational State Transfer.
. which means when a client machine places a request to obtain information about resources from a server.
. The server machine then transfers the current state of the resource back to the client machine.
    
.There are a few methods in this which are as follows.

. GET – Used by the client to select or retrieve data from the server
. POST – Used by the client to send or write data to the server
. PUT – Used by the client to update existing data on the server
. DELETE – Used by the client to delete existing data on the server   

# How to Set Up Flask with MongoDB

import json
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'your_database',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)

class User(db.Document):
    name = db.StringField()
    email = db.StringField()
    def to_json(self):
        return {"name": self.name,
                "email": self.email}

@app.route('/', methods=['GET'])
def query_records():
    name = request.args.get('name')
    user = User.objects(name=name).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(user.to_json())

@app.route('/', methods=['PUT'])
def create_record():
    record = json.loads(request.data)
    user = User(name=record['name'],
                email=record['email'])
    user.save()
    return jsonify(user.to_json())

@app.route('/', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    user = User.objects(name=record['name']).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        user.update(email=record['email'])
    return jsonify(user.to_json())

@app.route('/', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)
    user = User.objects(name=record['name']).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        user.delete()
    return jsonify(user.to_json())
