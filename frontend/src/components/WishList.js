import React from 'react'
import AnimalCard from "./AnimalCard"
import TabPanel from "./FeaturedTabs"
import { makeStyles } from '@material-ui/core/styles';

export default function WishList(props) {
    const useStyles = makeStyles(() => ({
        ul: {listStyleType: 'none'},
        root: {
          width:'100%'
        },
    }));
    const classes = useStyles();

    return (

      <div className={classes.root}>
        <ul className={classes.ul}>
            {props.animals.map(animal => {
              return (
                
                <li key={animal.id} id={animal.name}>
                  <AnimalCard animal={animal} />
                </li>
              );
            })}
        </ul>
      </div>
      );
}