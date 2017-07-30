# install C compiler
sudo yum install -y gcc

# install miniconda
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
bash miniconda.sh -b -p $HOME/miniconda
export PATH=$HOME/miniconda/bin:$PATH
conda update -y conda
echo 'export PATH=$HOME/miniconda/bin:$PATH' >> .bashrc

# install packages
conda install -y jupyter numpy scipy matplotlib
