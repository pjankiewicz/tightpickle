import cPickle as pickle
import zlib

""" Compressed version of pickle """ 

def zdumps(obj, compression_level = 3):
  return zlib.compress(pickle.dumps(obj,pickle.HIGHEST_PROTOCOL),compression_level)

def zloads(zstr):
  return pickle.loads(zlib.decompress(zstr))
  
def dump(obj,path):
    compr = zdumps(obj)
    with open(path,"wb") as fp:
        fp.write(compr)
        
def load(path):
    with open(path,"rb") as fp:
        compr = fp.read()
    return zloads(compr)
