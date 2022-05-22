#!/usr/bin/env bash

funct="$1"

if [ "$funct" == "infere" ]; then
    x="$2"
    hadoop fs -mkdir /Project || true;
    hadoop fs -mkdir /Project/Input || true;
    hadoop fs -put -f ./train.csv /Project/Input;
    hadoop fs -rm -r -f  /Project/Output > /dev/null 2> /dev/null || true;

    hadoop jar "$HADOOP_HOME/hadoop-streaming-3.3.0.jar" \
        -input /Project/Input \
        -output /Project/Output \
        -mapper "$(pwd)/knn.py map \"$x\"" \
        -reducer "$(pwd)/knn.py reduce" \
        -file "$(pwd)/constants.py" \
        -file "$(pwd)/model.txt" \
        -cmdenv "K=$K" > /dev/null 2> /dev/null;
    hadoop fs -cat /Project/Output/part-00000 2> /dev/null;

    exit 0;
fi
