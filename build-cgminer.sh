apt-get update
apt-get install git
git clone https://github.com/ckolivas/cgminer.git
cd cgminer
git checkout -b b-2-0-0 v2.0.0
sudo apt-get install -y build-essential autoconf automake libtool pkg-config libcurl3-dev libudev-dev libncurses-dev 
sh autogen.sh
./configure
make
make install
cgminer -V