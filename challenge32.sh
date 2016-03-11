#!/bin/bash

MESSAGE=$(curl --silent --cookie "PHPSESSID=8ic0a8ih38tqblg4ttrdvmliv2" https://ringzer0team.com/challenges/32 | grep -A1 BEGIN | tail -n1)
echo $MESSAGE
FIRST=$(echo "$MESSAGE" | awk '{ print $1 }')
SECOND=$((16#$(echo "$MESSAGE" | awk '{ print $3 }' | awk -Fx '{ print $2 }')))
THIRD=$((2#$(echo "$MESSAGE" | awk '{ print $5 }')))
echo $FIRST + $SECOND - $THIRD
curl --silent --cookie "PHPSESSID=8ic0a8ih38tqblg4ttrdvmliv2" https://ringzer0team.com/challenges/32/$(echo "$FIRST + $SECOND - $THIRD" | bc) | grep FLAG
