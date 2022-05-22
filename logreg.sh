#!/usr/bin/env bash

funct=$1

if [ "$funct" = 'train' ]; then
    hadoop fs -mkdir /Project || true;
    hadoop fs -mkdir /Project/Input || true;
    # hadoop fs -D dfs.blocksize=1048576 -put -f ./train.csv /Project/Input;
    hadoop fs -put -f ./train.csv /Project/Input;
    hadoop fs -rm -r -f  /Project/Output || true;

    hadoop jar "$HADOOP_HOME/hadoop-streaming-3.3.0.jar" \
        -input /Project/Input \
        -output /Project/Output \
        -mapper "$(pwd)/train_mapper.py" \
        -reducer "$(pwd)/train_reducer.py" \
        -file "$(pwd)/constants.py" \
        -file "$(pwd)/model.txt" \
        -cmdenv "MU=$MU" \
        -cmdenv "ETA=$ETA";

elif [ "$funct" = 'import' ]; then
    hadoop fs -cat /Project/Output/part-00000 > model.txt;
# else
#      # else body
fi