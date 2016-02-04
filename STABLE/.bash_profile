export PS1='\[\e[1;32m\][\u@\h \w]\$\[\e[0m\] '
if [ "$EUID" -ne 0 ]
  then export PS1='\[\e[1;31m\][\u@\h \W]\s\[\e[0m\] '
fi
alias ll='ls -l'

export PATH=$PATH:~/.bin
export PYTHONPATH=~/.py