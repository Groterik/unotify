#!/bin/bash

usage() { echo "Usage: $0 [-h] [-c] -m message "; }
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
      hash notify-send &> /dev/null
      excode=$?
      if [ $excode -eq 0 ];then
        echo "Command notify-send is available"
      else
        echo "Command notify-send is unavailable" 1>&2
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

notify-send "unotify" "${msg}"

