def  countPairs(k, a):
    dict={}
    res=0
    for i in range(len(a)):
        if a[i] in dict:
            res+=dict[a[i]]
        if k-a[i] in dict:
            dict[k-a[i]]+=1
        else: dict[k-a[i]]=1
    return res

int secondSmallest(vector < int > x) {
    int i,first,second;

    if (x.size()< 2)
        return 0;

    first = second = INT_MAX;
    for (i=0;i<x.size();i++){

        if (x[i]<first){
            second=first;
            first=x[i];
        }
        else if (x[i]<second )
            second =x[i];
    }
    return second;

}

int countPairs(int k, vector < int > a) {
    unordered_map<int,int> dict;
    int res=0;
    for (int i =0;i<a.size();i++)
        {
        if (dict.find(a[i])!=dict.end())
            res+=dict[a[i]];
        if (dict.find(k-a[i])!=dict.end())
            dict[k-a[i]]+=1;
        else
            dict[k-a[i]]=1;

    }
    return res;


}

