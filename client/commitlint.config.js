module.exports = {
  extends: ['@commitlint/config-conventional'],
  rules: {
    'scope-enum': [
      2,
      'always',
      [
        'core',
        'linting',
        'backend',
        'frontend',
        'authentication',
        'styles',
        'documentation',
        'misc',
      ],
    ],
  },
};
