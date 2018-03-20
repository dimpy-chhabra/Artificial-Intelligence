import sys

class RowCol:
    def __init__(self,row,col):
        self.row=row;
        self.col=col;

    def printRowCol(self):
        print(self.row," ",self.col);

    def checkEqual(self,rc):
        if(self.row==rc.row and self.col==rc.col):
            return True;
        return False;

    def toString(self):
        return str(self.row)+" "+str(self.col);
    
class Graph:
    def __init__(self,beginRow,beginCol,endRow,endCol,sRow,sCol):
        self.beginRow=beginRow;
        self.beginCol=beginCol;
        self.endRow=endRow;
        self.endCol=endCol;
        self.matrix=[];
        self.dest=RowCol(endRow,endCol);
        for r in range(0,sRow):
            row=[];
            for col in range(0,sCol):
                row.append(0);
            self.matrix.append(row);
            
    def matrixupdate(self):
        for r in range(0,sRow):
            for col in range(0,sCol):
                if(self.matrix[r][col]!=-1):
                    self.matrix[r][col]=0;
                    
    def addObstacle(self,row,col):
        self.matrix[row][col]=-1;
        
    def leftMove(self, rc):
        if(rc.col-1>=0):
            return RowCol(rc.row,rc.col-1);
        return RowCol(-1,-1);
    
    def rightMove(self, rc):
        if(rc.col+1<=self.endCol):
            return RowCol(rc.row,rc.col+1);
        return RowCol(-1,-1);
    
    def upMove(self, rc):
        if(rc.row-1>=0):
            return RowCol(rc.row-1,rc.col);
        return RowCol(-1,-1);
    
    def downMove(self, rc):
        if(rc.row+1<=self.endRow):
            return RowCol(rc.row+1,rc.col);
        return RowCol(-1,-1);
    
    def BFS(self):
        queue=[];
        output="";
        src=RowCol(self.beginRow,self.beginCol);
        self.matrix[self.beginRow][self.beginCol]=1;#1->visited -1->unreachable 0->unvisited
        queue.append(src);
        queueops=["N"];
        while queue:
            output+="\n"+queueops.pop(0);
            src=queue.pop(0);
            output+=src.toString();
            if(src.checkEqual(self.dest)):
                break;
            left=self.leftMove(src);
            if(left.col!=-1 and self.matrix[left.row][left.col]==0):
                queue.append(left);
                queueops.append("L");
                self.matrix[left.row][left.col]=1;
            right=self.rightMove(src);
            if(right.col!=-1 and self.matrix[right.row][right.col]==0):
                queue.append(right);
                queueops.append("R");
                self.matrix[right.row][right.col]=1;
            up=self.upMove(src);
            if(up.col!=-1 and self.matrix[up.row][up.col]==0):
                queue.append(up);
                queueops.append("U");
                self.matrix[up.row][up.col]=1;
            down=self.downMove(src);
            if(down.col!=-1 and self.matrix[down.row][down.col]==0):
                queue.append(down);
                queueops.append("D");
                self.matrix[down.row][down.col]=1;
        self.matrixupdate();
        return output;
    
    def DFS(self):
        queue=[];
        output="";
        src=RowCol(self.beginRow,self.beginCol);
        self.matrix[self.beginRow][self.beginCol]=1;#1->visited -1->obstacle 0->unvisited
        queue.append(src);
        queueops=["N"];
        while queue:
            output+="\n"+queueops.pop(0);
            src=queue.pop(0);
            output+=src.toString();
            if(src.checkEqual(self.dest)):
                break;
            left=self.leftMove(src);
            if(left.col!=-1 and self.matrix[left.row][left.col]==0):
                queue.insert(0,left);
                queueops.insert(0,"L");
                self.matrix[left.row][left.col]=1;
            right=self.rightMove(src);
            if(right.col!=-1 and self.matrix[right.row][right.col]==0):
                queue.insert(0,right);
                queueops.insert(0,"R");
                self.matrix[right.row][right.col]=1;

            up=self.upMove(src);
            if(up.col!=-1 and self.matrix[up.row][up.col]==0):
                queue.insert(0,up);
                queueops.insert(0,"U");
                self.matrix[up.row][up.col]=1;

            down=self.downMove(src);
            if(down.col!=-1 and self.matrix[down.row][down.col]==0):
                queue.insert(0,down);
                queueops.insert(0,"D");
                self.matrix[down.row][down.col]=1;
        self.matrixupdate();
        return output;
    
    def DLS(self,depth):
        self.output="DLS: N,";
        src=RowCol(self.beginRow,self.beginCol);
        self.output+=src.toString();
        self.matrix[self.beginRow][self.beginCol]=1;#1->visited -1->obstacle 0->unvisited
        ans = self.DLSHelper(src,depth);
        if(ans==False):
            self.output+="Destination not found for given depth";
        return self.output;

    def DLSHelper(self,src,depth):
        self.matrix[src.row][src.col]=1;
        if(src.checkEqual(self.dest)):
            return True;
        elif(depth==0):
            return False;

        left=self.leftMove(src);
        if(left.col!=-1 and self.matrix[left.row][left.col]==0):
            self.output+="\nL" + left.toString();
            ans=self.DLSHelper(left,depth-1);
            if(ans):
                return True;
        right=self.rightMove(src);
        if(right.col!=-1 and self.matrix[right.row][right.col]==0):
            self.output+="\nR" + right.toString();
            ans=self.DLSHelper(right,depth-1);
            if(ans):
                return True;
            
        up=self.upMove(src);
        if(up.col!=-1 and self.matrix[up.row][up.col]==0):
            self.output+="\nU" + up.toString();
            ans=self.DLSHelper(up,depth-1);
            if(ans):
                return True;
        down=self.downMove(src);
        if(down.col!=-1 and self.matrix[down.row][down.col]==0):
            self.output+="\nD" + down.toString();
            ans=self.DLSHelper(down,depth-1);
            if(ans):
                return True;
        return False;
    
file_in = open(sys.argv[1],'r');
file_out = open(sys.argv[2],'w');
lines=file_in.readlines();
sRow=int(lines[0][0]);
sCol=int(lines[0][2]);
beginRow=int(lines[1][0])-1;
beginCol=int(lines[1][2])-1;
endRow=int(lines[1][4])-1;
endCol=int(lines[1][6])-1;
algo=lines[3][0:3];
g=Graph(beginRow,beginCol,endRow,endCol,sRow,sCol);
osize=len(lines[2]);
osize/=4;
osize = int(osize)
for x in range(0,osize):
    row=int(lines[2][x*4])-1;
    col=int(lines[2][x*4+2])-1;
    g.addObstacle(row,col);

output="";
if(algo=="bfs"):
    output+=g.BFS()+"\n";
elif(algo=="dfs"):
    output+=g.DFS()+"\n";
elif(algo=="dls"):
    output+=g.DLS(12);
    
file_out.write(output);
file_out.close();
file_in.close();
