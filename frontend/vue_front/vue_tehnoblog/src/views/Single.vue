<template>
    <section>
        <!-- Page Content -->
        <div class="container">

            <div class="row">

                <!-- Post Content Column -->
                <div class="col-lg-8">

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


                </div>

                <!-- Sidebar Widgets Column -->
                <div class="col-md-4">

                    <!-- Sidebar Widgets Column -->
                    <Search/>

                    <!-- Sidebar Rubric Column -->
                    <Rubric/>

                    <!-- Side Widget Column -->
                    <Widget/>

                </div>

            </div>
            <!-- /.row -->

        </div>
        <!-- /.container -->
    </section>
</template>

<script>
    import {getSingleArticle} from "../router/requests";
    import Comment from '../components/Comment';
    import Rubric from "../components/Rubric";
    import Search from "../components/Search";
    import Widget from "../components/Widget";

    export default {
        name: 'Single',
        props: ['id'],
        components: {Comment, Rubric, Search, Widget},
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