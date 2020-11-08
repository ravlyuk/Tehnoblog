<template>

    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top">
        <div class="container">
            <router-link class="navbar-brand" to="/">
              Техноблог
            </router-link>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive"
                    aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarResponsive">
                <ul class="navbar-nav ml-auto">
                    <li :class="`nav-item${isHome}`">
                      <router-link class="nav-link" to="/">
                          Главная <span class="sr-only">(current)</span>
                      </router-link>
                    </li>
                    <li :class="`nav-item${isAbout}`">
                      <router-link class="nav-link" to="/about">О нас</router-link>
                    </li>
                    <li :class="`nav-item${isServices}`">
                      <router-link class="nav-link" to="/services">Сервисы</router-link>
                    </li>
                    <li :class="`nav-item${isContacts}`">
                      <router-link class="nav-link" to="/contacts">Контакты</router-link>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

</template>

<script>
export default {
  name: 'Nav',
  computed: {
    isHome: function() {
      return this.$route.path === '/' ? ' active' : '';
    },
    isAbout: function() {
      return this.$route.path === '/about' ? ' active' : '';
    },
    isServices: function() {
      return this.$route.path === '/services' ? ' active' : '';
    },
    isContacts: function() {
      return this.$route.path === '/contacts' ? ' active' : '';
    }
  }
}
</script>