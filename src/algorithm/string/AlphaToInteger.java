package algorithm.string;

public class AlphaToInteger {
    // 숫자로만 이루어진 value 문자열에 대해서
    // 각 글자를 숫자 데이터로 해석한 뒤
    // - 48 하면 숫자가 된다.
    public int aToi(String value) {
        int result = 0;
        int i = 0;
        boolean negative = false;
        if (value.charAt(i) == '-') {
            negative = true;
            i++;
        }
        // TODO 문자열을 한 글자씩 확인
        for (; i < value.length(); i++) {
            // TODO 자릿수 변환
            result *= 10;

            // TODO 글자를 숫자로 변환
            result += value.charAt(i) - 48;
        }

        if (negative) result *= -1;

        return result;
    }

    public static void main(String[] args) {
        AlphaToInteger aToi = new AlphaToInteger();
        System.out.println(aToi.aToi("12345") + 1);
        System.out.println(aToi.aToi("-4291"));
    }
}
