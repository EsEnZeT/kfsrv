#!/bin/bash
while true
do
./ucc-bin server KF-WestLondon.rom?game=KFmod.KFGameType?VACSecured=true?MaxPlayers=6?Difficulty=7 ini=kfsrv.ini log=../UserLogs/ServerLog_`date +%d-%m-%Y`.log -nohomedir
echo "--SPAWNING new session!--"
sleep 2
done
