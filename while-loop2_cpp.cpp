/* Goal:
        Understand the break and continue statements
*/

#include<iostream>

int main()
{
    int a = 0;

    // First while loop
    while(a < 5)
    {
        std::cout<<"a = " << a<< "\n";
        a++; // a +=

        if (a == 3) 
            break;
    }

    std::cout << "The first statement after the first while loop\n\n";

    // Second while loop
    while (a < 15)
    {
        a++;

        if (a == 10)
        {
            std::cout<< "\tWhen a=10, go back to the top of the loop";
            std::cout<< "\t This means a=10 is skipped.\n";
            continue;
        }
        std::cout << "After continue a = " << a <<"\n";
    }

    return 0;

}