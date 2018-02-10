class sumSquare {

	public static int findDifference() {
		int squareSum = 0;
    int sumSquare = 0;

    for (int i = 1; i < 101; i++) {
      squareSum += i;
      sumSquare += i*i;
    }
    squareSum *= squareSum;
    int difference = squareSum - sumSquare;
    return difference;
	}

	public static void main(String[] args)
	{
		long start = System.currentTimeMillis();
		int answer = findDifference();
		long finish = System.currentTimeMillis();
		System.out.println(findDifference());
		System.out.println(finish-start + "ms");
	}
}
