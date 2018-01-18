class Main {

	public static void main(String[] args) {
		System.out.println(new Main().run());
	}

	public String run() {
		long num = 600851475143L;
	  int x = 2;
	  while (x*x <= num){
	    while (num % x == 0) {
	      num /= x;
	    }
	    x++;
	  }
	  if (num > 1) {
	    return Long.toString(num);
	  }else {
	    return Integer.toString(x);

	  }
	}
}
