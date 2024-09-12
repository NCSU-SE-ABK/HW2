''' 
The function below generate an array of random numbers using shuf 
'''
import sys,logging
import subprocess

logging.basicConfig(filename='rand_debugging.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s  %(message)s')
logging.debug("NEW LOG RAND File" )
def random_array(arr):
    '''
    Shuffles an array by replacing its element with random integers using shuf command 
    '''
    logger = logging.getLogger(__name__)
    shuffled_num = None
  
    logger.debug("shuffled_num: %r",shuffled_num)
    # for i in range(len(arr)):

    for i, _ in enumerate(arr):
        logger.debug("Processing index: %r",i)

        shuffled_num = subprocess.run(
            ["/opt/homebrew/bin/shuf", "-i1-20", "-n1"], capture_output=True,check=True)
        
        # logger.debug("shuffled stdout: %r",shuffled_num)
        arr[i] = int(shuffled_num.stdout)
        logger.debug("Assigned random number %r to arr[%r]", arr[i],i)
    logger.debug("final arr: %r",arr)
    return arr
