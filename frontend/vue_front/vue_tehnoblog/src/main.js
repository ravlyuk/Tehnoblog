import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import CKEditor from '@ckeditor/ckeditor5-vue';
import ImageUploader from 'vue-image-upload-resize'
window.axios = require('axios');

Vue.use( CKEditor );
Vue.use(ImageUploader);
Vue.use(axios);

Vue.config.productionTip = false

export const bus = new Vue();


new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')
