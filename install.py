#! /usr/bin/python
# This script will add the EyeDoc as Daemon to SystemD
# Better yet it would be cooler if it could run with a curl one-liner like brew

import os
import shutil

# TODO: PARAMETERIZE SystemD file

# INSTALL SYSTEMD SERVICE
target_path = '/etc/systemd/eyedoc.service'
shutil.copyfile('systemd/eyedoc.service', target_path )
os.chmod( target_path , 0o664)

# COPY DAEMON BINARY
shutil.copyfile('systemd/eyedoc', '/usr/local/eyedoc' )
os.chmod( target_path , 0o664)