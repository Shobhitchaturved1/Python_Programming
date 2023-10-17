char * longestCommonPrefix(char ** strs, int strsSize){
    if (strsSize == 1) return strs[0];
    int i = 0;
    for(i = 0; strs[0][i] != '\0'; i++){
        char c = strs[0][i];
        for(int j = 0; j < strsSize; j++){
            if(strs[j][i] != c){
                strs[j][i] = '\0';
                return strs[j];
            }   
        }
    }
    strs[0][i] = '\0';
    return strs[0];
}