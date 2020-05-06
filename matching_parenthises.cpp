#include <string>
class Solution {
public:
    bool isValid(std::string s) {
        stack <char> Stack;
        for (int i = 0; i<s.length(); i++){
            // std::cout << s[i];
            if (s[i]=='('){
                Stack.push(')');
            }
            else if (s[i]=='{'){
                Stack.push('}');
            }
            else if (s[i]=='['){
                Stack.push(']');
            }
            else if (Stack.size() > 0) {
                if (s[i] != Stack.top()){
                    return false;
                }
                Stack.pop();
            }
            else{
                return false;
            }
        }
        if (Stack.size()!=0){
            return false;
        }
        else{
            return true;
        }
    }
};