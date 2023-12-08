#include <bits/stdc++.h>
using namespace std;
struct  Node{
    int value;
    struct Node* link;
};
int main()
{
    Node *p=NULL,*h=NULL ;
    int menu;
        while(true){
            cout<<"(Number 1: Add)"<<endl<<"(Number 2: Delete)"<<endl<<"(Number 3: Edit)"<<endl<<"(Number 4: Search)"<<endl;
            cout<<"(Number 5: Show)"<<endl<<"(Number 6: Exit)"<<endl;
            cout<<"Enter menu",cin>>menu;
            if(menu==1){//add
                p=(Node *)malloc(sizeof(Node));//find address
                cout<<"enter value",cin>>p->value;
                p->link=h,h=p;
            }
            else if(menu==2){//**delete
                int d;
                cout<<"Delete for :";
                cin>>d;
                p=h;
                while(p!=NULL&&p->value!=d)p=p->link;
                if(p==NULL)cout<<"No Data"<<endl;
                else{
                    if(p==h)h=h->link;
                    else{
                        Node *pp;
                        pp=h;
                        while(pp->link!=p)pp=pp->link;
                        pp->link=p->link;
                    }
                    free(p);
                    cout<<"Delete complete"<<endl;
                }
            }
            else if(menu==3){//**edit
                p=h;
                int edit;
                cout<<"Edit to";
                cin>>edit;
                while(p!=NULL&&p->value!=edit){
                    p=p->link;
                }
                if(p==NULL)cout<<"No Data"<<endl;
                else{
                    cout<<"Change to";
                    cin>>p->value;
                    cout<<"Edit Complete"<<endl;
                }
            }
            else if(menu==4){//***search
                p=h;
                int want;
                cout<<"Search value :";
                cin>>want;
                while(p!=NULL&&p->value!=want){
                    p=p->link;
                }
                if(p==NULL)cout<<"NO"<<endl;
                else cout<<"YES"<<endl;
            }
            else if(menu==5){//***show
                p=h;
                while(p!=NULL){
                    cout<<p->value<<endl;
                    p=p->link;
                }
            }
            else if(menu==6){
                return 0;
            }
        }
    return 0;
}
