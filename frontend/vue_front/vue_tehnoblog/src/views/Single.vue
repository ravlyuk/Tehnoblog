<template>
  <section>
    <!-- Title -->
    <h3 class="mt-4">{{ article.title }}</h3>
    <!-- Author -->
    <p class="lead">
      Автор:
      <a href="#">{{ article.name_author }}</a>
    </p>
    <hr>
    <!-- Date/Time -->
    <p>Опубликовано: {{ article.published }}</p>
    <hr>
    <!-- Preview Image -->
    <img class="img-fluid rounded" :src="article.picture" alt="">
    <hr>
    <!-- Post Content -->
    <p v-html="article.content"></p>
    <hr>
    <!-- Comment -->
    <Comment :comments="article.comments" :article="article.id" @reload="loadArticle"/>
  </section>
</template>

<script>
import {getSingleArticle} from "@/router/requests";
import Comment from '../components/Comment';

export default {
  name: 'Single',
  props: ['id'],
  components: {Comment},

  data() {
    return {
      article: {}
    }
  },
  created() {
    this.loadArticle();
  },
  methods: {
    async loadArticle() {
      this.article = await getSingleArticle(this.$store.getters.getServerUrl, this.id);
    }
  }
}
</script>