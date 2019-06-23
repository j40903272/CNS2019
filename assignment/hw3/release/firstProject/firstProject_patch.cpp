#include <stdio.h>
#include <unistd.h>
#include <iostream>
#include <signal.h>
#include <string>
#include "memory.h"
#include <math.h>
#include <stdlib.h>
#define TIMEOUT 120
#define MAX 5
using namespace std;

void handler(int sig)
{
    exit(3);
}

unsigned int count = 0;
char *allperson[MAX * 3];
void init_proc()
{
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);
    signal(SIGALRM, handler);
    alarm(TIMEOUT);
}

long long read_long()
{
    char buf[24];
    long long choice;
    read(0, buf, 23);
    choice = atoll(buf);
    return choice;
}

int read_int()
{
    char buf[24];
    int choice;
    read(0, buf, 23);
    choice = atoi(buf);
    return choice;
}

class Person
{
    string name;
    unsigned int age;

public:
    Person()
    {
    }
    ~Person()
    {
    }
    Person(int age, string uname) : age(age)
    {
        name = uname;
    }
    Person(const Person &p2) : age(p2.age)
    {
        name = p2.name;
    }
    int get_age()
    {
        return age;
    }
    string get_name()
    {
        return name;
    }
    void setname()
    {
        cout << "Name:";
        cin >> name;
    }
    void setnamebyname(string uname)
    {
        name = uname;
    }
    void setage(unsigned int uage)
    {
        age = uage;
    }
};

class PM : public Person
{
    char *project;
    unsigned int salary;

public:
    PM(string uname, unsigned int uage, char *uproject, unsigned int usalary)
    {
        setnamebyname(uname);
        setage(uage);
        project = new char[strlen(uproject)];
        memcpy(project, uproject, strlen(uproject));
        usalary = salary;
    }
    ~PM()
    {
        delete[] project;
        salary = 0;
    }
    char *get_project()
    {
        return project;
    }
    unsigned int get_salary()
    {
        return salary;
    }
    void show_info()
    {
        cout << "Title : PM" << endl;
        cout << "Name :" << get_name() << endl;
        cout << "Age  :" << get_age() << endl;
        cout << "Project :" << get_project() << endl;
        cout << "Salary : " << get_salary() << endl;
    }
    void edit_info()
    {
        setname();
        cout << "Project :";
        cin >> project;
        cout << "Done !" << endl;
    }
};

class RD : public Person
{
    string language;
    unsigned int salary;

public:
    RD()
    {
    }
    RD(string uname, unsigned int uage, string ulanguage, unsigned int usalary)
    {
        setnamebyname(uname);
        setage(uage);
        language = ulanguage;
        salary = usalary;
    }
    ~RD()
    {
        language.clear();
        salary = 0;
    }
    string get_language()
    {
        return language;
    }
    unsigned int get_salary()
    {
        return salary;
    }
    void show_info()
    {
        cout << "Title : RD" << endl;
        cout << "Name :" << get_name() << endl;
        cout << "Age  :" << get_age() << endl;
        cout << "Language :" << get_language() << endl;
        cout << "Salary : " << get_salary() << endl;
    }
    void edit_info()
    {
        setname();
        cout << "Language :";
        cin >> language;
        cout << "Done !" << endl;
    }
};

class HR : public Person
{
    string department;
    unsigned int salary;

public:
    HR()
    {
    }
    HR(string uname, unsigned int uage, string udepartment, unsigned int usalary)
    {
        setnamebyname(uname);
        setage(uage);
        department = udepartment;
        salary = usalary;
    }
    ~HR()
    {
        department.clear();
        salary = 0;
    }
    string get_department()
    {
        return department;
    }
    unsigned int get_salary()
    {
        return salary;
    }
    void show_info()
    {
        cout << "Title : HR" << endl;
        cout << "Name :" << get_name() << endl;
        cout << "Age  :" << get_age() << endl;
        cout << "Department :" << get_department() << endl;
        cout << "Salary : " << get_salary() << endl;
    }
    void edit_info()
    {
        setname();
        cout << "Department :";
        cin >> department;
        cout << "Done !" << endl;
    }
};

PM *pm_array[MAX];
RD *rd_array[MAX];
HR *hr_array[MAX];

void job_menu()
{
    puts("*********************");
    puts("       Position      ");
    puts("*********************");
    puts(" 1. PM              ");
    puts(" 2. RD             ");
    puts(" 3. HR             ");
    puts("*********************");
    printf("> ");
}

void new_person(int *pm_count, int *rd_count, int *hr_count)
{
    string name;
    unsigned int age = 0;
    unsigned int salary = 0;
    unsigned long idx;
    char *tmpname = NULL;
    job_menu();
    switch (read_long())
    {
    case 1:

        if (*pm_count < MAX)
        {
            cout << "Index :";
            idx = read_long();
            if (idx < MAX)
            {
                char project[64];
                memset(project, 0, 64);
                cout << "Name :";
                cin >> name;
                cout << "Age :";
                cin >> age;

                cout << "Project :";
                scanf("%64s", project);
                cout << "Salary :";
                cin >> salary;
                cout << "Done !" << endl;
                *pm_count++;
                pm_array[idx] = new PM(name, age, project, salary);
                tmpname = new char[strlen(name.c_str())];
                memcpy(tmpname, name.c_str(), strlen(name.c_str()));
                allperson[count] = tmpname;
                count++;
            }
        }
        return;
        break;
    case 2:
        if (*rd_count < MAX)
        {
            cout << "Index :";
            idx = read_long();
            if (idx < MAX)
            {
                string language;
                cout << "Name :";
                cin >> name;
                cout << "Age :";
                cin >> age;

                cout << "Language:";
                cin >> language;
                cout << "Salary :";
                cin >> salary;
                cout << "Done !" << endl;
                *rd_count++;
                rd_array[idx] = new RD(name, age, language, salary);
                tmpname = new char[strlen(name.c_str())];
                memcpy(tmpname, name.c_str(), strlen(name.c_str()));
                allperson[count] = tmpname;
                count++;
            }
        }
        return;
        break;
    case 3:
        if (*hr_count < MAX)
        {
            cout << "Index :";
            idx = read_long();
            if (idx < MAX)
            {
                string department;
                cout << "Name :";
                cin >> name;
                cout << "Age :";
                cin >> age;

                cout << "department :";
                cin >> department;
                cout << "Salary :";
                cin >> salary;
                cout << "Done !" << endl;
                *hr_count++;
                hr_array[idx] = new HR(name, age, department, salary);
                tmpname = new char[strlen(name.c_str())];
                memcpy(tmpname, name.c_str(), strlen(name.c_str()));
                allperson[count] = tmpname;
                count++;
            }
        }
        return;
        break;
    default:
        puts("Invalid");
        return;
    }
}

void show_person()
{
    int i = 0;
    cout << "- - - - - PM - - - - - " << endl;
    for (i = 0; i < MAX; i++)
    {
        if (pm_array[i])
        {
            cout << "################################" << endl;
            pm_array[i]->show_info();
        }
    }
    cout << "- - - - - RD - - - - - " << endl;
    for (i = 0; i < MAX; i++)
    {
        if (rd_array[i])
        {
            cout << "################################" << endl;
            rd_array[i]->show_info();
        }
    }
    cout << "- - - - - HR - - - - - " << endl;
    for (i = 0; i < MAX; i++)
    {
        if (hr_array[i])
        {
            cout << "################################" << endl;
            hr_array[i]->show_info();
        }
    }
}
template <class T>
void check(T p)
{
    if (p.get_age() > 100)
    {
        cout << "Invalid age !" << endl;
        exit(-1);
    }
}
void edit_person()
{
    string name;
    unsigned int age = 0;
    unsigned int salary = 0;
    int idx = 0;
    job_menu();
    switch (read_long())
    {
    case 1:
        cout << "index :";

        idx = read_int();
        if (idx < MAX && pm_array[idx])
        {
            PM *tpm = NULL;
            tpm = pm_array[idx];
            check(*tpm);
            tpm->edit_info();
        }
        return;
        break;
    case 2:
        cout << "index :";
        idx = read_int();

        if (idx < MAX && rd_array[idx])
        {
            RD *trd = NULL;
            trd = rd_array[idx];
            check(*trd);
            trd->edit_info();
        }
        break;
    case 3:
        cout << "index :";
        idx = read_int();
        if (idx < MAX && hr_array[idx])
        {
            HR *thr = NULL;
            thr = hr_array[idx];
            check(*thr);
            thr->edit_info();
        }
        return;
        break;
    default:
        return;
    }
}

void menu()
{
    puts("*********************");
    puts("   Profile manager   ");
    puts("*********************");
    puts(" 1. New              ");
    puts(" 2. Show             ");
    puts(" 3. Edit             ");
    puts(" 4. Employee list    ");
    puts(" 5. Exit             ");
    puts("*********************");
    printf("> ");
}

void listemployee()
{
    for (int i = 0; i < count; i++)
    {
        cout << allperson[i] << endl;
    }
}

int main()
{
    int pm_count = 0;
    int rd_count = 0;
    int hr_count = 0;
    unsigned long long choice;
    init_proc();
    while (1)
    {
        menu();
        choice = read_long();
        switch (choice)
        {
        case 1:
            new_person(&pm_count, &rd_count, &hr_count);
            break;
        case 2:
            show_person();
            break;
        case 3:
            edit_person();
            break;
        case 4:
            listemployee();
            break;
        case 5:
            exit(2);
            break;
        default:
            puts("Invalid Choice");
            break;
        }
    }
}