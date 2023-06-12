package algorithm.stack;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class ParTest2 {
    public boolean solution() throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String input = reader.readLine();

        Stack<Character> charStack = new Stack<>();
        for (int i = 0; i < input.length(); i++) {
            char next = input.charAt(i);
            // 소괄호, 중괄호, 대괄호의 여는 괄호를 만날 때 stack에 push
            if (next == '(' || next == '{' || next == '[') {
                charStack.push(next);
            } else if (next == ')' || next == '}' || next == ']') {
                if (charStack.empty()) return false;
                char top = charStack.pop();
                if (next == ')' && top != '(') return false;
                else if (next == '}' && top != '{') return false;
                else if (next == ']' && top != '[') return false;
            }
        }

        return charStack.empty();
    }

    public static void main(String[] args) throws IOException {
        System.out.println((new ParTest2()).solution());

    }
}
