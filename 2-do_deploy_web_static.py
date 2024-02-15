#!/usr/bin/python3
"""Fabric script to generate a .tgz archive"""

from fabric.api import local
from datetime import datetime

def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""

    # Create the 'versions' folder if it doesn't exist
    local("mkdir -p versions")

    # Get the current date and time
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")

    # Name of the archive
    archive_name = "web_static_{}.tgz".format(timestamp)

    # Compress the contents of the web_static folder into a .tgz archive
    result = local("tar -cvzf versions/{} web_static".format(archive_name))

    # Check if the compression was successful
    if result.failed:
        return None
    else:
        return "versions/{}".format(archive_name)
