#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers and deploy it
"""
from fabric.api import env, put, run
from os.path import exists

# Update env.hosts with the IP addresses of your web servers
env.hosts = ['23.20.91.208', '23.20.188.250']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Deploys the web_static archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Extract the archive to /data/web_static/releases/<archive_filename>/
        archive_filename = archive_path.split('/')[-1]
        release_path = '/data/web_static/releases/{}'.format(
            archive_filename[:-4])
        run('mkdir -p {}'.format(release_path))
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_path))

        # Remove the uploaded archive from the web server
        run('rm /tmp/{}'.format(archive_filename))

        # Move the contents of the archive to the web server's web_static directory
        run('mv {}/web_static/* {}'.format(release_path, release_path))

        # Remove the now empty web_static directory
        run('rm -rf {}/web_static'.format(release_path))

        # Delete the current symbolic link if it exists
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link to the deployed code
        run('ln -s {} /data/web_static/current'.format(release_path))

        return True
    except:
        return False
