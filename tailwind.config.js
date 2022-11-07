const Path = require("path");
const pwd = process.env.PWD;

// We can add current project paths here
const projectPaths = [
  Path.join(pwd, "./wagtail_app/templates/**/*.html"),
  // add js file paths if you need
];

const contentPaths = [...projectPaths];
console.log(`tailwindcss will scan ${contentPaths}`);

module.exports = {
  content: contentPaths,
  darkMode: 'class',
  theme: {
    extend: {
      typography: (theme) => ({
        dark: {
          css: {
            color: theme("colors.gray.300"),
            a: {
              color: theme("colors.green.500"),
              "&:hover": {
                color: theme("colors.green.500"),
              },
            },
            h1: {
              color: theme("colors.gray.300"),
            },
            h2: {
              color: theme("colors.gray.300"),
            },
            h3: {
              color: theme("colors.gray.300"),
            },
            h4: {
              color: theme("colors.gray.300"),
            },
            h5: {
              color: theme("colors.gray.300"),
            },
            h6: {
              color: theme("colors.gray.300"),
            },
            strong: {
              color: theme("colors.gray.300"),
            },
            figcaption: {
              color: theme("colors.gray.500"),
            },
            pre: {
              background: '#23241f',
            },
          },
        },
      }),
    },
  },
  variants: {
    extend: {
      typography: ["dark"],
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('@tailwindcss/forms'),
  ],
}
