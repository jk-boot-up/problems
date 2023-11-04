package com.jk.explore.problems.median.sorted.arrays;

public class MedianOfTwoSortedArraysBinarySearchImpl implements MedianOfTwoSortedArrays {
    @Override
    public double median(int[] sortedArrayA, int[] sortedArrayB) {
        if(isNullOrEmpty(sortedArrayA) || isNullOrEmpty(sortedArrayB)) {
            throw new IllegalArgumentException("sortedArrayA or sortedArrayB cannot be null or empty.");
        }
        int n = sortedArrayA.length;
        int m = sortedArrayB.length;
        if(n > m) {
            return median(sortedArrayB, sortedArrayA);
        }
        int start = 0;
        int end = n;
        int realMidInMergedArray = (m + n + 1) / 2;
        while (start <= end) {
            int mid = (start + end) / 2;
            int leftASize = mid;
            int leftBSize = realMidInMergedArray - mid;
            int leftA = leftASize > 0 ? sortedArrayA[leftASize - 1] : Integer.MIN_VALUE;
            int leftB = leftBSize > 0 ? sortedArrayB[leftBSize -1] : Integer.MIN_VALUE;
            int rightA = leftASize < n ? sortedArrayA[leftASize] : Integer.MAX_VALUE;
            int rightB = leftBSize < m ? sortedArrayB[leftBSize] : Integer.MAX_VALUE;
            if(leftA <= rightB && leftB <= rightA) {
                if((m + n) % 2 == 0) {
                    return (Math.max(leftA, leftB) + Math.min(rightA, rightB))/2;
                } else {
                    return Math.max(leftA, leftB);
                }
            } else if (leftA > rightB) {
                end = mid -1;
            } else {
                start = mid + 1;
            }
        }
        return 0;
    }

    protected boolean isNullOrEmpty(int [] array) {
        return array == null || array.length == 0;
    }

}
