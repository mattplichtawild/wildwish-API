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
            },
        },
        expand: {
            transform: 'rotate(180deg)',
            marginLeft: 'auto',
            transition: theme.transitions.create('transform', {
                duration: theme.transitions.duration.shortest,
            }),
        },
        expandOpen: {
            transform: 'rotate(0deg)',
        },
        content: {
        position: 'absolute',
        zIndex: 2,
        bottom: 0,
        width: '100%',
        },
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
                    <InfoCaption>{animal.bio}</InfoCaption>
                </Info>
                
                <CardActions disableSpacing>
                    <IconButton aria-label="add to favorites">
                    <FavoriteIcon />
                    </IconButton>
                    <IconButton aria-label="share">
                    <ShareIcon />
                    </IconButton>
                    <IconButton
                    className={clsx(classes.expand, {
                        [classes.expandOpen]: expanded,
                    })}
                    onClick={handleExpandClick}
                    aria-expanded={expanded}
                    aria-label="show more"
                    >
                    <ExpandMoreIcon />
                    </IconButton>
                </CardActions>
                <Collapse in={expanded} timeout="auto" unmountOnExit>
                    <CardContent>
                    <Typography paragraph>Donate:</Typography>
                    <DonateModal />
                    <Typography paragraph>
                        {/* This is the donate popup. */}
                    </Typography>
                    {/* <Typography paragraph>
                        Heat oil in a (14- to 16-inch) paella pan or a large, deep skillet over medium-high
                        heat. Add chicken, shrimp and chorizo, and cook, stirring occasionally until lightly
                        browned, 6 to 8 minutes. Transfer shrimp to a large plate and set aside, leaving chicken
                        and chorizo in the pan. Add pimentón, bay leaves, garlic, tomatoes, onion, salt and
                        pepper, and cook, stirring often until thickened and fragrant, about 10 minutes. Add
                        saffron broth and remaining 4 1/2 cups chicken broth; bring to a boil.
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