import java.awt.*;
import java.io.File;
import java.util.Scanner;
import java.awt.Desktop;

public class Main_wSecurity {
    public Main_wSecurity() {
    }
    public static void main(String[] var0) {
        // Scanner scanner is going to be how you take in the user's input (in terminal)
        Scanner scanner = new Scanner(System.in);
        boolean validInput = false; // default set user entry to invalid ... going to rerun until changed to true
        Integer var1 = null; // no valid value default set

        while (!validInput) {
            // take scanner in as a parameter
            var1 = showMenu(scanner);
            // check to see if variable is between 1 and 4 (a valid input)
            if (var1 != null && (var1 >= 1 && var1 <= 4)) {
                validInput = true;
                // otherwise continue to run that there has been no valid entry
            } else {
                System.out.println("Uh oh! Invalid input.");
                System.out.println(">>> Please enter a valid input.");
            }
        }

        Preset var3 = new Preset();
        if (var1 == 1) {
            System.out.println("\n\nWelcome to MANUAL SELECTION mode!\n____________________________________________\n");
            manualSelection();
            // use the logical OR operator to see if the entry is 1, 2, 3, 4
        } else if (var1 == 2 || var1 == 3 || var1 == 4) {
            System.out.println("selection: " + var1);
            var3.checkPreset();
        }
        // call runningCheck() to declare the status of what the user wants
        runningCheck();
    }

    public static Integer showMenu(Scanner scanner) { // make sure input taking is an int
        System.out.println("Enter a number (1, 2, 3, or 4): ");
        if (scanner.hasNextInt()) { // security to check if is integer
            return scanner.nextInt(); // nextInt() is a method of Java class
        } else {
            scanner.next(); // clear invalid input
            return null; // if program gets here ... not able to return a valid value so return nothing
        }
    }
    private static void runningCheck() {
        System.out.println("Success!\nWould you like to continue with another task or exit?\nEnter C to continue or E to exit:");
        Scanner var0 = new Scanner(System.in);
        String var1 = var0.nextLine();
        if (var1.toUpperCase().equals("C")) {
            main((String[])null);
        } else if (var1.toUpperCase().equals("E")) {
            System.out.println("\nStealthELF Backup Program exited.\nGoodbye!\n");
        } else {
            System.out.println(">>> Please enter a valid input.");
        }

    }

    public static int showMenu() {
        Scanner var0 = new Scanner(System.in);
        System.out.println("\n\nStealthELF Backup Software\n____________________________________________\n\nPlease make a selection below for what you would like to do first:\n\n\t(1) Manual Selection\n\t(2) Pick Preset\n\t(3) Create Preset\n\t(4) Delete Preset\n\nEnter menu number to select: ");

        try {
            String var1 = var0.nextLine().trim();
            Integer var2 = Integer.parseInt(var1);
            if (var2 > 0 && var2 < 5) {
                return Integer.parseInt(var1);
            }

            System.out.println("Please enter a valid input.");
        } catch (Exception var3) {
            System.out.println("Please enter a valid input.");
            showMenu();
        }

        return 1;
    }

    private static File validateFileLocation() {
        Scanner var0 = new Scanner(System.in);
        System.out.println("Please input a filepath: ");
        String var1 = var0.nextLine();
        File var2 = new File(var1);
        Desktop var3 = Desktop.getDesktop();
        if (var2.exists()) {
            System.out.println("File location successfully located.");

            try {
                var3.open(var2);
            } catch (Exception var5) {
                System.out.println(var5);
            }
        } else {
            System.out.println("Uh oh! File location not found!");
            validateFileLocation();
        }

        return var2;
    }

    static void manualSelection() {
        System.out.println("Please copy and paste the path to the directory you would like to backup below.\n____________________________________________\n");
        File var0 = validateFileLocation();
        Backup.copyFile(var0);
    }
}
