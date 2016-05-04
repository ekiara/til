(resource 'https://www.linode.com/docs/security/firewalls/control-network-traffic-with-iptables')
(resource 'https://www.digitalocean.com/community/tutorials/how-the-iptables-firewall-works')
(resource 'https://www.digitalocean.com/community/tutorials/how-to-set-up-an-iptables-firewall-to-protect-traffic-between-your-servers')

$ /sbin/iptables -nL --line-numbers
$ /sbin/iptables -I INPUT {LINE_NUMBER} -i eth1 -p tcp --dport 21 -s 123.123.123.123 -j ACCEPT -m comment --comment "This rule is here for this reason"
$ /sbin/iptables -I INPUT 5 -p tcp --dport 80 -j ACCEPT -m comment --comment "Allow access on PORT 80"
$ /sbin/iptables-save > /etc/iptables_<hostname>.local
$ /sbin/iptables-restore < /etc/iptables_<hostname>.local
