import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
// import java.util.scanner;

public class inputTut
{
  public static void main(String args[]) throws IOException {
    BufferedReader br = null;
    try {
      br = new BufferedReader(new InputStreamReader(System.in));
      int val = Integer.parseInt(br.readLine());
      System.out.println("Value is"+val);
    } catch(Exception e) {
      System.out.println("Issues with travelling");
    } finally {
      br.close();
    }
  }

  // // input using scanner
  // Scanner sc = new Scanenr(System.in);
  // int val = sc.nextInt();
}
