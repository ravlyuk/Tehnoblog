<template>
    <section>
        <!-- Page Content -->
        <div class="container">

            <div class="row">

                <!-- Post Content Column -->
                <div class="col-lg-8">

                    <!-- Title -->
                    <h1 class="mt-4">{{ article.title }}</h1>

                    <!-- Author -->
                    <p class="lead">
                        by
                        <a href="#">Start Bootstrap</a>
                    </p>

                    <hr>

                    <!-- Date/Time -->
                    <p>Posted on January 1, 2019 at 12:00 PM</p>

                    <hr>

                    <!-- Preview Image -->
                    <img class="img-fluid rounded" :src="article.picture" alt="">

                    <hr>

                    <!-- Post Content -->
                    <p v-html="article.content"></p>

                    <hr>
                    <!-- Comment -->
                    <Comment :comments="article.comments" :article="article.id" @reload="loadArticle" />


                </div>

                <!-- Sidebar Widgets Column -->
                <div class="col-md-4">

                    <!-- Search Widget -->
                    <div class="card my-4">
                        <h5 class="card-header">Search</h5>
                        <div class="card-body">
                            <div class="input-group">
                                <input type="text" class="form-control" placeholder="Search for...">
                                <span class="input-group-append">
                <button class="btn btn-secondary" type="button">Go!</button>
              </span>
                            </div>
                        </div>
                    </div>

                    <Rubric :rubrics="rubrics"/>

                    <!-- Side Widget -->
                    <div class="card my-4">
                        <h5 class="card-header">Side Widget</h5>
                        <div class="card-body">
                            You can put anything you want inside of these side widgets. They are easy to use, and
                            feature the new Bootstrap 4 card containers!
                        </div>
                    </div>

                </div>

            </div>
            <!-- /.row -->

        </div>
        <!-- /.container -->
    </section>
</template>

<script>
    import {getRubrics, getSingleArticle} from "../router/requests";
    import Comment from '../components/Comment';
    import Rubric from "../components/Rubric";

    export default {
        name: 'Single',
        props: ['id'],
        components: {Comment, Rubric},
        data() {
            return {
                article: {}
            }
        },
        created() {
            this.loadArticle();
            this.loadListRubrics();
        },
        methods: {
            async loadArticle() {
                this.article = await getSingleArticle(this.$store.getters.getServerUrl, this.id);
            },

            async loadListRubrics() {
                this.getrubrics = await getRubrics(this.$store.getters.getServerUrl);
                this.rubrics = this.getrubrics.results
            },
        }
    }
</script>