import React, { Component } from "react";
import Button from '@material-ui/core/Button';

class AnimalCard extends Component {
    constructor(props) {
        super(props);
        this.state = {
            animal: props.animal
        }
    }

    render() {
        const animal = this.state.animal
        return (
            <div>
                <h2>{animal.name}</h2>
                <p>{animal.species}</p>
                <p>{animal.bio}</p>
                <p>{animal.zoo}</p>
                <a href={animal.recent_img.upload}>Picture</a>
                <Button variant="contained" color="primary">
                    Hello World
                </Button>
            </div>
        )
    }
}

export default AnimalCard;