import React, { Component } from "react";
import { render } from "react-dom";
import axios from "axios";
import WishList from "./WishList";
import Landing from "./Landing"

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }

  componentDidMount() {
    axios
        .get('animals/api')
        .then(resp => {
            if (resp.status > 400) {
                return this.setState( () => {
                    return { placeholder: "Something's fucky" }
                })
            }
            console.log(resp)
            return resp.data;
        })
        .then(data => {
            this.setState(() => {
                return {
                    data,
                    loaded: true
                }
            })
        })
  }
  
  render() {
    return (
      <>
      <Landing />
      {/* <p>Why are you here? This is the dev site.</p>
      <p><a type='mailto:' href='mattplichtawild@gmail.com'>Email me</a> if you know Javascript or Python and want to help.</p> */}
      {/* <WishList animals={this.state.data}/> */}
      </>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);