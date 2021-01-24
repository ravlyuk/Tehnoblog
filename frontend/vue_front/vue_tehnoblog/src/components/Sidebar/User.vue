<template>
  <div class="card my-4">
    <h5 class="card-header">{{ username }}</h5>
    <div class="card-body">
      <div class="row">
        <div class="col-lg">
          <!--          <router-link class="link" :to="/login">Вход</router-link>-->
          <component :is="dynamicComponent"></component>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import {bus} from '@/main';
import UserPanel from "@/components/Sidebar/UserMenu/UserPanel";
import UserLogin from "@/components/Sidebar/UserMenu/UserLogin";

export default {
  name: "User",
  components: {UserPanel, UserLogin},
  data() {
    return {
      username: 'Авторизация',
      dynamicComponent: 'UserLogin',
    };
  },
  created() {
    bus.$on('username', data => {
      this.username = 'Добро пожаловать, ' + data;
      this.dynamicComponent = 'UserPanel';
    })
  }
}

</script>

<style scoped>


</style>