import subprocess


if __name__ == "__main__":
    subprocess.call('gunicorn --workers=2 -b 127.0.0.1:8000 -c wonderwars/gunicorn_config.py wonderwars.vader.vader_serve:app', shell=True)
