#!/bin/bash

# module 5 solution

# shows home directory
echo $HOME

# shows terminal type
echo $TERM
set -x
# shows services, that started in runlevel 3
ls /etc/rc3.d/S*
set +x

echo "done!"
