package com.jk.explore.problems;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class TwoNumbersSumTest {


    @Test
    public void summation1() {
        TwoNumbersSum.Util util = new TwoNumbersSum.Util();
        TwoNumbersSum.DigitLinkedList one = util.getLinkedList(342);
        TwoNumbersSum.DigitLinkedList two = util.getLinkedList(465);
        TwoNumbersSum.DigitLinkedList sumList = util.add(one, two);
        Integer sum = util.getNumber(sumList);
        Assertions.assertEquals(807, sum);
    }

    @Test
    public void summation2() {
        TwoNumbersSum.Util util = new TwoNumbersSum.Util();
        TwoNumbersSum.DigitLinkedList one = util.getLinkedList(999);
        TwoNumbersSum.DigitLinkedList two = util.getLinkedList(1);
        TwoNumbersSum.DigitLinkedList sumList = util.add(one, two);
        Integer sum = util.getNumber(sumList);
        Assertions.assertEquals(1000, sum);
    }

    @Test
    public void summation3() {
        TwoNumbersSum.Util util = new TwoNumbersSum.Util();
        TwoNumbersSum.DigitLinkedList one = util.getLinkedList(1);
        TwoNumbersSum.DigitLinkedList two = util.getLinkedList(9999);
        TwoNumbersSum.DigitLinkedList sumList = util.add(one, two);
        Integer sum = util.getNumber(sumList);
        Assertions.assertEquals(10000, sum);
    }

    @Test
    public void summation4() {
        TwoNumbersSum.Util util = new TwoNumbersSum.Util();
        TwoNumbersSum.DigitLinkedList one = util.getLinkedList(234);
        TwoNumbersSum.DigitLinkedList two = util.getLinkedList(456);
        TwoNumbersSum.DigitLinkedList sumList = util.add(one, two);
        Integer sum = util.getNumber(sumList);
        Assertions.assertEquals(690, sum);
    }

    @Test
    public void summation5() {
        TwoNumbersSum.Util util = new TwoNumbersSum.Util();
        TwoNumbersSum.DigitLinkedList one = util.getLinkedList(9);
        TwoNumbersSum.DigitLinkedList two = util.getLinkedList(1);
        TwoNumbersSum.DigitLinkedList sumList = util.add(one, two);
        Integer sum = util.getNumber(sumList);
        Assertions.assertEquals(10, sum);
    }

    @Test
    public void summation6() {
        TwoNumbersSum.Util util = new TwoNumbersSum.Util();
        TwoNumbersSum.DigitLinkedList one = util.getLinkedList(0);
        TwoNumbersSum.DigitLinkedList two = util.getLinkedList(1);
        TwoNumbersSum.DigitLinkedList sumList = util.add(one, two);
        Integer sum = util.getNumber(sumList);
        Assertions.assertEquals(1, sum);
    }

    @Test
    public void summation7() {
        TwoNumbersSum.Util util = new TwoNumbersSum.Util();
        TwoNumbersSum.DigitLinkedList one = util.getLinkedList(1);
        TwoNumbersSum.DigitLinkedList two = util.getLinkedList(20);
        TwoNumbersSum.DigitLinkedList sumList = util.add(one, two);
        Integer sum = util.getNumber(sumList);
        Assertions.assertEquals(21, sum);
    }

}
