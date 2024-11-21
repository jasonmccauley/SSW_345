public class MyPizzaApp {
    public static void main(String[] args){
        if(args.length != 2){
            System.out.println("Please enter the following: MyPizzaApp <franchise> <pizzaKind>");
            System.exit(1);
        }

        String franchise = args[0];
        String pizzaKind = args[1];
        PizzaStore store = null;
        if(franchise.equals("NYPizzaStore")){
            store = new NYPizzaStore();
        }
        else if (franchise.equals("ChicagoPizzaStore")){
            store = new ChicagoPizzaStore();
        }
        else{
            System.out.println("Unknown franchise: " + franchise);
            System.exit(1);
        }

        Pizza pizza = store.orderPizza(pizzaKind);
        System.out.println("\nHere's your pizza:\n" + pizza.toString());
    }
}
