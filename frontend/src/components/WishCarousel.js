import React, { useEffect } from 'react'
import WishList from "./WishList"
import { makeStyles } from '@material-ui/core/styles';
import axios from "axios";

export default function WishCarousel(props) {
    
    useEffect(() => {
        axios
        .get('animals/api')
        .then(resp => {
            if (resp.status > 400) {
                return this.setState( () => {
                    return { placeholder: "Something's fucky" }
                })
            }
            console.log(resp)
            return resp.data;
        })
        .then(data => {
            this.setState(() => {
                return {
                    data,
                    loaded: true
                }
            })
        })
    });

    return (
        <WishList animals={this.state.data} />
      );
}