import sys,re
# ensure posts-<bid>.md uses 104-based numbering
for bid in sys.argv[1:]:
    p=f'/mnt/project-files/needle-debate/batches/posts-{bid}.md'
    t=open(p).read(); k=int(bid[1:]); want=104+10*(k-1)
    first=int(re.search(r'^=== R(\d+)',t,re.M).group(1))
    d=want-first
    if d:
        t=re.sub(r'^=== R(\d+)',lambda m:f'=== R{int(m.group(1))+d}',t,flags=re.M)
        t=re.sub(r'Round (\d+):',lambda m:f'Round {int(m.group(1))+d}:',t)
        open(p,'w').write(t)
    print(bid,'shift',d)
