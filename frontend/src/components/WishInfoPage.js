import React, { Component, useEffect, useState } from 'react'
import { makeStyles } from '@material-ui/core/styles';
import axios from "axios";
import { useParams } from 'react-router-dom'
import { Divider, Typography } from '@material-ui/core';
import DonateBox from './DonateBox';

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
            // <div> 
            //     <p>This is the wish info page for Wish ID {state.wish.id}. The wish is for {state.wish.animal.name}.</p>
            // </div>
            <div>
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
            <div> Loading Wish ID {wish_id}</div>
        )
    }
}