#!/bin/bash

docker run -d -v /root/study/docker/portia/data:/app/slyd/data:rw -p 9001:9001 --name portia scrapinghub/portia
