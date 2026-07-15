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
python -m profiling.sampling run --async-aware --flamegraph -o demo.html demo.py
```
