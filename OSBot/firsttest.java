import org.osbot.rs07.api.filter.Filter;
import org.osbot.rs07.api.map.constants.Banks;
import org.osbot.rs07.api.model.Player;
import org.osbot.rs07.api.ui.Message;
import org.osbot.rs07.script.Script;

import org.osbot.rs07.script.ScriptManifest;

import java.util.List;

@ScriptManifest(name = "firsttest", author = "Chris", version = 1.0, info = "", logo = "")

public class firsttest extends Script {

    Player currentTarget;
    int targetResponse = 10;
    int responseWaitTime = 10;

    @Override
    public void onStart() {
        List<Player> players = getPlayers().getAll();

        // Print the name from the list....
        for(Player player : players) {
            log(player.getName());
        }
    }

    @Override
    public void onExit() {
        //Code here will execute after the script ends
    }

    @Override
    public int onLoop() {

        // check if target has responded
        if (targetResponse >= responseWaitTime){
            // if we waited for a minute with no response, find another player
            boolean closestPlayerExists = true;
            try {
                Player currentClosestPlayer = getClosestPlayer();
                log("Following player: " + currentClosestPlayer.getName());
                currentClosestPlayer.interact("Follow");
                keyboard.typeString("Hello, " + currentClosestPlayer.getName() + "! I am a friendly chat bot.");
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

    public void onMessage(Message m) {
        if (m.getType() == Message.MessageType.PLAYER){
            if(m.getUsername().equals(currentTarget.getName())){
                targetResponse = 0;
                log("TARGET SAID: " + m.getMessage());
            } else {
                log(m.getUsername() + " said: " + m.getMessage());
            }
        }
    }
}