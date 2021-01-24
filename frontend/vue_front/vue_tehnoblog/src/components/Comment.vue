<template>
  <section>
    <!-- Comments Form -->
    <div class="card my-4">
      <h5 class="card-header">Оставить комментарий:</h5>
      <div class="card-body">
        <form id="formComment2" action="#" method="get">
          <label class="label_class">Имя
            <input type="text" class="form-control" v-model="name" required><br>
          </label>
          <label class="label_class">Email
            <input type="email" class="form-control" v-model="email" required><br>
          </label>
          <label class="label_class">Комментарий
            <textarea class="form-control" rows="3" v-model="content" required></textarea><br>
          </label>
          <input value="Отправить" type="submit" class="btn btn-primary" @click="sendComment()">
        </form>
      </div>
    </div>


    <!-- Comment with nested comments -->
    <div class="media mb-4" v-for="comment in comments" :key="comment.id">
      <img class="d-flex mr-3 rounded-circle" src="../assets/img/user.png" alt="">
      <div class="media-body">
        <h5 class="mt-0">{{ comment.name }}</h5>
        <p v-html="comment.content"></p>
        <a href="#formComment" @click="addParent(comment.id)">Ответить</a>

        <div class="media mt-4" v-for="child in comment.children">
          <img class="d-flex mr-3 rounded-circle" src="../assets/img/user.png" alt="">
          <div class="media-body">
            <h5 class="mt-0">{{ child.name }}</h5>
            <p v-html="child.content"></p>
          </div>
        </div>


      </div>
    </div>

  </section>
</template>

<script>

export default {
  name: "Comment",
  props: ['comments', 'article'],
  data() {
    return {
      name: '',
      email: '',
      content: '',
      parent: null,
    }
  },
  methods: {
    async sendComment() {
      let data = {
        name: this.name,
        email: this.email,
        content: this.content,
        parent: this.parent,
        article: this.article,
      }
      fetch(`${this.$store.getters.getServerUrl}/comment/`,
          {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
          }
      ).then(response => {
        this.$emit('reload')
        this.clearForm()
      })
    },
    addParent(id) {
      this.parent = id
    },
    clearForm() {
      console.log('log:', this.name, this.email, this.content);
      if (this.name && this.email && this.content) {
        this.name = '';
        this.email = '';
        this.content = '';
        this.parent = null;
      }
    }
  }
}
</script>

<style scoped>
.label_class {
  width: 100%;
}

</style>