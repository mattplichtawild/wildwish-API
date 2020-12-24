import React, { Component } from "react";
import { makeStyles } from '@material-ui/core/styles';
import Box from '@material-ui/core/Box';
import Card from '@material-ui/core/Card';
import CardMedia from '@material-ui/core/CardMedia';
import {
  Info,
  InfoCaption,
  InfoSubtitle,
  InfoTitle,
} from '@mui-treasury/components/info';
import { useGalaxyInfoStyles } from '@mui-treasury/styles/info/galaxy';
import { useCoverCardMediaStyles } from '@mui-treasury/styles/cardMedia/cover';
import { Button } from "@material-ui/core";

function AnimalCard(props) {
    const animal = props.animal
    const useStyles = makeStyles(() => ({
        card: {
        borderRadius: '1rem',
        boxShadow: 'none',
        position: 'relative',
        minWidth: 200,
        minHeight: 360,
        width: '100%',
        '&:after': {
            content: '""',
            display: 'block',
            position: 'absolute',
            width: '100%',
            height: '75%',
            bottom: 0,
            zIndex: 1,
            background: 'linear-gradient(to top, #000, rgba(0,0,0,0))',
        },
        },
        content: {
        position: 'absolute',
        zIndex: 2,
        bottom: 0,
        width: '100%',
        },
    }));

    const mediaStyles = useCoverCardMediaStyles({ bgPosition: 'top' });
    const styles = useStyles();

    const handleClick = () => {
        alert('clicked')
        // open modal window for donation form

    }

    return (
        <div>
            <Card className={styles.card}>
                <CardMedia
                classes={mediaStyles}
                image={animal.recent_img.upload}
                />
                <Box py={3} px={2} className={styles.content}>
                <Info useStyles={useGalaxyInfoStyles}>
                    <InfoTitle>{animal.name}</InfoTitle>
                    <InfoSubtitle>{animal.zoo}</InfoSubtitle>
                    <InfoCaption>{animal.bio}</InfoCaption>
                </Info>
                <Button 
                variant='outlined' 
                color='primary' 
                onClick={() => handleClick()} 
                >
                    Donate
                </Button>
                </Box>
            </Card>
        </div>
        
    )
}

export default AnimalCard;