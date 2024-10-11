#!/bin/bash

if [ "$ROOTPW" != "" ]; then
    echo "root:$ROOTPW" | chpasswd
fi

if [ "$DNS" != "" ]; then
    for d in $DNS
    do
     echo "nameserver $d" >> /etc/resolv.conf
    done
fi

ip -o addr show | cut -d' ' -f 2 |
while read i
do
 if [ "$i" != "lo" ]; then
     if [ "$REMIP" != "" ]; then
         ip addr del $(ip -o addr sho $i | cut -d' ' -f 7) dev $i
     else
         if [ "$i" != "eth0" ]; then
             ip addr del $(ip -o addr sho $i | cut -d' ' -f 7) dev $i
         fi
     fi
 fi
done

if [ "$(hostname)" == "node1" ]; then
    echo "RkxBRyAxLzM6IENDSVR7bGV2ZWwwX3A0cnQxCg==" | base64 -d
fi

if [ "$(hostname)" == "node2" ]; then
    echo "FLAG 2/3: _p4rt2"
fi

if [ "$(hostname)" == "node3" ]; then
    echo "FLAG 3/3: _p4rt3_end}"
fi

exec /usr/sbin/sshd -D
