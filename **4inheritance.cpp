#include <bits/stdc++.h>
using namespace std;

//Abstraction  hides the complexity from the users
class Abstractemployee{
    virtual void Askforpromotion()=0;
};



class Employee:Abstractemployee{//class Employee sign the contract from class Abstractemployee
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


//inheritance
class Developer:public Employee{
public:
    string favprogramlanguage;//specific for only developer class
    Developer(string Name ,string Company , int Age, string Favprogramlanguage)
        :Employee(Name,Company,Age)
    {
        favprogramlanguage=Favprogramlanguage;
    }

     void fixbug(){
        cout<<getname()<<" fixed bug using "<<favprogramlanguage<<endl;
     }
};

int main()
{
    Developer d=Developer("Rod","Amazon",30,"c++");
    d.fixbug();
    d.Askforpromotion();//if in the class developer, i did not code public
                        //---> i can not use this function because of the private of Employee

}
