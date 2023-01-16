#!/bin/bash
#编写一键部署yum脚本
rm -rf /etc/yum.repos.d/*.repo
echo "[abc]
name=test
baseurl=http://172.25.254.254/content/rhel7.0/x86_64/dvd/
enabled=1
gpgcheck=0" > /etc/yum.repos.d/xx.repo

