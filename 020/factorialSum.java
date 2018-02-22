import java.math.BigInteger;

class factorialSum {
  public static void main(String[] args) {
    System.out.println(digSum(100));
  }

  private static String digSum(int num) {
    String factorial = factorial(num);
    int sum = 0;

    for (int i = 0; i < factorial.length(); i++) {
      sum += factorial.charAt(i) - '0';
    }
    return Integer.toString(sum);
  }

  /*
   *The result of 100! is too long, even formtype Long int. BigInteger
   *must be used
   */

  private static String factorial(int num) {
    BigInteger result = new BigInteger("1");
    String resultString = "";
    for(int i = 1; i < num ; i++){
        result = result.multiply(BigInteger.valueOf(i));
    }
    resultString = result.toString();
    return resultString;
  }
}
