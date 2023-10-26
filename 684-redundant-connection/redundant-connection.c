/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int find_set(int x,int parent[]){
     if(parent[x]!=x){
         parent[x]=find_set(parent[x],parent);
     }
     return parent[x];
 }
void union_set(int x, int y, int parent[],int rank[]){
    int p1=find_set(x,parent);
    int p2=find_set(y,parent);
    if(rank[p1]<rank[p2]){
        parent[p1]=p2;
    }
    else if(rank[p2]<rank[p1]){
        parent[p2]=p1;
    }
    else{
        parent[p1]=p2;
        rank[p2]++;
    }
}
int* findRedundantConnection(int** edges, int edgesSize, int* edgesColSize, int* returnSize){
    int m=edgesSize;
    int n=*edgesColSize;
    int parent[m*n];
    int rank[m*n];
    for(int i=0;i<m*n;i++){
        parent[i]=i;
        rank[i]=0;
    }
    int *ans=(int*)malloc(2*sizeof(int));
    for(int i=0;i<edgesSize;i++){
        if(find_set(edges[i][0],parent)==find_set(edges[i][1],parent)){
            ans[0]=edges[i][0];
            ans[1]=edges[i][1];
            break;
        }
        union_set(edges[i][0],edges[i][1],parent,rank);
    }
    *returnSize=2;
    return ans;
}