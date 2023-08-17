import yaml

with open('settings.yml', 'r') as file:
    settings = yaml.safe_load(file)

time_settings = settings['time_settings']
email_settings = settings['email_settings']
options = settings['options']

cycle_timer = time_settings['cycle_timer']
specified_time = time_settings['specified_time']
timer = time_settings['timer']
each_time = time_settings['each_time']

email_sender = email_settings['email_sender']
email_password = email_settings['email_password']
email_targets = email_settings['email_targets']

email_name = email_settings['email_name']
email_subject = email_settings['email_subject']

smtp_server = email_settings['smtp_server']
smtp_port = email_settings['smtp_port']

send_email = options['send_email']

file_list = settings['file_list']

def get_email_content_header():
    email_content_header = email_settings['email_content_header']
    if email_content_header is None:
        email_content_header = "PowerBi Autobot Report"
    return email_content_header

def get_email_content_body():
    email_content_body = email_settings['email_content_body']
    if email_content_body is None:
        email_content_body = '<p style="color:red;">Este e-mail foi enviado automaticamente, não o responda.</p>'
        email_content_body += '<p>Alerta de erro.</p>'
    else:
        email_content_body = '<p>'+email_content_body+'</p>'
    return email_content_body

