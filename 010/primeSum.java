class primeSum{

  public static void main(String[] args){
    long start = System.currentTimeMillis();
    long answer = primeSum();
		long finish = System.currentTimeMillis();
		System.out.println("The sum of all primes below two million is " + answer);
		System.out.println(finish-start + "ms");
	}


  private static long primeSum() {
    long total = 2;

    for (int i = 3 ; i <= 2000000 ; i += 2){
      for (int j = 3 ; j < i ; j += 2) {
          if (i % j == 0) {
            break;
          }
          else if (j*j > i) {
            total += i ;
            break;
          }
      }
      }
    return total;
    }
}
