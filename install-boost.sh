BOOST_VERSION=1.58.0
ZIP_FILE_NAME=boost_${BOOST_VERSION//./_}
ZPI_FILE_EXT=tar.gz
wget http://nchc.dl.sourceforge.net/project/boost/boost/$BOOST_VERSION/$ZIP_FILE_NAME.$ZPI_FILE_EXT
apt-get update
apt-get install -y python-dev
apt-get install -y mpi-default-dev
apt-get install -y libicu-dev
apt-get install -y libbz2-dev 
tar -xzf $ZIP_FILE_NAME.$ZPI_FILE_EXT
cd $ZIP_FILE_NAME
./bootstrap.sh
./b2 --buildtype=complete stage
./b2 install
cd ..
rm -r -f $ZIP_FILE_NAME
rm -f $ZIP_FILE_NAME.$ZPI_FILE_EXT


#reference
#http://nyc1991.blog.51cto.com/6424159/1133388
