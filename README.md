# Tachyon as a timeline profiler

Create environment (one-time):

```bash
sudo apt-get install libzstd-dev
pyenv install 3.15.0b3
```

Activate environemnt:

```bash
pyenv shell 3.15.0b3
```

## Threads

The timeline for threads:

```bash
python -m profiling.sampling run --gecko -o outputs/tdemo.json --all-threads  scripts/tdemo.py
```

![tdemo](screenshots/tdemo.png)

is as expected:

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


## Processes

The timeline for processes:

```bash
python -m profiling.sampling run --gecko -o outputs/pdemo.json --subprocesses scripts/pdemo.py
```

![pdemo](screenshots/pdemo.png)

is one-line, I would expect:

```
Time (s)  0.0         0.5         1.0         1.5         2.0         2.5
          |           |           |           |           |           |
Main      [                         request                          ]
          [ pre_proc ][            processing            ][post_proc ]

Process-1             [          sub_processing          ]
                      [   foo    ][   bar    ][   baz    ]

Process-2             [          sub_processing          ]
                      [   foo    ][   bar    ][   baz    ]

Process-3             [          sub_processing          ]
                      [   foo    ][   bar    ][   baz    ]
```

## Asyncio Tasks

The timeline for asyncio tasks:

```bash
python -m profiling.sampling run --gecko -o outputs/ademo.json --async-aware --async-mode=all  scripts/ademo.py
```

fails with:

```python
Traceback (most recent call last):
  File "<frozen runpy>", line 201, in _run_module_as_main
  File "<frozen runpy>", line 87, in _run_code
  File "/home/dfroger/.pyenv/versions/3.15.0b3/lib/python3.15/profiling/sampling/__main__.py", line 65, in <module>
    main()
    ~~~~^^
  File "/home/dfroger/.pyenv/versions/3.15.0b3/lib/python3.15/profiling/sampling/cli.py", line 977, in main
    _main()
    ~~~~~^^
  File "/home/dfroger/.pyenv/versions/3.15.0b3/lib/python3.15/profiling/sampling/cli.py", line 1133, in _main
    handler(args)
    ~~~~~~~^^^^^^
  File "/home/dfroger/.pyenv/versions/3.15.0b3/lib/python3.15/profiling/sampling/cli.py", line 1280, in _handle_run
    collector = sample(
        process.pid,
    ...<9 lines>...
        blocking=args.blocking,
    )
  File "/home/dfroger/.pyenv/versions/3.15.0b3/lib/python3.15/profiling/sampling/sample.py", line 529, in sample
    profiler.sample(collector, duration_sec, async_aware=async_aware)
    ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dfroger/.pyenv/versions/3.15.0b3/lib/python3.15/profiling/sampling/sample.py", line 192, in sample
    raise e from None
  File "/home/dfroger/.pyenv/versions/3.15.0b3/lib/python3.15/profiling/sampling/sample.py", line 173, in sample
    flush_pending()
    ~~~~~~~~~~~~~^^
  File "/home/dfroger/.pyenv/versions/3.15.0b3/lib/python3.15/profiling/sampling/sample.py", line 152, in flush_pending
    collector.collect(prev_stack, timestamps_us=ts)
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dfroger/.pyenv/versions/3.15.0b3/lib/python3.15/profiling/sampling/gecko_collector.py", line 255, in collect
    for thread_info in interpreter_info.threads:
                       ^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: '_remote_debugging.AwaitedInfo' object has no attribute 'threads'. Did you mean '.thread_id' instead of '.threads'?
```


I would expected:

```
Time (s)  0.0         0.5         1.0         1.5         2.0         2.5
          |           |           |           |           |           |
Main      [                         request                          ]
          [ pre_proc ][            processing            ][post_proc ]

Task-1                [          sub_processing          ]
                      [   foo    ][   bar    ][   baz    ]

Task-2                [          sub_processing          ]
                      [   foo    ][   bar    ][   baz    ]

Task-3                [          sub_processing          ]
                      [   foo    ][   bar    ][   baz    ]
```
