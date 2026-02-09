class Parent
{
  Parent() {
    System.out.println("Inside the parent class");
  }

  public void show(String value) {
    System.out.println(value);
  }
}

class Child extends Parent
{
  Child() {
    System.out.println("Inside the child class");
  }
}

class classTut
{
  public static void main(String args[]) {
    Child child = new Child();
  }
}