import React, { Component } from "react";
import { render } from "react-dom";

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
    fetch("animals/api")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });
  }

  render() {
     
      return (
          <ul>
        {this.state.data.map(animal => {
            console.log(animal)
            console.log(animal.recent_img.upload)
            return (
            <li key={animal.id}>
                <h2>{animal.name}</h2>
                <p>{animal.species}</p>
                <p>{animal.bio}</p>
                <p>{animal.zoo}</p>
                <a href={animal.recent_img.upload} >Picture</a>
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