module.exports = {
  env: {
    browser: true,
    es2021: true,
    jest: true,
  },
  extends: ['standard', '@nuxtjs', 'prettier', 'plugin:cypress/recommended'],
  parserOptions: {
    ecmaVersion: 'latest',
    sourceType: 'module',
  },
  plugins: ['vue', 'cypress'],
  rules: {
    'vue/attribute-hyphenation': ['never'],
  },
};
