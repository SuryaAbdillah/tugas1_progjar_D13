import os.path
# very simple way: open-read-close
f = open('files/s41066-020-00226-2.pdf', 'r')
#data = f.read() 
#print(data)

fpath = 'files/s41066-020-00226-2.pdf'
sz = os.path.getsize(fpath)
print(f'The {fpath} size is', sz, 'bytes')

f.close()