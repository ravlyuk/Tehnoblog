<template>
  <div class="col-md-4">

    <!-- Sidebar Search Column -->
    <Search/>

    <!-- Sidebar User Column -->
    <User/>

    <!-- Sidebar Rubric Column -->
    <Rubric/>

    <!-- Side Widget Column-->
    <Widget/>

  </div>
</template>

<script>
import Rubric from "./Sidebar/Rubric";
import Search from "./Sidebar/Search";
import Widget from "./Sidebar/Widget";
import User from "./Sidebar/User";

export default {
  name: "Sidebar",
  components: {Search, Rubric, Widget, User},
}
</script>

<style scoped>

</style>