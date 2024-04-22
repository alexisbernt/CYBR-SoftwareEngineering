import java.io.File;
import java.util.*;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.FileWriter;
import java.text.SimpleDateFormat;
import java.nio.file.Paths;

class Preset {

    public static void main(String[] args){
        System.out.println("\nIn preset class.\n");
    }

    public List<List<String>> showPresets() {
        File presetfile = new File("Code/stealthELFstore.csv");
        List<List<String>> presetsArray = new ArrayList<>();
        try{
            Scanner readFile = new Scanner(presetfile);
            readFile.nextLine();
            System.out.println("\nAVAILABLE PRESETS:\nFormat: [Preset name, file path, last backup date]\n"+ //
                                "__________________________________\n");
            Integer acc = 0;
            while(readFile.hasNextLine()) {
                acc++;
                presetsArray.add(getRow(acc + ", " + readFile.nextLine()));
            }
            for(List<String> s : presetsArray){
                System.out.println(s);
            }
            System.out.println("\n__________________________________\n\n");
            
        } catch (FileNotFoundException e) {
            System.out.println("FILE ERROR.\nUnable to find preset records.");
        }
        return presetsArray;
    }

    private List<String> getRow(String row) {
        List<String> rowContents = new ArrayList<String>();
        try{
            Scanner scanRow = new Scanner(row);
            scanRow.useDelimiter(",");
            while(scanRow.hasNext()) {
                rowContents.add(scanRow.next());
            }
 //           scanRow.close();
        } catch(Exception e) {
            System.out.println(e);
        }
        
        return rowContents;
    }

    public List<String> checkPreset(String presetNum, List<List<String>> presetsArray){
        List<String> found = null;
        System.out.println("Checking for preset.\n");
        for(int i = 0; i < presetsArray.size(); i++){
            if(presetsArray.get(i).get(0).equals(presetNum)) {
                found = presetsArray.get(i);
                break;
            }
        }
        return found;
    }

    public void newPreset(){
        try{
            FileWriter presetWriter = new FileWriter("Code/stealthELFstore.csv", true);
            Scanner scanName = new Scanner(System.in);
            System.out.print("New Preset Name: ");
            String newPresetName = scanName.nextLine();
            String timeStamp = new SimpleDateFormat("MM-dd-yyyy HH:mm:ss").format(Calendar.getInstance().getTime());
            presetWriter.write(newPresetName + "," + Backup.validateBackupPath() + "," + timeStamp + "\n");
            presetWriter.close();
        } catch (IOException e) {
            System.out.println("FILE ERROR.");
        }
    }

    public void loadPreset(List<String> preset){
        System.out.println("Loading Preset...");
        Backup.copyFile(Paths.get(preset.get(2)));

    }

    public void deletePreset(){
        List<List<String>> presetArray = showPresets();
        System.out.println("Enter preset number to delete: ");
        Scanner presetScan = new Scanner(System.in);
        String presetNum = presetScan.nextLine();
        List<String> foundPreset = null;
        do {
            foundPreset = checkPreset(presetNum, presetArray);
            if(foundPreset == null)
                System.out.println("Invalid Selection! Please try again.");
        }
        while(foundPreset == null);
        
        System.out.println("Deleting preset...");
        presetArray.remove(foundPreset);

        try{
            FileWriter presetWriter = new FileWriter("Code/stealthELFstore.csv");
            presetWriter.write("presetName,filePaths,date\n");
            for(int i = 0; i < presetArray.size(); i++){
                String name = presetArray.get(i).get(1).trim();
                String path = presetArray.get(i).get(2).trim();
                String lastBackup = presetArray.get(i).get(3).trim();
                presetWriter.write(name + "," + path + "," + lastBackup + "\n");
            }
            presetWriter.close();
        } catch (IOException e) {
            System.out.println("FILE ERROR.");
        }

    }

    public static File validatePresetLocation(){
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
            validatePresetLocation();
        }
        return file;
    }
}
