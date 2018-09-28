ipaddr=`ifconfig enp2s0|awk 'NR==2{print $2}'|cut -d : -f2`
killall -9 node
gulp clean && gulp webpack:build
nohup /usr/bin/node /root/WebstormProjects/stf/lib/cli triproxy app001 --bind-pub tcp://$ipaddr:7111 --bind-dealer tcp://$ipaddr:7112 --bind-pull tcp://$ipaddr:7113 &
nohup /usr/bin/node /root/WebstormProjects/stf/lib/cli triproxy dev001 --bind-pub tcp://$ipaddr:7114 --bind-dealer tcp://$ipaddr:7115 --bind-pull tcp://$ipaddr:7116 &
nohup /usr/bin/node /root/WebstormProjects/stf/lib/cli processor proc001 --connect-app-dealer tcp://$ipaddr:7112 --connect-dev-dealer tcp://$ipaddr:7115 &
nohup /usr/bin/node /root/WebstormProjects/stf/lib/cli processor proc002 --connect-app-dealer tcp://$ipaddr:7112 --connect-dev-dealer tcp://$ipaddr:7115 &
nohup /usr/bin/node /root/WebstormProjects/stf/lib/cli reaper reaper001 --connect-push tcp://$ipaddr:7116 --connect-sub tcp://$ipaddr:7111 &
nohup /usr/bin/node /root/WebstormProjects/stf/lib/cli provider --name $ipaddr --min-port 7400 --max-port 7700 --connect-sub tcp://$ipaddr:7114 --connect-push tcp://$ipaddr:7116 --group-timeout 900 --public-ip $ipaddr --storage-url http://localhost:7100/ --adb-host 127.0.0.1 --adb-port 5037 --vnc-initial-size 600x800 --mute-master never --allow-remote &
nohup /usr/bin/node /root/WebstormProjects/stf/lib/cli auth-mock --port 7120 --secret kute kittykat --app-url http://$ipaddr:7100/ &
nohup /usr/bin/node /root/WebstormProjects/stf/lib/cli app --port 7105 --secret kute kittykat --auth-url http://$ipaddr:7100/auth/mock/ --websocket-url http://$ipaddr:7110/ &
nohup /usr/bin/node /root/WebstormProjects/stf/lib/cli api --port 7106 --secret kute kittykat --connect-push tcp://$ipaddr:7113 --connect-sub tcp://$ipaddr:7111 &
nohup /usr/bin/node /root/WebstormProjects/stf/lib/cli websocket --port 7110 --secret kute kittykat --storage-url http://$ipaddr:7100/ --connect-sub tcp://$ipaddr:7111 --connect-push tcp://$ipaddr:7113 &
nohup /usr/bin/node /root/WebstormProjects/stf/lib/cli storage-temp --port 7102 &
nohup /usr/bin/node /root/WebstormProjects/stf/lib/cli storage-plugin-image --port 7103 --storage-url http://$ipaddr:7100/ &
nohup /usr/bin/node /root/WebstormProjects/stf/lib/cli storage-plugin-apk --port 7104 --storage-url http://$ipaddr:7100/ &
nohup /usr/bin/node /root/WebstormProjects/stf/lib/cli poorxy --port 7100 --app-url http://$ipaddr:7105/ --auth-url http://$ipaddr:7120/ --api-url http://$ipaddr:7106/ --websocket-url http://$ipaddr:7110/ --storage-url http://$ipaddr:7102/ --storage-plugin-image-url http://$ipaddr:7103/ --storage-plugin-apk-url http://$ipaddr:7104/ &
