import React from 'react'
import AnimalCard from "./AnimalCard"
import { makeStyles } from '@material-ui/core/styles';

export default function Home(props) {
    const useStyles = makeStyles(() => ({
        ul: {listStyleType: 'none'}

    }));
    const styles = useStyles();

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