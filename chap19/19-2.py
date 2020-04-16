"""
メール送受信処理
smtplibとemailモジュール
 通信部分をsmtplib，MIME文章構築をemailモジュールが担当する
"""
"""
メールを送信する
import smtplib
s=smtplib.SMTP('localhost:25')
s.sendmail(
    'from@youremail.com',
    ['to@yourfriendemail.com'],
    'hello,message!'
)
s.close()
"""
"""
外部メールサーバから送信
s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo() ehloaでESMTPサーバに身元を明かす
s.starttls() TLSモードで通信開始
s.ehlo()
s.login('yourmail@gmail.com', 'password') SMTPサーバにログイン
s.sendmail(
    'yourmail@gmail.com',
    ['to@friendmail.com'],
    'hello'
)
s.close()
"""
"""
#メッセージを構築する
# emailモジュールを使うと，MIME文書を構造的に構築できる
from email.mime import text
from email.utils import formatdate

FROM_ADDR = 'from@youremail.com'
TO_ADDR = 'to@yourfriendemail.com'

message = text.MIMEText(
    'hello,body',
    'plain',
)

message['Subject'] = 'Hello, subject!'
message['From'] = FROM_ADDR
message['To'] = TO_ADDR
message['Date'] = format_datetime()

s = smtplib.SMTP('localhost:25')
s.sendmail(
    FROM_ADDR,
    [TO_ADDR],
    message.as_string()
)
s.close()
"""

#日本語対応
import smtpd
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formatdate
'''
FROM_ADDR = 'from@youremail.com'
TO_ADDR = 'to@yourfriendemail.com'
ENCODING = 'iso-2022-jp'

message = MIMEText(
    'こんにちは，本文！'.encode(ENCODING),
    'plain',
    ENCODING,
)

message['Subject'] = str(Header('こんにちは，件名',ENCODING))
message['From'] = '%s <%s>'%(
    str(Header('あなた', ENCODING)),
    FROM_ADDR,
)
message['To'] = '%s <%s>'%(
    str(Header('友人',ENCODING)),
    TO_ADDR,
)
message['Date'] = formatdate()
'''
'''
CCやBCCでメールを送信
 CCやBCCの設定は
 まずCCのアドレスをMIMETextオブジェクトのヘッダ情報に設定する
 次にsendmailメソッドの宛先アドレスの引数において，元の宛先と共にCCやBCCのアドレスを追加する
 CCに複数のメールアドレスを追加したい場合はカンマでメールアドレス同士を結合する
'''
