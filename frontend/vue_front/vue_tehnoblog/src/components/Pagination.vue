<template>
    <div>
        <ul class="pagination justify-content-center mb-4">

            <li class="page-item" :class="{disabled: page === 1}">
                <span class="page-link" @click="changePage(1)">Первая</span>
            </li>
            <li class="page-item" :class="{disabled: page === 1}">
                <span class="page-link"  @click="changePage(page - 1)">&larr; назад</span>
            </li>

            <li class="page-item" v-for="p in totalPages">
                <span class="page-link" :class="{active: page === p}"  @click="changePage(p)">{{p}}</span>
            </li>

            <li class="page-item" :class="{disabled: page === totalPages}">
                <span class="page-link"  @click="changePage(page + 1)">далее &rarr;</span>
            </li>

            <li class="page-item" :class="{disabled: page === totalPages}">
                <span class="page-link"  @click="changePage(totalPages)">Последняя</span>
            </li>

        </ul>
    </div>

</template>

<script>
    export default {
        name: "Pagination",
        props: {
          page: {
            default: 1
          },
          total: {
            default: 0
          },
          page_size: {
            default: 0
          }
        },
        computed: {
            totalPages() {
                if (!this.total) {
                  return 0;
                }
                return Math.ceil(this.total / this.page_size)
            }
        },
        methods: {
            changePage(pageNumber) {
                this.$emit('page-changed', pageNumber)
            },

        }
    }
</script>


<style scoped>
    .pagination li {
        color: #0062cc;
        cursor: pointer;
        padding: 0 5px;
    }

    .active {
        background-color: #007bff;
        color: white;
    }
</style>
