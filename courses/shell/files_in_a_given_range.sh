#!/usr/bin/env bash

IFN='input'
counter=1
line=''
start_at=0
stop_at=-1


while read -r line ; do
    if (( 1 == counter )) ; then
        IFS=' ' read -r start_at stop_at <<< "${line}"
    else #(( 0 != counter )) ; then
        if (( start_at <= counter )) && (( counter <= stop_at )) ; then
            echo "${line}"
        fi
    fi
    if (( stop_at < counter )) ; then
        exit
    fi
    ((counter+=1))
done < "${IFN}"
