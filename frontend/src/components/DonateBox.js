import React from 'react'
import DonateModal from './DonateModal' 
// import clsx from 'clsx';
import { Input, Container, IconButton, Typography} from '@material-ui/core'
import AddIcon from '@material-ui/icons/Add';
import RemoveIcon from '@material-ui/icons/Remove'

export default function DonateBox(props) {

    const [amount, setAmount] = React.useState(1)
    const handleChange = (event) => {
        setAmount(event.target.value)
    }

    const increaseAmount = () => {
        setAmount(parseInt(amount) + 1)
    }

    const decreaseAmount = () => {
        if (amount > 1) {
            setAmount(parseInt(amount) - 1)
        }
    }

    return (
        <>
        <Typography variant='overline'>Help their wish come true</Typography>
        <Container name='Amount Pick'>
            <IconButton onClick={decreaseAmount} size='medium' >
                <RemoveIcon fontSize='inherit' color='inherit' />
            </IconButton>
            <Typography variant='overline'>$</Typography>
            <Input 
                id='amount'
                name='amount'
                color='primary'
                // disabled={!hasActiveWish}
                disableUnderline
                type='number'
                inputProps={{min: 1}}
                onChange={handleChange}
                value={amount}
                // inputComponent='number'
            />
            <IconButton onClick={increaseAmount} size='medium' >
                <AddIcon fontSize='inherit' color='inherit'/>
            </IconButton>
            {/* <label htmlFor="amount"/>
            <input type='number' name='amount' id='amount' value={amount} min='1' onChange={handleChange}/> */}
            
            <DonateModal amount={amount} data={props.data} />
        </Container>
        </>
    )
}