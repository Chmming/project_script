#!/bin/bash
yum -y install vsftpd &> /dev/null
systemctl start vsftpd
systemctl enabled vsftpd
