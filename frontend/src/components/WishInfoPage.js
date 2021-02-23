import React, { Component, useEffect, useState } from 'react'
import { makeStyles } from '@material-ui/core/styles';
import axios from "axios";
import { useParams } from 'react-router-dom'

export default function WishInfoPage(props) {
    // id used by react router
    let { id }  = useParams();

    const [data, setData] = useState();

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
     
          setData({wish: result.data});
          console.log(result.data)
        };
     
        // Change this so it only fires if wishData doesn't have an image_set
        const fetchAnimalData = async () => {
            const result = await axios(
                'animals/' + data.wish.animal_id
            )
        }

        // Wait for wishData promise to resolve before trying to set animalData
        // Could also utilize params if url was changed to 'animals/:id/wishes/:id'
        fetchWishData()
        .then(fetchAnimalData())

        console.log(data)
    }, []);
    

    if (data == undefined) {
        return (
            <div> Loading Wish ID {id}</div>
        )
        } else {
        return (
            <div> This is the wish info page for Wish ID {data.wish.id}. The wish is for Animal ID {data.wish.animal_id}</div>
        )
    }
}