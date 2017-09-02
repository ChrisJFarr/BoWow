package com.example.bowow.bowow;

/**
 * Created by Saba on 8/30/2017.
 */
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import java.util.HashMap;
import java.util.Map;

public class PostFragment extends Fragment {
    private EditText inputKey, inputValue, inputURL;
    private Button buttonSendData;
    RequestQueue queue;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.tab_post_fragment, container, false);
        inputKey = (EditText) view.findViewById(R.id.input_key);
        inputValue = (EditText) view.findViewById(R.id.input_value);
        inputURL = (EditText) view.findViewById(R.id.input_url);
        buttonSendData = (Button) view.findViewById(R.id.btn_send_data);
        queue = Volley.newRequestQueue(getActivity().getApplicationContext());
        buttonSendData.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                getJsonData(inputKey.getText().toString(), inputValue.getText().toString(), inputURL.getText().toString());
            }
        });
        return view;
    }

    private void getJsonData(final String pKey, final String pValue, String pUrl) {
        //if (pUrl.equals("")) {
            pUrl = "http://192.168.1.189/androidVolley.php";
       // }
        StringRequest postRequest = new StringRequest(Request.Method.POST, pUrl,
                new Response.Listener < String > () {
                    @Override
                    public void onResponse(String response) {
                        // response
                        Toast.makeText(getActivity(), response.toString(), Toast.LENGTH_SHORT).show();
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        // error
                        Toast.makeText(getActivity(), error.toString(), Toast.LENGTH_SHORT).show();
                    }
                }
        ) {
            @Override
            protected Map < String, String > getParams() {
                Map < String, String > params = new HashMap < String, String > ();
                params.put("key", pKey);
                params.put("value", pValue);

                return params;
            }
        };
        postRequest.setShouldCache(false);
        queue.add(postRequest);
    }
}