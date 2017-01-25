//Given n integers, count the number of pairs of integers whose difference is k.
#include <iostream>
#include <unordered_set>
using namespace std;

unordered_set<int> s; //for creating hash table; fast inquiry

int main()
{
	//n = no. of elements, k = difference required
    int n, k, val;
    cin>>n>>k;
    for (int i = 0; i < n; i++)
    {
        cin>>val;
        s.insert(val);
    }
    int ans = 0;    
    //to check whether current n+k or n-k is present in hash table
    for(unordered_set<int>::iterator it = s.begin(); it != s.end(); ++it)
        if (s.find(*it + k) != s.end()) 
        	ans++;
    cout<<ans<<endl;
    return 0;
}