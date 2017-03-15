var JasmineWebpackPlugin = require('jasmine-webpack-plugin');
 
module.exports = {
  entry: ['./spec/golSpec.js'],
  // ... more configuration 
  plugins: [new JasmineWebpackPlugin()]
};