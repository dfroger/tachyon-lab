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
python -m profiling.sampling run --gecko -o outputs/tdemo.json --all-threads  scripts/tdemo.py
python -m profiling.sampling run --gecko -o outputs/ademo.json --async-aware  scripts/ademo.py
python -m profiling.sampling run --gecko -o outputs/pdemo.json --subprocesses scripts/pdemo.py
```

The expected outputs are:

```
Time (s)  0.0         0.5         1.0         1.5         2.0         2.5
          |           |           |           |           |           |
Main      [                         request                          ]
          [ pre_proc ][            processing            ][post_proc ]

Thread-1              [          sub_processing          ]
                      [   foo    ][   bar    ][   baz    ]

Thread-2              [          sub_processing          ]
                      [   foo    ][   bar    ][   baz    ]

Thread-3              [          sub_processing          ]
                      [   foo    ][   bar    ][   baz    ]
```

- `ademo.py`: `Task-1` intead of `Thread-1`,
- `pdemo.py`: `Process-1` intead of `Thread-1`.
