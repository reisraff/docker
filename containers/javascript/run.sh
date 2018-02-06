#!/bin/bash

node -v && npm -v && gulp -v && bower -v && sleep 3 && echo 'Container Done!'

tail -f /dev/null
