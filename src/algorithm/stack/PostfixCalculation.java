package algorithm.stack;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class PostfixCalculation {
    public void solution() throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String input = reader.readLine();

        Stack<Integer> digitStack = new Stack<>();
        for (int i = 0; i < input.length(); i++) {
            char token = input.charAt(i);

            // 1. 숫자라면, 스택에 push한다.
            // Character.isDigit(token) -> token이 숫자가 표현된 글자인지 판단하는 메소드
            // token을 int로 변환 -> token - '0'
            if (Character.isDigit(token)) digitStack.push(token - '0');

            // 2. 숫자가 아니라면, 연산자 스택에서 두번 pop하고 계산한다.
            else {
                int num1 = digitStack.pop();
                int num2 = digitStack.pop();
                switch (token) {
                    case '+' -> digitStack.push(num2 + num1);
                    case '-' -> digitStack.push(num2 - num1);
                    case '*' -> digitStack.push(num2 * num1);
                    case '/' -> digitStack.push(num2 / num1);
                    default -> throw new IllegalArgumentException("invalid operator");
                }
            }
        }

        System.out.println(digitStack.pop());

    }

    public static void main(String[] args) throws IOException {
        new PostfixCalculation().solution();
    }
}
