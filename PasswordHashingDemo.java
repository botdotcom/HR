package com.hashing;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class PasswordHashingDemo {

	Map<String, String> DB = new HashMap<String, String>();
	public static final String SALT = "random-demo-text-as-salt";

	public PasswordHashingDemo() {
		//prevent direct instantiation
	}
	
	public static void main(String args[]) {
		PasswordHashingDemo demo = new PasswordHashingDemo();
		Scanner input = new Scanner(System.in);
		System.out.println("Enter username to signup: ");
		String signUpUsername = input.next();
		System.out.println("Enter password to signup: ");
		String signUpPassword = input.next();
		//sign up using a username-password pair
		demo.signup(signUpUsername, signUpPassword);
		System.out.println("User signup successful!");
		//login using a username-password pair
		System.out.println("Enter username to signin: ");
		String signInUsername = input.next();
		System.out.println("Enter password to signin: ");
		String signInPassword = input.next();
		// login should succeed or fail based on given username-password pair
		if (demo.login(signInUsername, signInPassword))
			System.out.println("User login successful!");
		else
			System.out.println("Invalid password!");
	}

	public void signup(String username, String password) {
		String saltedPassword = SALT + password;
		String hashedPassword = generateHash(saltedPassword);
		//System.out.println(hashedPassword);
		DB.put(username, hashedPassword);
	}

	public Boolean login(String username, String password) {
		Boolean isAuthenticated = false;
		//note: same salt used for signup and signin
		String saltedPassword = SALT + password;
		String hashedPassword = generateHash(saltedPassword);
		String storedPasswordHash = DB.get(username); //previously stored password
		if(hashedPassword.equals(storedPasswordHash) && DB.containsKey(username))
			isAuthenticated = true;
		else
			isAuthenticated = false;
		return isAuthenticated;
	}

	public static String generateHash(String input) {
		StringBuilder hash = new StringBuilder();
		try {
			//SHA-256 hashing algorithm
			MessageDigest sha = MessageDigest.getInstance("SHA-256");  
			//getBytes()=string into bytes 
			//digest()=completes the hash computation by performing final operations such as padding
			byte[] hashedBytes = sha.digest(input.getBytes());
			//hexadecimal digits
			char[] digits = { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
					'a', 'b', 'c', 'd', 'e', 'f' }; 
			//converts into desired hash
			for (int idx = 0; idx < hashedBytes.length; ++idx) {
				byte b = hashedBytes[idx];
				hash.append(digits[(b & 0xf0) >> 4]); //f0 = 0000 0000 1111 0000
				hash.append(digits[b & 0x0f]); //0f = 0000 0000 0000 1111
			}
		} 
		catch (NoSuchAlgorithmException e) {
			//if given algorithm doesn't exist
			System.out.println("No Such Algorithm Exception");
		}
		return hash.toString();
	}

}