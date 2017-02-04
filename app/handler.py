from kik_config import kik
from kik.messages import TextMessage, PictureMessage, SuggestedResponseKeyboard, \
    TextResponse
from app import db
from models import User


class Handler(object):
    @staticmethod
    def send_text_message(to, chat_id, body, keyboards=[], hidden=False):
        message = TextMessage(to=to, chat_id=chat_id, body=body)
        print to
        print chat_id
        print body
        print keyboards
        if len(keyboards) > 0:
            message.keyboards.append(
                SuggestedResponseKeyboard(
                    hidden=hidden,
                    responses=keyboards
                )
            )

        kik.send_messages([
            message
        ])

    @staticmethod
    def send_picture_message(to, chat_id, pic_url):
        kik.send_messages([
            PictureMessage(
                to=to,
                chat_id=chat_id,
                pic_url=pic_url
            )
        ])

    @staticmethod
    def handle_new_user(to, chat_id):
        message = 'Hey there, I will take you anywhere on the earth! Jump on and enjoy.'
        Handler.send_text_message(to, chat_id, message)
        message = 'Check out the picture below. Can you guess which country you just saw?'
        Handler.send_text_message(to, chat_id, message)
        db.session.add(User(to, chat_id))
        db.session.commit()

    @staticmethod
    def update_last_guess(user_name, country):
        print 'updating...'
        print user_name
        print country
        db.session.query(User).filter_by(name=user_name).update({"last_country": country.name})
        db.session.commit()
        print 'finished...'

    @staticmethod
    def check_the_answer(user_name, chat_id, answer):
        user = db.session.query(User).filter_by(name=user_name).first()
        print user
        if user is None:
            db.session.add(User(user_name, chat_id))
            db.session.commit()
        else:
            if user.last_country == answer:
                win = user.win
                win += 1
                db.session.query(User).filter_by(name=user_name).update({"win": win})
                Handler.send_text_message(user_name, chat_id, 'You are correct!')
            else:
                lose = user.lose
                lose += 1
                db.session.query(User).filter_by(name=user_name).update({"lose": lose})
                Handler.send_text_message(user_name, chat_id, 'You are wrong! Correct one is ' + user.last_country)
            db.session.commit()



