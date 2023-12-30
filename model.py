from collections import deque
parent=[[0]*12 for i in range(12)]


def GetNeighbours(x,y):
    neighbours=[]
    if x-1>=0: # top
        neighbours.append((x-1,y))
    
    if x+1<10: # bottom
        neighbours.append((x+1,y))
    
    if y+1<10: # right
        neighbours.append((x,y+1))
    
    if y-1>=0: # left
        neighbours.append((x,y-1))
    
    return neighbours

def GetHuristic(x,y,Goals):
    Min=10**10
    for i,j in Goals:
        N=abs(i-x)+abs(j-y)
        if Min>N:
            Min=N
    return Min


def Path(x,y,parent):
    path=[(x,y)]
    while parent[x][y]:
        x,y=parent[x][y]
        path.append((x,y))
    return path[::-1]

def GetStat(Id):
    Stat=[]
    F=open(f'stat/{Id}.txt')
    for i in range(10):
        B=F.readline().split(' ')
        B[9]=B[9][0]
        Stat.append(B)
    F.close()
    return Stat

def GetBoard(Id):

    monster=[]
    Board= [[0]*10 for i in range(10)]
    StartPoint=[0,0]
    Goals=[]
    stat=GetStat(Id)
    for i in range(10):
        for j in range(10):
            match stat[i][j]:
                case '#':
                    Board[i][j]=-1

                case 'P':
                    Board[i][j]=1000
                    StartPoint[0],StartPoint[1]=i,j

                case 'E':
                    Board[i][j]=1000
                    Goals.append((i,j))

                case 'M':
                    Board[i][j]=0
                    monster.append((i,j))

                case _:
                    Board[i][j]=1000
                
                
                

    
    while len(monster):
        x,y=monster.pop(0)
        neighbours=GetNeighbours(x,y)
        for i,j in neighbours:
            if Board[x][y]+1<Board[i][j]:
                Board[i][j]=Board[x][y]+1
                monster.append((i,j))
    return[Board,StartPoint,Goals]
def solve(Id,algorithm=1):
    Board,StartPoint,Goals=GetBoard(Id)
    if algorithm ==1:
        return BFS(StartPoint[0],StartPoint[1],Board,Goals)
    elif algorithm ==2:
        return DFS(StartPoint[0],StartPoint[1],Board,Goals)
    elif algorithm ==3:
        return UCS(StartPoint[0],StartPoint[1],Board,Goals)
    elif algorithm==4:
        return A_Star(StartPoint[0],StartPoint[1],Board,Goals)
    else:
        return greed(StartPoint[0],StartPoint[1],Board,Goals)

def UCS(x,y,Board,Goals):
    
    Board[x][y]=0
    fronter=[(0,x,y)]
    while len(fronter):
        fronter.sort()
        cost,x,y=fronter.pop(0)
        if (x,y) in Goals:
            return Path(x,y,parent)
        neighbours=GetNeighbours(x,y)
        for i,j in neighbours:
            if Board[i][j]>cost+1:
                Board[i][j]=cost+1
                fronter.append((cost+1,i,j))
                parent[i][j]=(x,y)
    return [(-1,-1)]

