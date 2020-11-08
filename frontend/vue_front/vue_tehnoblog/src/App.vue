<template>
    <div id="app">
        <Nav/>
        <router-view/>
        <Footer/>
    </div>

</template>

<style>
    @import "assets/css/style.css";
    @import "assets/css/bootstrap.min.css";
    @import "assets/css/blog-home.css";
</style>

<script>

    import Nav from './components/Nav';
    import Footer from './components/Footer'

    export default {
        components: {Nav, Footer}
    }

</script>


