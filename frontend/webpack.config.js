// var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  watch: true,
    module: {
      rules: [
        {
          test: /\.js$/,
          exclude: /node_modules/,
          use: {
            loader: "babel-loader"
          }
        }
      ]
    },
  };