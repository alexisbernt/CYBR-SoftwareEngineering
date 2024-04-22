import java.io.File;
import java.util.*;
import static java.nio.file.StandardCopyOption.*;
import java.nio.file.Path;
import java.nio.file.Files;
import java.nio.file.Paths;

class Backup {

    public static void copyFile(Path inputFile){
        System.out.println("File to backup: " + inputFile + "\nPlease enter backup destination path below.");
        Path destFile = validateDestinationPath(inputFile.getFileName());
        try {
            Files.copy(inputFile, destFile);
            System.out.println("Success!\n");
        } catch(Exception e) {
            System.out.println("Error.\n" + e);
        }
    }

    public static Path validateDestinationPath(Path fileName){
        Scanner scanner = new Scanner(System.in);

        System.out.print("Please input a filepath: ");
        String filePathStr = (scanner.nextLine());
        Path destFilePath = null;

        File file = new File(filePathStr);
        if(file.isDirectory()){
            System.out.println("File location successfully located.");
            destFilePath = Paths.get(filePathStr + "/" + fileName.toString());
        }
        else {
            System.out.println("Uh oh! File location not found!\nYou inputted: " + destFilePath);
            validateDestinationPath(fileName);
        }
        return destFilePath;
    }

    public static Path validateBackupPath(){
        Scanner scanner = new Scanner(System.in);

        System.out.print("Please input a filepath: ");
        String filePathStr = (scanner.nextLine());;
        Path filePath = Paths.get(filePathStr);

        File file = new File(filePathStr);
        if(file.exists()){
            System.out.println("File location successfully located.");
        }
        else {
            System.out.println("Uh oh! File location not found!");
            validateBackupPath();
        }
        return filePath;
    }
}
