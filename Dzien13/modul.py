
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def wyslij_mail(temat, tresc):
    """
    Funkcja, która wysła maila o określonym temacie i treści do "isapy@o2.pl"

    :param temat: temat maila
    :param tresc: tresc maila
    :return:
    """

    mail = MIMEMultipart()
    mail["Subject"] = temat
    mail["To"] = 'isapy@o2.pl'
    mail["From"] = 'isapy@int.pl'

    body = MIMEText(tresc)
    mail.attach(body)

    serwer = smtplib.SMTP('poczta.int.pl')
    serwer.login('isapy@int.pl', 'isapython;')
    serwer.send_message(mail)
    serwer.quit()

    print("Wysłano mail!")