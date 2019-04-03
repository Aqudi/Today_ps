/*********************************************************
* Name		 : 허태정
* Student ID : 20181708
* Program ID : HW#2 infix_to_postfix
* Description: 중위 표기(infix notation)법으로 표현된 식을 컴퓨터가 
			   읽기 편하도록 후위 표기(postfix notation)법으로 
			   쓰인 식으로 바꾸는 프로그램이다.
* Algorithm  : 
	main 함수
	data.txt 파일에는 여러가지 infix form 형태를 띈 식들이 저장되어 있다.
	1. C++의 파일 입출력 스트림은 fstream의 ifstream 객체인 reader를 선언한다.
	2. 선언한 reader객체를 통해서 파일의 eof를 만날 때까지 파일을 읽어들인다.
	3. 읽어들인 줄을 string 객체인 str에 저장한다.
	4. 후술할 infix_postfix_converter함수를 통해서 컴퓨터가 계산하기 쉬운 수식의
		형태로 변환한다.
	5. 변환한 결과값을 string 객체인 post_form_expression에 저장한다.
	6. post_form_expression에 저장된 식을 후술할 postfix_form_calculate함수의 인자로
		넘겨서 계산한다.
	7.계산한 결과값을 int형 변수인 result에 저장하여 출력한다.

	infix_postfix_converter 함수
	1. 결과값을 저장할 스트링 객체인 str_r을 선언한다.
	2. char형태로 식을 분해하여 읽을 것이기 때문에 char형의 stack객체 op를 선언한다.
	3. 인덱싱 변수인 i가 식을 담은 ex변수에 길이에 도달하기 전까지 for루프를 돈다.
	3-1. ex변수의 [i]번쨰 아이템들을 대상으로 isdigit()함수를 사용하여 숫자임을 판별한다.
	3-1-1. 숫자라면 str_r에 현재 읽은 ex[i]의 값을 붙여넣고 continue한다..
	3-2. ex[i]의 값이 '(' 일 때 스택 객체 op에 그 값을 push한다.
	3-2-1.ex[i]번째 값이 ')'일 때 '('가 나올 때까지 while루프를 시행한다.
	3-2-1-1. op스택의 맨 윗 값을 peek함수로 확인하면서 '('가 맨 위에 있을 때까지 루프를 진행한다.
	3-2-2. 스택의 맨 윗 값을 peek함수로 엿보면서 '('가 맨 위에 있을 때 
		   루프를 중지시키고 '('을 pop함수로 스택에서 제거해준다.
	3-3. ex[i]의 값이 '+'이거나 '-'일때
	3-3-1. op스택의 맨 윗 값이 '+'나 '-'보다 연산 우선순위가 높은 '*', '/'인지 확인해준다.
	3-3-1-1. 만약 op스택의 맨 윗 값이 '*'이나 '/'이라면 str_r에 op.pop()의 결과값을 덧붙여준다.
		     그리고 ex[i]의 값을 스택에 넣는다.
	3-3-1-2. 아니라면 ex[i]의 값을 스택 op에 넣는다.
	3-3-2. ex[i]값이 위 3-1부터의 조건에 걸리지 않고 '*', '/'라면 그 값을 스택에 push한다.
	4. 스택 op가 비지 않을 때까지 str_r에 남은 스택의 값들을 pop해서 붙여넣는다.
	5. 결과값 str_r을 반환한다.

	postfix_form_calculate 함수
	1. 결과값을 저장할 int형 변수 result를 선언한다.
	2. 피연산자들을 저장할 int형 stack 객체 cal_stack을 선언한다.
	3.인덱싱 변수인 i가 식을 담은 ex변수에 길이에 도달하기 전까지 for루프를 돈다.
	3-1. 읽어온 식의 i번째 값을 char형 변수 o에 저장한다.
	3-2. o가 숫자라면
	3-2-1-1. o에 '0'문자를 빼주어 int형으로 변환하여 변수 op에 저장한다.(아스키 코드의 특성)
	3-2-1-2. cal_stack에 변환한 값 op를 push한다.
	3-2-2-1. 숫자가 아니라면 int형 변수 num1, num2를 선언하고 각각에 cal_stack.pop()결과를 저장한다.
	3-2-2-2. 연산자가 '+'라면 더하기 연산 후 cal_stack에 push한다.
	3-2-2-2. 연산자가 '-'라면 빼기 연산 후 cal_stack에 push한다.
	3-2-2-3. 연산자가 '*'라면 곱하기 연산 후 cal_stack에 push한다.
	3-2-2-4. 연산자가 '/'라면 나누기 연산 후 cal_stack에 push한다.
	4. result변수에 cal_stack으로 계산한 값을 뽑아낸뒤 그 결과값을 반환한다.

* Variables  :
	infix_postfix_converter(string &ex) - ex변수에 식을 받아서 infix form을 postfix 
										  form으로 변환하여 반환
	postfix_form_calculate(string ex) - postfix form으로 쓰여진 식을 ex변수로 받아 계산하여 반환
	stack - 스택을 구현한 클래스 식들의 연산 순서대로 식을 변환하기 위하여 사용

	reader - 파일 입출력 스트림인 fstream의 ifstream객체 파일을 읽을 때 사용한다.
	str - 메인 함수에서 reader로 읽어들인 식을 저장하는 변수
	post_form_expression - infix_postfix_converter함수를 통해 
						   postfix form으로 변한 식을 저장하는 변수
	result - post_form_calculate함수로 계산한 값을 반환받는 int형 변수
*********************************************************/

#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <ctype.h> 
#include <stdlib.h>

using namespace std;

string infix_postfix_converter(string &ex);
int postfix_form_calculate(string ex);

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


/*********************************************************
* Class 	 : stack
* Desciption : 타입변수 T를 사용하여 경우에 따라서 유연하게 타입을 선언할 수 있는 스택
* Variables	 :
	stack_array - 스택의 아이템들을 저장하는 배열
	top - 스택의 맨 윗부분을 가르키는 변수
	push - 스택의 top위치에 수를 집어넣고 동시에 top의 값을 1 증가시킴
	pop - 스택의 top위치에 있는 수를 반환함과 동시에 top의 값을 1 감소시킴
	peek - 스택의 top위치에 있는 수를 반환
	isEmpty - 스택이 비었으면 1, 아니면 0
*********************************************************/
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


/*********************************************************
* Function	 : infix_postfix_converter
* Desciption : ex변수에 식을 받아서 infix form을 postfix form으로 변환하여 반환
			   계산하기 쉬운 형태로 변환하여 이후 계산을 용이하게 도와줌
* Variables	 :
	str_r - infix_postfix_converter함수내에서 반환할 결과값을 저장하는 변수
	op - 인수로 받은 식 정보를 담은 string 객체인 ex변수의 일부를 저장할 char타입의 스택
*********************************************************/
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


/*********************************************************
* Function	 : postfix_form_calculate
* Desciption : ex변수에 postfix form으로 변환된 식을 받아서 계산하여 값을 반환하는 함수
* Variables	 :
	result - 결과값을 받아서 반환할 때 사용하는 변수
	cal_stack - 식을 계산할 때 피연사자들을 저장할 때 사용하는 스택
	o - 읽어온 식의 일부 ex변수의 i번째 값들
	op - operand의 약자로 피연산자를 의미 o의 값에 '0'값을 빼줘서 
		 int형으로 변환(아스키코드의 특성)
	cal_result - 계산 도중에 나오는 결과들을 저장해두는 변수
*********************************************************/
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
			if (o == '+')
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

