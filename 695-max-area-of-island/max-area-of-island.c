int find_set(int x,int parent[]){
    if(parent[x]!=x){
        parent[x]=find_set(parent[x],parent);
    }
    return parent[x];
}
void union_set(int x, int y,int par[],int rank[]){
    int p1=find_set(x,par);
    int p2=find_set(y,par);
    if(p1==p2){
        return;
    }
    if(rank[p1]<rank[p2]){
        par[p1]=p2;
        rank[p2]+=rank[p1];
    }
    else{
        par[p2]=p1;
        rank[p1]+=rank[p2];
    }
}
int maxAreaOfIsland(int** grid, int gridSize, int* gridColSize){
    int m=gridSize;
    int n=*gridColSize;
    int parent[m*n];
    int rank[m*n];
    for(int i=0;i<m*n;i++){
        parent[i]=i;
        rank[i]=1;
    }
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            if(grid[i][j]==1){
                int x1=i*n+j;
                if((i+1<=m-1) && grid[i+1][j]==1){
                    int x2=x1+n;
                    union_set(x1,x2,parent,rank);
                }
                if((j+1<=n-1) && grid[i][j+1]==1){
                    int x2=x1+1;
                    union_set(x1,x2,parent,rank);
                }
            }
            else{
                rank[i*n+j]=0;
            }
        }
    }
    int ans=0;
    for(int i=0;i<m*n;i++){
        if(find_set(i,parent)==i){
            if(rank[i]>=ans){
                ans=rank[i];
            }
        }
    }
    //printf(rank);
    return ans;
}