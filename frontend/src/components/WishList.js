import React from 'react'
import AnimalCard from "./AnimalCard"
import TabPanel from "./FeaturedTabs"
import { makeStyles } from '@material-ui/core/styles';
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';
import GridListTileBar from '@material-ui/core/GridListTileBar';
import ListSubheader from '@material-ui/core/ListSubheader';

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
        height: '100%',
      },
      icon: {
        color: 'rgba(255, 255, 255, 0.54)',
      },
    }));

    const classes = useStyles();

    return (
      <div className={classes.root}>
      <GridList cellHeight={180} className={classes.gridList}>
        {props.animals.map((animal) => {
          return (
            <AnimalCard animal={animal} />
          );
        })}
      </GridList>
    </div>
    );
}

