import React, { Component } from "react";
import { render } from "react-dom";
import axios from "axios";

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
            <div>
            <h2>Basic Front Page to hook React up</h2>
            <p>No CSS or any styling.</p>
            <ul>
        {this.state.data.map(animal => {
            return (
            <li key={animal.id}>
                <h2>{animal.name}</h2>
                <p>{animal.species}</p>
                <p>{animal.bio}</p>
                <p>{animal.zoo}</p>
                <a href={animal.recent_img.upload}>Picture</a>
            </li>
          );
        })}
      </ul>
      </div>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);