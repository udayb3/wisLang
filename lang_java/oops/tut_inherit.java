
class Point2D {
  int x,y;
  Point2D(int x, int y){this.x = x; this.y=y;}
  void display(){System.out.println("x="+x+"y="+y);}
}

class Point3D extends Point2D {
  int z;
  Point3D(int x, int y, int z){ super(x, y); this.z = z; }
  void display(){System.out.println("x="+x+"y="+y+"z="+z);}
}

public class tut_inherit {
  public static void main(String[] args){
    Point2D p1 = new Point2D(1, 2);
    Point3D p2 = new Point3D(3, 4, 5);

    p1.display();
    p2.display();

    // Dynamic Method dispatching
    Point2D p3 = new Point2D(4, 5); // example of up casting
    p3.display();    
  }  
}
