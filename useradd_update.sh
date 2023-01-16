#!/bin/bash
read -p "input username:" Unamei
useradd $Uname
#关闭回显，屏蔽密码
stty -echo 
read -p "input password:" Passwd
#打开回显
stty echo
#useradd $Uname
echo $Passwd | passwd --stdin $Uname
