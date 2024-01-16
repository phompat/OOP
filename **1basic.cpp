#include <bits/stdc++.h>
using namespace std;

class Employee{
public:
    string name,company;
    int age;

    //class method
    void introduceyourself(){
        cout<<"Name"<<" "<<name<<endl;
        cout<<"Company"<<" "<<company<<endl;
        cout<<"Age"<<" "<<age<<endl;
        cout<<"********************"<<endl;
    }

    //constructor
    Employee(string Name ,string Company , int Age){
        name=Name;
        company=Company;
        age=Age;
    }

};

int main()
{
    Employee em1=Employee("Phom","youtube",17);
    em1.introduceyourself();

    Employee em2=Employee("john","facebook",32);
    em2.introduceyourself();

}
