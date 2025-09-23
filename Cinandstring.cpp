/*Goal: practice std::cin for strings
**Write a program that prompts two users for their
**name, address, and phone number. 
**Print the information to the console in the following format:
**name
**\/t\/t address
**\/t\/tphone number
*/

# include <iostream>
# include <string>
using namespace std;

int main()
{
    string name1, address1, phone1;
    std::getline(std::cin, name1);
    std::getline(std::cin, address1);
    std::getline(std::cin, phone1);
    
    string name2, address2, phone2;
    std::getline(std::cin, name2);
    std::getline(std::cin, address2);
    std::getline(std::cin, phone2);
    
    
    std::cout <<"\n" << name1 << "\n"
              <<"\t\t" << address1 << "\n"
              <<"\t\t" << phone1 << "\n";
    
    
    std::cout <<"\n" << name2 << "\n"
              <<"\t\t" << address2 << "\n"
              <<"\t\t" << phone2 << "\n";
    return 0;
}