abstract class Base {
  final String level = "Beyonder";

  Base(){System.out.println("Base constructor");}

  abstract void klein();

  void moretti(){System.out.println("Moreitti");}
}

class Derived extends Base {
  Derived(){System.out.println("Derived constructor");}

  void klein(){System.out.println("Introducing klein as "+super.level);}
  void moretti(){System.out.println("Correct sirname is Moretti");}
}

public class tut_abstract {
  public static void main(String[] args) {
    Derived d1 = new Derived();
    d1.klein();
    System.out.println(d1.level+"'s powers are great.");
  }
}
