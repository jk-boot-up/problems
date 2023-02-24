package com.jk.explore.problems.palindrome.number;

public class PalindromeNumber {

    /**
     * Time complexity: O(m) where m is the length of the given input number n
     * @param n
     * @return true if the number is palindrome
     */
    public boolean isPalindrome(int n) {
        if(n < 0) {
            return false;
        }
        int reversedNumber = reverse(n);
        return reversedNumber == n;
    }


    /**
     * Time complexity: O(m) where m is the length of the given input number
     * @param number
     * @return reversed number
     */
    public int reverse(int number) {
        int reversed = 0;
        while (number > 0) {
            int lastDigit = number % 10;
            number = number / 10;
            reversed = reversed * 10 + lastDigit;
        }
        return reversed;
    }

    public int reverseWithCharApi(int number) {
        char[] chars = String.valueOf(number).toCharArray();
        int left = 0;
        int right = chars.length -1;
        char temp;
        while(left < right) {
            temp = chars[right];
            chars[right] = chars[left];
            chars[left] = temp;
            left++;
            right--;
        }
        String reversedString = new String(chars);
        return Integer.valueOf(reversedString).intValue();
    }



}
