#include <iostream>

using namespace std;

void types_size()
{
	cout << "This program outputs the size of diffrent variable types." << endl;
	
	cout << "The size of a bool is: " << sizeof(bool) << endl;
	cout << "The size of a int is: " << sizeof(int) << endl;
	cout << "The size of a unsigned int is: " << sizeof(unsigned int) << endl;
	cout << "The size of a long is: " << sizeof(long) << endl;
	cout << "The size of a long long is: " << sizeof(long long) << endl;
	cout << "The size of a char is: " << sizeof(char) << endl;
	cout << "The size of a double is: " << sizeof(double) << endl;
}

int main()
{
	types_size();
	return 0;
}
