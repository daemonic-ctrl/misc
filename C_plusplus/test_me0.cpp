#include <iostream>

using namespace std;

/*declaring global variables*/
int x = 0;
int n = 0;

void add_function()
{
	int a = 0;
	cout << "Enter Number: ";
	cin >> a;
	n = x + a;
	cout << n << endl;
}
int main()
{
	cout << "Enter X Value: ";
	cin >> x;
	add_function();
	cout << n;
	return 0;
}
