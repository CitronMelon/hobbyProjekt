from tkinter import *
window = Tk()
p1 = [6,6,6,6,6,6,0]
p2 = [6,6,6,6,6,6,0]
a = [6,6,6,6,6,6,0,6,6,6,6,6,6,0]

def k(a_p,u_p,p_2,map,g):
    print("   "+"".join([f"[{i}]"for i in a_p])+"\n"+"".join([f"[{i}]"for i in u_p[6::-1]]))
    (start, end) = (lambda j ,h: h(j(),h,j))(lambda:int(input(f"P{p_2+1}, choose a bowl between 1 and 6 :")),lambda i,f,g : (i,(i+map[i-1]-1)%13) if 0<i<7 and a_p[i-1]!=0 else f(g(),f,g))


    map =[max(0,((g(end,map,start)+g(12-end,map,start)))*(-2)**(i!=6)*(12<start+map[start-1]<21)*(map[end]==0)*(i in [end,12-end,6]) + g(i,map,start)) for i in range(13)]


    return f"Winner is Player{2-((u_p[6]<sum(map))+(p_2))%2}"if not sum(map[:6]) else k(map[:7],map[7:]+u_p[6:],p_2,map,g) if end==6 else k(map[7:]+u_p[6:],map[:7],not p_2,map[7:]+u_p[6:]+map[:6],g)


# print(k([6,6,6,6,6,6,0],[6,6,6,6,6,6,0],False, [6,6,6,6,6,6,0,6,6,6,6,6,6],lambda i,map,start: map[i]*(i!=start-1)+map[start-1]//13+((i-start)%13<map[start-1]%13)))

m = [[6,6,6,6,6,6,0,6,6,6,6,6,6,0]]
map_g = lambda i,start: m[0][i]*(i!=start-1)+m[0][start-1]//13+((i-start)%13<m[0][start-1]%13)
map_f =lambda end,start:[max(0,((map_g(end,start)+map_g(12-end,start)))*(-2)**(i!=6)*(12<start+m[0][start-1]<21)*(m[0][end]==0)*(i in [end,12-end,6]) + map_g(i,start)) for i in range(14)]
btns = [Button(window,bg='grey',text=f"{a[i]}",command=lambda i=i:exec("m[0]= map_f(i%7+1+m[0][i%7],i%7+1);[btns[j].config(text=f'{m[0][j]}') for j in range(14)]")) for i in range(14)]

btns_g = [btns[i].grid(row=(i<7),column=(i%7),padx=10,pady=10) for i in range(14)]
window.mainloop()



