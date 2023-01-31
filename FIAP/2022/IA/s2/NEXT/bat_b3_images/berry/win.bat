

qemu-system-arm ^
-M versatilepb ^
-cpu arm1176 ^
-m 256 ^
-drive "file=2020-02-13-raspbian-buster.img,if=none,index=0,media=disk,format=raw,id=disk0" ^
-device "virtio-blk-pci,drive=disk0,disable-modern=on,disable-legacy=off" ^
-net "user,hostfwd=tcp::5022-:22" ^
-dtb versatile-pb-bullseye-5.10.63.dtb^
-append "root=/dev/vda2 panic=1 rootfstype=ext4 rw init=/bin/bash" ^
-kernel kernel-qemu-5.10.63-bullseye ^
-no-reboot