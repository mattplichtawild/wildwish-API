import React from 'react'
import { makeStyles, createMuiTheme, ThemeProvider } from '@material-ui/core/styles'
import { Container } from '@material-ui/core';
import Typography from '@material-ui/core/Typography';
import Paper from '@material-ui/core/Paper';
import ArrowDownwardIcon from '@material-ui/icons/ArrowDownward';

const useStyles = makeStyles((theme) => ({
    root: {
      display: 'flex',
      flexWrap: 'wrap',
      '& > *': {
        margin: theme.spacing(1),
        padding: theme.spacing(4),

        // width: theme.spacing(16),
        // height: theme.spacing(16),
      },
      '& p': {
          paddingTop: theme.spacing(4)
      }
    },
  }));

const theme = createMuiTheme();
    theme.typography.h1 = {
    fontSize: '2rem',
    '@media (min-width:600px)': {
        fontSize: '1.5rem',
    },
    [theme.breakpoints.up('md')]: {
        fontSize: '4rem',
    },
};

export default function Landing() {
    const classes = useStyles();

    return (
        <ThemeProvider theme={theme}>
        <Container className={classes.root}>
            <Paper elevation='0'>
                <Typography variant='h1'>Let's make wildlife feel wild again.</Typography>
                <Typography variant='body1'>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</Typography>

                <Container className={classes.root}>
                    <Typography variant='overline'>Scroll to start</Typography>
                    <ArrowDownwardIcon />
                </Container>
            </Paper>
        </Container>
        
        </ThemeProvider>
      );
}