import reader
import normald

a=reader.trainortest()

dcount=a[2]
attrbc=a[1]
data=a[0]
metad=a[3]
metad=metad.split(',')
lspos=[];lsneg=[]
tcountpos=[];tcountneg=[]
pcheck=[];ncheck=[]
p_crux=[];n_crux=[]
pcount=[];ncount=[]
for x in range(0,attrbc-1):
    lspos.append([])
    lsneg.append([])
    tcountpos.append([])
    tcountneg.append([])
    
for rit in data:
    dtemp=rit.split(',')
    if(dtemp[-1]!='' and int(dtemp[-1])>0):
        for x in range(0,attrbc-1):
            lspos[x]+=[dtemp[x]]
    elif(dtemp[-1]!='' and int(dtemp[-1])==0):
        for x in range(0,attrbc-1):
            lsneg[x]+=[dtemp[x]]

        
for x in range(0,attrbc-1):
    lspos[x].sort()
    lsneg[x].sort()

for x in range(0,attrbc-1):
    z=1
    while(z==1):
        if ('Mi' in lspos[x]):
            lspos[x].remove('Mi')
        else:
            z=0
    z=1
    while(z==1):
        if ('Mi' in lsneg[x]):
            lsneg[x].remove('Mi')
        else:
            z=0

#parse conversion to float
for x in range(0,attrbc-1):
    n1=len(lspos[x])
    n2=len(lsneg[x])
    for meg in range(0,n1):
        lspos[x][meg]=float(lspos[x][meg])
    for meg in range(0,n2):
        lsneg[x][meg]=float(lsneg[x][meg])

#divisor values
for x in range(0,attrbc-1):
    tcountpos[x]=len(lspos[x])
    tcountneg[x]=len(lsneg[x])
    
for x in range(0,attrbc-1):
    trunc=[]
    for rn in range(0,len(lspos[x])):
                    if(lspos[x][rn] not in trunc):
                        trunc+=[lspos[x][rn]]
    if(len(trunc)>2):
       pcheck+=['m']
    else:
        pcheck+=['b']
    trunc=[]
    for rn in range(0,len(lsneg[x])):
                    if(lsneg[x][rn] not in trunc):
                        trunc+=[lsneg[x][rn]]
    if(len(trunc)>2):
       ncheck+=['m']
    else:
        ncheck+=['b']

for x in range(0,attrbc-1):
    if(pcheck[x]=='m'):
        m1=normald.mean(lspos[x])
        s1=normald.sd(lspos[x],m1)
        p_crux+=[(m1,s1)]
    elif(pcheck[x]=='b'):
        p_crux+=[(0,100)]
    if(ncheck[x]=='m'):
        m2=normald.mean(lsneg[x])
        s2=normald.sd(lsneg[x],m2)
        n_crux+=[(m2,s2)]
    elif(ncheck[x]=='b'):
        n_crux+=[(0,100)]

for x in range(0,attrbc-1):
    zval=0;oval=0
    if(pcheck[x]=='b'):
        for rn in range(0,len(lspos[x])):
            if(int(lspos[x][rn])==0):
                zval+=1
            else:
                oval+=1
    pcount+=[(zval,oval)]
    zval=0;oval=0
    if(ncheck[x]=='b'):
        for rn in range(0,len(lsneg[x])):
            if(int(lsneg[x][rn])==0):
                zval+=1
            else:
                oval+=1
    ncount+=[(zval,oval)]
            
print("Training is complete")
retry='y'
while(retry=='y'):
    atb=[]
    scorep=1
    scoren=1
    for x in range(0,attrbc-2):
        print("Enter the value of attribute "+metad[x] +" type: "+pcheck[x]+" \t")
        r=int(input())
        atb+=[r]
    for meg in range(0,len(atb)):
        if(pcheck[meg]=='b'):
            scorep*=((pcount[meg][int(atb[meg])]+1)/tcountpos[meg])
        elif(pcheck[meg]=='m'):
            scorep*=normald.n_distro(float(atb[meg]),p_crux[x][0],p_crux[x][1])
    for meg in range(0,len(atb)):
        if(ncheck[meg]=='b'):
            scoren*=((ncount[meg][int(atb[meg])]+1)/tcountneg[meg])
        elif(ncheck[meg]=='m'):
            scoren*=normald.n_distro(float(atb[meg]),n_crux[x][0],n_crux[x][1])
    print("\nScore obtained for postive case"+str(scorep))
    print("\nScore obtained for negative case"+str(scoren))
    if(scorep<scoren):
        print("Patient is safe. For now\n")
    elif(scoren<scorep):
        print("Patient is unsafe. Report for treatement ASAP\n")
    elif(scoren==scorep):
        print("Predicition Problem. Please report for further testing\n")
    print("Enter y if you want to continue")
    retry=input()
