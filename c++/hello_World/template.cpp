#include "utils.h"

template<typename T>

void Swap(T& a, T& b){
    T temp;
    temp = a;
    a = b;
    b = temp;
}

namespace my
{
    void greeting(void){
        cout<<"hello world"<<endl;
    }
} // namespace my1

namespace yours
{
    void greeting(void){
        cout<<"Namaskara"<<endl;
    }    
} // namespace yours



int main(int argc, char *argv[]) {
    
    string a = "hello", b = "world";
    cout << a << " - " << b << endl;
    Swap(a,b);
    cout << a << " - " << b << endl;
    
    my::greeting();
    yours::greeting();

    return 0;
}