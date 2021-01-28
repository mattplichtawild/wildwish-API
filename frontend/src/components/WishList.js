import React from 'react'
import AnimalCard from "./AnimalCard"
import TabPanel from "./FeaturedTabs"
import { makeStyles } from '@material-ui/core/styles';
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';
import GridListTileBar from '@material-ui/core/GridListTileBar';
import ListSubheader from '@material-ui/core/ListSubheader';
import Grid from '@material-ui/core/Grid'

export default function WishList(props) {
  const useStyles = makeStyles((theme) => ({
    root: {
      flexGrow: 1,
    },
    paper: {
      // padding: theme.spacing(2),
      textAlign: 'center',
      color: theme.palette.text.secondary,
    },
  }));

    const classes = useStyles();

    return (
      <div className={classes.root}>
        <Grid container spacing={3} >
          {props.animals.map((animal) => {
            return (
            <Grid item xs={12} sm={6} lg={4}>
              <AnimalCard animal={animal} className={classes.paper}/>
            </Grid>
            );
          })}
        </Grid>
      </div>
    );
}

