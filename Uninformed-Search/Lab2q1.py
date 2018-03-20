import sys
from collections import defaultdict
in1 = sys.argv[1]
out1 = sys.argv[2]

f_in = open(in1,'r')
f_out = open(out1,'w')

class Node:
    def __init__(self,vp,c1,c2,c3,c4):
        self.vpos=vp;
        self.rooms=[vp,c1,c2,c3,c4];

    def compare(self,temp):
        a = self.rooms
        b = temp.rooms
        ans = (a > b) - (a < b) ==0;
        return ans;

    def printNode(self):
        print(self.rooms);

    def checkDestination(self):
        r1 = self.rooms[1]==0;
        r2 = self.rooms[2]==0;
        r3 = self.rooms[3]==0;
        r4 = self.rooms[4]==0;
        return r1 and r2 and r3 and r4;

class Graph:
    def __init__(self,src):
        self.config=[]
        cnt=0;
        for pos in range(1,5):
            for r1 in range(0,2):
                for r2 in range(0,2):
                    for r3 in range(0,2):
                        for r4 in range(0,2):
                            self.config.append(Node(pos,r1,r2,r3,r4));
                            cnt+=1;
        
        self.src=src;
        self.count=cnt;



    def rightMove(self,source):
        if((source.vpos==1) or (source.vpos==3)):
            dest=Node(int(source.vpos)+1,int(source.rooms[1]),int(source.rooms[2]),int(source.rooms[3]),int(source.rooms[4]));
            for idx in range(0,self.count):
                if(dest.compare(self.config[idx])==True):
                    return idx;
        return -1;

    def leftMove(self,source):
        if((source.vpos==2) or (source.vpos==4)):
            dest=Node(int(source.vpos)-1,int(source.rooms[1]),int(source.rooms[2]),int(source.rooms[3]),int(source.rooms[4]));
            for idx in range(0,self.count):
                if(dest.compare(self.config[idx])==True):
                    return idx;
        return -1;

    def upMove(self,source):
        if((source.vpos==3) or (source.vpos==4)):
            dest=Node(int(source.vpos)-2,source.rooms[1],int(source.rooms[2]),int(source.rooms[3]),int(source.rooms[4]));
            for idx in range(0,self.count):
                if(dest.compare(self.config[idx])==True):
                    return idx;
        return -1;

    def downMove(self,source):
        if((source.vpos==1) or (source.vpos==2)):
            dest=Node(int(source.vpos)+2,int(source.rooms[1]),int(source.rooms[2]),int(source.rooms[3]),int(source.rooms[4]));
            for idx in range(0,self.count):
                if(dest.compare(self.config[idx])==True):
                    return idx;
                    break;
        return -1;

    def suckOper(self,source):
        pos=int(source.vpos);
        if(source.rooms[pos]==0):
            return -1;
        dest=Node(source.vpos,int(source.rooms[1]),int(source.rooms[2]),int(source.rooms[3]),int(source.rooms[4]));
        dest.rooms[pos]=0;
        for idx in range(0,self.count):
            if(dest.compare(self.config[idx])==True):
                return idx;
                
       

    def search(self,node):
        for idx in range(0,self.count):
            if(node.compare(self.config[idx])==True):
                return idx;

    def mark_visited(self):
        visited={};
        for node in range(0,64):
            visited[node]=False;
        return visited;
    
    
    def BFS(self):
        idxs = self.search(self.src);
        visited=self.mark_visited();
        queue=[];
        queue.append(idxs);
        visited[idxs] = True
        qops=['N'];
        output="";
        
        while queue:
            s = queue.pop(0);
            output+=str(self.config[s].vpos)+", " + qops.pop(0)+"\n";
            if(self.config[s].checkDestination()):
                break;
            suck = self.suckOper(self.config[s]);
            if(suck>=0 and suck<64 and visited[suck]==False):
                visited[suck]=True;
                queue.append(suck);
                qops.append('S');
            left = self.leftMove(self.config[s]);
            if(left != -1 and visited[left]==False):
                visited[left]=True;
                queue.append(left);
                qops.append('L');
            right = self.rightMove(self.config[s]);
            if(right != -1 and visited[right]==False):
                visited[right]=True;
                queue.append(right);
                qops.append('R');
            up = self.upMove(self.config[s]);
            if(up != -1 and visited[up]==False):
                visited[up]=True;
                queue.append(up);
                qops.append('U');
            down = self.downMove(self.config[s]);
            if(down != -1 and visited[down]==False):
                visited[down]=True;
                queue.append(down);
                qops.append('D');
        return output;

    
    def DFS(self):
        idxs = self.search(self.src);
        visited=self.mark_visited();
        queue=[];
        queue.append(idxs);
        visited[idxs] = True
        qops=['N'];
        output="";
        
        while queue:
            s = queue.pop(0);
            output+=str(self.config[s].vpos)+", " + qops.pop(0)+"\n";
            if(self.config[s].checkDestination()):
                break;
            suck = self.suckOper(self.config[s]);
            if(suck>=0 and suck<64 and visited[suck]==False):
                visited[suck]=True;
                queue.insert(0,suck);
                qops.insert(0,'S');
            left = self.leftMove(self.config[s]);
            if(left != -1 and visited[left]==False):
                visited[left]=True;
                queue.insert(0,left);
                qops.insert(0,'L');
            right = self.rightMove(self.config[s]);
            if(right != -1 and visited[right]==False):
                visited[right]=True;
                queue.insert(0,right);
                qops.insert(0,'R');
            up = self.upMove(self.config[s]);
            if(up != -1 and visited[up]==False):
                visited[up]=True;
                queue.insert(0,up);
                qops.insert(0,'U');
            down = self.downMove(self.config[s]);
            if(down != -1 and visited[down]==False):
                visited[down]=True;
                queue.insert(0,down);
                qops.insert(0,'D');
        return output;

    
    #depth=3 by default
    def DLS(self,depth):
        self.visited={};
        self.output="DLS: ";
        s=self.search(self.src);
        self.visited=self.mark_visited();
        self.output+=str(self.src.vpos)+", N\n";
        ans = self.DLSHelper(s,depth);
        if(ans==False):
            self.output+="\nDestination not found for given depth";
        return self.output;

    def DLSHelper(self,sourceNode,depth):
        self.visited[sourceNode]=True;
        if(self.config[sourceNode].checkDestination()):
            return True;
        if(depth==0):
            return False;

        suck = self.suckOper(self.config[sourceNode]);
        if(suck>=0 and suck<64 and self.visited[suck]==False):
            self.output+=str(self.config[sourceNode].vpos)+", S\n";
            ans=self.DLSHelper(suck,depth-1);
            if(ans):
                return True;

        left = self.leftMove(self.config[sourceNode]);
        if(left != -1 and self.visited[left]==False):
            self.output+=str(self.config[left].vpos)+", L\n";
            ans=self.DLSHelper(left,depth-1);
            if(ans):
                return True;

        right = self.rightMove(self.config[sourceNode]);
        if(right != -1 and self.visited[right]==False):
            self.output+=str(self.config[right].vpos)+", R\n";
            ans=self.DLSHelper(right,depth-1);
            if(ans):
                return True;

        up = self.upMove(self.config[sourceNode]);
        if(up != -1 and self.visited[up]==False):
            self.output+=str(self.config[up].vpos)+", U\n";
            ans=self.DLSHelper(up,depth-1);
            if(ans):
                return True;
            
        down = self.downMove(self.config[sourceNode]);
        if(down != -1 and self.visited[down]==False):
            self.output+=str(self.config[down].vpos)+", D\n";
            ans=self.DLSHelper(down,depth-1);
            if(ans):
                return True;
        return False

 
        
lines=f_in.readlines();
pos=int(lines[0][0]);
room1=int(lines[1][0]);
room2=int(lines[1][2]);
room3=int(lines[1][4]);
room4=int(lines[1][6]);
algo=lines[2][:3];
output="";
source = Node(pos,room1,room2,room3,room4);
g = Graph(source);
if(algo=="bfs"):
    output+=g.BFS()+"\n";
elif(algo=="dfs"):
    output+=g.DFS()+"\n";
elif(algo=="dls"):
    output+=g.DLS(4);
print(output);
f_out.write(output) #overwrites file every time

f_out.close()
f_in.close()
