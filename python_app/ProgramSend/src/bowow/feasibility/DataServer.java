package bowow.feasibility;

/**
 * A TCP server that runs on port 9090.  When a client connects, it
 * sends the client the current date and time, then closes the
 * connection with that client.  Arguably just about the simplest
 * server you can write.
 */

import java.io.IOException;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Date;

// TODO next steps, build mobile app to connect to computer app
// Resource http://cs.lmu.edu/~ray/notes/javanetexamples/

public class DataServer {

        public static void main(String[] args) throws IOException {
        ServerSocket listener = new ServerSocket(9090);
        try {
            while (true) {
                Socket socket = listener.accept();
                try {
                    // TODO research other types of io object other than PrintWriter for bytes, etc
                    PrintWriter out =
                            new PrintWriter(socket.getOutputStream(), true);
                    out.println("I love you Shannon :) ");
                } finally {
                    socket.close();
                }
            }
        }
        finally {
            listener.close();
        }
    }
}
