References:
-----------



Java:
-----
https://www.digitalocean.com/community/tutorials/how-to-install-java-with-apt-on-ubuntu-20-04



sudo apt update -y
sudo apt install default-jre -y
sudo apt install default-jdk -y



Test Java installation:
------------------------
vudeadmin@cdedops-vude2:/opt/quick_build/quickbuild-10.0.39$ java -version
openjdk version "11.0.16" 2022-07-19
OpenJDK Runtime Environment (build 11.0.16+8-post-Ubuntu-0ubuntu120.04)
OpenJDK 64-Bit Server VM (build 11.0.16+8-post-Ubuntu-0ubuntu120.04, mixed mode, sharing)
--------------------------------------------------------------------------------------------------------



Quickbuild Install GUIDES:
---------------------------



https://wiki.pmease.com/display/QB80/Server+Installation+Guide
https://wiki.pmease.com/display/QB12/Documentation+Home
https://build.pmease.com/build/5442



Goto :  
  https://www.pmease.com/downloads/latest/linux
  COPY Link
  Goto your VM
    1. sudo mkdir /opt/quick_build/
    2. cd /opt/quick_build/
    3. sudo chown -R $USER /opt/quick_build/
    4. curl -L -O https://build.pmease.com/download/5442/artifacts/quickbuild-10.0.39.tar.gz
    5. tar -zxvf quickbuild-10.0.39.tar.gz
    6. ls -R /opt/quick_build/
    7. cd /opt/quick_build/quickbuild-10.0.39
    8. ./bin/server.sh start
--------------------------------------------------------------------------------------------------------



Video trainings:
----------------
\\elements.local\FW\Users\azaleski\qb_trainings
--------------------------------------------------------------------------------------------------------



Additional documentation:
--------------------------
https://npsg-wiki.elements.local/display/INFS/Quickbuild+CI+2.0+Data+Spec



ElasmoCI:
---------
https://npsg-wiki.elements.local/display/CME/elasmo+CI
--------------------------------------------------------------------------------------------------------