package com.jk.explore.problems.add.two.numbers;

import java.util.LinkedList;

@FunctionalInterface
public interface NumberToLinkedListConverter {

    LinkedList<Integer> convert(int number);


}
