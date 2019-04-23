package andrei.com.chatboot1.activity;

import android.app.AlertDialog;
import android.app.Dialog;
import android.content.Context;
import android.content.DialogInterface;
import android.support.design.widget.TextInputLayout;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.support.v7.widget.Toolbar;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.List;

import andrei.com.chatboot1.R;
import andrei.com.chatboot1.adapter.Adapter;
import andrei.com.chatboot1.model.Atendimento;
import andrei.com.chatboot1.service.HttpService;

public class MainActivity extends AppCompatActivity {

    private TextView campoMensagem;
    private Button btnEnviar;
    private Toolbar toolbar;
    private RecyclerView recyclerView;
    private List<Atendimento> listaAtendimentos = new ArrayList<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        recyclerView = findViewById(R.id.recyclerAtendimento);
        btnEnviar = findViewById(R.id.btEnviar);
        toolbar = findViewById(R.id.toolbar);
        campoMensagem = findViewById(R.id.campoMensagem);

        TextInputLayout textInputLayout = new TextInputLayout(this);
        final EditText input = new EditText(this);
        //textInputLayout.setHint("Nome");
        textInputLayout.addView(input);

        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setTitle("Olá!");
        builder.setMessage("Para melhorar nossa qualidade de resposta, você pode identificar-se inserindo seu nome");
        builder.setView(textInputLayout);

        builder.setPositiveButton("Quero me identificar", new DialogInterface.OnClickListener() {
            public void onClick(DialogInterface dialog, int whichButton) {
                String usuario = input.getText().toString();
                Toast.makeText(getApplicationContext(), "Bem vindo " + usuario, Toast.LENGTH_LONG).show();
            }});
        builder.setNegativeButton("Não quero me identificar", new DialogInterface.OnClickListener() {
            public void onClick(DialogInterface dialog, int whichButton) {
            }});
        builder.show();

        setSupportActionBar(toolbar);
        btnEnviar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                try {
                    String user = input.getText().toString();
                    Atendimento atendimento = new HttpService(user != null ? user : "andrei", campoMensagem.getText().toString()).execute().get();

                    //Salva pergunta
                    Atendimento pergunta = new Atendimento();
                    pergunta.setAnswer(campoMensagem.getText().toString());

                    listaAtendimentos.add(pergunta);
                    listaAtendimentos.add(atendimento);

                    //Configurar adapter
                    Adapter adapter = new Adapter(listaAtendimentos);

                    //Configurar recycler view
                    RecyclerView.LayoutManager layoutManager = new LinearLayoutManager(getApplicationContext());
                    recyclerView.setLayoutManager(layoutManager);
                    recyclerView.setHasFixedSize(true);
                    recyclerView.setAdapter(adapter);

                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });
    }
}
