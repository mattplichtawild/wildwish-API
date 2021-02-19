import React, { Component, useEffect, useState } from 'react'
import { makeStyles } from '@material-ui/core/styles';
import axios from "axios";
import { useParams } from 'react-router-dom'


export default function WishInfoPage(props) {
    // id used by react router
    let { id } = useParams();

    const [data, setData] = useState({ });

    useEffect(async () => {
        const result = await axios(
          'wishes/' + id,
        );
     
        setData(result.data);
    }, []);
    
    
    return (
        <div> This is the wish info page for Wish ID {id}</div>
    )
}