package andrei.com.chatboot1.adapter;

import android.support.annotation.NonNull;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;

import andrei.com.chatboot1.R;
import andrei.com.chatboot1.model.Atendimento;


public class Adapter extends RecyclerView.Adapter<Adapter.MyViewHolder> {

    private List<Atendimento> listaAtendimentos;

    public Adapter(List<Atendimento> listaAtendimentos) {
        this.listaAtendimentos = listaAtendimentos;
    }

    @NonNull
    @Override
    public MyViewHolder onCreateViewHolder(@NonNull ViewGroup viewGroup, int viewType) {
        View itemLista = LayoutInflater.from(viewGroup.getContext())
                .inflate(R.layout.mensagens, viewGroup, false);
        return new MyViewHolder(itemLista);
    }

    @Override
    public void onBindViewHolder(@NonNull MyViewHolder holder, int position) {
        Atendimento atendimento = this.listaAtendimentos.get(position);

        Date data = new Date();
        SimpleDateFormat formatador = new SimpleDateFormat("dd/MM/yyyy | HH:mm:ss");

        holder.assunto.setText(atendimento.getAnswer());
        holder.data.setText(formatador.format(data));
    }

    @Override
    public int getItemCount() {
        return listaAtendimentos.size();
    }

    public class MyViewHolder extends RecyclerView.ViewHolder{
        TextView assunto;
        TextView data;

        public MyViewHolder(@NonNull View itemView) {
            super(itemView);
            assunto = itemView.findViewById(R.id.textAssunto);
            data = itemView.findViewById(R.id.textData);
        }
    }
}
