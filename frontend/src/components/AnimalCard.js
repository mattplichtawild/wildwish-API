import React, { Component } from "react";
import clsx from 'clsx';
import { makeStyles } from '@material-ui/core/styles';
import Box from '@material-ui/core/Box';
import Typography from '@material-ui/core/Typography';
import Card from '@material-ui/core/Card';
import CardMedia from '@material-ui/core/CardMedia';
import CardContent from '@material-ui/core/CardContent';
import CardActions from '@material-ui/core/CardActions';
import {
  Info,
  InfoCaption,
  InfoSubtitle,
  InfoTitle,
} from '@mui-treasury/components/info';
import { useGalaxyInfoStyles } from '@mui-treasury/styles/info/galaxy';
import { useCoverCardMediaStyles } from '@mui-treasury/styles/cardMedia/cover';
// import { Button } from "@material-ui/core";
import DonateModal from './DonateModal' 
import GridListTile from '@material-ui/core/GridListTile';
import GridListTileBar from '@material-ui/core/GridListTileBar';
import ListSubheader from '@material-ui/core/ListSubheader';
import IconButton from '@material-ui/core/IconButton';
import InfoIcon from '@material-ui/icons/Info';
import { Grid } from "@material-ui/core";
import Collapse from '@material-ui/core/Collapse';
import FavoriteIcon from '@material-ui/icons/Favorite';
import ShareIcon from '@material-ui/icons/Share';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import Button from '@material-ui/core/Button';

function AnimalCard(props) {
    const animal = props.animal
    const [expanded, setExpanded] = React.useState(false);
    const handleExpandClick = () => {
        setExpanded(!expanded);
      };

    const [amount, setAmount] = React.useState(1)
    const handleChange = (event) => {
        setAmount(event.target.value)
    }

    const useStyles = makeStyles((theme) => ({
        card: {
            // borderRadius: '1rem',
            boxShadow: 'none',
            position: 'relative',
            // minWidth: 200,
            minHeight: 500,
            // height: '100%',
            // width: '100%',
            '&:after': {
                content: '""',
                display: 'inline-block',
                position: 'absolute',
                width: '100%',
                height: '35%',
                bottom: 0,
                zIndex: 1,
                background: 'linear-gradient(to top, #000, rgba(0,0,0,0))',
                // background: 'linear-gradient(#000, white)'
            },
        },
        expand: {
            transform: 'rotate(0deg)',
            marginLeft: 'auto',
            color: 'white',
            // transition: theme.transitions.create('transform', {
            //     duration: theme.transitions.duration.shortest,
            // }),
        },
        expandOpen: {
            // This should be getting set in App.js, is it being overridden somewhere?
            // color: theme.palette.primary.main
            color: 'red'
            // transform: 'rotate(0deg)',
        },
        content: {
        position: 'absolute',
        zIndex: 2,
        bottom: 0,
        width: '100%',
        },
        infoDrawer: {
            // background: 'linear-gradient(#0000, white)'
            background: 'white'
        }
    }));

    const mediaStyles = useCoverCardMediaStyles({ bgPosition: 'top' });
    const classes = useStyles();

    const defaultAvatar = {upload: 'https://wildwishdev.s3.amazonaws.com/media/default-avatar.jpg'}

    if (!animal.avatar){
        animal.avatar = animal.images[0] || defaultAvatar
    }

    return (
            <Card className={classes.card}>
                <CardMedia
                classes={mediaStyles}
                image={animal.avatar.upload}
                />
                <Box py={3} px={2} className={classes.content}>
                <Info useStyles={useGalaxyInfoStyles}>
                    <InfoTitle>{animal.name}</InfoTitle>
                    <InfoSubtitle>{animal.zoo}</InfoSubtitle>
                </Info>
                <CardActions disableSpacing>
                    <IconButton aria-label="add to favorites">
                    </IconButton>
                    <IconButton aria-label="share">
                    </IconButton>
                    <IconButton
                    className={clsx(classes.expand, {
                        [classes.expandOpen]: expanded,
                    })}
                    onClick={handleExpandClick}
                    aria-expanded={expanded}
                    aria-label="show more"
                    >
                        <FavoriteIcon 
                        
                        style={{paddingRight: 18}} />
                    </IconButton>
                </CardActions>
                <Collapse className={classes.infoDrawer} in={expanded} timeout="auto" unmountOnExit>
                    <CardContent>
                    <Typography >Help {animal.name}'s wish come true by giving</Typography>
            
                    <input type='number' name='amount' id='amount' value={amount} min='1' onChange={handleChange}/>
                    
                    <DonateModal amount={amount} animal={animal}/>
                    <Typography paragraph>
                        {/* This is the donate popup. */}
                    </Typography>
                    {/* can't get this icon to go to the right... */}
                    <ShareIcon style={{color: 'white'}}/>
                    {/* <Typography paragraph>
                        {amount}
                    </Typography> */}
                    {/* <Typography paragraph>
                        Add rice and stir very gently to distribute. Top with artichokes and peppers, and cook
                        without stirring, until most of the liquid is absorbed, 15 to 18 minutes. Reduce heat to
                        medium-low, add reserved shrimp and mussels, tucking them down into the rice, and cook
                        again without stirring, until mussels have opened and rice is just tender, 5 to 7
                        minutes more. (Discard any mussels that don’t open.)
                    </Typography> */}
                    {/* <Typography>
                        Set aside off of the heat to let rest for 10 minutes, and then serve.
                    </Typography> */}
                    </CardContent>
                </Collapse>
{/*                 
                <Button 
                variant='outlined' 
                color='primary' 
                onClick={() => handleClick()} 
                >
                    Donate
                </Button> */}
                </Box>
            </Card>
        
    )
}

export default AnimalCard;