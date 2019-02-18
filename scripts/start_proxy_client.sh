#!/bin/bash

echo "Start PD proxy client ..."
sudo /usr/bin/sslocal -c /etc/shadowsocks/config_client.json &
