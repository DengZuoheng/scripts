GLOBAL_INSTALL_TOOL="apt-get"
PYTHON_INSTALL_TOOL="pip"
PYINS="${PYTHON_INSTALL_TOOL} install"
#install python-install-tool
${GLOBAL_INSTALL_TOOL} install -y python-${PYTHON_INSTALL_TOOL}
#install python-dev
${GLOBAL_INSTALL_TOOL} install -y python-dev
#install libs
${PYINS} pycurl
${PYINS} pyquery
${PYINS} django
${PYINS} pycrypto
${PYINS} paramiko