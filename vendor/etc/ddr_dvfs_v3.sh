#!/bin/bash
# files description
# Copyright Huawei Technologies Co., Ltd. 2010-2018. All rights reserved.
# Author:

set -e

echo "ddr auto freq script"

node_name=/sys/class/devfreq/ddrfreq/available_frequencies
node_separator_num=$(cat "$node_name" | grep -o ' ' | busybox wc -l)
freq_level_num=$(("$node_separator_num"+1))
echo "$node_separator_num" "$freq_level_num"

while true
do

for i in $(busybox seq 1 1 "$freq_level_num")
do
freq=$(cat "$node_name" | busybox cut -d ' ' -f "$i")
echo lock freq is "$freq"
echo "$freq" > /sys/class/devfreq/ddrfreq/max_freq
echo "$freq" > /sys/class/devfreq/ddrfreq/min_freq
echo "$freq" > /sys/class/devfreq/ddrfreq/max_freq
echo "$freq" > /sys/class/devfreq/ddrfreq_up_threshold/max_freq
echo "$freq" > /sys/class/devfreq/ddrfreq_up_threshold/min_freq
echo "$freq" > /sys/class/devfreq/ddrfreq_up_threshold/max_freq
sleep 0.5s
cat /sys/class/devfreq/ddrfreq/cur_freq
echo 0 > /sys/class/devfreq/ddrfreq/max_freq
echo 0 > /sys/class/devfreq/ddrfreq/min_freq
echo 0 > /sys/class/devfreq/ddrfreq/max_freq
echo 0 > /sys/class/devfreq/ddrfreq_up_threshold/max_freq
echo 0 > /sys/class/devfreq/ddrfreq_up_threshold/min_freq
echo 0 > /sys/class/devfreq/ddrfreq_up_threshold/max_freq
done

freq_min=$(cat "$node_name" | busybox cut -d ' ' -f 1)
freq_max=$(cat "$node_name" | busybox cut -d ' ' -f "$freq_level_num")
echo min freq is "$freq_min", max freq is "$freq_max"
echo "$freq_min" > /sys/class/devfreq/ddrfreq/min_freq
echo "$freq_max" > /sys/class/devfreq/ddrfreq/max_freq
sleep 1

for j in $(seq 1 1 20)
do
echo "$j"
for i in $(busybox seq 1 1 "$freq_level_num")
do
freq=$(cat "$node_name" | busybox cut -d ' ' -f "$i")
echo lock freq is "$freq"
echo "$freq" > /sys/class/devfreq/ddrfreq/max_freq
echo "$freq" > /sys/class/devfreq/ddrfreq/min_freq
echo "$freq" > /sys/class/devfreq/ddrfreq/max_freq
echo "$freq" > /sys/class/devfreq/ddrfreq_up_threshold/max_freq
echo "$freq" > /sys/class/devfreq/ddrfreq_up_threshold/min_freq
echo "$freq" > /sys/class/devfreq/ddrfreq_up_threshold/max_freq
sleep 0.1s
cat /sys/class/devfreq/ddrfreq/cur_freq
echo 0 > /sys/class/devfreq/ddrfreq/max_freq
echo 0 > /sys/class/devfreq/ddrfreq/min_freq
echo 0 > /sys/class/devfreq/ddrfreq/max_freq
echo 0 > /sys/class/devfreq/ddrfreq_up_threshold/max_freq
echo 0 > /sys/class/devfreq/ddrfreq_up_threshold/min_freq
echo 0 > /sys/class/devfreq/ddrfreq_up_threshold/max_freq
done

done

done
