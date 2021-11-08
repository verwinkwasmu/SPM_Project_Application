export default {
  // Target: https://go.nuxtjs.dev/config-target
  target: 'static',
  ssr: false,
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'NuxtApp',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ],
    script: [
      {
        type: 'text/javascript',
        src: 'js/aos.js',
        body: true
      },
      {
        type: 'text/javascript',
        src: 'js/bootstrap.bundle.min.js',
        body: true
      },
      {
        type: 'text/javascript',
        src: 'js/glightbox.min.js',
        body: true
      },
      {
        type: 'text/javascript',
        src: 'js/isotope.pkgd.min.js',
        body: true
      },
      {
        type: 'text/javascript',
        src: 'js/swiper-bundle.min.js',
        body: true
      },
      {
        type: 'text/javascript',
        src: 'js/noframework.waypoints.js',
        body: true
      },
      {
        type: 'text/javascript',
        src: 'js/main.js',
        body: true
      }
    ]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    '@/assets/css/bootstrap.min.css',
    '@/assets/css/style.css',
    '@/assets/vendor/aos/aos.css',
    '@/assets/vendor/boxicons/css/boxicons.min.css',
    '@/assets/vendor/glightbox/css/glightbox.min.css',
    '@/assets/vendor/remixicon/remixicon.css',
    '@/assets/vendor/swiper/swiper-bundle.min.css',
    '@/assets/vendor/bootstrap-icons/bootstrap-icons.css'
  ],
  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    { src: '~/plugins/vue-datepicker', ssr: false },
    { src: '~/plugins/vue-table', ssr: false },
    { src: '~/plugins/vue-basebutton', ssr: false },    
  ],
  

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/bootstrap
    'bootstrap-vue/nuxt',
  ],

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
  }

  
}
