#!/bin/bash

usage() { echo "Usage: $0 [-h] [-n] [-i interval_sec] [-m max_tries] command arguments"; }

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
neg="false"
maxtries=5000
interval=5

while getopts ":hni:m:" o; do
  case "${o}" in
    n)
      neg=true
      ;;
    h)
      usage
      exit 0
      ;;
    i)
      interval=${OPTARG}
      ;;
    m)
      maxtries=${OPTARG}
      ;;
    *)
      usage 1>&2
      exit 1
      ;;
  esac
done

shift $((OPTIND-1))

for i in $(seq 1 ${maxtries})
do
  eval "$@"
  st=$?
  if [ "${neg}" == "false" ]; then
    if [ "${st}" == "0" ]; then
      exit 0
    fi
  else
    if [ "${st}" != "0" ]; then
      exit 0
    fi
  fi
  sleep ${interval}
done


exit 1
