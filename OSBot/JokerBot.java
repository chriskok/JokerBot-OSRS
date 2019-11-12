import org.osbot.rs07.api.filter.Filter;
import org.osbot.rs07.api.map.constants.Banks;
import org.osbot.rs07.api.model.Player;
import org.osbot.rs07.api.ui.Message;
import org.osbot.rs07.script.Script;

import org.osbot.rs07.script.ScriptManifest;

import java.io.*;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.List;
import java.util.Scanner;

@ScriptManifest(name = "JokerBot", author = "Chris", version = 1.0, info = "", logo = "")

public class JokerBot extends Script {

    Player currentTarget;
    int targetResponse = 60;
    int responseWaitTime = 60;
    boolean DEBUG = true;

    //get the localhost IP address, if server is running on some other IP, you need to use that
    InetAddress host;

    {
        try {
            host = InetAddress.getLocalHost();
        } catch (UnknownHostException e) {
            e.printStackTrace();
        }
    }

    Socket socket = null;
    PrintWriter out =  null;
    BufferedReader in = null;
    Scanner scanner = new Scanner(System.in);


    @Override
    public void onStart() {
        try {
            socket = new Socket(host.getHostName(), 9876);
            out = new PrintWriter(socket.getOutputStream(), true);
            in = new BufferedReader(new InputStreamReader(
                    socket.getInputStream()));
            BufferedReader stdIn = new BufferedReader(
                    new InputStreamReader(System.in));

        } catch (UnknownHostException e) {
            System.err.println("Unknown Host.");
            // System.exit(1);
        } catch (IOException e) {
            System.err.println("Couldn't get I/O for "
                    + "the connection.");
            //  System.exit(1);
        }

        List<Player> players = getPlayers().getAll();

        // Print the name from the list....
        for(Player player : players) {
            log(player.getName());
        }
    }

    @Override
    public void onExit() {
        //Code here will execute after the script ends
        try {
            out.close();
            in.close();
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    public int onLoop() {
        if (DEBUG) {log("resp timer: " + targetResponse);}
        // check if target has responded
        if (targetResponse >= responseWaitTime){
            // if we waited for a minute with no response, find another player
            boolean closestPlayerExists = true;
            try {
                Player currentClosestPlayer = getClosestPlayer();
                log("Following player: " + currentClosestPlayer.getName());
                currentClosestPlayer.interact("Follow");
                keyboard.typeString("Hello, " + currentClosestPlayer.getName() + "! I am a friendly chat bot. How are you?");
            }
            catch(Exception e) {
                closestPlayerExists = false;
                log("No player found. Walking to GE!");
            }

            // if there are no players in the area, walk to GE
            if (!closestPlayerExists){
                getWalking().webWalk(Banks.GRAND_EXCHANGE);
            }

            targetResponse = 0;
        } else {
            targetResponse += 1;
        }

        return 1000; //The amount of time in milliseconds before the loop starts over
    }

    public Player getClosestPlayer(){
        Player closestPlayer = getPlayers().closest(new Filter<Player>() {
            @Override
            public boolean match(Player p) {
                return p != null && !p.equals(myPlayer()) && !p.equals(currentTarget);
            }
        });

        currentTarget = closestPlayer;

        return closestPlayer;
    }

    public String sendMessage(String msg){
        try{
            out.print(msg);
            out.flush();
            String message = (String) in.readLine();
            log("Response: " + message);
            return message;

        } catch (UnknownHostException e) {
            log("Unknown Host.");
        } catch (IOException e) {
            log("Couldn't get I/O for "
                    + "the connection.");
        }

        return "failed";
    }

    public void onMessage(Message m) {
        if (m.getType() == Message.MessageType.PLAYER){
            if(m.getUsername().equals(currentTarget.getName())){
                targetResponse = 0;
                log("TARGET SAID: " + m.getMessage());

                if(m.getMessage().toLowerCase().contains("go away")){
                    targetResponse = responseWaitTime + 1;
                    keyboard.typeString("Goodbye, " + currentTarget.getName() + "!");
                } else {
                    String response = sendMessage(m.getMessage());
                    keyboard.typeString(response);
                }
            } else {
                log(m.getUsername() + " said: " + m.getMessage());
            }
        }
    }
}
