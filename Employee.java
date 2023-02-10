import java.util.NoSuchElementException;
import java.util.Scanner;

class Employee extends Manager {

  public Employee() {

  }

  public Employee(String name) {
    this.name = name;
    // System.out.println("Enter an Integer to enter the store[1]");
    System.out.println("Welcome to mario's Game store, Hello my name is[Employee] " + name + " How may i help you?");
  }

  public void speakToCustomer() {
    boolean quit = false;
    Scanner sc = new Scanner(System.in);

    do {
      System.out.println("What may i assist you with?");
      System.out.println(
          "[1] Displays items in store, [2] Sell to Store, [3] Buys Items, [4] Calls the manager, [5] Leave Store");
    } while (quit);
    while (!quit) {
      Scanner mew = new Scanner(System.in);
        System.out.println("Anything else?[Refering to the main employee options] ");
          int response = mew.nextInt();
          switch (response) {
            case 1:
              displayItems();
              break;
            case 2:
              buyCustomerItem();
              break;
            case 3:
              getItem();
              break;
            case 4:
              getManager();
              break;
            case 5:
        System.out.println("Thank you come again!");
              quit = true;
              // mew.close();
              break;
            default:
              System.out.println("None of the options were selected");
          }
    }
    }



  public void getManager() {
    Manager myBoss = new Manager();
    myBoss.Introduce();
  }

  public void displayItems() {
    for (int gh = 0; gh < 1; gh++) {
      String key = Products.toString();
      System.out.println("We have " + key + "in store");
    }
  }

  // Looping iteration void method
  public void getItem() {
    System.out.println("Select what item you would like");
    System.out.println(Products.toString());
   Scanner mew = new Scanner(System.in);
        System.out.println(
            "Enter the item name:   Disclaimer: for items in the back shelf you will be asked multiple times. Also all Sales are final.");
        String input = mew.nextLine();
        try {
          if (Products.containsKey(input)) {
            System.out.println("Here you go! Thank you for your purchase of " + input + " have an nice day!");
            removeProducts(input);
          }
        } catch (NoSuchElementException mom) {
        }
    }


  public void addItem() {
    Scanner net = new Scanner(System.in);
        boolean quit = false;
        do {
          System.out.println("Would you like to add product? (Y/N)");
          String answer = net.next();
          switch (answer) {
            case "Y":
              System.out.println("Whats the name of the game *In camelText*");
              String game = net.next();
              System.out.println("How much is the game");
              int price = net.nextInt();
              super.addProducts(game, price);
              break;
            case "N":
              quit = true;
              break;
            default:
              System.out.println("not responsive");
              break;

          }
        } while (!quit);
    }


  public void buyCustomerItem() {
    Scanner net = new Scanner(System.in); 
        boolean quit = false;

        while (quit == false) {
          System.out.println("Would you like to sell a game to us (Y/N)");
          String answer = net.next();
          if (answer.equals("Y")) {
            System.out.println("What game is it");
            String userSale = net.next();
            // Since its supering from the managers method, the managers method is also in a
            // loop so it asks if the user would like to sell after "You got yourself a
            // deal", then when out it thanks the user for the sale but does not close the
            // loop it then prompts the buyCustomer Items loop to ask if the user would like
            // to sell again, Simply saying N would take you out of the method and into the
            // main employee loop
            super.buyFrom();
            System.out.println("Thank you for selling us " + userSale);
          } else if (answer.equals("N")) {
            quit = true;
          }
        }
    }
  }

