Tools to measure OS performance (Disk and CPU)
==============================================

Created to measure the stability of cloud VMs

How to
------
- Requires [SysBench](http://sysbench.sourceforge.net/)
- Add the following like to cron:
> */5 * * * * python /home/leonardo/noisyneighbors/monitor.py /home/leonardo/noisyneighbors.log
- Collect statistics with stats.py

Optimal conditions require no other processes running besides OS processes





