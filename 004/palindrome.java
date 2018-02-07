class palindrome {

	private static int findPalindrome()
	{
		int palindrome = 0;
		for (int i = 999; i >= 900; i--)
		{
			for (int j = 999; j >= 900; j--)
			{
				palindrome = i * j;
				String palString = Integer.toString(palindrome);
				String revPalString = new StringBuffer(palString).reverse().toString();
				if (palString.equals(revPalString))
					return palindrome;
			}
		}
		return 0;
	}

	public static void main(String[] args)
	{
		long start = System.currentTimeMillis();
		int maxPalindrome = findPalindrome();
		long finish = System.currentTimeMillis();
		System.out.println(maxPalindrome);
		System.out.println(finish-start + "ms");
	}
}
