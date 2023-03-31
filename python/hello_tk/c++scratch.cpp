#include <iostream>
#include <math.h>

using namespace std;


    int minStoneSum(int piles[], int k) {

        class node {
            public:
                class node *next = NULL;
                class node *prev = NULL;
                int value = 0;
        };

        class linked_list {
            public:
                class node *head = NULL;
                // for(int pile: piles)
            void insert_node(int pile) {
                if(head == NULL) {
                head = new node();
                head->value = pile;
                } else {
                    class node *tmp = head;
                    while(true) {
                        if (tmp->value < pile) {
                            // cout << "*" << "inserting" << pile << "*";
                            class node *new_node = new node();
                            new_node->prev = tmp->prev;
                            new_node->next = tmp;
                            tmp->prev = new_node;
                            if (new_node->prev !=NULL) new_node->prev->next = new_node;
                            else
                                head = new_node;
                            new_node->value = pile;
                            break;
                        } else {
                            if(tmp->next != NULL) tmp = tmp->next;
                            else {
                                class node *new_node = new node();
                                tmp->next = new_node;
                                new_node->prev = tmp;
                                new_node->value = pile;
                                break;
                            }
                        }
                    }
                }
            }
        };

        class linked_list pils;

        for (int i = 0; i < 3 ;i++){
            cout << i << " "<<piles[i]<<endl;
        pils.insert_node(piles[i]);
        class node *tmp1 = pils.head;
        while(true) {
                cout << tmp1->value<<" ";
                if (tmp1->next == NULL)
                    break;
                tmp1 = tmp1->next;
        }
        cout << endl<<"------"<<endl;
        }

        

        for(int i = 0; i < k; i++){
            
            class node *tmp = pils.head;
            while(true) {
                cout << tmp->value<<" ";
                if (tmp->next == NULL)
                    break;
                tmp = tmp->next;
            }
            cout << endl;
            tmp = pils.head;

            int new_value = tmp->value;
            new_value = tmp->value - floor(new_value/2);
            pils.head = tmp->next;
            pils.head->prev = NULL;
            delete tmp;
            pils.insert_node(new_value);

        }
        

         class node *tmp2 = pils.head;
            while(true) {
                cout << tmp2->value<<" ";
                if (tmp2->next == NULL)
                    break;
                tmp2 = tmp2->next;
            }
            cout << endl;

        int sum = 0;
        class node *tmp = pils.head;
        while(true) {
            sum += tmp->value;
            if (tmp->next == NULL) break;
            tmp = tmp->next;
        }

        return sum;


        
    }

    int main() {
        int input[] = {5, 4, 9};
        cout << minStoneSum(input, 2)<<endl;
    }
