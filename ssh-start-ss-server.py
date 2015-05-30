#!/usr/bin/python  
# -*- coding: utf-8 -*-
import paramiko
login_info = {
    'hostname' = '116.251.218.79'
    'username' = 'root'
    'password' = '299792458'
}
cmd = 'python scripts/start-ss-server.py'
ssh_client =paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
ssh_client.connect(**login_info) 
stdin,stdout,stderr = ssh_client.exec_command(cmd)
print stdout.read() 
ssh_client.close()
