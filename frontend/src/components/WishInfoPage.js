import React, { Component, useEffect, useState } from 'react'
import { makeStyles } from '@material-ui/core/styles';
import axios from "axios";
import { useParams } from 'react-router-dom'

export default function WishInfoPage(props) {
    // id used by react router
    let { id }  = useParams();

    const [state = {}, setState] = useState();

    // useEffect(async () => {
    //     const result = await axios(
    //       'wishes/' + id,
    //     );
     
    //     setData(result.data);
    //     console.log(result.data)
    //     console.log(data)
    // }, []);
    
    useEffect(() => {
        // could rewrite this so 'url' is parameter
        const fetchWishData = async () => {
          const result = await axios(
            'wishes/' + id,
          );
     
          setState(result.data);
          console.log(result.data)
        };
     
        // Change this so it only fires if wishData doesn't have an image_set
        const fetchAnimalData = async () => {
            console.log(state.animal_id)
            const result = await axios(
                'animals/' + state.animal_id
            )
        }

        // Wait for wishData promise to resolve before trying to set animalData
        // Could also utilize params if url was changed to 'animals/:id/wishes/:id'
        fetchWishData()
        // .then(fetchAnimalData())

        console.log(state)
    }, []);
    

    if (state != undefined && state.id != undefined) {
        return (
            <div> This is the wish info page for Wish ID {state.id}. The wish is for Animal ID {state.animal_id}</div>
            )
        } else {
            return (
            <div> Loading Wish ID {id}</div>
        )
    }
}