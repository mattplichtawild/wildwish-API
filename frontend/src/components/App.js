import React, { Component } from "react";
import { render } from "react-dom";
// import axios from "axios";
// import WishList from "./WishList";
import WishCarousel from './WishCarousel'
import Landing from "./Landing"
import NavBar from "./NavBar";

// Todo: Rewrite this as functional component
class App extends Component {
  
  render() {
    return (
      <>
      <NavBar />
      <Landing />
      {/* <p>Why are you here? This is the dev site.</p>
      <p><a type='mailto:' href='mattplichtawild@gmail.com'>Email me</a> if you know Javascript or Python and want to help.</p> */}
      {/* <WishList animals={this.state.data}/> */}
      <WishCarousel />
      </>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);