import React from 'react'
import AnimalCard from "./AnimalCard"
import TabPanel from "./FeaturedTabs"
import { makeStyles } from '@material-ui/core/styles';

export default function WishList(props) {
    const useStyles = makeStyles((theme) => ({
      root: {
        display: 'flex',
        flexWrap: 'wrap',
        justifyContent: 'space-around',
        overflow: 'hidden',
        backgroundColor: theme.palette.background.paper,
      },
      gridList: {
        width: 500,
        height: 450,
      },
      icon: {
        color: 'rgba(255, 255, 255, 0.54)',
      },
    }));

    const classes = useStyles();

    return (
      props.animals.map(animal => {
        return (
            <AnimalCard animal={animal} />
        );
      })
    );
}