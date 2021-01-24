<template>
  <div class="container">
    <div class="row">
      <section>
        <div class="card my-4">
          <h5 class="card-header">Опубликовать статью</h5>
          <div class="card-body">
            <form id="formComment2" action="#" method="get">
              <label class="label_class">Заголовок
                <input type="text" class="form-control" v-model="title" required><br>
              </label>
              <label class="label_class">Автор
                <input type="text" class="form-control" v-model="name_author" required><br>
              </label>

              <!-- Rubric -->
              <label class="label_class">Рубрика</label>

              <div class="input-group mb-3">
                <div class="input-group-prepend">
                  <label class="input-group-text" for="inputGroupSelect01">Выбрать</label>
                </div>
                <select v-model="selected" class="custom-select" id="inputGroupSelect01">
                  <option v-for="rubric in rubrics" :key="rubric.id" :value="rubric.id">{{ rubric.name }}</option>
                </select>
              </div>

              <!-- Image -->
              <label class="label_class">Изображение</label>
              <div class="input-group mb-3">
                <image-uploader
                    :debug="1"
                    :maxWidth="512"
                    :quality="0.7"
                    :autoRotate=true
                    outputFormat="verbose"
                    :preview=false
                    :className="['fileinput', { 'fileinput--loaded' : hasImage }]"
                    capture="environment"
                    accept="video/*,image/*"
                    doNotResize="['gif', 'svg']"
                    @input="setImage"
                ></image-uploader>
              </div>

              <!-- Page Content -->
              <label class="label_class">Содержание статьи</label>
              <div class="ckeditor">
                <div id="app">
                  <ckeditor :editor="editor" v-model="content" :config="editorConfig"></ckeditor>
                </div>
              </div>
              <input value="Отправить" type="submit" class="btn btn-primary" @click="sendArticle()">
            </form>
          </div>
        </div>
      </section>
    </div>


  </div>


</template>

<script>
import ClassicEditor from '@ckeditor/ckeditor5-build-classic';
import {getRubrics} from "@/router/requests";
import ImageUploader from 'vue-image-upload-resize'

export default {
  name: 'AddArticle',
  data() {
    return {
      editor: ClassicEditor,
      editorConfig: {},
      title: '',
      content: '',
      name_author: '',
      selected: '',
      rubrics: [],
      hasImage: false,
      picture: null,
    };
  },
  created() {
    this.loadListRubrics()
  },
  methods: {
    setImage: function (output) {
      this.hasImage = true;
      this.picture = output.dataUrl;
      console.log('Info', output.info)
    },
    async loadListRubrics() {
      const {results} = await getRubrics(this.$store.getters.getServerUrl);
      this.rubrics = results;
    },
    async sendArticle() {
      let data = {
        title: this.title,
        content: this.content,
        name_author: this.name_author,
        rubric: this.selected,
        picture: this.picture,
      }
      if (!data.picture) {
        delete data.picture
      }
      fetch(`${this.$store.getters.getServerUrl}/article/`,
          {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
          }
      ).then(response => {
        this.$emit('reload')
        this.clearForm()
      })
    },
    clearForm() {
      console.log('log:', this.title, this.content, this.name_author);
      if (this.title && this.content && this.name_author) {
        this.title = '';
        this.content = '';
        this.name_author = '';
      }
    }

  }
}
</script>

<style scoped>
.label_class {
  width: 100%;
}

.ckeditor {
  padding-bottom: 30px;
  max-height: 50%;
}

.ck-blurred ck ck-content ck-editor__editable ck-rounded-corners ck-editor__editable_inline {
  height: 300px;
}


</style>