Setting up SSHD on a first-time Ubuntu installation

(resource 'https://help.ubuntu.com/community/SSH/OpenSSH/Configuring')

$ sudo apt-get update && sudo apt-get upgrade --show-upgraded
$ sudo apt-get install openssh-server
$ sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.factory-defaults
$ sudo chmod a-w /etc/ssh/sshd_config.factory-defaults
(FOR Ubuntu 12.04 and older) sudo restart ssh
$ sudo systemctl restart ssh
