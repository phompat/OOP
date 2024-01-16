#include <bits/stdc++.h>
using namespace std;
//polymorphism

class Abstractemployee{
    virtual void Askforpromotion()=0;
};

class Employee:Abstractemployee{
private:
    string name,company;
    int age;
public:
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
    virtual void Work(){//**coding virtual allows to make line 72 work.
        cout<<name<<" is checking email , task backlog, performing tasks ...."<<endl;
    }

    //constructor
    Employee(string Name ,string Company , int Age){
        name=Name,company=Company,age=Age;
    }

};


//inheritance
class Developer:public Employee{
public:
    string favprogramlanguage;
    Developer(string Name ,string Company , int Age, string Favprogramlanguage)
        :Employee(Name,Company,Age)
    {
        favprogramlanguage=Favprogramlanguage;
    }

     void fixbug(){
        cout<<getname()<<" fixed bug using "<<favprogramlanguage<<endl;
     }
     void Work(){
        cout<<getname()<<" is writting "<<favprogramlanguage<<" code"<<endl;
    }
};



int main()
{
    Developer d=Developer("Rod","Amazon",30,"c++");
    d.fixbug();
    d.Askforpromotion();
    d.Work();


    Employee *e=&d;
    e->Work();

}
