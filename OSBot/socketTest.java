import java.io.*;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Scanner;

public class socketTest {
    public static void main(String[] args) throws UnknownHostException, IOException, ClassNotFoundException, InterruptedException{
        //get the localhost IP address, if server is running on some other IP, you need to use that
        InetAddress host = InetAddress.getLocalHost();
        Socket socket = null;
        ObjectOutputStream oos = null;
        ObjectInputStream ois = null;
        Scanner scanner = new Scanner(System.in);

        try {

            socket = new Socket(host.getHostName(), 9876);

            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

            BufferedReader in = new BufferedReader(new InputStreamReader(
                    socket.getInputStream()));

            BufferedReader stdIn = new BufferedReader(
                    new InputStreamReader(System.in));

            //read the server response message
//            ois = new ObjectInputStream(socket.getInputStream());


            String line = "";
            while(!line.equals("exit")) {
                line = scanner.nextLine();
                out.print(line);
                out.flush();
                String message = (String) in.readLine();
                System.out.println("Message: " + message);
            }

            out.close();
            in.close();
            socket.close();

        } catch (UnknownHostException e) {
            System.err.println("Unknown Host.");
            // System.exit(1);
        } catch (IOException e) {
            System.err.println("Couldn't get I/O for "
                    + "the connection.");
            //  System.exit(1);
        }
    }
}
