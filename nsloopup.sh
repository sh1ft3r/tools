#!/bin/bash
#
# Domein lijst path:
domain_list='domains.txt'
#
# Delay in secondes voor de lookup:
loop_wait='1'

echo "Domain name, IP Adres, NameServer";
for domain in `cat $domain_list`
do
    ip=`dig a +short $domain`; # IP adres lookup
    if [ ! -n "$ip" ]
        then 
            echo "$domain,Geen IP,,"; 
        else 
            echo "$domain,$ip,"`dig ns +short $domain`;

    fi
    sleep $loop_wait #
done;
