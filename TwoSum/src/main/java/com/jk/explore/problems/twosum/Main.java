package com.jk.explore.problems.twosum;

import static java.lang.String.format;
import static java.lang.System.out;

public class Main {

    public static void main(String[] args) {
        TwoSumProblem twoSumProblem = new TwoSumProblem();
        int[] myNumbers = {2, 7, 11, 5, 20, 30};
        int twoSum = 41;
        int[] indices = twoSumProblem.findIndices(myNumbers, twoSum);
        if(indices != null) {
            out.println(format("Indices are: {%d} & {%d}", indices[0], indices[1]));
        } else {
            out.println("Two Sum doesn't exist");
        }
    }
}