package algorithm.stack;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class InfixToPostfix {
    // 연산자인지 검증하는 메소드
    private boolean isOperator(char token) {
        return token == '(' || token == '+' || token == '-' || token == '*' || token == '/';
    }

    // 스택 내부에서의 우선 순위
    private int inStackPriority(char operator) {
        if (operator == '+' || operator == '-') return 1;
        else if (operator == '*' || operator == '/') return 2;
        else if (operator == '(') return 0;
        else throw new IllegalArgumentException("not allowed operator");
    }

    // 스택 외부에서의 우선 순위
    private int inComingPriority(char operator) {
        if (operator == '+' || operator == '-') return 1;
        else if (operator == '*' || operator == '/') return 2;
        else if (operator == '(') return 3;
        else throw new IllegalArgumentException("not allowed operator");
    }
    public void solution() throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String input = reader.readLine();

        // 결과를 담아줄 StringBuilder
        StringBuilder answerBuilder = new StringBuilder();
        // 연산자를 담는 스택
        Stack<Character> operStack = new Stack<>();

        for (int i = 0; i < input.length(); i++) {
            char token = input.charAt(i);
            // 연산자일 때
            if (isOperator(token)) {
                // 스택이 비어있다면 push
                if (operStack.empty()) {
                    operStack.push(token);
                } else {
                    // 스택의 제일 위의 연산자가 나보다 우선순위가 낮은 연산자가 올때까지 pop (while)
                    while (inStackPriority(operStack.peek()) >= inComingPriority(token)) {
                        answerBuilder.append(operStack.pop());
                        if (operStack.empty()) break;
                    }

                    operStack.push(token);

                }

            } else if (token == ')') {
                // 스택에서 여는 괄호가 나올 때까지 pop
                char top = operStack.pop();
                while (top != '(') {
                    answerBuilder.append(top);
                    top = operStack.pop();
                }

            } else answerBuilder.append(token);


        }
        while (!operStack.empty()) {
            answerBuilder.append(operStack.pop());
        }

        System.out.println(answerBuilder);
    }

    public static void main(String[] args) throws IOException {
        new InfixToPostfix().solution();
    }
}
