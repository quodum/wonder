# wonder

## Install

```sh
# If necessary, use pyenv to set the local python recommended version to 2.7.15
pyenv install 2.7.15
pyenv local 2.7.15

# Create virtual environment
virtualenv -p python2 env

# Activate environment
. env/bin/activate

# Install package
make
```

## Use

```
cd wonder

python -m wonderwars.hello

python -m wonderwars.vader
python -m wonderwars.yoda
```
