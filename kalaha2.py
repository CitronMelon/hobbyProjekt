def turn(d):
    f=[lambda i,s,h:s+6-h+i>12,lambda i:(d[5][i],0)[i==d[2]-1]+d[3]//14+d[7].count(i),lambda:(f[1](d[4])==1 and d[3]>7 and(d[4]in range(d[0]-6,d[0]))),lambda:sum([f[1](i)for i in range(d[0]-6,d[0])])]
    print("".join([f"[{i}]"for i in d[5][0:6]])+"\n"+"".join(f"[{b}]"for b in[d[5][13],0,0,0,0,d[5][6]])+"\n"+"".join([f"[{i}]"for i in d[5][12:6:-1]]))
    g=[lambda x,o,w:d[8](int(input(f"Player {d[0]%6+1}´s turn,\nchoose a bowl between 1 and 6 :"))+d[0]-6,d[0],d[5],x,d,f[0],d[1],o,w),lambda i:(sum(d[5][(d[0]+1)%14:d[1]]),0)[i!=d[0]]]
    d[2:8]=g[0](g[0],lambda i,f,a,s,h:[(i+u+f(u,s,h))%14 for u in range(a[(i-1)]%14)],lambda i,a,e:(i-1+a[i-1])%14+((i-1+a[i-1])%14==e))
    d[5]=[(f[1](i)+((0,g[1](i))[not f[3]()],f[1](d[4])+f[1](12-d[4]))[f[2]()and i==d[0]],0)[i==d[2]-1 or(f[2]()and i in[d[4],12-d[4]])or(not f[3]()and i not in d[:2])]for i in d[6]]
    return f"Winner is Player{d[5][6]<d[5][13+1]}"if not sum([b for b in d[6]if b not in d[:2]])else turn(d if d[4]==d[0]else[d[1],d[0]]+d[2:])
print(turn([6,13,-1,0,0,[0,0,0,0,0,0,6,6,6,6,6,6,0],range(14),[],lambda i,h,a,g,d,f,e,o,w:[i,a[i-1],w(i,a,e)]+d[5:7]+[o(i,f,a,i,h)]if(i-h+6 in range(1,7)and a[i-1]!=0)else g(g,o,w)]))