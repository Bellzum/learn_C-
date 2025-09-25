/*
Goal: practice using stringstream
Goal: practice getting string inputs and 
 **converting them to numeric variables using
 **stringstream.
 **
 **Prompt the user for the length of a room. 
 **Then prompt for the width of the room.
 **Print out the area of the room. 
 */
 

 #include <iostream>
 #include <string>
 #include <sstream>
 
 int main()
 {
     std::string stringLength, stringWidth;
     float length = 0.0;
     float width = 0.0;
     float area =0.0;
     
     std::cout << "Enter number of length: ";
     std::getline(std::cin, stringLength);
     std::stringstream(stringLength) >> length;
     
     std::cout << "Enter number of width: ";
     std::getline(std::cin, stringWidth);
     std::stringstream(stringWidth) >> width;
     
     area = length*width;
     std::cout << "The area of the room is " << area << "\n";

     return 0;
 }

 