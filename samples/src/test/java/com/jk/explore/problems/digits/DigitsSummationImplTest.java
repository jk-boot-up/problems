package com.jk.explore.problems.digits;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class DigitsSummationImplTest {

    private DigitsSummationImpl digitsSummation = new DigitsSummationImpl();

    @Test
    public void findDigitsArray() {
        DigitsSummationImpl digitsSummation = new DigitsSummationImpl();
        int[] digits = digitsSummation.getDigits(1234);
        Assertions.assertArrayEquals(new int[] {4, 3, 2, 1}, digits);
        digits = digitsSummation.getDigits(0);
        Assertions.assertArrayEquals(new int[] {0}, digits);
    }

    @Test
    public void getSingleDigitSum() {
        int singleDigitSum = digitsSummation.getSingleDigitSum(1234);
        Assertions.assertEquals(singleDigitSum, 1);
        singleDigitSum = digitsSummation.getSingleDigitSum(0);
        Assertions.assertEquals(singleDigitSum, 0);
        singleDigitSum = digitsSummation.getSingleDigitSum(78612354);
        Assertions.assertEquals(singleDigitSum, 9);
    }
}
