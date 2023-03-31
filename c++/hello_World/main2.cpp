#include <iostream>
#include <array>
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {
    
   /* array<int,4> a = {1,2,3,4};

    int N = a.size();
    for(int i=0;i<N;i++) {
        cout<<a[i]<<endl;
    }

    cout <<a.at(1)<<" "<< a.empty() << " " << a.front() << " " << a.back() << endl;
    */

   /*vector<int> v = {1,2,3};

    //nfor(int i:v) cout << i << " ";
    cout<<endl<<v.capacity()<<" "<<v.size()<<endl;
    v.push_back(4);
    cout<<endl<<v.capacity()<<" "<<v.size()<<endl;
    

    cout<<endl<<"v.clear"<<endl;
    v.clear();
    cout<<endl<<v.capacity()<<" "<<v.size()<<endl;

    //for(int i:v) cout << i << " ";
    //cout << endl;*/

    vector<int> a(5,2);
    vector<int> b(a);
    for(int i:b) cout<<i<<endl;
    return 0;
}