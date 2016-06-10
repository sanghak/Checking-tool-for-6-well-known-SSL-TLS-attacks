#!/bin/bash

list=`ls /home/osh/nmap_shell/sitelist`
for file in `echo $list`
do
	echo $file
	nmap -p 443 --script ssl-heartbleed $file >> /home/osh/nmap_shell/result/"$file.txt"
	nmap -sV --version-light --script ssl-poodle -p 443 $file >> /home/osh/nmap_shell/result/"$file.txt"
	nmap --script ssl-dh-params $file >> /home/osh/nmap_shell/result/"$file.txt"
	nmap -p 443 --script ssl-ccs-injection $file >> /home/osh/nmap_shell/result/$file.txt
done
python DROWN_WebDriver.py
