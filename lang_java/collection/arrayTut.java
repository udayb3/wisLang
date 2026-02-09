class Student
{
  int rollno;
  String name;
  int marks;
}

public class arrayTut
{
  public static void main(String[] args) {
    int arr[][] = new int[3][];
    arr[0]= new int[3];
    arr[1] = new int[4];
    arr[2] = new int[5];
    for(int i=0;i<3;i++) {
      for(int j=0;j<arr[i].length;j++){
        arr[i][j] = (int)(Math.random()*100);
      }
    }

    for(int t1[]: arr) {
      for(int el: t1){
        System.out.println(el + " ");
      }
      System.out.println();
    }


  }

  public static void objectArray() {
    Student students[] = new Student[3];
    Student s1 = new Student();
    s1.rollno = 1;
    s1.name = "test1";
    s1.marks = 1;

    Student s2 = new Student();
    s2.rollno = 2;
    s2.name = "test2";
    s2.marks = 2;

    Student s3 = new Student();
    s3.rollno = 3;
    s3.name = "test3";
    s3.marks = 3;

    students[0] = s1;    
    students[1] = s2;
    students[2] = s3;

    for(Student stud : students) {
      System.out.println(stud.name);
    }

  }
}