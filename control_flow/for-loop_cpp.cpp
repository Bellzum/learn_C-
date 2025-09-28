#include <iostream>
using namespace std;

int main()
{
    float input;
    float sum = 0;
    for (int i =0; i<5; i++)
    {
        std::cout<<"What is the next number?\n";
        std::cin>>input;
        sum = sum + input;
    }
    std::cout<<"Sum = "<<sum<<"\n";
    std::cout<<"Average = "<<sum/5<<"\n";
    return 0;
}