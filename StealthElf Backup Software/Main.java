import java.io.File;
import java.util.Scanner;
import java.nio.file.Path;
import java.util.*;

public class Main {

    public static void main(String[] args){
        Integer userSelection = showMenu();
        Scanner scanner = new Scanner(System.in);
        Preset preset = new Preset();

        // Take actions based on validated user input
        if(userSelection == 1){ // MANUAL SELECTION
            System.out.println("\n\nWelcome to MANUAL SELECTION mode!\n____________________________________________\n");
            manualSelection();
        } 
        else if (userSelection == 2){// PICK PRESET
            System.out.println("\n____________________________________________\n\n\t\tPICK PRESET\n____________________________________________\n");
            List<List<String>> presetsArray = preset.showPresets();
            System.out.print("Enter Preset Number: ");
            List<String> foundPreset = null;
            do {
                foundPreset = preset.checkPreset(scanner.nextLine(), presetsArray);
                if(foundPreset == null)
                    System.out.println("Invalid Selection! Please try again.");
            }
            while(foundPreset == null);
            preset.loadPreset(foundPreset);
        }
        else if(userSelection == 3){ // CREATE PRESET
                preset.newPreset();;
        } 
        else if(userSelection == 4){ // DELETE PRESET
            preset.deletePreset();
        }
        else {
            System.out.println("Invalid input.");
            main(null);
        }
        runningCheck();
    }

    private static void runningCheck() {
        System.out.print("Would you like to continue with another task or exit?\n" + //
                        "Enter C to continue or E to exit:");
        Scanner scanner = new Scanner(System.in);
        String running = scanner.nextLine();
        if(running.toUpperCase().equals("C")) {
            main(null);
        } else {
            if(running.toUpperCase().equals("E")) {
                System.out.println("\nStealthELF Backup Program exited.\nGoodbye!\n");
            } else {
                System.out.println(">>> Please enter a valid input.");
                runningCheck();
            }
        }
    }

    public static int showMenu(){ // Returns the numerical selection of the user
        Scanner scanner = new Scanner(System.in);
        System.out.print("\n\nStealthELF Backup Software\n____________________________________________\n\n" + //
                        "Please make a selection below for what you would like to do:\n\n" + //
                        "\t(1) Manual Selection\n\t(2) Pick Preset\n\t(3) Create Preset\n\t(4) Delete Preset\n" + //
                        "\nEnter menu number to select: ");

        try {
            String menuInput = scanner.nextLine().trim();
            Integer menuInputNum = Integer.parseInt(menuInput);
            if(menuInputNum > 0 && menuInputNum < 5){
                return Integer.parseInt(menuInput);
            } 
            else {
                System.out.println("Please enter a valid input.");
                showMenu();
            }
        }
        catch (Exception e) {
            System.out.println("Please enter a valid input.");
            showMenu();
        }
        return 1;
    }

    public static File validateFileLocation(){
        Scanner scanner = new Scanner(System.in);

        System.out.print("Please input a filepath: ");
        String filePath = scanner.nextLine();

        File file = new File(filePath);
        if(file.exists()){
            System.out.println("File location successfully located.");
            try{
            } catch (Exception e) {
                System.out.println(e);
            }
        }
        else {
            System.out.println("Uh oh! File location not found!");
            validateFileLocation();
        }
        return file;
    }

    static void manualSelection(){
        System.out.println("Please copy and paste the path to the file you would like to backup below.\n" + //
        "____________________________________________\n");
        Path selectedFile = Backup.validateBackupPath();
        Backup.copyFile(selectedFile);
        
        System.out.println("Would you like to backup another path?\nEnter y for yes or n for no:");
        Scanner scanner = new Scanner(System.in);
        String running = scanner.nextLine();
        if(running.toUpperCase().equals("y")) {
            manualSelection();
        } else {
            if(running.toUpperCase().equals("n")) {
                System.out.println("Manual selection complete.\n");
                runningCheck();
            } else {
                runningCheck();
            }
        }
    }
}
