#!/bin/bash

NoPlayers(){
/etc/init.d/kfsrv stop
/etc/init.d/kfsrv update
/etc/init.d/kfsrv start
}

Check(){
if echo -ne "\\players\\" | nc -u -w 1 127.0.0.1 7717 | grep -Eoq "player_[0-9]+"; then
  sleep 360
  Check
else
  NoPlayers
fi
}

Check
