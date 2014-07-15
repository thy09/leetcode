#include <iostream>
#include <string>
#include <string.h>
using std::string;
class Solution {
public:
    void reverseWords(string &s) {
        char* head = (char*)s.data();
        char* tail = strchr(head,' ');
        char* next = tail+1;
        char temp;
        while (tail != NULL)
        {
					next = tail + 1;
					tail --;
					reverseBetween(head,tail);
					head = next;
					tail = strchr(head,' ');
				}
				reverseStr(head);
				reverseStr((char*)s.data());
				s = string(rmSpaces((char*)s.data()));
    }
private:
		void reverseBetween(char* head, char* tail)//dangerous function
		{
			char temp;
			while (head < tail)
			{
				temp = *head;
				*head++ = *tail;
				*tail-- = temp;
			}
		}
		void reverseStr(char* s)
		{
			char* tail = s + strlen(s)-1;
			reverseBetween(s,tail);
		}
		char* rmSpaces(char* s)
		{
			char* left = s;
			char* right = s;
			while (*right == ' ' && *right != '\0') right++;
			while (*right != '\0')
			{
				while (*right != ' ' && *right != '\0') *left++ = *right++;
				while (*right == ' ' && *right != '\0') right++;
				if (*right == '\0')
					break;
				*left++ = ' ';
			}
			*left++ = '\0';
			return s;
		}
};

int main()
{
	string st;
	Solution solu;
	getline(std::cin,st);
	solu.reverseWords(st);
	std::cout<<'|'<<st<<'|'<<std::endl;
	return 0;
}
