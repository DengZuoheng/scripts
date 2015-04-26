apt-get update -y 
apt-get install build-essential autoconf libtool libssl-dev gcc -y
apt-get install git -y
git clone https://github.com/shadowsocks/shadowsocks-libev.git
cd shadowsocks-libev
./configure
make
make install



