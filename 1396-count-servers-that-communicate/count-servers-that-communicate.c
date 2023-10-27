int find_set(int x,int parent[]){
    if(parent[x]!=x){
        parent[x]=find_set(parent[x],parent);
    }
    return parent[x];
}
void union_set(int x, int y,int parent[],int rank[]){
    int p1=find_set(x,parent);
    int p2=find_set(y,parent);
    if(p1==p2){
        rank[p2]++;
        return;
    }
    if(rank[p1]<rank[p2]){
        parent[p1]=p2;
        rank[p2]+=rank[p1];
    }
    else{
        parent[p2]=p1;
        rank[p1]+=rank[p2];
    }
}
int countServers(int** grid, int gridSize, int* gridColSize){
    int m=gridSize;
    int n=*gridColSize;
    int parent[m*n];
    int rank[m*n];
    for(int i=0;i<m*n;i++){
        parent[i]=i;
        rank[i]=1;
    }
    //int ans=0;
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            if(grid[i][j]==1){
                union_set(i,j+m,parent,rank);
            }
        }
    }
    int ans=0;
    for(int i=0;i<m*n;i++){
        if((parent[i]==i) && rank[i]>2){
            ans+=rank[i]-1;
        }
    }
    return ans;
}