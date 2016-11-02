package com.example.bhramar.feeder07;

        import retrofit2.Call;
        import retrofit2.http.Field;
        import retrofit2.http.FormUrlEncoded;
        import retrofit2.http.POST;

public interface RetrofitInterface {
    @FormUrlEncoded
    @POST("/login/android/")
    Call<GsonModels.UserDetails> getUserDetails(@Field("username") String username, @Field("password") String password);
}

