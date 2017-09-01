package com.example.bowow.bowow;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.content.Context;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    private View mContentView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mContentView = findViewById(R.id.button);

        // Set up the user interaction to manually show or hide the system UI.
        mContentView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                pingAction();
            }
        });

    }

    private void pingAction() {
        Context context = getApplicationContext();
        CharSequence text = "Hello toast!";
        int duration = Toast.LENGTH_SHORT;

        Toast toast = Toast.makeText(context, text, duration);
        toast.show();
    }
}
