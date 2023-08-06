package com.jk.explore.problems.add.two.numbers;

import java.util.Iterator;
import java.util.LinkedList;

public class SumImpl implements Sum {

    @Override
    public LinkedList<Integer> add(LinkedList<Integer> n1, LinkedList<Integer> n2) {
        assert n1 != null;
        assert n2 != null;
        LinkedList<Integer> sum = new LinkedList<>();
        Iterator<Integer> i1 = n1.iterator();
        Iterator<Integer> i2 = n2.iterator();
        int carry = 0;
        while (i1.hasNext() || i2.hasNext()) {
            int digit1 = i1.hasNext() ? i1.next() : 0;
            int digit2 = i2.hasNext() ? i2.next() : 0;
            carry = updateSumAndGetCarry(digit1, digit2, carry, sum);
        }
        if(carry > 0) {
            sum.add(carry);
        }
        return sum;
    }

    private int updateSumAndGetCarry(int digit1, int digit2, int carry, LinkedList<Integer> sum) {
        int digit;
        int digitsSum;
        digitsSum = digit1 + digit2 + carry;
        if(digitsSum > 10) {
            digit = digitsSum % 10;
            carry = digitsSum / 10;
        } else {
            digit = digitsSum;
        }
        sum.add(digit);
        return carry;
    }
}
