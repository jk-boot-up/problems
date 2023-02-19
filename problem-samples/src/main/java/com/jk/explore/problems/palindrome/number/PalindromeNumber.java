package com.jk.explore.problems.palindrome.number;

public class PalindromeNumber {

    public boolean isPalindrome(int n) {
        int originalNumber = n;
        if(n < 0) {
            return false;
        }
        int reversedNumber = 0;
        while(n > 0) {
            reversedNumber = reversedNumber * 10 + (n % 10);
            n = n / 10;
        }
        return reversedNumber == originalNumber;
    }
}
