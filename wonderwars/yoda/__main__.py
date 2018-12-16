import subprocess


if __name__ == "__main__":
    subprocess.call('gunicorn --workers=2 -c wonderwars/gunicorn_config.py wonderwars.yoda.yoda_serve:app', shell=True)
