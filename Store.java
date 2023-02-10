import java.util.*;

class Store extends Corporate {

  private String gameName;
  int StoreBudget = 1000;
  String Color = "Red";
  String floor = "first floor";
  String storeName;

  public Store() {

  }

  public String store(String name) {
    return name = storeName;
  }

  public void store() {
    System.out.println("Welcome to " + storeName + "game Store");
  }

  public String getProductName() {
    return this.gameName;
  }

  public String setProductName(String newGame) {
    return gameName = newGame;
  }

  public int getStoreBudget() {
    return StoreBudget;
  }

  @Override
  public int cookTheBooks() {
    try (Scanner money = new Scanner(System.in)) {
        boolean quick = false;

        System.out.println("The current store budget is " + getStoreBudget());
        System.out.println("How much do you want to increase the store Budget by?");
        int flow = money.nextInt();
        int newStoreBudget = StoreBudget + flow;
        System.out.println("The Store budget has been increased by " + flow + " and is now " + newStoreBudget);
        System.out.println("Do you want to add more money or not [add / no]");
        while (!quick) {
          String answer = money.next();
          if (answer.equals("no")) {
            System.out.println("Good, watch out for the IRS!");
            return newStoreBudget;
          } else if (!answer.equals("add")) {
            System.out.println("Invalid must be add or no");
          }
        }
    }
    return 0;
  }

  @Override
  public void callStore() {
    System.out.println(
        "Welcome to Game Store, Business is going swell. We have recently remodeled and now the buidling is a bright "
            + Color);
  }

  public void buildingColor() {
    System.out.println("The Building color is currently: " + Color);
  }

  public void paintBuilding() {
    Scanner mew = new Scanner(System.in);
    boolean nice = false;
    do {
      System.out.println("What color would you like to Paint it?");
      String change = mew.next();
      Color = change;
      System.out.println("The building is now: " + change);
      System.out.println("Do you want to change the color or leave it the same [change / leave]");
      String answer = mew.next();
      switch (answer) {
        case "change":
          nice = false;
          break;
        case "leave":
          System.out.println("The building looks nice!");
          nice = true;
          mew.close();
          break;
        default:
          System.out.println("Not responsive");
      }
    } while (!nice);

  }

}
