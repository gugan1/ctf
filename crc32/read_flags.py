flag=[]
with open(".\\flag.txt",'r') as f :
    for i in range(0,10):
        flag.append(f.readline())
flags=[]     
for l1 in range(0,10):
    for l2 in range(0,10):
        for l3 in range(0,10):
            for l4 in range(0,10):
                for l5 in range(0,10):
                    for l6 in range(0,10):
                        for l7 in range(0,10):
                            for l8 in range(0,10):
                                for l9 in range(0,10):
                                    for l10 in range(0,10):
                                        flags.append(flag[l1]+flag[l2]+flag[l3]+flag[l4]+flag[l5]+flag[l6]+flag[l7]+flag[l8]+flag[l9]+flag[l10]+'\n')

            with open(".\\flags.txt",'w') as f1 :
                f1.write(str(flags))
                flags.clear()
                                        
                                    
     
     