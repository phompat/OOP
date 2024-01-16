#include <bits/stdc++.h>
using namespace std;
//encapsulation

class Employee{
private://will not access anymore outside the class
    string name,company;
    int age;
public:
    //setter and getter
    void setname(string Name){name=Name;}
    string getname(){return name;}

    void setcompany(string Company){company=Company;}
    string getcompany(){return company;}

    void setage(int Age){
        if(Age>=18)age=Age;
    }
    int getage(){return age;}


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
    em1.setname("Through");
    em1.setage(25);
    em1.introduceyourself();

    Employee em2=Employee("john","facebook",32);
    em2.setage(17);
    em2.setcompany("Google");
    em2.introduceyourself();

}
