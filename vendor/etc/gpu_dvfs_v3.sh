#!/bin/bash
# files description
# Copyright Huawei Technologies Co., Ltd. 2010-2018. All rights reserved.
# Author:

set -e

echo "gpu auto freq script"

node_name=/sys/class/devfreq/gpufreq/available_frequencies
node_separator_num=$(cat "$node_name" | grep -o ' ' | busybox wc -l)
freq_level_num=$(("$node_separator_num"+1))
echo "$node_separator_num" "$freq_level_num"

while true
do

for i in $(busybox seq 1 1 "$freq_level_num")
do
freq=$(cat "$node_name" | busybox cut -d ' ' -f "$i")
echo lock freq is "$freq"
echo "$freq" >  /sys/class/devfreq/gpufreq/max_freq
echo "$freq" >  /sys/class/devfreq/gpufreq/min_freq
echo "$freq" >  /sys/class/devfreq/gpufreq/max_freq
sleep 1
cat /sys/class/devfreq/gpufreq/cur_freq
done

freq_min=$(cat "$node_name" | busybox cut -d ' ' -f 1)
freq_max=$(cat "$node_name" | busybox cut -d ' ' -f "$freq_level_num")
echo min freq is "$freq_min", max freq is "$freq_max"
echo "$freq_min" >  /sys/class/devfreq/gpufreq/min_freq
echo "$freq_max" >  /sys/class/devfreq/gpufreq/max_freq
sleep 3

done
