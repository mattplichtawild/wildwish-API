import React, { Component, useEffect } from 'react'
import WishList from "./WishList"
import { makeStyles } from '@material-ui/core/styles';
import axios from "axios";
import { CircularProgress } from '@material-ui/core';

export default class WishCarousel extends Component {
    constructor(props) {
        super(props);
        this.state = {
        data: [],
        loaded: false,
        placeholder: "Loading"
        };
    }

    

    componentDidMount() {
        const fetchData = (position) => {
            axios
            .get('wishes/' + this.props.url)
            .then(resp => {
                if (resp.status > 400) {
                    return this.setState( () => {
                        return { placeholder: "Something's fucky" }
                    })
                }
                console.log(resp)
                // console.log(position)
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
        }

        // Using navigator.geolocation times out, don't use
        // const error = (err) => {
        //     console.warn(`ERROR(${err.code}): ${err.message}`);
        //   }
        
        // navigator.geolocation.getCurrentPosition(fetchData, error, {timeout:60000, enableHighAccuracy: false})
        fetchData()
    };

    render() {
        if (this.state.data.length) {
            if (this.props.url === 'nearby' && !("geolocation" in navigator)) {
                return (
                    <h1>Turn on location please</h1>
                )
            } else {
            return (
                <WishList data={this.state.data} />
            );
            }
        } else {
            return <CircularProgress />
        }
    }
}