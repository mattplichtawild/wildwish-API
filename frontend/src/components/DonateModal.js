import React from 'react'
import { Button, Form, Header, Icon, Modal } from 'semantic-ui-react'

function DonateModal() {
  const [open, setOpen] = React.useState(false)

  function handleSubmit(e) {
      alert('clicked');
    e.preventDefault();
    // whatever you want to do when user submits a form
  };

  return (
    <Modal
      closeIcon
    //   as={Form}
    //   onSubmit={e => handleSubmit(e)}
      open={open}
      trigger={<Button>Donate</Button>}
      onClose={() => setOpen(false)}
      onOpen={() => setOpen(true)}
    >
      <Header icon='archive' content='Archive Old Messages' />
      <Modal.Content>
        <p>
          Your inbox is getting full, would you like us to enable automatic
          archiving of old messages?
        </p>
      </Modal.Content>
      <Modal.Actions>
        <Button color='red' onClick={() => setOpen(false)}>
          <Icon name='remove' /> No
        </Button>
        <Button color='green' onClick={() => setOpen(false)}>
          <Icon name='checkmark' /> Yes
        </Button>
      </Modal.Actions>
    </Modal>
  )
}

export default DonateModal;