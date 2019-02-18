#!/bin/bash

for imageUrl in `awk -F ',' '{print $1}' scrapy_output.csv`
do
    wget "${imageUrl}" --show-progress
done
