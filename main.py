import json
import os
import time
import requests


def text_to_speech(text='Привет друг!'):
    headers = {"Authorization": f"Bearer {os.getenv('API_KEY')}"}
    url = 'https://api.edenai.run/v2/audio/text_to_speech'

    payload = {
        'providers': 'lovoai',
        'language': 'ru-RU',
        # 'option': 'FEMALE',
        # 'lovoai': 'ru-RU_Anna Kravchuk',
        'option': 'MALE',
        'lovoai': 'ru-RU_Alexei Syomin',
        'text': f'{text}'
    }

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    unx_time = int(time.time())

    # with open(f'{unx_time}.json', 'w') as file:
    #     json.dump(result, file, indent=4, ensure_ascii=False)

    audio_url = result.get('lovoai').get('audio_resource_url')
    r = requests.get(audio_url)

    with open(f'{unx_time}.wav', 'wb') as file:
        file.write(r.content)
    

def main():
    text_to_speech(text=' Повседневная практика показывает, что дальнейшее развитие различных форм деятельности способствует подготовки и реализации модели развития.')


if __name__ == '__main__':
    main()
