import sys, datetime, os, time

from random import randrange
MAX_WAIT_TIME_SECS = 10 # max waiting time to launch benchmark

MAX_PRIME = 10000 # max prime. The higher is the number, the harder is the CPU benchmark

if __name__ == '__main__':
    if len(sys.argv)!=2:
        print "Usage:\n ",sys.argv[0]," <stats-file> "
    stats_file = sys.argv[1]

    time.sleep(randrange(MAX_WAIT_TIME_SECS)) 

    now_formated = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    #do the CPU tests
    os.system("sysbench --test=cpu --cpu-max-prime="+str(MAX_PRIME)+" run | sed -rn 's/\s*total time:\s*([0-9.]*)s/CPU "+now_formated+" \\1/p' >> "+stats_file)
    
    
    # do the disk I/O tests   
    now_formated = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    os.system("sysbench --test=fileio --file-total-size=500M prepare")
    os.system("sysbench --test=fileio --file-total-size=500M --file-test-mode=rndrw --init-rng=on --max-time=30 --max-requests=0 run |  sed -rn 's/.*\(([0-9.]+)Mb\/sec\).*/DISK "+now_formated+" \\1/p' >> "+stats_file)
    os.system("sysbench --test=fileio --file-total-size=500M cleanup")

        
    
