Find all symbolic links

"Are you afraid of doing an `rm -Rf` on a bunch of directories but you are
not sure if they have symbolic links that might result in you deleting things
that you did not intend to? Then find the symbolic links first."

$ ls -alFh --recursive /opt/music/Viral/|grep ^l
