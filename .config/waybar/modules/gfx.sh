#!/bin/bash

mode="$(supergfxctl -g)"
state="$(supergfxctl -S)"
pending="$(supergfxctl -P)"
action="$(supergfxctl -p)"
case $mode in 
	Integrated)
		modestring="I"
	;;
	Hybrid)
		modestring="H"
	;;
	AsusMuxDgpu)
		modestring="D"
	;;
esac

if [ $state = "suspended" ]; then
	enabled="\"class\":\"disabled\","
elif [ $state = "active" ]; then
	enabled="\"class\": \"enabled\","
fi
	
waybarjson="{\"text\":\"$modestring\",$enabled\"tooltip\":\"dGPU power: $state\nPending mode: $pending\nPending action: $action\"}"

echo $waybarjson 

exit 0
