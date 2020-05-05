import java.io.*;
class check
{
	public static void main(String args[])
	{
	try
	{
		Runtime.getRuntime().exec("python");
	}
	catch(IOException e)
	{
		System.out.println("error of you");
	}
}}