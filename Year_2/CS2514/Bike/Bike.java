public class Bike {
    private Brakes brakes;
    private Saddle saddle;
    private Wheels wheels;
    private Handlebar handlebar;


    void printComponents(){
        System.out.println("components here.");
    }

    public Bike ( ){
        this.brakes = new Brakes();
        this.wheels = new Wheels();
        this.saddle = new Saddle();
        this.handlebar = new Handlebar();
    }
}

class Brakes {

}

class Wheels {

}

class Saddle {

}

class Handlebar {

}