#!/bin/bash

for ImageURL in `cat ./fengniao.csv | awk -F ',' '{print $1}'`
do
    wget "${ImageURL}" --show-progress
done
