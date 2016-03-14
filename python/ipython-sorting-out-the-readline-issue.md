IPython, sorting out the readline issue

Essentially, you first need to install libraries with names similar to
'libreadline-dev' and 'libcurses-dev' to your distro (Ubuntu is differenct
from Fedora etc)

And second you need to run the `pip install readline` command to install
readline library to your python-environment/virtualenv.

[Ubuntu]

(venv)$ sudo apt-get install libreadline-gplv2-dev libncursesw5-dev \
    libssl-dev libsqlit e3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev                                                                            
(venv)$ sudo apt-get install libncurses5-dev
(venv)$ pip install readline
(venv)$ pip install --upgrade readline

[Fedora / CentOS]

(venv)$ sudo yum search curses|grep lib
(venv)$ sudo yum install ncurses-libs.x86_64 ncurses-static.x86_64 ncurses-devel.x86_64
(venv)$ sudo yum search readline|grep lib
(venv)$ sudo yum install readline.x86_64
(venv)$ pip install readline
(venv)$ pip install --upgrade readline
