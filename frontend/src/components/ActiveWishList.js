import React, { useState, useEffect } from 'react'
import { makeStyles } from '@material-ui/core/styles';

function ActiveWishList(props) {

    useEffect(() => {
        axios
        .get('animals/wishes/active')
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
    });

    return (
        <ul className={styles.ul}>
            {props.animals.map(animal => {
              return (
                <li key={animal.id} id={animal.name}>
                  <AnimalCard animal={animal} />
                </li>
              );
            })}
        </ul>
    );
}