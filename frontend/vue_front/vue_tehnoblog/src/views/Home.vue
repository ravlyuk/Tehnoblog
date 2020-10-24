<template>

    <div class="home">

        <!-- Page Content -->
        <div class="container">

            <div class="row">

                <!-- Blog Entries Column -->
                <div class="col-md-8">


                    <!-- Blog Post -->
                    <div v-for="article in listArticle" :key="article.id" class="card mb-4">
                        <img class="card-img-top" :src="article.picture" alt="Card image cap">
                        <div class="card-body">
                            <h2 class="card-title">
                                <a href="#" @click="goTo(article.id)">{{ article.title }}</a>
                            </h2>
                            <p class="card-text">{{ article.content.substring(0,400)+".." }}</p>
                            <a href="#" @click="goTo(article.id)" class="btn btn-primary">Читать далее &rarr;</a>
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

                    <Pagination :total="total" :page_size="page_size" @page-changed="loadListArticles"/>

                </div>


                <!-- Sidebar Widgets Column -->
                <div class="col-md-4">

                    <!-- Search Widget -->
                    <div class="card my-4">
                        <h5 class="card-header">Поиск</h5>
                        <div class="card-body">
                            <div class="input-group">
                                <input type="text" class="form-control" placeholder="Введите запрос...">
                                <span class="input-group-append">
                <button class="btn btn-secondary" type="button">Найти</button>
              </span>
                            </div>
                        </div>
                    </div>

                    <Rubric :rubrics="rubrics" @page-changed="loadListRubrics"/>

                    <!-- Side Widget -->
                    <div class="card my-4">
                        <h5 class="card-header">Виджет сайта</h5>
                        <div class="card-body">
                            Вы можете поместить все, что захотите, внутрь этих боковых виджетов. Они просты в использовании и оснащены новыми контейнерами для карточек Bootstrap 4!
                        </div>
                    </div>

                </div>

            </div>


        </div>

    </div>

</template>

<script>
    import {getArticles, getRubrics} from '../router/requests.js';
    import Pagination from "../components/Pagination";
    import Rubric from "../components/Rubric";

    export default {
        name: 'Home',
        props: ['id', 'rubrics'],
        data() {
            return {
                listArticle: [],
                listStar: [1, 2, 3, 4, 5],
                page: 1,
                total: 0,
                page_size: 0,
            }
        },
        components: {Pagination, Rubric},
        created() {
            this.loadListArticles(this.page);
            this.loadListRubrics();
        },
        methods: {
            async loadListArticles(pageNumber) {
                this.getlistArticle = await getArticles(this.$store.getters.getServerUrl, this.id, pageNumber);
                this.listArticle = this.getlistArticle.results;
                this.total = this.getlistArticle.count;
                this.page_size = this.getlistArticle.page_size;
            },
            goTo(id) {
                this.$router.push({name: 'Single', params: {id: id}})
            },

            async loadListRubrics() {
                this.getrubrics = await getRubrics(this.$store.getters.getServerUrl);
                this.rubrics = this.getrubrics.results
            },

        }
    }
</script>
