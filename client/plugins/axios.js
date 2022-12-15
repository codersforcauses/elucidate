export default function ({ $axios, $auth }) {
  $axios.onRequest(async (config) => {
    try {
      // / Store action to get or retrieve a token if it has expired
      const token = $auth.strategy.token.get().token;
      $axios.setToken(token, 'Bearer');
    } catch (error) {
      console.log('Could not update token:', error);
    }
    return config;
  });
}
