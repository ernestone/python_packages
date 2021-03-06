#  coding=utf-8
#
#  Author: Ernesto Arredondo Martinez (ernestone@gmail.com)
#  Created: 7/6/19 18:23
#  Last modified: 7/6/19 18:21
#  Copyright (c) 2019

# Functions to send mail from a server (environment variable MAIL_SERVER)

import datetime
import mimetypes
import os
import smtplib, ssl
import warnings
import docutils.core


def set_attachment_to_msg(msg, file_path):
    """

    Args:
        msg (EmailMessage): objecto EmailMessage donde se hara attach
        file_path: path del fichero a vincular al mensaje

    Returns:

    """
    if not os.path.isfile(file_path):
        return

    # Guess the content type based on the file's extension.  Encoding
    # will be ignored, although we should check for simple things like
    # gzip'd or compressed files.
    ctype, encoding = mimetypes.guess_type(file_path)
    if ctype is None or encoding is not None:
        # No guess could be made, or the file is encoded (compressed), so
        # use a generic bag-of-bits type.
        ctype = 'application/octet-stream'
    maintype, subtype = ctype.split('/', 1)
    with open(file_path, 'rb') as fp:
        msg.add_attachment(fp.read(),
                           maintype=maintype,
                           subtype=subtype,
                           filename=os.path.basename(file_path))


def sendMailWithAttach(server=os.environ.get('MAIL_SERVER', 'server-mail.com'),
                       frm='', to='', subject='', body='', lineSep='not_line_separator', files=None,
                       to_html=False):
    """
    Permet enviar un E-mail des de FROM a TO amb SUBJECT amb BOBY line_separator (cas body amb multilinea) i ATTACH

    Args:
        server (str=os.environ.get('MAIL_SERVER'):
        frm (str=""):
        to (str=""):
        subject (str=""):
        body (str=""):
        lineSep (str="not_line_separator"):
        files (list=None): lista de paths de ficheros a adjuntar
        to_html (bool=False): Si true parsea con docutils (reestructuredText [rst], Latex, ...)
                              el texto del body enviado y lo convierte a html

    Returns:

    """
    from email.message import EmailMessage

    msg = EmailMessage()

    msg['From'] = frm
    msg['To'] = to
    msg['Subject'] = subject
    msg.epilogue = ''

    if lineSep != 'not_line_separator' and body.find(lineSep) >= 0:
        body = '\n'.join(body.split(lineSep))

    msg.set_content(body)
    if to_html:
        msg.add_alternative(docutils.core.publish_string(body, writer_name="html").decode('utf-8'), subtype='html')

    if files:
        for file_path in files:
            set_attachment_to_msg(msg, file_path)

    srv = None
    try:
        codi = 0
        context = ssl.create_default_context()
        srv = smtplib.SMTP(server)
        srv.ehlo()
        srv.starttls(context=context)
        srv.ehlo()
        srv.send_message(msg)
    except smtplib.SMTPException:
        # XXX Per motius desconeguts el connection refused tira una excepcio diferent
        codi = 1
    finally:
        if srv:
            srv.quit()

    return codi


FROM_MAIL = 'yourcount@mail.com'


def enviar_mail(subject, body, user_mail_list, to_html=False, *attach_path_files):
    """
    Envia mail desde la cuenta FROM_MAIL a la lista de mails especificados y adjunta los logs del gestor
    si estos han generado entradas

    Args:
        subject (str): Le asignará el nombre de la máquina desde la que está corriendo
        body (str): Texto con el cuerpo del mail. Por defecto buscará '$$NEWLINE$$' para substituir por saltos de línea
        user_mail_list (list): Lista de strings con los correos
        to_html (bool=False): Si true parsea con docutils (reestructuredText [rst], Latex, ...)
                      el texto del body enviado y lo convierte a html
        *attach_path_files: PATHs de ficheros a adjuntar

    Returns:
        ok (bool)
    """
    ok = False
    subject = "{} {}".format(os.getenv("COMPUTERNAME"), subject)

    # SendMail
    try:
        codi = sendMailWithAttach(frm=FROM_MAIL,
                                  to=", ".join(user_mail_list),
                                  subject="{} {}".format(subject,
                                                         datetime.datetime.now().strftime('%Y-%m-%d %H:%M')),
                                  body=body,
                                  lineSep='$$NEWLINE$$',
                                  files=list(attach_path_files),
                                  to_html=to_html)

        ok = (codi == 0)
    except:
        warnings.warn("No se ha podido enviar el mail con subject '{subject}'".format(subject=subject))

    return ok


if __name__ == '__main__':
    import fire

    fire.Fire({
        enviar_mail.__name__: enviar_mail,
    })
