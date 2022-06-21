module.exports = {
  extends: ['@commitlint/config-conventional'],
  rules: {
    'scope-enum': [
      2,
      'always',
      [
        'core',
        'linting',
        'frontend',
        'backend',
        'auth',
        'styles',
        'misc',
        'config',
        'ci',
        'cd',
      ],
    ],
  },
};
