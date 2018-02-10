class evenFibs {

	public static void main(String[] args) {
		System.out.println(new Main().run());
	}

	public String run() {
		int a = 1;
    		int b = 1;
    		int sum = 0;
		while (b <= 4000000) {
			if (b % 2 == 0)
				sum += b;
			int c = a + b;
      			a = b;
      			b = c;
		}
		return Integer.toString(sum);
	}
}
