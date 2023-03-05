def enviarEmail(nome, destinatario_email, premio, tipo_premio):

  import smtplib
  import email.message

  PASSWORD = '' # Digite aqui a senha temporária de quem mandará o email

  corpo_texto = f"""
  
  <h1>Congratulações, {nome}</h1>
  <p>Você acaba de ganhar um prêmio no sorteio! Venha para a Rua 42, Quadra 3, Casa 114, Bairroso para retirar seu {tipo_premio} {premio}!</p>
  
  """

  msg = email.message.Message()
  msg['Subject'] = f'Congratulações, {nome}'
  msg['From'] = '' # Digite aqui o email de quem mandará o email
  msg['To'] = destinatario_email
  msg.add_header('Content-Type', 'text/html')
  msg.set_payload(corpo_texto)

  with smtplib.SMTP('smtp.gmail.com: 587') as smtp:
    smtp.starttls()
    smtp.login(msg['From'], PASSWORD)
    smtp.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

  
