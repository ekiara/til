virt-manager/KVM creating qcow2 files where you want them
(resource "https://kashyapc.com/2011/09/24/creating-a-qcow2-virtual-machine/")


virt-manager has a specific location that it saves all your virtual manager
volumes (somewhere in /var I think).

If your root is full but your /home has space, then you can manually create a
qcow2 file in ~ and then when your are creating a new virtual machine or
moving one, you can specify the location of that file:

$ /usr/bin/qemu-img create -f qcow2 -o preallocation=metadata ~/vmimgs/vm-volume-001.qcow2 16G
