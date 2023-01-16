#!/bin/bash
#编写一键部署yum脚本
rm -rf /etc/yum.repos.d/*.repo
url=http://172.25.254.254/content/rhel7.0/x86_64/dvd/
#此处不可以用单引号，因为它会屏蔽特殊符号$url中的$的作用
echo "[abc]
name=test
baseurl=$url
enabled=1
gpgcheck=0" > /etc/yum.repos.d/xx.repo

