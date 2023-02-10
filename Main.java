import java.util.*;

class Main {
  public static void main(String[] args) {
    // There is are some scopes which can only be accessed by the parent/ manager.
    // This is a Game store, The manager and employee are the only two workers, for
    // items to be put on the shelf to sell, ask and employee to addProducts to the
    // shelf, as the manager. And if you want to buy from the store ask the Employee
    // to buy an Item from the store but only after it has been placed there.

     
    
    Employee Emp1 = new Employee("Wyatt");
    // As the manager now ask Wyatt to stock the shelfs
    Emp1.addProducts("Game1", 100);
    Emp1.addProducts("Best2", 150);
    Emp1.addProducts("WoW", 15);
    Emp1.addProducts("Hewman", 16);
    // Given three chances to interact with the employee

   // Emp1.speakToCustomer();
    Manager gM = new Manager("Derrick");
    // Asking the manager how well the store is doing today
 // gM.Introduce();
    // The manager speaks to you as the employee to answer for the performance
  // gM.performanceToday();
    // As the customer you have the choice on what to sell and how much you sell
    // that.
    gM.buyFrom();
    // Calling the corporate office
   gM.callStore();


   
    Store gameStore = new Store();
    // Changing aspects of the store
    // increasing the storebudget
   gameStore.cookTheBooks();
    // Asking what color the building is
    gameStore.buildingColor();
  // Changing the color of the building
    gameStore.paintBuilding();
    // Using the Corporate callstore checking up on the business
    gameStore.callStore();

    // The Goal is to make a store that is interactable with the employee to acheive
    // the ablity to buy items in the store. I think i achieved it

  }
}