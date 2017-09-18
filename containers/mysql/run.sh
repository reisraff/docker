#!/bin/bash

/etc/init.d/mysql stop
/etc/init.d/mysql start

tail -f /dev/null
