import React, { Component, useEffect, useState } from 'react'
import { makeStyles } from '@material-ui/core/styles';
import axios from "axios";
import { useParams } from 'react-router-dom'

export default function WishInfoPage(props) {
    // id used by react router
    let { animal_id, wish_id }  = useParams();
    const [state = {}, setState] = useState({ wish: {}, animal: {} });
    
    let wish = state.wish
    let animal = state.animal

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
            'wishes/' + wish_id,
            );
            
            setState({...state}, state.wish=result.data);
              console.log(state)
        };
        
        // Change this so it only fires if wishData doesn't have an image_set
        const fetchAnimalData = async () => {
            const result = await axios(
                'animals/' + animal_id
                )
                
                setState({...state}, state.animal=result.data);
                // console.log(result.data)
                console.log(state)
            };
            
        // Wait for wishData promise to resolve before trying to set animalData
        // Could also utilize params if url was changed to 'animals/:id/wishes/:id'
        fetchAnimalData()
        fetchWishData()

        // console.log(state)
    }, []);
    

    // state.animal.id != undefined && state.wish.id != undefined
    if (state.animal && state.wish) {
        // console.log(props)
        // console.log(state)
        // console.log(state)
        return (
            <div> 
                <p>This is the wish info page</p>
                <p>This is the wish info page for Wish ID {state.wish.id}. The wish is for Animal ID {state.animal.id}</p>
                {/* <p>{props.animal.name}</p> */}
            </div>
            )
        } else {
            return (
            <div> Loading Wish ID {wish_id}</div>
        )
    }
}