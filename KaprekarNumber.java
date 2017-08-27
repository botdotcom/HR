/*
 Consider an n-digit number k. Find if it is a Kaprekar number. 
 A Kaprekar number is a number whose square when divided into two parts 
 and such that sum of parts is equal to the original number 
 and none of the parts has value 0.
 */
package after;

import java.util.*;

public class KaprekarNumber {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("Enter a number: ");
		int checkNum = input.nextInt();
		boolean isKapre = isKaprekar(checkNum);
		if(isKapre)
			System.out.println("A Kaprekar number");
		else
			System.out.println("Not a Kaprekar number");
	}

	private static boolean isKaprekar(int checkNum) {
		if(checkNum == 1)
			return true;
		//square of number in question
		int sqNum = checkNum * checkNum;
		int copySqNum = sqNum, countDig = 0;
		//count number of digits
		while(copySqNum != 0) {
			countDig++;
			copySqNum /= 10;
		}
		//divide the number into 2 parts
		for(int rDig = 1; rDig < countDig; rDig++) {
			int part = (int) Math.pow(10, rDig);
			if(part == checkNum)
				continue; //for 10, 100, 1000...
			int sum = (sqNum / part) + (sqNum % part); //sum of both parts
			if(sum == checkNum)
				return true;
		}
		return false;
	}
}
