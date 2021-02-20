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
        const fetchData = async () => {
          const result = await axios(
            'wishes/' + id,
          );
     
          setData({wish: result.data});
          console.log(result.data)
        };
     
        fetchData();
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