import sys
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        if v not in self.graph[u]:
            self.graph[u].append(v)
        if u not in self.graph[v]:
            self.graph[v].append(u)

    def mark_visited(self,vertices):
        visited={};
        for node in vertices:
            visited[node]=False;
        return visited;
    
    def BFS(self, s, vertices,Destination):
        output="BFS: ";
        visited={};
        queue = []
        visited=self.mark_visited(vertices);
        queue.append(s)
        visited[s] = True;
        while queue:
            s = queue.pop(0)
            output+=str(s)+", ";
            if(s==Destination):
                break;
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        return output;

                    
    def DFS(self,s,vertices,Destination):
        output="DFS: ";
        visited={};
        stack=[];
        visited=self.mark_visited(vertices);
        stack.append(s);
        visited[s]=True;
        while stack:
            element=stack.pop();
            output+=str(element)+", ";
            if(element==Destination):
                break;
            for i in self.graph[element]:
                if visited[i]==False:
                    stack.append(i)
                    visited[i]=True;
        return output;

    
    def DLS(self,s,vertices,Destination,depth):
        self.visited={};
        self.output="DLS: ";
        self.visited=self.mark_visited(vertices);
        ans = self.DLSHepler(s,depth,Destination);
        if(ans==False):
            print("Destination not found for given depth");
        return self.output;

    def DLSHepler(self,sourceNode,depth,Destination):
        if(self.visited[sourceNode]):
            return False;
        self.output+=str(sourceNode)+", ";
        self.visited[sourceNode]=True;
        if(sourceNode==Destination):
            return True;
        if(depth==0):
            return False;
        for i in self.graph[sourceNode]:
            if self.visited[i]==False:
                ansnext = self.DLSHepler(i,depth-1,Destination);
                if(ansnext==True):
                    return True;
        return False
    

    def BDS(self,s,vertices,Destination):
        queue1=[];
        queue2=[];
        visited1=self.mark_visited(vertices);
        visited2=self.mark_visited(vertices);
        output1=[];
        output2=[];
        queue1.append(s);
        queue2.append(Destination);
        visited1[s]=True;
        visited2[Destination]=True;
        search2=False;
        search1=False;
        element2s=-1;
        while(queue1 and queue2):
            element1=queue1.pop(0);
            output1.append(element1);
            element2=queue2.pop(0);
            output2.append(element2);
            if(visited1[element2]==True):
                search1=True;
                element2s=element2;
                break;
            if(visited2[element1]==True):
                search2=True;
                element2s=element2;
                break;
            for child in self.graph[element1]:
                if(visited1[child]==False):
                    visited1[child]=True;
                    queue1.append(child);
            for child in self.graph[element2]:
                if(visited2[child]==False):
                    visited2[child]=True;
                    queue2.append(child);
        output="BDS: ";
        elementfound=False;
        if(search1):
            for element in output1:
                output+=str(element)+", " ;
                if(element==element2s):
                    elementfound=True;
                    break;
            if(elementfound==False):
                for element in queue1:
                    output+=str(element)+", " ;
                    if(element==element2s):
                        break;
            len2=len(output2);
            for i in range(2,len2+1):
                idx=len2-i;
                element=output2[idx];
                output+=str(element)+", ";
        elif(search2):
            for element in output2:
                output+=str(element)+", " ;
                if(element==element2s):
                    elementfound=True;
                    break;
            if(elementfound==False):
                for element in queue2:
                    output+=str(element)+", " ;
                    if(element==element2s):
                        break;
            len1=len(output1);
            for i in range(2,len1+1):
                idx=len1-i;
                element=output1[idx];
                output+=str(element)+", ";
        else:
            output="Destination not found";

        return output;

                
file_in = open(sys.argv[1],'r');
file_out=open(sys.argv[2],'w');

lines=file_in.readlines();
line1=lines[0];
vertices=[];
t=[];
rows=len(lines);
source=lines[1][0];
Destination=lines[rows-2][0];
g=Graph();
for i in range(len(lines[0])-1):
    if(i%2==0):
        vertices.append(lines[0][i]);
for i in range(2,rows-2):
    src=lines[i][0];
    des=lines[i][2];
    g.addEdge(src,des);
for ch in line1:
    if(ch!=',' and ch!='\n'):
        vertices.append(ch);
output="";
output+=g.BFS(source,vertices,Destination)
output+="\n";
output+=g.DFS(source,vertices,Destination)
output+="\n";
output+=g.DLS(source,vertices,Destination,4);
output+="\n";
output+=g.BDS(source,vertices,Destination);
file_out.write(output);
