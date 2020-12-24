import React, { Component } from "react";
import { render } from "react-dom";
import axios from "axios";
import AnimalCard from "./AnimalCard"
import Button from '@material-ui/core/Button';

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
      <ul>
          {this.state.data.map(animal => {
            return (
              <li key={animal.id}>
                <AnimalCard animal={animal} />
              </li>
            );
          })}
      </ul>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);