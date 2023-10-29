int find_set(int x,int parent[]){
    if(parent[x]!=x){
        parent[x]=find_set(parent[x],parent);
    }
    return parent[x];
}
void union_set(int x,int y, int parent[],int rank[],int fishes[]){
    int p1=find_set(x,parent);
    int p2=find_set(y,parent);
    if(p1==p2){
        return;
    }
    parent[p2]=p1;
    fishes[p1]+=fishes[p2];
}
int findMaxFish(int** grid, int gridSize, int* gridColSize){
    int m=gridSize;
    int n=*gridColSize;
    int parent[m*n];
    int rank[m*n];
    int fishes[m*n];
    for(int i=0;i<m*n;i++){
        parent[i]=i;
        rank[i]=0;
    } 
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            fishes[i*n+j]=grid[i][j];
            if(grid[i][j]!=0){
                int x1=i*n+j;
                if(i+1<=m-1 && grid[i+1][j]!=0){
                    int x2=x1+n;
                    fishes[x2]=grid[i+1][j];
                    union_set(x1,x2,parent,rank,fishes);
                }
                if(j+1<=n-1 && grid[i][j+1]!=0){
                    int x2=x1+1;
                    fishes[x2]=grid[i][j+1];
                    union_set(x1,x2,parent,rank,fishes);
                }
            }
        }
    }
    int ans=0;
    for(int i=0;i<m*n;i++){
        if(fishes[i]>ans){
            ans=fishes[i];
        }
    }
    return ans;
}