import React, { Component, useEffect, useState } from 'react'
import { makeStyles } from '@material-ui/core/styles';
import axios from "axios";
import { useParams } from 'react-router-dom'

export default function WishInfoPage(props) {
    // id used by react router
    let { animal_id, wish_id }  = useParams();
    const [state, setState] = useState({ wish: null, animal: null });
            
    useEffect(() => {
        const fetchData = async () => {
            const wishResp = await axios(
                'wishes/' + wish_id,
            );

            const animalResp = await axios(
                'animals/' + animal_id
            )

            setState({ wish: wishResp.data, animal: animalResp.data})
        }

        fetchData();
    }, []);
    

    // state.animal.id != undefined && state.wish.id != undefined
    if (state.animal && state.wish) {
        console.log(state)
        return (
            <div> 
                <p>This is the wish info page for Wish ID {state.wish.id}. The wish is for {state.animal.name}</p>
                {/* <p>{props.animal.name}</p> */}
            </div>
            )
        } else {
            return (
            <div> Loading Wish ID {wish_id}</div>
        )
    }
}