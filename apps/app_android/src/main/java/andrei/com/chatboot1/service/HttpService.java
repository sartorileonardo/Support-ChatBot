package andrei.com.chatboot1.service;

import android.os.AsyncTask;

import com.google.gson.Gson;

import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.message.BasicNameValuePair;
import org.apache.http.util.EntityUtils;

import java.util.ArrayList;
import java.util.List;

import andrei.com.chatboot1.model.Atendimento;

public class HttpService extends AsyncTask<Void, Void, Atendimento> {

    private String pergunta;

    public HttpService(String pergunta) {
        this.pergunta = pergunta;
    }

    @Override
    protected Atendimento doInBackground(Void... voids) {
        HttpResponse httpresponse = null;
        String resposta = null;
        try {
            HttpClient httpclient = new DefaultHttpClient();
            HttpPost httppost = new HttpPost("http://dc.shoto.com.br:8089/ask");

            List<NameValuePair> nameValuePairs = new ArrayList<NameValuePair>();
            nameValuePairs.add(new BasicNameValuePair("user", "andrei"));
            nameValuePairs.add(new BasicNameValuePair("apikey", "432ref4824ijio4343233243243=="));
            nameValuePairs.add(new BasicNameValuePair("messageText", pergunta));

            httppost.setEntity(new UrlEncodedFormEntity(nameValuePairs));
            UrlEncodedFormEntity encodedFormEntity = new UrlEncodedFormEntity(nameValuePairs);
            httppost.setEntity(encodedFormEntity);
            httpresponse = httpclient.execute(httppost);
            resposta = EntityUtils.toString(httpresponse.getEntity());

        } catch (Exception e) {
            e.printStackTrace();
    }
        return new Gson().fromJson(resposta, Atendimento.class);
    }
}
