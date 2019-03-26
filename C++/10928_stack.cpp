#include <iostream>
#include <sstream>
using namespace std;
const int Stack_Size = 1000;

class stackarray
{
  private:
    int stack[Stack_Size];
    int top;

  public:
    stackarray() { top = -1; }
    void push(int item) { stack[++top] = item; }
    void pop() { cout << stack[top--] << "\n"; }
    void size() { cout << top + 1 << "\n"; }
    void peek() { cout << stack[top] << "\n"; }
    int isEmpty() { return top == -1; }
    int isFull() { return top == Stack_Size - 1; }
    void displayStack()
    {
        int cusur;
        if (isEmpty())
        {
            cout << "Stack is empty!\n";
        }
        else
        {
            cusur = top;
            while (cusur != -1)
                cout << stack[--cusur] << " ";
        }
        cout << "\n";
    }
};

int string_split(string s, string *first, int *num);

int main()
{
    stackarray my_stack;
    char input_c[256];
    string input;
    int times;
    cin >> times; //횟수
    int num;
    string cmd; //명령어와 옵션
    
    for (int i = 0; i < times; i++)
    {   
        cin.clear();
        cin.getline(input_c, 256);
        input = input_c;
        string_split(input, &cmd, &num);
        if (cmd.compare("push") == 0)
        {
            if (!my_stack.isFull())
            {
                my_stack.push(num);
            }
            // else
            //     cout << "Stack is full \n";
            continue;
        }
        if (cmd.compare("pop") == 0)
        {
            if (!my_stack.isEmpty())
            {
                my_stack.pop();
            }
            // else
            //     cout << "Stack is empty \n";
            continue;
        }
        if (cmd.compare("top") == 0)
        {
            if (!my_stack.isEmpty())
                my_stack.peek();
            continue;
        }
        if (cmd.compare("size") == 0 && input.compare("q") != 0)
            my_stack.size();
        if (cmd.compare("empty") == 0)
        {
            int em = my_stack.isEmpty();
            cout << em << "\n";
            continue;
        }
        cout << "Try input the correct command\n";
    }

    return 0;
}

int string_split(string s, string *first, int *num)
{
    int cutAt = s.find(" ");
    if (cutAt > -1)
    {
        *first = s.substr(0, cutAt);
        *num = atoi(s.substr(cutAt).c_str());
        return 0;
    }
    else
        return -1;
}