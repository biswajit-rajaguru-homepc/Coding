#include <iostream>
#include <math.h>

using namespace std;
int main(){

    class ll_node {
        public:
            class ll_node *next = NULL;
            class ll_node *prev = NULL;
            int value;
    };

    class ll {
        public:
            class ll_node *head = NULL;
            class ll_node *active = NULL;
    };

    struct ll piles;
    int data[] = {34, 65, 345, 32, 56, 334,100,101,10000,1000000,5};
    for (int i = 0; i < sizeof(data) / sizeof(int);i++) {
        

        if (i==0) {
            piles.head = new ll_node();
            piles.head->value = data[i];
            piles.active = piles.head;
        } else  {
            struct ll_node *temp = piles.head;
            while(true) {
                if (temp->value < data[i]) {
                    struct ll_node *new_node = new ll_node();
                    new_node->next = temp;
                    new_node->prev = temp->prev;
                    if (temp->prev != NULL) temp->prev->next = new_node;
                    temp->prev = new_node;
                    new_node->value = data[i];
                    if (temp == piles.head)
                        piles.head = new_node;
                    break;
                }
                else
                {
                    if(temp->next == NULL) {
                        struct ll_node *new_node = new ll_node();
                        new_node->next = NULL;
                        new_node->prev = temp;
                        temp->next = new_node;
                        new_node->value = data[i];
                        break;
                    } else {
                        temp = temp->next;
                    }
                }
            }

        //     piles.active->next = new ll_node();
        //     piles.active->next->prev = piles.active;
        //     piles.active = piles.active->next;
        //     piles.active->value = data[i];
        }
    }

    struct ll_node *present = piles.head;
    while(true){
        cout << present->value << " ";
        if (present->next == NULL)
            break;
        present = present->next;
        
    }
    
    while(piles.head != NULL){
        struct ll_node *temp = piles.head;
        piles.head = piles.head->next;
        delete temp;
    }

    cout << endl;


}