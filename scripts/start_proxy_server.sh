#!/bin/bash

echo "Start PD proxy server ..."
sudo /usr/bin/ssserver -c /etc/shadowsocks/config_server.json &
