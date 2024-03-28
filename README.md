# Installation
## Install of UD-DASK/X on UBUNTU Desktop
1. Install Ubuntu 20.04 LTS.
   ```bash
   foo@bar:~$ sudo apt update
   foo@bar:~$ sudo apt upgrade
   ```
2. Install development tools.
   ```bash
   foo@bar:~$ sudo apt install build-essential
   foo@bar:~$ sudo apt install git
   foo@bar:~$ sudo apt install vim
   foo@bar:~$ sudo apt install python3-dev
   foo@bar:~$ sudo apt install python3-cffi
   ```
3. Install latest supported by driver linux kernel.
   1. At the time of writing UD-DASK/X driver version is 21.12
   2. Get supported kernel with `dpkg -I ud-dask_ubuntu_21.12.release.deb`
   3. Install selected kernel
      ```bash
      foo@bar:~$ sudo apt install linux-image-5.4.0-91
      foo@bar:~$ sudo apt install linux-headers-5.4.0-91
      foo@bar:~$ sudo apt install linux-modules-extra-5.4.0-91
      ``` 
   4. Configure Grub 
      1. Copy /etc/default/grub to /etc/default/grub.bak
      2. Edit /etc/default/grub. Set GRUB_DEFAULT="Advanced options for Ubuntu>Ubuntu, with Linux 5.4.0-91-generic"
      3. Run `sudo update-grub`
   5. Reboot to newly installed kernel.
4. Install UD-DASK/X driver
   ```bash
   foo@bar:~$ sudo apt install ./ud-dask_ubuntu_21.12.release.deb
   ```

## Install Python 3.11 from source
1. Install libraries and headers needed for compilation
   ```bash
   foo@bar:~$ sudo apt install checkinstall \ 
   libreadline-gplv2-dev  libncursesw5-dev libssl-dev \
   libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
   ```
2. Build and install Python from the source code
   ```bash
   foo@bar:~$ wget https://www.python.org/ftp/python/3.11.8/Python-3.11.8.tgz
   foo@bar:~$ tar -zxvf Python-3.11.8.tgz
   foo@bar:~$ cd  Python-3.11.8
   foo@bar:~$ sudo ./configure --enable-optimizations
   foo@bar:~$ sudo make altinstall
   foo@bar:~$ python3.11 -V
   Python 3.11.8
   foo@bar:~$ pip3.11 -V
   pip 24.0 from /usr/local/lib/python3.11/site-packages/pip (python 3.11)
   ```
3. Install and setup virtualenvwrapper
   ```bash
   foo@bar:~$ sudo pip3.11 install virtualenvwrapper
   ```
   Add to `~/.bashrc` following three lines
   ```bash
   export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3.11
   export WORKON_HOME=$HOME/.virtualenvs
   export PROJECT_HOME=$HOME/Devel
   source /usr/local/bin/virtualenvwrapper.sh
   ```
   Logout and log back in to terminal to source virtualenvwrapper config.

## Compile UD-DASK/X Python wrapper
1. Make virtualenv and compile the wrapper. The UD-DASK/X driver must be installed at this moment.  
   ```bash
   foo@bar:~$ mkvirtualenv BDudask
   (BDudask) foo@bar:~$ cd BDudask
   (BDudask) foo@bar:~$ pip install -r requirements.txt
   (BDudask) foo@bar:~$ python ./udask_build.py
   Compilation
   generating ./_udask_cffi.c
   the current directory is '/home/.../.../BDudask'
   ```
2. Check the operation of the wrapper. Make sure that USB DAQ device is connected to the PC.
   ```bash
   (BDudask) foo@bar:~$ python ./demo.py
   ```