package com.jk.explore.problems.digits;

import java.util.ArrayList;
import java.util.List;

public class DigitsSummationImpl implements DigitsSummation {

    @Override
    public int getSingleDigitSum(int number) {
        if(number == 0) {
            return 0;
        }
        int tempNumber = number;
        while(tempNumber > 0) {
            int[] digits = getDigits(tempNumber);
            int digitsSum = 0;
            for(int i=0; i< digits.length; i++) {
                digitsSum = digitsSum + digits[i];
            }
            if(digitsSum < 10) {
                return digitsSum;
            }
            tempNumber = digitsSum;
        }
        return 0;
    }

    public int[] getDigits(int number) {
        List<Integer> digits = new ArrayList<>();
        if(number == 0) {
            return new int[] {0};
        }
        while(number > 0) {
            int digit = number % 10;
            number = number / 10;
            digits.add(digit);
        }
        int[] digitsArray = new int[digits.size()];
        for(int i=0; i < digitsArray.length; i++) {
            digitsArray[i] = digits.get(i);
        }
        return digitsArray;
    }
}
