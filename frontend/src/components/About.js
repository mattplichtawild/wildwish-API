import React from 'react';
import { Container, Paper, Typography } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import { NavLink } from 'react-router-dom';

const useStyles = makeStyles((theme) => ({
    root: {
      display: 'flex',
      flexWrap: 'wrap',
      padding: theme.spacing(1),
      margin: theme.spacing(1),
      '& p': {
          fontSize: '1rem',
          padding: theme.spacing(1)
      },
    },
}));

function About() {
    const classes = useStyles();

    return (
        <Container>
            <Paper className={classes.root} elevation={0}>
                <Typography variant="h1" >
                Enriching the lives of wild animals in captivity.
                </Typography>
                <Typography variant="body1">
                That was the mission when I started WildHeart in a coffee shop in 2015, and it's the mission now.
                </Typography>
                <br/>
                <Typography variant="body1">
                The core work is improving enclosures with pools, furniture, and other additions. But the foundation was built on providing enrichment for
                animals in zoos around the world. Zookeepers would reach out on social media, and WildHeart would send them a toy.
                </Typography>
                <br/>
                <Typography variant="body2">
                Wildwish.org connects people with the animals their money is helping. Toys and enrichment are crowdsourced with microdonations, and donors are
                notified when their animal gets the toy they helped buy. No more need for zookeepers to message us on Facebook and then wait while we collect donations 
                to fund a piece of enrichment.
                </Typography>
                <br />
                <Typography variant="body2">
                This program is free for zoos and wildlife sanctuaries. We often get asked &quot;What&apos;s the catch?&quot; when working with a zoo to
                provide enrichment. The answer is that there isn&apos;t one. The WildHeart Foundation is a passion project; an organization consisting
                of me and some friends who love and work with wildlife. The projects we&apos;ve worked on have been acheivements on par with 
                larger nonprofits, but WildHeart is still ran from coffee shops on weekends (except in times of pandemic), and volunteering is
                scheduled around day jobs or while using vacation time. We do this because we want to see happy animals.
                </Typography>
                <br />
                <Typography variant="body2">
                We do this because our hearts are wild.
                </Typography>
                <Typography variant="body2">
                    
                </Typography>
                <Typography variant="body2">
                    
                </Typography>
                <Typography variant='overline'>
                    <NavLink to="/">Start helping</NavLink>
                </Typography>
            </Paper>
        </Container>
    )
}

export default About