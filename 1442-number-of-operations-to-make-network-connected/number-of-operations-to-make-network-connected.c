int find_set(int x,int parent[]){
    if(parent[x]!=x){
        parent[x]=find_set(parent[x],parent);
    }
    return parent[x];
}
void union_set(int x,int y, int parent[],int rank[]){
    int p1=find_set(x,parent);
    int p2=find_set(y,parent);
    if(p1==p2){
        return;
    }
    if(rank[p1]<rank[p2]){
        parent[p1]=p2;
    }
    else if(rank[p2]<rank[p1]){
        parent[p2]=p1;
    }
    else{
        parent[p2]=p1;
        rank[p1]++;
    }
}
int makeConnected(int n, int** connections, int connectionsSize, int* connectionsColSize){
    if(n-1>connectionsSize){
        return -1;
    }
    int parent[n];
    int rank[n];
    for(int i=0;i<n;i++){
        parent[i]=i;
        rank[i]=0;
    }
    for(int i=0;i<connectionsSize;i++){
        union_set(connections[i][0],connections[i][1],parent,rank);
    }
    int ans=0;
    for(int i=0;i<n;i++){
        if(find_set(i,parent)==i){
            ans++;
        }
    }
    return ans-1;
}