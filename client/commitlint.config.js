module.exports = {
  extends: ['@commitlint/config-conventional'],
  rules: {
    'scope-enum': [
      2,
      'always',
      [
        'core',
        'frontend',
        'backend',
        'auth',
        'linting',
        'styles',
        'misc',
        'config',
        'ci',
        'cd',
        'deps',
      ],
    ],
  },
};
