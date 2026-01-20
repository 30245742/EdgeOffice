import os, hashlib, queue, threading

work_q = queue.Queue()
results = {}

def worker(hash_alg):
    h = hashlib.new(hash_alg)
    while True:
        path = work_q.get()
        if path is None:
            break
        with open(path, 'rb') as f:
            h_copy = h.copy()
            h_copy.update(f.read())
        stat = os.stat(path)
        results[path] = {
            "size": stat.st_size,
            "mtime": stat.st_mtime,
            "hash": h_copy.hexdigest()
        }
        work_q.task_done()

def scan(root):
    for dirpath, _, files in os.walk(root):
        for f in files:
            work_q.put(os.path.join(dirpath, f))