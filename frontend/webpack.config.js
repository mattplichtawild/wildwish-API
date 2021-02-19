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
        },
      },
      // Below configs used when trying to bundle Semantic UI
      // Ended up using CDN for instead of using bundler
      // {
      //   test: /\.(png|jpg|gif|svg|eot|ttf|woff|woff2)$/,
      //   loader: 'url-loader',
      //   options: {
      //       limit: 10000,
      //   },
      // },
      // {
      //   // Preprocess our own .css files
      //   // This is the place to add your own loaders (e.g. sass/less etc.)
      //   // for a list of loaders, see https://webpack.js.org/loaders/#styling
      //   test: /\.css$/,
      //   exclude: /node_modules/,
      //   use: ['style-loader', 'css-loader'],
      // },
    ]
  },
};