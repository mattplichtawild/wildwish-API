import React from 'react'
import Modal from '@material-ui/core/Modal'
import { makeStyles } from '@material-ui/core/styles';
import DonateForm from './DonateForm'

const useStyles = makeStyles((theme) => ({
    paper: {
      position: 'absolute',
      width: 400,
      backgroundColor: theme.palette.background.paper,
      border: '2px solid #000',
      boxShadow: theme.shadows[5],
      padding: theme.spacing(2, 4, 3),
    },
  }));

function DonateModal() {
  const [open, setOpen] = React.useState(false);
  const classes = useStyles();

  function handleSubmit(e) {
      alert('clicked');
    e.preventDefault();
    // whatever you want to do when user submits a form
  };

  const handleOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  const body = (
    <div className={classes.paper}>
      <h2 id="simple-modal-title">Donate!</h2>
      <p id="simple-modal-description">
        Write some bullshit here
      </p>
      {/* <DonateModal /> */}
        <DonateForm />
    </div>
  );

  return (
    <div>
      <button type="button" onClick={handleOpen}>
        Donate
      </button>
      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby="simple-modal-title"
        aria-describedby="simple-modal-description"
      >
        {body}
      </Modal>
    </div>
  );
}

export default DonateModal;