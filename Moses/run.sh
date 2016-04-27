
#!/bin/bash

cd /home/saurabhd04/CS547/TokenRingProtocol/Moses
gnome-terminal  -e "java -cp libs/*:Moses.jar Moses -sp9001"  --window-with-profile=Saurabh
gnome-terminal  -e "java -cp libs/*:Moses.jar InteractiveAgent new-host.home 9001 tokenring.law manager"  --window-with-profile=Saurabh
gnome-terminal  -e "java -cp libs/*:Moses.jar InteractiveAgent new-host.home 9001 tokenring.law server"  --window-with-profile=Saurabh
gnome-terminal  -e "java -cp libs/*:Moses.jar InteractiveAgent new-host.home 9001 tokenring.law a"  --window-with-profile=Saurabh
gnome-terminal  -e "java -cp libs/*:Moses.jar InteractiveAgent new-host.home 9001 tokenring.law b"  --window-with-profile=Saurabh
gnome-terminal  -e "java -cp libs/*:Moses.jar InteractiveAgent new-host.home 9001 tokenring.law c"  --window-with-profile=Saurabh
gnome-terminal  -e "java -cp libs/*:Moses.jar InteractiveAgent new-host.home 9001 tokenring.law d"  --window-with-profile=Saurabh

