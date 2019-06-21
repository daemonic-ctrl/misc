#include <iostream>

using namespace std;

int main()
{
	enum eYourCards {Ace = 43, Jack, Queen, King};
	eYourCards card = Queen;
	cout << "Queen card value is: " << card << endl;
	return 0;
}
