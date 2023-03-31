#include <iostream>
using namespace std;

int print_menu(string name){
    int choice;
    
    cout << "\n---------------------------------------------------\n1. Add to list.\n2. Print list.\n3. Quit\n";
    cout << "Dear " << name << ": Enter choice:";
    cin >> choice;

    if( choice == 3) exit(0);

    cout<<"\n Choice not Implemnted\n";

    return choice; 

}