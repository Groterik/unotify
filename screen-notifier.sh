#!/bin/bash

usage() { echo "Usage: $0 [-h] [-c] -m message "; }
msg="<no-msg>"

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
declare -a CMDS=("macosx-notifier.sh" "osd-notifier.sh")

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
      excode=0
      for i in "${CMDS[@]}"
      do
        "${DIR}/""${i}" -c
        cmdcode=$?
        excode=$((excode || cmdcode))
      done
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

for i in "${CMDS[@]}"
do
  CMD=${DIR}/"${i}"
  ${CMD} -c &> /dev/null
  if [ $? -eq 0 ];then
    ${CMD} -m "${msg}"
    exit $?
  fi
done

echo "Screen notification is unsupported" 1>&2

exit 1

