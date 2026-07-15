# Tachyon as a timeline profiler

Create environment (one-time):

```bash
sudo apt-get install libzstd-dev
pyenv install 3.15.0b3
pyenv shell 3.15.0b3
python -m venv venv
```

Activate environemnt:

```bash
source venv/bin/activate
```

Run profiler:

```bash
python -m profiling.sampling run --gecko -o tdemo.json --all-threads tdemo.py
python -m profiling.sampling run --gecko -o ademo.json --async-aware ademo.py
python -m profiling.sampling run --gecko -o pdemo.json --subprocesses pdemo.py
```
