
public class anyaSpy {
	
	
    public boolean canFastAttack(boolean knightIsAwake) {
          if(knightIsAwake == true){
             return false;
          } else{
             return true;
          }
    }
    
 public boolean canSpy(boolean knightIsAwake, boolean archerIsAwake, boolean prisonerIsAwake) {
        if(knightIsAwake || prisonerIsAwake || archerIsAwake == true){
        	  return true;
           } else {
        	return false;
        }
        }
    public boolean canSignalPrisoner(boolean archerIsAwake, boolean prisonerIsAwake) {
       if(archerIsAwake == false && prisonerIsAwake == true) {
    	   return true;	   
    } else { return false;
    } 
    }
    
    public boolean canFreePrisoner(boolean knightIsAwake, boolean archerIsAwake, boolean prisonerIsAwake, boolean petDogIsPresent) {
    	 if(petDogIsPresent == true && archerIsAwake == false){return true;} 
    	 else if(prisonerIsAwake == true && archerIsAwake == false && knightIsAwake == false){ return true; } 
    	 else{return false;}                 
        }


    

	public static void main(String [] args) {
 
    	anyaSpy melissa = new anyaSpy();
    	System.out.println(melissa.canFastAttack(true));
    	System.out.println(melissa.canFreePrisoner(false, false, false, false));
    	System.out.println(melissa.canSignalPrisoner(true, false));
    	System.out.println(melissa.canSpy(false, false, false));
}

}


