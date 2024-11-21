public class MushroomDecorator extends ToppingDecorator {
    public MushroomDecorator(Pizza pizza){
        super(pizza);
    }

    @Override
    public String getDescription(){
        return pizza.getDescription() + ", mushrooms";
    }

    @Override
    public double getCost(){
        return pizza.getCost() + 1.25;
    }
}
