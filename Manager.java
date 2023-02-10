import java.util.*;

class Manager extends Store {

  String name;
  private int price;

  HashMap<String, Integer> Products = new HashMap<>();

  public Manager(){
    
  }

  public Manager(String name){
    this.name = name;
    System.out.println("Welcome to the store hope you find what game you're looking for the employee would be right with you");
  }
  
  
  public void Introduce() {
    System.out.println("hello im the manager " + name);
  }

  public int getPrice() {
    return price;
  }

  public int setPrice(int newPrice) {
   return price = newPrice;
 }

  public void addProducts(String Game, int price) {
    Products.put(Game, price);
  }

  public void removeProducts(String Game) {
    Products.remove(Game);
  }

  public void buyFrom() {
    super.getStoreBudget();
    boolean nice = false;
    do{
    System.out.println("You want to sell a game? Sure [Customer], How much is the game you're selling worth");
    Scanner x = new Scanner(System.in);
    int p = x.nextInt();
    if (p < StoreBudget) {
      StoreBudget -= p;
      System.out.println("You got yourself a deal");
    } else if (p > StoreBudget) {
      System.out.println("Wow! i can't afford it ");
    }
      System.out.println("Anything more you want to sell? (Y/N)");
      String answer = x.next();
      switch (answer){
        case "Y":
          nice = false;
          break;
        case "N":
          System.out.println("Thank you come again");
          nice = true;
          //x.close();
          break;
        default:
          System.out.println("not responsive");
      }
  } while(!nice);
  } 


  public void performanceToday() {
    try(Scanner fv = new Scanner(System.in);){
    System.out.println("Hey Wyatt[Employee] how many customers did we have today?");
    int f = fv.nextInt();
    System.out.println("how much did we sell as well?");
    int sale = fv.nextInt();
    try {
    } catch (ArithmeticException cc) {
      // cc.printStackTrace();
      System.out.println("Jerry- Wow no one in the store today huh.");
    }
    double compareMath = (float) sale / (float) f;
    System.out.println("We performed at " + compareMath + " % ");
  }
}

  @Override
  public void callStore() {
    System.out.println("Hi my name is Jerry from corporate, what do you need?");
  }

}
