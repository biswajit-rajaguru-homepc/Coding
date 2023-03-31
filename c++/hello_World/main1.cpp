#include <iostream>
using namespace std;

#include "utils.h"

class Person {
    private:
        string name;
        string location;
        short age;
        float height;

    public :
    
    Person(string n, string l, short a, float h){
        name = n;
        location = l;
        age = a;
        height = h;

    }

   void get_info(void){
        cout<<endl<<name<<" "<<location<<" "<<age<<" "<<height<<endl;
    }

    
};

class IITian : public Person {
    public:
        IITian(string n, string l, float a, float h) : Person(n, l, a, h){

        }
};

string space = " ";

int main(int argc, char *argv[]) {
    
    IITian Munu("Biswajit Rajaguru", "Rourkela", 40, 5.3);
    //string a = Munu.get_name();
    // cout<<Munu.name<<space<<Munu.location<<space<<Munu.height<<space<<Munu.age<<endl;
    Munu.get_info();
    return 0;
}

