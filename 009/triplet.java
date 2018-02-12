class triplet{

  public static void main(String[] args){
    long start = System.currentTimeMillis();
    int answer = findTriplet();
		long finish = System.currentTimeMillis();
		System.out.println("The pythagorean triplet product is " + answer);
		System.out.println(finish-start + "ms");
	}


  private static int findTriplet() {
    int product = 0;
    for (int a = 1; a < 500; a++) {
      for (int b = a + 1; b < 500; b++) {
        int c = 1000 - a - b;   //eliminates need for third loop
        if (a*a + b*b == c*c) {
          product = a * b * c;
          return product;
        }
      }
    }
    throw new AssertionError("Try again");
  }
}
