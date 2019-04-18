package andrei.com.chatboot1.activity;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

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

        setSupportActionBar(toolbar);
        btnEnviar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                try {
                    Atendimento atendimento = new HttpService(campoMensagem.getText().toString()).execute().get();

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
