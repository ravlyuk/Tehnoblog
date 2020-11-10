<template>

    <div class="home">

        <!-- Page Content -->
        <div class="container">

            <div class="row">

                <!-- Blog Entries Column -->
                <div class="col-md-8">

                    <!-- Blog Post -->
                    <div v-for="article in listArticle" :key="article.id" class="card mb-4">
                        <router-link
                            class="link"
                            :to="getLinkTo(article.id)"
                        >
                          <img class="card-img-top" :src="article.picture" alt="Card image cap">
                        </router-link>
                        <div class="card-body">
                            <h3 class="card-title">
                                <router-link
                                    class="link"
                                    :to="getLinkTo(article.id)"
                                >
                                  {{ article.title }}
                                </router-link>
                            </h3>
                            <p class="card-text">{{ article.content.substring(0,400)+".." }}</p>
                            <router-link :to="getLinkTo(article.id)" class="btn btn-primary">Читать далее &rarr;</router-link>
                        </div>
                        <div class="card-footer text-muted">
                            Опубликовано: 29 октября 2020, автор:
                            <a href="#">Евгений Равлюк</a>
                            <ul class="star">
                                Рейтинг
                                <li v-for="star in listStar" :key="star">
                                    <a href="#">
                                        <span class="fa" :class="star <= article.middle_star ? 'fa-star' : 'fa-star-o' "
                                              aria-hidden="true">

                                        </span>
                                    </a>

                                </li>
                            </ul>
                        </div>
                    </div>

                    <Pagination :page="page" :total="total" :page_size="page_size" @page-changed="changePage"/>

                </div>

                <div class="col-md-4">

                    <!-- Sidebar Widgets Column -->
                    <Search/>

                    <!-- Sidebar Rubric Column -->
                    <Rubric/>

                    <!-- Side Widget Column -->
                    <Widget/>

                </div>
            </div>
        </div>
    </div>


</template>

<script>
    import {getArticles} from '../router/requests.js';
    import Pagination from "../components/Pagination";
    import Rubric from "../components/Rubric";
    import Search from "../components/Search";
    import Widget from "../components/Widget";

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
        components: {Search, Pagination, Rubric, Widget},
        created() {
            this.loadListArticles();
        },
        watch: {
          id: function() {
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
            }
        }
    }
</script>

<style scoped>

.link {
  text-decoration: none;
}

</style>
