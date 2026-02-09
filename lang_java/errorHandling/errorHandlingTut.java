public class errorHandlingTut
{
  public static void main(String args[]) {
    int i=0, j=0;
    try {
      j = 10/i;
    } catch(Exception e) {
      System.out.println("Issues with travelling");
    }
  }
}