export default {
  server: {
    host: '0.0.0.0',
    port: '8080',
  },

  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'elucidate-frontend',
    htmlAttrs: {
      lang: 'en',
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' },
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
  },

  // Global CSS: https://go.nuxtjs.dev/config-css

  css: [
    '@fontsource/montserrat/variable.css',
    '@fortawesome/fontawesome-svg-core/styles.css',
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: ['~/plugins/fontawesome.js'],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: {
    dirs: [
      '~/components',
      '~/components/Section',
      '~/components/Input',
      '~/components/Auth',
    ],
  },

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/tailwindcss
    '@nuxtjs/tailwindcss',
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    '@nuxtjs/auth-next',
    '@nuxt/image',
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    baseURL: process.env.BACKEND_URL || 'http://127.0.0.1:8081/api/',
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
    transpile: ['vee-validate/dist/rules'],
  },
  devServerHandlers: [],
  watchers: {
    webpack: {
      poll: true,
    },
  },
  // Purge CSS Configuration: https://go.nuxtjs.dev/config-purgecss
  purgeCSS: {
    whitelistPatterns: [/svg.*/, /fa.*/],
  },

  router: {
    // set to false for easier testing
    // middleware: ['auth'],
  },

  auth: {
    strategies: {
      local: {
        token: {
          property: 'token',
          global: true,
          // required: true,
          // type: 'Bearer'
        },
        user: {
          property: 'user',
          // autoFetch: true
        },
        endpoints: {
          login: { url: 'auth/login/', method: 'post' },
          logout: { url: 'auth/logout/', method: 'post' },
          user: { url: 'auth/user/', method: 'get' },
        },
      },
    },
  },
};
