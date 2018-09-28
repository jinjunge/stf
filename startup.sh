killall -9 node
ipaddr=`ifconfig enp2s0|awk 'NR==2{print $2}'|cut -d : -f2`
DATE=`date +%F`
gulp clean && gulp webpack:build
stf local --public-ip $ipaddr --allow-remote >> /var/stf/log/$DATE.log 2>&1 &
sleep 3
