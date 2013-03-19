#!/usr/bin/env python
# Author: SnZ <snz@spinacz.org> ~ http://spinacz.org
# License: Released under the GPL license (http://www.gnu.org/copyleft/gpl.html)

import re, glob
from optparse import OptionParser
lmagic=76561197960265728

def parse_logs():
  all=[]
  for file in glob.glob('./UserLogs/ServerLog_*.log'):
    with open(file, 'r') as f:
      out = sorted(set(re.findall(r'New Player (.*) id=([0-9]+)', f.read())))
      all += out
  for id in all:
    print "%s %s http://steamcommunity.com/profiles/%d" % (id[0], id[1], lmagic+long(id[1]))

def g2s(options):
  print "Global ID: %s" % options.g2s
  print "SteamID: %d" % (lmagic+long(options.g2s))
  print "Steam Profile: http://steamcommunity.com/profiles/%d" % (lmagic+long(options.g2s))

def s2g(options):
  print "SteamID: %s" % options.s2g
  print "Global ID: %d" % (long(options.s2g)-lmagic)

def main():
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option("-s", "--g2s", dest="g2s",
                      help="Converts Global ID to SteamID (ex. 51877527)")
    parser.add_option("-g", "--s2g", dest="s2g",
                      help="Converts SteamID to Global ID (ex. 76561198012143255)")
    parser.add_option("-p", "--parse", dest="parse", action="store_true",
                      help="Parse all logs in ./UserLogs directory")

    (options, args) = parser.parse_args()

    if options.parse:
      parse_logs()
    elif options.g2s:
      g2s(options)
    elif options.s2g:
      s2g(options)
    else:
      parser.print_help()

if __name__ == "__main__":
    main()
