import React, { useState, useEffect } from 'react'
import { makeStyles } from '@material-ui/core/styles';

function ActiveWishList(props) {

    useEffect(() => {
        
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