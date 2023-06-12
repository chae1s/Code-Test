package algorithm.sort;

import java.util.Arrays;

public class BubbleSort {
    public static void main(String[] args) {
        int[] arr = {36, 12, 18, 15, 41, 19};
        int n = arr.length;

        // 첫 번째 원소와 인접한 원소를 비교
        // 두 번째 원소와 세 번째 원소를 비교
        // ...
        // n - 1 번째 원소와 n 번째 원소를 비교
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    //교환
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }

        System.out.println(Arrays.toString(arr));
    }
}
