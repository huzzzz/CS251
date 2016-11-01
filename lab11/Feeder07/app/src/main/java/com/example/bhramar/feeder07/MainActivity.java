package com.example.bhramar.feeder07;

import android.content.Intent;
import android.content.SharedPreferences;
import android.support.v4.app.FragmentTransaction;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import android.preference.PreferenceManager;
import android.widget.Toast;

import com.roomorama.caldroid.CaldroidFragment;

import java.util.Calendar;
import java.util.HashMap;

public class MainActivity extends AppCompatActivity {

    SessionManager session;
    Button LogoutButton;
    Button ExitButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        session = new SessionManager(getApplicationContext());

        CaldroidFragment caldroidFragment = new CaldroidFragment();
        Bundle args = new Bundle();
        Calendar cal = Calendar.getInstance();
        args.putInt(CaldroidFragment.MONTH, cal.get(Calendar.MONTH) + 1);
        args.putInt(CaldroidFragment.YEAR, cal.get(Calendar.YEAR));
        caldroidFragment.setArguments(args);

        FragmentTransaction t = getSupportFragmentManager().beginTransaction();
        t.replace(R.id.calendar1, caldroidFragment);
        t.commit();

        LogoutButton = (Button) findViewById(R.id.logoutButton);
        ExitButton = (Button) findViewById(R.id.exitButton);

        Toast.makeText(getApplicationContext(), "User Login Status: " + session.isLoggedIn(), Toast.LENGTH_LONG).show();
        session.checkLogin();

        HashMap<String, String> user = session.getUserDetails();

        LogoutButton.setOnClickListener(new View.OnClickListener(){
            public void onClick(View org0){
                session.logoutUser();
            }
        });

        ExitButton.setOnClickListener(new View.OnClickListener() {
            public void onClick(View arg0){
                Intent intent = new Intent(Intent.ACTION_MAIN);
                intent.addCategory(Intent.CATEGORY_HOME);
                intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                startActivity(intent);
            }
        });

    }
}
