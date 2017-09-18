#!/bin/bash

/etc/init.d/oracle-xe stop
/etc/init.d/oracle-xe start

tail -f /dev/null
