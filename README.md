# CSEP-561 Project 3: Mininet Bufferbloat

This directory contains starter and support code for project 3. You may want to
version control this file for your team and will need to update this readme file
with your own information in your final submission.

For details of the project itself, see the
[Project 3 page](https://courses.cs.washington.edu/courses/csep561/22sp/projects/project3/)
of the course website.

# Submission Details

Name: Jason Bian
UWNetID: 2101685


## Instructions to reproduce your results:
  > reno: sudo ./run.sh
  > bbr: sudo ./run_bbr.sh
  > sudo mn -c to clear between runs

## Answers to the questions:

### Part 2
  1. 20: Mean latency: 0.7047572857142858
Standard deviation of latency: 0.5085332211104274
     100: Mean latency: 2.565839296296297
Standard deviation of latency: 1.6100090516245167
  2. Reno attempts to achieve full utilization by increasing output buffer size until the link is full. This causes the switch to congest and new TCP connections have packets placed at end of queue. 
  3. 1000 packet max, 1500*1000*8/(100 MB/s) = 0.12 s
  4. As queue size increases, the upper threshold of the sawtooth also raises, average RTT increases with queue size
  5. Using different queue management control such as reno or TCP that drop packets prior to queue fill up would prevent long lived TCP flows from congesting the network.
     Differentication of flows between short and long flows via TCP headers

### Part 3
  1. 20: Mean latency: 0.31808247368421055
Standard deviation of latency: 0.07666478577367182
     100: Mean latency: 0.3227190789473684
Standard deviation of latency: 0.06987078885168625

  2. For both, the shorter queue gives a faster fetch time than Part2. Bbr also has less variance between q=20 and q= 100. 
  3. BBR drops packets more often compared to the saw-tooth seen in TCP-Reno. This is due to different queue management control and drop critera.
  4. I think so, bbr should solve the bufferbloat problem in legacy loss-based congestion control. However, I'm not sure how this extrapolates to all congestion cases outside of this assignment scenario.
