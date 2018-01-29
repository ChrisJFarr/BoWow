package bowow.feasibility;

import java.io.IOException;

/*

Application to send a communication through a serial port
to be received by a sister application.

 */




public class Main {

    public static void main(String[] args) {

        // Prompt user for input
        // Send input to sister application
        // Loop
        // Wait for q from user to break

        try {
            // Testing DataServer
            DataServer server = new DataServer();
            server.main(args);
        } catch(IOException e) {
            System.out.println("Failure");
        }
    }
}
