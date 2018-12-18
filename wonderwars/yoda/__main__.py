import subprocess


if __name__ == "__main__":
    subprocess.call('gunicorn --workers=2 -b 127.0.0.1:8100 -c wonderwars/gunicorn_config.py wonderwars.yoda.yoda_serve:app', shell=True)
