#!/usr/bin/python3
from fabric.api import env, put, run
from os.path import exists

# Set the SSH key and username as Fabric environment variables
env.key_filename = '~/.ssh/id_rsa'
env.user = 'john_akech'
env.hosts = ['23.20.91.208', '23.20.188.250']

def do_deploy(archive_path):
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Extract the archive to /data/web_static/releases/<archive filename without extension> on the web server
        filename = archive_path.split('/')[-1]
        foldername = '/data/web_static/releases/' + filename.split('.')[0]
        run('mkdir -p {}'.format(foldername))
        run('tar -xzf /tmp/{} -C {}'.format(filename, foldername))
        run('rm /tmp/{}'.format(filename))
        run('mv {}/web_static/* {}'.format(foldername, foldername))
        run('rm -rf {}/web_static'.format(foldername))

        # Delete the symbolic link /data/web_static/current from the web server
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link /data/web_static/current on the web server
        run('ln -s {} /data/web_static/current'.format(foldername))

        print("New version deployed!")
        return True
    except Exception as e:
        print(e)
        return False
