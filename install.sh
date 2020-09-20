#!/bin/bash

yum install -y  gcc gcc-c++ make git patch openssl-devel zlib-devel readline-devel sqlite-devel bzip2-devel

cd ~
git clone git://github.com/yyuu/pyenv.git ~/.pyenv
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> .bashrc
echo 'eval "$(pyenv init -)"' >> .bashrc
source .bashrc

pyenv install 2.7.9
pyenv install 3.7.2
pyenv virtualenv 2.7.9 env1
pyenv virtualenv 3.7.2 env2