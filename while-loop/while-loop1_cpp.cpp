/*Goal: In the programming quiz, use a while loop to prompt
**the user to guess a target number. 
**Tell the user if the guess is too high or too low. 
**The user enters -1  or guesses the target number to end 
**the program.
*/

#include <iostream>
#include<sstream>

int main() 
{
    int target = 55;
    std::string userString;
    int guess = -1;

    // Keep asking until the user guesses target or enters -1
    while (guess != target) 
    {
        std::cout << "Guess a number between 0 and 100 (-1 to quit): ";
        std::cin >> guess;
        std::cout<< guess<<"\n";
        
        if (guess < target) 
        {
            std::cout << "This number is lower than the target number.\n";
        } 
        else if  ( guess > target)
        { 
            std::cout << "This number is higher than the target number.\n";
        }
        else
        {
            std::cout << "You guessed the target!\n";
            
        }
        
        if (guess == -1) 
        {
            std::cout << "Good bye!\n";
            break;
        }

    }
    return 0;
}
