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
        return;
    }
    if(rank[p1]<rank[p2]){
        parent[p1]=p2;
    }
    else if(rank[p2]<rank[p1]){
        parent[p2]=p1;
    }
    else{
        parent[p1]=p2;
        rank[p2]+=1;
    }
}
bool validPath(int n, int** edges, int edgesSize, int* edgesColSize, int source, int destination){
    int parent[n+1];
    int rank[n+1];
    for(int i=0;i<n+1;i++){
        parent[i]=i;
        rank[i]=0;
    }
    for(int i=0;i<edgesSize;i++){
        union_set(edges[i][0],edges[i][1],parent,rank);
    }
    return (find_set(source,parent)==find_set(destination,parent));
}