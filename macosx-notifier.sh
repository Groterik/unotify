#!/bin/bash

usage() { echo "Usage: $0 [-h] -m message "; }
msg="<no-msg>"

while getopts ":hcm:" o; do
  case "${o}" in
    m)
      msg=${OPTARG}
      ;;
    h)
      usage
      exit 0
      ;;
    c)
      hash osascript &> /dev/null
      excode=$?
      if [ $excode -eq 0 ];then
        echo "Mac OS X osascript notifier is available"
      else
        echo "Mac OS X osascript notifier is unavailable" 1>&2
      fi
      exit $excode
      ;;
    *)
      usage 1>&2
      exit 1
      ;;
  esac
done

if [ "$msg" == "<no-msg>" ]; then
  usage 1>&2
  exit 1
fi

osascript -e "display notification \"${msg/\"/\\\"}\" with title \"Notification\""

