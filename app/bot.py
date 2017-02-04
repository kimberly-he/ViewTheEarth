from kik_config import kik
from kik.messages import messages_from_json, TextMessage, StartChattingMessage, \
    TextResponse
from flask import request, Response, Blueprint
from handler import Handler
from google_map import GoogleMap
from random import shuffle

bot = Blueprint('simple_page', __name__)


@bot.route('/incoming', methods=['POST'])
def incoming():
    if not kik.verify_signature(request.headers.get('X-Kik-Signature'), request.get_data()):
        return Response(status=403)

    messages = messages_from_json(request.json['messages'])

    for message in messages:
        if isinstance(message, TextMessage):
            Handler.check_the_answer(message.from_user, message.chat_id, message.body)
            send_a_game(message)
        elif isinstance(message, StartChattingMessage):
            Handler.handle_new_user(message.from_user, message.chat_id)
            send_a_game(message)

    return Response(status=200)


def send_a_game(message):
    pic_url, countries = GoogleMap.get_street_view()
    Handler.send_picture_message(message.from_user, message.chat_id, pic_url)
    body = 'Make a guess! Where are you right now?'
    countries_text = []
    keyboards = []
    for country in countries:
        countries_text.append(country.name)
    Handler.update_last_guess(message.from_user, countries[0])
    # make the order of the countries random
    shuffle(countries_text)
    for country in countries_text:
        keyboards.append(TextResponse(country))

    Handler.send_text_message(message.from_user, message.chat_id, body, keyboards)



