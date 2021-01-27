#include <iostream> // a PREPROCESSOR directive
#include <fstream>
#include <string>


int main() // function header
{ // start of function body
    using namespace std; // make definitions visible
    ifstream inFile;
    string input[4];
    string buffer;
    int i = 0;
    inFile.open("tekateki.txt");
    while (getline (inFile,buffer)){
        input[i] = buffer;
        i++;
    }
    cout << input[2] << endl;
    inFile.close();
    return 0; // terminate main()
} // end of function body

