class triangular {

  public static void main(String[] args) {
    long start = System.currentTimeMillis();
    int num = 1;
    int triangular = 0;

    while (true) {
      triangular += num;
      if (divisors(triangular) > 500) {
        break;
        }
        num++;
    }

    long finish = System.currentTimeMillis();
    System.out.println(triangular);
    System.out.println("--- " + (finish-start) + " ms ---");
  }

  public static int divisors(long num) {
    int divisors = 0;
    long number = num;

    for (int i = 1; i <= (int) Math.sqrt(number); i++) {
      if (num % i == 0) {
        divisors += 2;
        }
    }
    return divisors;
  }
}
