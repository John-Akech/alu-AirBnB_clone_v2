from fabric.api import env, put, run, task
from os.path import exists, isdir
import os.path
import re

# Set the username and host for SSH connection to the server
env.user = 'ubuntu'
env.hosts = ['54.197.135.244', '54.167.3.103']
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """
    Distributes archive to web servers
    """
    # Check if the archive file exists
    if not exists(archive_path):
        raise Exception("Archive does not exist.")

    # Upload the archive to the /tmp/ directory of the web server
    put(archive_path, "/tmp/")

    # Uncompress the archive to the folder
    filename = re.search(r'[^/]+$', archive_path).group(0)
    folder = "/data/web_static/releases/{}".format(os.path.splitext(filename)[0])

    # Create the folder if it doesn't exist
    if not exists(folder):
        run("mkdir -p {}".format(folder))

    # Extract files from archive
    run("tar -xzf /tmp/{} -C {}".format(filename, folder))

    # Remove archive from web server
    run("rm /tmp/{}".format(filename))

    # Move all files from web_static to the new folder
    run("mv {}/web_static/* {}".format(folder, folder))

    # Remove the web_static folder
    run("rm -rf {}/web_static".format(folder))

    # Delete the symbolic link
    run("rm -rf /data/web_static/current")

    # Create new symbolic link
    run("ln -s {} /data/web_static/current".format(folder))


@task
def synchronize_files(c):
    """
    Synchronize files from web_static to web servers
    """
    # Create 'hbnb_static' directory if it doesn't exist
    if not isdir("/var/www/html/hbnb_static"):
        c.sudo("mkdir -p /var/www/html/hbnb_static")

    # Sync 'hbnb_static' with 'current' on each server
    for host in env.hosts:
        c.sudo("rsync -avz --delete /data/web_static/current/ /var/www/html/hbnb_static/", user="root")

    print("Files synchronized successfully.")


# Usage:
# fab -f deploy.py do_deploy:/path/to/file.tgz
# fab -f deploy.py synchronize_files
