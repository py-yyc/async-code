# async programming

Note: this code is totally taken without permission from David Beazleys
talk (https://www.youtube.com/watch?v=ZzfHjytDceU). Inside that
unassuming dad-bod is an absolute titan of Python knowledge and I highly
recommend that everybody watches his talks on YouTube.

## install

make a python 3 virtual environment

```bash
virtualenv -p python3.6 venv
source venv/bin/activate
```

## run

```bash
./echoserver.py
```

from another terminal


```bash
nc localhost 2500
# type a string then enter
# ctrl-d to "hangup"
```
