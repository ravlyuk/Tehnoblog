<template>
    <div>
        <ul class="pagination justify-content-center mb-4">

            <li class="page-item" :class="{disabled: currentPage === 1}">
                <span class="page-link pagination" @click="changePage(1)">Первая</span>
            </li>
            <li class="page-item" :class="{disabled: currentPage === 1}">
                <span class="page-link pagination"  @click="changePage(currentPage - 1)">&larr; назад</span>
            </li>

            <li class="page-item" v-for="p in totalPages">
                <span class="page-link pagination" :class="{active: currentPage === p}"  @click="changePage(p)">{{p}}</span>
            </li>

            <li class="page-item" :class="{disabled: currentPage === totalPages}">
                <span class="page-link pagination"  @click="changePage(currentPage + 1)">далее &rarr;</span>
            </li>

            <li class="page-item" :class="{disabled: currentPage === totalPages}">
                <span class="page-link pagination"  @click="changePage(totalPages)">Последняя</span>
            </li>

        </ul>
    </div>

</template>

<script>
    export default {
        name: "Pagination",
        props: ['total', 'page_size'],
        data() {
            return {
                currentPage: 1
            }
        },
        computed: {
            totalPages() {
                return Math.ceil(this.total / this.page_size)
            }
        },
        methods: {
            changePage(pageNumber) {
                this.currentPage = pageNumber
                this.$emit('page-changed', pageNumber)
            },

        }
    }
</script>


<style scoped>
    .pagination {
        color: #0062cc;
    }

    .active {
        background-color: #007bff;
        color: white;
    }
</style>
