#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <ctype.h> 
#include <stdlib.h>

using namespace std;

string stack_array[1024];

template <typename T> // 두가지 타입의 스택이 필요하므로 템플릿을 이용한다.
class stack
{ // 간단한 스택 자료형을 만들어준다.
private:
	int top = -1; //스택의 맨 위를 표시해 줄 포인타
	T stack_array[1024];

public:
	void push(T s)
	{ // 포인터를 한 칸 올린 뒤 데이터를 저장
		stack_array[++top] = s;
	}
	T pop()
	{ // 데이터를 뽑아낸 뒤 포인터를 한 칸 뒤로물림
		return stack_array[top--];
	}
	T peek()
	{ // 데이터를 뽑아내는 것이 아니라 확인만 필요할 때 사용
		return stack_array[top];
	}
	int isEmpty()
	{ // stack이 비었으면 1, 아니면 0을 반환
		return top == -1;
	}
};

string infix_postfix_converter(string &ex)
{
	string str_r; // 결과값을 저장할 스트링객체
	stack<char> op; // operator를 담을 스택
	for (unsigned int i = 0; i < ex.length(); i++)
	{
		if (isdigit(ex[i])) { // 읽어들이는 위치의 값이 숫자면 결과값에 바로 push_back
			// cout << ex[i] << endl; 확인코드
			str_r.push_back(ex[i]);
			continue;
		}
		if (ex[i] == '(') // 괄호를 열였을 때 무조건 스택에 푸시
		{
			op.push(ex[i]);
		}
		else if (ex[i] == ')')
		{
			while (op.peek() != '(') {// 여는 괄호가 나올때까지 pop
				str_r.push_back(op.pop()); // 변수 o에 pop한 결과를 저장
			}
			op.pop(); // 여는 괄호를 제거함
		}
		else if (ex[i] == '+' || ex[i] == '-') 
		{ // 연산자 우선순의가 낮은 +, -는 스택에 * . / 연산자보다 먼저 push된다.
			if (op.peek() == '*' || op.peek() == '/') 
			{ // *, / 연산자가 앞에 있을 시 먼저 계산되고 +, - 연산자를 push 한다.
				str_r.push_back(op.pop());
				op.push(ex[i]);
			}
			else
			{
				op.push(ex[i]);
			}
		}
		else if (ex[i] == '*' || ex[i] == '/') 
		{
			op.push(ex[i]);
		}
	}
	while (!op.isEmpty())
	{
		str_r.push_back(op.pop());
	}

	return str_r;
}

int postfix_form_calculate(string ex)
{
	int result; // 결과값을 저장할 변수
	stack<int> cal_stack; // 계산에 이용하기 위한 스택 객체
	for (unsigned int i = 0; i < ex.length(); i++)
	{ // 식을 전부 읽을 때까지 동작
		char o = ex[i]; // 읽어온 식
		if (isdigit(o)) 
		{ // o가 operand라면 int형으로 변환하여 op에 저장
			int op = ex[i] - '0';
			cal_stack.push(op); // 스택에 op를 저장하여 연산자를 만날 때 계산
		}
		else
		{ // o가 operater라면
			int num1, num2; // 계산할 두 피연산자를 받는 변수
			num1 = cal_stack.pop();
			num2 = cal_stack.pop();
			int cal_result; // 계산결과를 받는 변수
			if(o == '+')
			{ // 연산자에 따른 계산
				cal_result = num1 + num2;
				cal_stack.push(cal_result);
			}
			else if (o == '-') 
			{
				cal_result = num2 - num1;
				cal_stack.push(cal_result);
			}
			else if (o == '*')
			{
				cal_result = num1 * num2;
				cal_stack.push(cal_result);
			}
			else if (o == '/')
			{
				cal_result = num1 / num2;
				cal_stack.push(cal_result);
			}
		}
	}
	result = cal_stack.pop();
	return result;
}

int main()
{
	ifstream reader("data.txt"); // 파일 입출력을 위한 stream 객체를 선언한다.
	string str; // 파일입력 결과를 저장할 스트링 객체
	while(!reader.eof())
	{
		getline(reader, str);
		cout << "1) Echo data (infix form) : \t" << str << "\n"; //입력받은 데이터 표기
		string post_form_expression = infix_postfix_converter(str); // 결과값 저장할 스트링객체, 함수 호출
		cout << "2) Conversion (postfix form) : \t" << post_form_expression << "\n"; // 결과값 출력
		int result = postfix_form_calculate(post_form_expression); //계산
		cout << "3) Result : \t" << result << "\n\n"; // 결과 출력
	}
}
