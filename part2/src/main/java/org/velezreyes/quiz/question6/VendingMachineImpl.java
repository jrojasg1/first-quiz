package org.velezreyes.quiz.question6;

public class VendingMachineImpl {

  public static VendingMachine getInstance() {
    // Fix me!
   
    
    VendingMachine vendingMachine = new VendingMachine() {
        int quarter = 0;
        @Override
        public void insertQuarter() {
            quarter += 25;
        }

        @Override
        public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
            
            Drink drink = new Drink(){
                
                @Override
                public String getName() {
                    return name;
                }

                @Override
                public boolean isFizzy() {
                   String _nameLower = name.toLowerCase();
                   return _nameLower.contains("cola");
                }
            };
            
            if ( !(drink.getName().equalsIgnoreCase("ScottCola")  || drink.getName().equalsIgnoreCase("KarenTea") ) ) {
                throw new UnknownDrinkException();
            }
            //not money
            if (quarter==0) {
                throw new NotEnoughMoneyException();
            }
            //NotEnoughMoneyException drink costs more than 75 cents
            if (quarter < 75 && (drink.getName().equalsIgnoreCase("ScottCola") || drink.getName().equalsIgnoreCase("KarenTea"))) {
                throw new NotEnoughMoneyException();
            }
            //NotEnoughMoneyException drink at least 75 cents
            if (quarter == 75 && drink.getName().equalsIgnoreCase("KarenTea")) {
                throw new NotEnoughMoneyException();
            }

            quarter -= 75;

            
            return drink;
        }
    };
    return vendingMachine;
  }
  
}
