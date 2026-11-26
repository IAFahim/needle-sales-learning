import sys,re,os
D='/mnt/project-files/needle-debate/'
B=D+'batches/'
def parse(path):
    t=open(path).read()
    parts=re.split(r'^## A(\d+)\s*$',t,flags=re.M)
    out={}
    for i in range(1,len(parts),2):
        out[int(parts[i])]=parts[i+1].strip()
    return out
def field(block,name):
    m=re.search(r'^'+name+r':\s*(.*?)(?=^\w[\w ]*?:|\Z)',block,re.M|re.S)
    return m.group(1).strip().replace('\n',' ') if m else ''
for bid in sys.argv[1:]:
    if os.path.exists(B+f'merged-{bid}'): print(bid,'already'); continue
    k=int(bid[1:]); base=104+10*(k-1)
    A=parse(B+f'attacks-{bid}.md'); Df=parse(B+f'defenses-{bid}.md'); V=parse(B+f'verdicts-{bid}.md')
    log=''; design=''; summ=''
    for i in range(1,11):
        n=base+i-1
        a,d,v=A.get(i,''),Df.get(i,''),V.get(i,'')
        topic=field(a,'TOPIC'); win=field(v,'Winner').split()[0] if field(v,'Winner') else '?'
        why=field(v,'Why'); fix=field(v,'Fix needed'); add=field(v,'Worth adding')
        hard=field(d,'NEW HARDENING')
        log+=f"\n### Round {n}. Winner: {win}\n- Topic: {topic}\n- Attack: {field(a,'SCENARIO')} {field(a,'WHY IT BREAKS')}\n- Defense: {field(d,'DEFENSE')}\n- Verdict: {why}\n"
        if win=='Breaker':
            log+=f"- Fix: {fix}\n"; design+=f"- R{n} (LOST, fixed): {topic}. Fix: {fix}\n"
        elif hard and hard.lower().strip('. ') not in ('none','n/a',''):
            design+=f"- R{n} (won, hardened): {hard[:400]}\n"
        summ+=f"{n}\t{win}\t{topic}\t{fix if win=='Breaker' else ''}\t{add}\n"
    open(B+f'log-{bid}.md','w').write(log)
    with open(D+'design.md','a') as f: f.write(design)
    with open(B+'summary.tsv','a') as f: f.write(summ)
    open(B+f'merged-{bid}','w').write('1')
    print(bid,'merged', summ.count('\tBreaker\t'),'losses')
