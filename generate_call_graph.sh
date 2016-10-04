#!/usr/bin/env bash
binary=$1
if [[ $1 == "-h" ]]; then
    echo "Usage: $0 <binary> [rootFunction=main]"
    exit
fi
shift
opts=$@
tmpFile=$(mktemp)
objdump -d ${binary} | sed -r '/(^0|callq[^\*]*$)/!d;s/^.*callq[^<]*<([^>]*)>.*$/\t\1/;s/^0[^<]*<([^>]*)>.*/\1/' | c++filt -i -p > ${tmpFile}
echo "[$(./parse_objdump.py ${tmpFile} ${opts})]"
