import time
import multiprocessing



start = time.perf_counter()

def do_something():
    print("sleeping 6 second...")
    time.sleep(6)
    print("Done sleeping...")

def do_something2():
    print("sleeping 3 second...")
    time.sleep(3)
    print("Done sleeping...")

def main():
    p1 = multiprocessing.Process(target=do_something)
    p2 = multiprocessing.Process(target=do_something)
    p3 = multiprocessing.Process(target=do_something2)
    
    p1.start()
    finish = time.perf_counter()

    print(f"Finished in {round(finish-start, 2)} second(s)")


if __name__ == '__main__':
    main()
