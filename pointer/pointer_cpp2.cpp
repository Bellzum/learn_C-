/*For this program print for each variable
**print the value of the variable, 
**then print the address where it is stored. 
*/
#include<iostream>
#include<string>

int main()
{
    std::string name;
    int givenInt;
    float givenFloat;
    double givenDouble ;
    std::string givenString;
    char givenChar;
    int * pointerGivenInt; /*stores the address of an integer*/
    int **pointerPointerGivenInt; /*stores the address of a pointer to an integer.*/
    
    pointerGivenInt = &givenInt;
    pointerPointerGivenInt = &pointerGivenInt;
    
    std::cout<<"integer = \n";
    std::cin>>givenInt;
    
    std::cout<<"float = \n";
    std::cin>>givenFloat;
    
    std::cout<<"double = \n";
    std::cin>>givenDouble;
    
    std::cout<<"character = \n";
    std::cin>>givenChar;
    
    std::cout<<"string = \n";
    std::cin.ignore();
    std::getline (std::cin, givenString);
    
    std::cout<<"integer = "<<givenInt<<"\n";
    std::cout<<"float = "<<givenFloat<<"\n";
    std::cout<<"double = "<<givenDouble<<"\n";
    std::cout<<"character = "<<(char)givenChar<<"\n";
    std::cout<<"string = "<<givenString<<"\n";
    
    std::cout<<"address integer = "<<&givenInt<<"\n";
    std::cout<<"address float = "<<&givenFloat<<"\n";
    std::cout<<"address double = "<<&givenDouble<<"\n";
    std::cout<<"address character = "<<(void *) &givenChar<<"\n";
    std::cout<<"address string = "<<&givenString<<"\n";   


    
    return 0;
}
