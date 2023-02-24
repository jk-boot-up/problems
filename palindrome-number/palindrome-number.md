# Palindrome number
A palindromic number (also known as a numeral palindrome or a numeric palindrome) is a number 
(such as 12321) that remains the same when its digits are reversed.
## Extract digits
### Using Modulo Operator(%) and division operator / in Java
#### Example for extracting digits of a number one by one in Java 
    123 % 10 = 3; 123/10 = 12;
    12 % 10 = 2; 12/10 = 1;
    1 % 10 = 1; 1/10 = 0;

#### Algorithm
    Input for palindrome test: n

    Step 1: Find reversal of input number
    Step 2: Check if the reversed number equals to the input number n

        Step 1: Find reversed number for given number:

            originalNumber = n;
            if(n < 0) {
                return false;
            }
            int reversedNumber = 0;
            while(n > 0) {
                // n % 10 gives last digit of n
                reversedNumber = reversedNumber * 10 + (n % 10);
                // n / 10 gives left over number after extracting last digit from n
                n = n / 10;
            }
            return reversedNumber;

        Step 2: return reversedNumber ==  originalNumber;
### String approach
    Convert to string from number with Integer/Long API in Java
    OR
    Reverse it with string/char traversal in Java
## Github location

    https://github.com/jk-boot-up/problems.git
    Module: palindrome-number

### Prerequisites to run Java solution
    Java 8+
    Junit 5 - optional - for tests only
    Maven
    Any IDE

### How to run the Maven build

    cd problems/palindrome-number
    mvn clean install






