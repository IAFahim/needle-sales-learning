import sys,re
brief='/mnt/project-files/needle-debate/breaker-brief-v2.md'
b=open(brief).read()
added=0
for bid in sys.argv[1:]:
    t=open(f'/mnt/project-files/needle-debate/batches/attacks-{bid}.md').read()
    for m in re.findall(r'^TOPIC:\s*(.+)$',t,re.M):
        line='- '+m.strip()
        if line not in b:
            b=b.rstrip()+'\n'+line+'\n'; added+=1
open(brief,'w').write(b)
print('added',added)
