module.exports = {
  env: {
    browser: true,
    es2021: true,
    jest: true,
  },
  extends: [
    'plugin:vue/essential',
    'standard',
    'prettier',
    'plugin:cypress/recommended',
  ],
  parserOptions: {
    ecmaVersion: 'latest',
    sourceType: 'module',
  },
  plugins: ['vue', 'cypress'],
  rules: {
    'vue/multi-word-component-names': [
      'error',
      {
        ignores: ['default'],
      },
    ],
  },
};
