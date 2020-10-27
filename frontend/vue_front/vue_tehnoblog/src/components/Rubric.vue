<template>
    <!-- Categories Widget -->
    <div class="card my-4">
        <h5 class="card-header">Рубрики</h5>
        <div class="card-body">
            <div class="row">
                <div class="col-lg">
                    <ul class="list-unstyled mb-0">
                        <li v-for="rubric in rubrics" :key="rubric">
                            <a href="#" @click="goTo(rubric.id)">{{rubric.name}}</a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

    export default {
        name: "List",
        props: ['rubrics'],
        methods: {
            goTo(id) {
                this.$router.push({name: 'List', params: {id: id}})
            },
        }

    }
</script>

<style scoped>

</style>