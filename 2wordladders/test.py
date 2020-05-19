import multiprocessing

def worker(procnum, return_dict):
    '''worker function'''
    print(str(procnum) + ' represent!')
    return_dict.put(procnum)


if __name__ == '__main__':
    manager = multiprocessing.Queue()
    return_dict = manager
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,return_dict))
        jobs.append(p)
        p.start()

    for proc in jobs:
        proc.join()
    
    for _ in range(return_dict.qsize()):
        print(return_dict.get())