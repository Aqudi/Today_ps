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
  int isEmpty() { return (top == -1) ? 1 : 0; }
  int isFull() { return top == Stack_Size - 1; }
};

int main()
{
  stackarray my_stack;
  string str;
  int n;

  cin >> n;
  for (int i = 0; i < n; i++)
  {
    cin >> str;

    if (str == "push")
    {
      int num;
      cin >> num;
      if (!my_stack.isFull())
        my_stack.push(num);
      continue;
    }

    if (str == "pop")
    {
      if (!my_stack.isEmpty())
        my_stack.pop();
      else
        cout << "-1\n";
      continue;
    }
    if (str == "empty")
    {
      cout << my_stack.isEmpty() << "\n";
      continue;
    }

    if (str == "top")
    {
      if (!my_stack.isEmpty())
        my_stack.peek();
      else
        cout << "-1\n";
      continue;
    }
    if (str == "size")
    {
      my_stack.size();
      continue;
    }
  }

  return 0;
}