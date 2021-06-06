import time
from directkeys import ReleaseKey, PressKey, W, A, S, D, E, F8


def main():
    
    for i in list(range(3))[::-1]:
            print(i+1)
            time.sleep(1)


    while(True):
        PressKey(E)
        time.sleep(1)
        ReleaseKey(E)
        time.sleep(10)
        
    
main()
