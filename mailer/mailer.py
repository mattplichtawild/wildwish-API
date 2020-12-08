from decouple import config
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, To
# from sendgrid.helpers.mail.to_email import To

# Use SendGrid Dynamic Templates (https://mc.sendgrid.com/dynamic-templates)

# Argument is 'Donation' object from 'animals' app
def send_recpt(donation):
    
    message = Mail(
        from_email = 'roar@wildheart.foundation',
        to_emails = donation.email,
        # subject = f'Your Donation to {donation.wish.animal.name}',
        # html_content = '<strong>Hey thanks for donating.</strong>'
    )
    
    message.dynamic_template_data = {
        'subject': f'Your Donation to {donation.wish.animal.name}',
        'name': donation.first_name,
        'animal_name': donation.wish.animal.name
    }
    
    # SG template name: Donation Receipt
    message.template_id = 'd-397bbaeafd9e4933934aa42d1826d7fc'

    try:
        sg = SendGridAPIClient(config('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.body)    
        

def send_donor_imgs(wish):
    print(f'Images from {wish.animal.name}\'s wish have been emailed.')
    
    # Get list of emails from wish.donations
    # The to array must at least have an email parameter with a valid email address and it may also contain a name parameter
    # {"email": "example@example.com", "name": "Example Recipient"}
    d_set = wish.donation_set.all()
    email_list = []
    for d in d_set:
        # Needs logic to check if email is valid
        rec_obj = To(email=d.email, name=d.first_name, substitutions=None)
        
        email_list.append(rec_obj)
        
        # if d.
    
    print(email_list)
        
    message = Mail(
        from_email = 'roar@wildheart.foundation',
        to_emails = email_list,
        # subject = f'Your Donation to {donation.wish.animal.name}',
        # html_content = '<strong>Hey thanks for donating.</strong>'
    )
    
    message.dynamic_template_data = {
        'subject': f'Thanks to you, {wish.animal.name} got their wish',
        # How to handle substitutions for multiple name list?
        # 'name': donation.first_name,
        'animal_name': wish.animal.name
    }
    
    # SG template name: Wish Image Update
    message.template_id = 'd-6bcd2497b984421da06081c03982f718'

    try:
        sg = SendGridAPIClient(config('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.body)    
    