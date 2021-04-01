import React, { Component, useEffect, useState } from 'react'
import { makeStyles } from '@material-ui/core/styles';
import axios from "axios";
import { useParams } from 'react-router-dom'
import { CircularProgress, Divider, Typography } from '@material-ui/core';
import DonateBox from './DonateBox';
import {Helmet} from "react-helmet";

export default function WishInfoPage() {
    // params from '/wishes/:id/animals/:id' url
    let { wish_id } = useParams();
    const [state, setState] = useState({ wish: null });

    useEffect(() => {
        const fetchData = async () => {
            const wishResp = await axios(
                'wishes/' + wish_id,
            );

            // const animalResp = await axios(
            //     'animals/' + animal_id
            // )

            // setState({ wish: wishResp.data, animal: animalResp.data})
            setState({ wish: wishResp.data})
        }

        fetchData();
    }, []);
    
    const remaining_funding = () => {
        return (parseInt(state.wish.toy.price) - parseInt(state.wish.current_funding))
    }

    if (state.wish) {
        console.log(state)
        return (
            <div >
            <Helmet>
                <title>Make {state.wish.animal.name}'s wish come true!</title>
                <meta charSet="utf-8" />
                <meta property="og:url" content={"http://dev.wildwish.com/#/wishes/" + state.wish.id} />
                <meta property="og:type" content="website" />
                <meta property="og:title" content={"Make " + state.wish.animal.name + "'s wish come true!"}/>
                <meta property="og:description" content={state.wish.animal.name + " is getting a " + state.wish.toy.name + "!"} />
                <meta property="og:image" content={state.wish.animal.images[0].upload} />
                {/* <meta property="og:image:width" content='600' />
                <meta property="og:image:height" content='600' /> */}
                <link rel="canonical" href={"http://dev.wildwish.com/#/wishes/" + state.wish.id} />
            </Helmet>
           
            <Typography variant='h2' >{state.wish.animal.name}</Typography>
            <Typography variant='body2' >{state.wish.animal.zoo.name}</Typography>
            <Typography variant='body2' >{state.wish.animal.zoo.city}, {state.wish.animal.zoo.st}</Typography>
            <Divider/>
            {state.wish.active ?
            <>
            <Typography variant='overline' >${remaining_funding()} remaining!</Typography> 
            <Typography variant='body1' >{state.wish.animal.name} is getting a {state.wish.toy.name}!</Typography>
            <Typography variant='body1' >{state.wish.toy.description}</Typography>
            <DonateBox data={state.wish} />
            </>
            :
            <>
            <Typography variant='overline' >Wish fulfilled!</Typography> 
            <Typography variant='body1' >{state.wish.animal.name} received a {state.wish.toy.name}!</Typography>
            <Typography variant='body1' >{state.wish.toy.description}</Typography>
            </>
            }
            </div>
            )
        } else {
            return (
                <CircularProgress />
            
        )
    }
}