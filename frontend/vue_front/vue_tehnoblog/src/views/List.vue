<template>

  <div>
    <!-- Blog Post -->
    <div v-for="article in listArticle" :key="article.id" class="card mb-4">
      <router-link class="link" :to="getLinkTo(article.id)">
        <img class="card-img-top" :src="article.picture" alt="Card image cap">
      </router-link>
      <div class="card-body">
        <h3 class="card-title">
          <router-link class="link" :to="getLinkTo(article.id)">
            {{ article.title }}
          </router-link>
        </h3>
        <p class="card-text">
          {{
            article.content.substring(0, 400).replace('><', '> <').replace("/p>", '/p> ').replace(/<\/?[^>]+(>|$)/g, "") + ".."
          }}</p>
        <router-link :to="getLinkTo(article.id)" class="btn btn-primary">Читать далее &rarr;</router-link>
      </div>
      <div class="card-footer text-muted">
        Опубликовано: {{ article.published }}, автор:
        <a href="#">{{ article.name_author }}</a>
        <ul class="star">
          Рейтинг
          <li v-for="star in listStar" :key="star">
            <a href="#">
                    <span class="fa" :class="star <= article.middle_star ? 'fa-star' : 'fa-star-o' " aria-hidden="true">
                    </span>
            </a>
          </li>
        </ul>
      </div>
    </div>
    <Pagination :page="page" :total="total" :page_size="page_size" @page-changed="changePage"/>
  </div>


</template>

<script>

import {getArticles} from '@/router/requests';
import Pagination from "../components/Pagination";


export default {
  name: 'List',
  props: ['id'],
  data() {
    return {
      listArticle: [],
      listStar: [1, 2, 3, 4, 5],
      page: 1,
      total: 0,
      page_size: 0,
    }
  },
  components: {Pagination,},
  created() {
    this.loadListArticles();
  },
  watch: {
    id: function () {
      this.changePage(1);
    }
  },
  methods: {
    getLinkTo(id) {
      return {name: 'Single', params: {id: id}}
    },
    changePage(pageNumber) {
      this.page = pageNumber;
      this.loadListArticles();
    },
    async loadListArticles() {
      this.getlistArticle = await getArticles(this.$store.getters.getServerUrl, this.id, this.page);
      this.listArticle = this.getlistArticle.results;
      this.total = this.getlistArticle.count;
      this.page_size = this.getlistArticle.page_size;
    },
    filters: {
      markhtml: function (markdown) {
        if (typeof markdown !== 'undefined') {
          return marked(markdown)
        }
        return null
      }
    },
  }
}
</script>

<style scoped>

.link {
  text-decoration: none;
}

.preview-card {
  font-size: 14px;
}

</style>
