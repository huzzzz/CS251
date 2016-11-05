package com.example.bhramar.feeder07;

import okhttp3.OkHttpClient;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class ServiceGenerator {

    private static final String BASE_URL = "http://10.0.2.2:8007";

    private static OkHttpClient.Builder clientBuilder = new OkHttpClient.Builder();

    private static Retrofit.Builder retrofitBuilder = new Retrofit.Builder()
            .baseUrl(BASE_URL)
            .addConverterFactory(GsonConverterFactory.create());

    public static Retrofit retrofit;

    public static <S> S createService(Class<S> serviceClass){
        retrofit = retrofitBuilder.client(clientBuilder.build()).build();
        return retrofit.create(serviceClass);
    }
}

