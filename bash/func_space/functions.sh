#!/bin/bash

text() {
    echo "huli nam hackeram"
}

ten() {
    for i in {1..10} 
    do
        echo "$i"
    done
}

hack() {
    echo "self-destruction start in 10..."
    for i in {1..10} 
    do
        echo "$((10-i)).."
        sleep 1
    done
}

