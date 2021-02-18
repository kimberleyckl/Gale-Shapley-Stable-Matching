## UPI: clin834
## ID: 955333969
## Name: Chien-Li LIN
## Find the stable maximum matching using Gale-Shapley algorithm.
## input a instance(n), for next 2n lines will be the ranking list, first n lines is blue nodes and second
## n lines are pink nodes. Blue purpose to pink nodes.
    


def main():
    c = 0
    x = input()
    while x != "0":
        instance = int(x)
        c = c+1
        blue,w =getblue(instance)
        pink=getpink(instance)
        match = GS(blue, pink, w)
        match.sort()
        out(c, match)
        
        x= input()


################################################### Gale-Shapley Algorithm ###################################################
def GS(blue, pink, w):
    p = []                                      # pink nodes that matched already
    m = []
    while len(w) != 0:
        x = w.pop(0)                    # take the first blue node on waiting list
        rank = blue[x]                  # get it's rank
        i = 0
        p,m,w = GS1(i, rank, p, m, pink, w, x)
    return m
               
################################################### Gale-Shapley Algorithm ###################################################
def GS1(i, rank, p, m, pink, w, x):
    if rank[i] not in p :
        p+= [rank[i]]
        m+= [[x,rank[i]]]
        return (p,m,w)
    else:
        preflist = pink[rank[i]]
        new_index = preflist.index(x)
        a , im = find_old_index(m , rank[i])
        old_index = preflist.index(a)
        if new_index <old_index:             #do prefer new blue node
            m.pop(im)
            m += [[x,rank[i]]]
            w += [a]
            return (p,m,w)
        else:
            i = i+1
            p,m,w = GS1(i, rank, p, m, pink, w, x)
            return (p,m,w)

################################################### print output ###################################################
def find_old_index(m,num):
    for i in range (0,len(m)):
        if m[i][1] == num:
            return (m[i][0] , i)                                       
        
################################################### print output ###################################################
def out(c,m):
    print ("Instance " +str(c) +":")
    for i in m:
        print ("Blue node" , i[0], "matched with pink node", i[1])

################################################### get blue nodes' rank and waiting list ###################################################
def getblue(instance):
    blue ={}
    wi = []
    for i in range (1,instance+1):
        x = input().split()
        wi += [i]
        blue[i] = [ int(i) for i in x]
    return (blue, wi)

################################################### get pink nodes' rank ###################################################
def getpink(instance):
    blue ={}
    for i in range (1,instance+1):
        x = input().split()
        blue[i] = [ int(i) for i in x]
    return (blue)
    
main()
