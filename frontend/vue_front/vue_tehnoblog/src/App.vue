<template>
  <div id="app">
    <Nav/>
    <MainContent/>

    <div class="home">
      <div class="container">
        <div class="row">
          <div class="col-md-8">
            <router-view/>
          </div>
          <Sidebar/>
        </div>
      </div>
    </div>

    <Footer/>
  </div>
</template>


<style>
@import "assets/css/style.css";
@import "assets/css/bootstrap.min.css";
@import "assets/css/blog-home.css";
@import "assets/css/font-awesome.min.css";
</style>

<script>

import Nav from './components/Nav';
import Footer from './components/Footer';
import Sidebar from './components/Sidebar'

export default {
  components: {Nav, Footer, Sidebar}
}


</script>


