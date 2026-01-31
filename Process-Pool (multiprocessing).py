import os, hashlib
from multiprocessing import Pool

def hash_file(args):
    path, hash_alg = args
    h = hashlib.new(hash_alg)
    with open(path, 'rb') as f:
        h.update(f.read())
    stat = os.stat(path)
    return path, {
        "size": stat.st_size,
        "mtime": stat.st_mtime,
        "hash": h.hexdigest()
    }

def scan(root, hash_alg):
    files = []
    for d, _, fs in os.walk(root):
        for f in fs:
            files.append((os.path.join(d, f), hash_alg))
    with Pool() as p:
        return dict(p.map(hash_file, files))
