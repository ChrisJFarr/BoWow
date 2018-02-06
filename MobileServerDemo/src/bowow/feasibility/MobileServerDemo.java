package bowow.feasibility;


import static com.codename1.ui.CN.*;
import com.codename1.ui.Display;
import com.codename1.ui.Form;
import com.codename1.ui.Dialog;
import com.codename1.ui.Label;
import com.codename1.ui.plaf.UIManager;
import com.codename1.ui.util.Resources;
import com.codename1.io.Log;
import com.codename1.ui.Toolbar;
import java.io.IOException;
import com.codename1.ui.layouts.BoxLayout;

/**
 * This file was generated by <a href="https://www.codenameone.com/">Codename One</a> for the purpose 
 * of building native mobile applications using Java.
 */
public class MobileServerDemo {

    private Form current;
    private Resources theme;

    public void init(Object context) {
        theme = UIManager.initFirstTheme("/theme");

        // Enable Toolbar on all Forms by default
        Toolbar.setGlobalToolbar(true);

        // Pro only feature
        Log.bindCrashProtection(true);
    }
    
    public void start() {
        if(current != null){
            current.show();
            return;
        }
        Form hi = new Form("Hi World", BoxLayout.y());
        hi.add(new Label("Hi World"));
        hi.show();
    }

    public void stop() {
        current = getCurrentForm();
        if(current instanceof Dialog) {
            ((Dialog)current).dispose();
            current = getCurrentForm();
        }
    }
    
    public void destroy() {
    }

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.IOException;
import java.nio.ByteBuffer;
import java.util.Collections;
import java.util.HashSet;
import java.util.Set;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.websocket.OnClose;
import javax.websocket.OnMessage;
import javax.websocket.OnOpen;
import javax.websocket.Session;
import javax.websocket.server.ServerEndpoint;

    /**
     *
     * @author shannah
     */
    @ServerEndpoint("/chat")
    public class ChatDemoEndpoint {


        private static Set<Session> peers = Collections.synchronizedSet(new HashSet<Session>());
        @OnMessage
        public String onMessage(Session session, String message) {
            System.out.println(session.getUserProperties());
            if (!session.getUserProperties().containsKey("name")) {
                session.getUserProperties().put("name", message);
                return null;
            }
            for (Session peer: peers) {
                try {
                    peer.getBasicRemote().sendText(session.getUserProperties().get("name")+": "+message);
                    peer.getBasicRemote().sendBinary(ByteBuffer.wrap(new byte[]{1,2,3}));
                } catch (IOException ex) {
                    Logger.getLogger(ChatDemoEndpoint.class.getName()).log(Level.SEVERE, null, ex);
                }
            }
            return null;
        }

        @OnOpen
        public void onOpen(Session peer) {
            peers.add(peer);
        }

        @OnClose
        public void onClose(Session peer) {
            peers.remove(peer);
        }

    }


}