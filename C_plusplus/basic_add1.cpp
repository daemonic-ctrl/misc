#include <iostream>

using namespace std;

int main()
{
	/*without making the integers initaly equal something you cant be sure about their place in memory which isn good for programs*/
	int num0 = 0;
	int num1 = 0;
	
	cout << "Enter First Number: ";
	cin >> num0;

	cout << "Enter Second Number: ";
	cin >> num1;

	cout << endl << num0 << " + " << num1 << " = " << num0 + num1 << endl;
}
