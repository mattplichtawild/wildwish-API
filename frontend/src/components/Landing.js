import React from 'react'
import { makeStyles, createMuiTheme, ThemeProvider } from '@material-ui/core/styles'
import { Container, Grid, Link } from '@material-ui/core';
import Typography from '@material-ui/core/Typography';
import Paper from '@material-ui/core/Paper';
import ArrowDownwardIcon from '@material-ui/icons/ArrowDownward';

const useStyles = makeStyles((theme) => ({
    root: {
      display: 'flex',
      flexWrap: 'wrap',
      padding: theme.spacing(4),
      margin: theme.spacing(1),
      '& > *': {

        // width: theme.spacing(16),
        // height: theme.spacing(16),
      },
      '& p': {
          fontSize: '1.5rem',
          paddingTop: theme.spacing(4)
      },
      '& a': {
          fontSize: '1rem',
          marginTop: theme.spacing(4)
      }
    },
  }));

export default function Landing() {
    const classes = useStyles();

    return (
        
        <Container className={classes.root} >
            <Paper elevation={0}>
                <Typography variant='h1'>Let's make wildlife feel wild again.</Typography>
                <Typography variant='body1'>WildWish connects you to wildlife living in sanctuaries and zoos all over the world.</Typography>
                <Typography variant='body1'>Choose any animal, contribute any amount. Get updates with pictures and video when animals get their new toys!</Typography>
                <Typography >
                    <Link >Learn more</Link>
                </Typography>
                <Container className={classes.root}>
                    <Typography variant='overline'>Scroll to start</Typography>
                    <Container >
                        <ArrowDownwardIcon />
                    </Container>      
                </Container>

            </Paper>
        </Container>
        
       
      );
}