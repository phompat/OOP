#include <bits/stdc++.h>
using namespace std;

//Abstraction  hides the complexity from the users
class Abstractemployee{
    virtual void Askforpromotion()=0;
};


//class Employee sign the contract from class Abstractemployee
class Employee:Abstractemployee{

//will not access anymore outside the class
private:
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
        cout<<"Name"<<" "<<name<<endl<<"Company"<<" "<<company<<endl;
        cout<<"Age"<<" "<<age<<endl<<"********************"<<endl;
    }
    void Askforpromotion(){
        if(age>30)cout<<name<<" got promoted"<<endl;
        else cout<<name<<" did not get promoted"<<endl;
    }

    //constructor
    Employee(string Name ,string Company , int Age){
        name=Name,company=Company,age=Age;
    }

};

int main()
{
    Employee em1=Employee("Phom","youtube",17);
    em1.Askforpromotion();
    Employee em2=Employee("john","facebook",32);
    em2.Askforpromotion();

}
