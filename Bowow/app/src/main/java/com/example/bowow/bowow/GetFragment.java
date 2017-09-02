package com.example.bowow.bowow;

/**
 * Created by Saba on 8/30/2017.
 */
import android.content.Context;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.view.inputmethod.InputMethodManager;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONObject;

public class GetFragment extends Fragment {
    private EditText inputUrl;
    private Button buttonGetData;
    private TextView jsonText;
    private RequestQueue queue;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.tab_get_fragment, container, false);
        inputUrl = (EditText) view.findViewById(R.id.input_url);
        buttonGetData = (Button) view.findViewById(R.id.btn_send_data);
        jsonText = (TextView) view.findViewById(R.id.jsonTextView);
        queue = Volley.newRequestQueue(getActivity().getApplicationContext());
        buttonGetData.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                getJsonData(inputUrl.getText().toString());
            }

        });
        return view;
    }

    private void getJsonData(String pUrl) {
        View view = this.getActivity().getCurrentFocus();
        if (view != null) {
            InputMethodManager imm = (InputMethodManager) getActivity().getSystemService(Context.INPUT_METHOD_SERVICE);
            imm.hideSoftInputFromWindow(view.getWindowToken(), 0);
        }
        /*if (pUrl.equals("")) {
            pUrl = "http://192.168.1.189/request.txt";
        }*/
        pUrl = "http://192.168.1.189/request.json";
        JsonObjectRequest getRequest = new JsonObjectRequest(Request.Method.GET, pUrl, null,
                new Response.Listener < JSONObject > () {
                    @Override
                    public void onResponse(JSONObject response) {
                        // display response
                        jsonText.setText(response.toString());
                        Toast.makeText(getActivity().getApplicationContext()
                                     , response.toString()
                                     , Toast.LENGTH_SHORT).show();
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        jsonText.setText(error.toString());
                    }
                }
        );

        // add it to the RequestQueue
        getRequest.setShouldCache(false);
        queue.add(getRequest);
    }
}