import React from 'react'
import AnimalCard from "./AnimalCard"
import TabPanel from "./AnimalSelectTabs"
import { makeStyles } from '@material-ui/core/styles';
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';
import GridListTileBar from '@material-ui/core/GridListTileBar';
import ListSubheader from '@material-ui/core/ListSubheader';
import Grid from '@material-ui/core/Grid'
import { Route } from 'react-router-dom'

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
        {/* <Grid container spacing={3} > */}
          {props.data.map((wish) => {
            return (
            // <Grid item xs={12} sm={6} lg={4}>
              <AnimalCard key={wish.id} data={wish} className={classes.paper}/>
            // </Grid>
            );
          })}
        {/* </Grid> */}
      </div>
    );
}

