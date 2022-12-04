#!/bin/bash
# Bring up Deployments

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
