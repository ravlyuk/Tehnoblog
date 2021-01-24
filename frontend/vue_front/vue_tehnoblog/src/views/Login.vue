<template>
  <div id="login">
    <h3 class="text-center text-white pt-5">Login form</h3>
    <div class="container p-5">
      <div id="login-row" class="row justify-content-center align-items-center">
        <div id="login-column" class="col-md-6">
          <div id="login-box" class="col-md-12">
            <form v-on:submit.prevent="submitForm" id="login-form" class="form" action="" method="post">
              <h3 class="text-center text-info text-dark">Авторизация</h3>
              <div class="form-group">
                <label for="username" class="text-info text-dark">Логин:</label><br>
                <input type="text" name="username" id="username" class="form-control" v-model="form.username">
              </div>
              <div class="form-group">
                <label for="password" class="text-info text-dark">Пароль:</label><br>
                <input type="text" name="password" id="password" class="form-control" v-model="form.password">
              </div>
              <div class="form-group">
                <!--                <label for="remember-me" class="text-info"><span>Remember me</span> <span><input id="remember-me"-->
                <!--                                                                                                 name="remember-me"-->
                <!--                                                                                                 type="checkbox"></span></label><br>-->
                <input type="submit" name="submit" class="btn btn-info btn-md navbar-dark bg-primary" value="Войти">
              </div>
              <div id="register-link" class="text-right">
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

import axios from 'axios';

<script>
import {bus} from '@/main';

export default {
  name: "Login",
  data() {
    return {
      form: {
        username: '',
        password: '',
      },
    }
  },
  methods: {
    submitForm() {
      axios.post('http://127.0.0.1:8000/api/token/', this.form)
          .then((res) => {
            //Perform Success Action
            console.log(res);
            bus.$emit('username', this.form.username);
            // window.location.href = '/';
          })
          .catch((error) => {
            // error.response.status Check status code
          }).finally(() => {
        //Perform action in always
      });
    }
  }
}
</script>

<style scoped>

</style>