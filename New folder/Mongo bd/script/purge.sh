#!/bin/bash
# Clean-up and create namespace

function namespace() {

echo "Clean-up & create a new namespace :: $1"
kubectl delete all --all -n $1
kubectl delete pvc --all -n $1
kubectl delete services --all -n $1
kubectl create ns $1

echo " "

}
function main() {

 namespace $1

}

main $1
