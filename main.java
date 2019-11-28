import java.util.Scanner;
import java.util.Random;

class ingame extends Player{
	private int choose;
	private double itemstat;

	public ingame(double r, double c, double s, double o) {
		super(r, c, s, o);
		Roamingstat = r;
		Csstat = c;
		Skillstat = s;
		Objectstat = o;
		Itemstat = 0;
	}

	public double getItemstat() {
		return Itemstat;
	}
}

class Player{
	protected double Roamingstat;
	protected double Csstat;
	protected double Skillstat;
	protected double Objectstat;

	public Player(double r, double c, double s, double o) {
		Roamingstat = r;
		Csstat = c;
		Skillstat = s;
		Objectstat = o;
	}
}
class Main {
    public static void main(String[] args) {
            System.out.println("hello, world!");
	        }
}
