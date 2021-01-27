import React, { Component } from "react";
import { render } from "react-dom";
import App from "./App"
import WishCarousel from './WishCarousel'
import Landing from "./Landing"
import NavBar from "./NavBar";
// import WishList from "./WishList";
// import axios from "axios";
import { BrowserRouter as Router, Route } from 'react-router-dom';
import About from './About'

// AppContainer containes async requests to fetch top level state like user, etc
class AppContainer extends Component {

  render() {
    return (
      <>
      <App />
      </>
    );
  }
}

export default AppContainer;

const container = document.getElementById("app");
render(<AppContainer />, container);