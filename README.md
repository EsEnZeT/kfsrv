# kfsrv
=========

Kfsrv is a solution containing various scripts responsible for the automation of the [Killing Floor] server.
[Killing Floor]: http://store.steampowered.com/app/1250/


## Features
#### [`kfsrv`]
* Server start/stop/restart
* Server update
* Server password lock/unlock/check
* Show current server status

#### [`loader.sh`]
* Part of the [`kfsrv`] service -- auto restart server if died/crashed

#### [`kfsrv-autoup.sh`]
* Server auto update (99.9% safe, will update only if server is empty)

#### [`kfsrv-logread.py`]
* Ability to parse through server logs and show player nicks and their steam profiles
* Single Global ID -> SteamID
* Sigle SteamID -> Global ID
[`kfsrv`]: https://raw.github.com/EsEnZeT/kfsrv/master/kfsrv
[`loader.sh`]: https://raw.github.com/EsEnZeT/kfsrv/master/loader.sh
[`kfsrv-autoup.sh`]: https://raw.github.com/EsEnZeT/kfsrv/master/kfsrv-autoup.sh
[`kfsrv-logread.py`]: https://raw.github.com/EsEnZeT/kfsrv/master/kfsrv-logread.py

## Prerequisites
* installed Killing Floor server + new user (ex. kf)
* [SteamCMD]
* [Netcat]
* [Python]
* [Screen]

[SteamCMD]: https://developer.valvesoftware.com/wiki/SteamCMD
[Netcat]: http://netcat.sourceforge.net/
[Python]: http://www.python.org/
[Screen]: http://linux.die.net/man/1/screen

## Installation

#### Debian
```bash
apt-get update
apt-get install netcat python screen

git clone https://github.com/EsEnZeT/kfsrv.git && cd kfsrv
mv kfsrv-autoup.sh .mscreen.conf /home/kf/
mv kfsrv-logread.py /home/kf/Server/
mv loader.sh /home/kf/Server/System/
mv kfsrv /etc/init.d/
```

Auto start on boot
```bash
update-rc.d kfsrv defaults
```

Auto updates at 7am `crontab -e`
```bash
0 7 * * * /home/kf/kfsrv-autoup.sh
```

Edit `/etc/init.d/kfsrv`
```bash
# Example options
TITLE='Killing Floor Server'                                          # Script title (ex. KF Server)
NAME='kfsrv'                                                          # Name for screen session (ex. kfsrv)
LOADER='loader.sh'                                                    # Server loader
DIR='/home/kf'                                                        # User dir (ex. /home/kf)
KFBIN='/home/kf/Server/System'                                        # Game path (ex. /home/kf/Server/System)
USER='kf'                                                             # Server user (ex. kf)
sUSER='steam1user'                                                    # Steam user (create one!)
sPASS='steam1pass'                                                    # Steam password
INI='kfsrv.ini'                                                       # Server configuration file (ex. server.ini)
```

Default location for [SteamCMD] is `$DIR/SteamCMD`.

You may need to edit `kfsrv-autoup.sh` if you are using custom ports (7717 is default GameSpy query port).

Remember to fix file permissions and ownership if needed.


## Usage
#### `kfsrv-logread.py -h`
```bash
Usage: kfsrv-logread.py [options] arg

Options:
  -h, --help         show this help message and exit
  -s G2S, --g2s=G2S  Converts Global ID to SteamID (ex. 64148252)
  -g S2G, --s2g=S2G  Converts SteamID to Global ID (ex. 76561198024413980)
  -p, --parse        Parse all logs in ./UserLogs directory
```


#### `service kfsrv`
```bash
Usage: ./kfsrv {start|stop|restart|update|pwd <?>|pwdc|status}
```


## License
Released under the GPL license (http://www.gnu.org/copyleft/gpl.html).

