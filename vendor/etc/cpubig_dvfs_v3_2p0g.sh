#!/bin/bash
# files description
# Copyright Huawei Technologies Co., Ltd. 2010-2018. All rights reserved.
# Author:

set -e

echo "a72 big auto freq script"

node_name=/sys/devices/system/cpu/cpu4/cpufreq/scaling_available_frequencies
node_separator_num=$(cat "$node_name" | grep -o ' ' | busybox wc -l)
freq_level_num=$(("$node_separator_num"))
echo "$node_separator_num" "$freq_level_num"

while true
do

for i in $(busybox seq 1 1 "$freq_level_num")
do
freq=$(cat "$node_name" | busybox cut -d ' ' -f "$i")
echo lock freq is "$freq"
echo "$freq" >  /sys/devices/system/cpu/cpu4/cpufreq/scaling_max_freq
echo "$freq" >  /sys/devices/system/cpu/cpu4/cpufreq/scaling_min_freq
echo "$freq" >  /sys/devices/system/cpu/cpu4/cpufreq/scaling_max_freq
sleep 1
cat /sys/devices/system/cpu/cpu4/cpufreq/scaling_cur_freq
done

freq_min=$(cat "$node_name" | busybox cut -d ' ' -f 1)
freq_max=$(cat "$node_name" | busybox cut -d ' ' -f "$freq_level_num")
echo min freq is "$freq_min", max freq is "$freq_max"
echo "$freq_min" >  /sys/devices/system/cpu/cpu4/cpufreq/scaling_min_freq
echo "$freq_max" >  /sys/devices/system/cpu/cpu4/cpufreq/scaling_max_freq
sleep 3

done
