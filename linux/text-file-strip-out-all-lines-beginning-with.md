TEXTFILE: Strip out all lines from a textfile beginning with 'something'
----------------------------------------

You have a bunch of text files (log files) that contain lines that you want to
strip out (i.e. every line that begins either with 'debug' or 'Debug'). This
is what you do.

$ sed -i.bak '/^[dD]ebug/d' ./infile

<or>

$ ls
$ for logfile in `/bin/ls`; do sed -i.bak '/^[dD]ebug/d' ./infile; done
