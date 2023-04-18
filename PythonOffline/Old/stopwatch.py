import time
import os, sys
# Composed by AI
def stopwatch():
    input("Press Enter to start the stopwatch" )
    start_time = time.time()
    input("Press Enter again to stop the stopwatch" )
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.3f} seconds")

os.system()

if __name__ == '__main__':
    stopwatch()

