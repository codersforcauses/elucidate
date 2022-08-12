/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [],
  theme: {
    extend: {
      colors: {
        transparent: 'transparent',
        current: 'currentColor',
        primary: '#53DFCB',

        blue: '#7087FF',
        blue2: '#7087FF75',
        blue3: '#7087FF50',
        blue4: '#7087FF25',

        darkblue: '#132D54',

        green: '#53DFCB',
        green2: '#53DFCB75',
        green3: '#53DFCB50',
        green4: '#53DFCB25',

        yellow: '#FCD47C',
        yellow2: '#FCD47C75',
        yellow3: '#FCD47C50',
        yellow4: '#FCD47C25',

        red: '#F54A87',
        red2: '#F54A8775',
        red3: '#F54A8750',
        red4: '#F54A8725',

        orange: '#FCD47C',

        white: '#FFFFFF',
        lightgrey: '#E6E6E6',
        darkgrey: '#ADADAD',

        black: '#000000',
      },
      dropShadow: {
        md: '0px 4px 4px rgba(0, 0, 0, 0.25)',
      },
      fontFamily: {
        sans: ['Montserrat', 'sans-serif'],
        openSans: ['Open Sans', 'sans-serif'],
        roboto: ['Roboto', 'sans-serif'],
      },
    },
  },
  plugins: [],
};
