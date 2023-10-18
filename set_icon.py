



# import requests

# cookies = {
#     'remixscreen_dpr': '1',
#     'remixscreen_depth': '24',
#     'remixluas2': 'ZmEwMGFiNzQ3OWEwZWMzNGZmMWExODUz',
#     'remixdark_color_scheme': '0',
#     'remixcolor_scheme_mode': 'light',
#     'tmr_lvid': 'ca95398f42e562e68c1e94499914f7c0',
#     'tmr_lvidTS': '1590861869071',
#     '_ga': 'GA1.2.1261002999.1677948576',
#     'remixstlid': '9081614195937680450_enfGZcM352K9xqzEMVifkMsh8ZsTXSdiCBLElMSoDh8',
#     'remixstid': '1095409668_Kt9QFGzZbYccyq4sPN3e6fUlFcpDg3EKQIqJpOjaZzk',
#     'remixdt': '7200',
#     'remixuas': 'OTM0ZWUwNGVjNzQyZjJhZGY2MjEyYTA4',
#     'remixdmgr': '53035f5b23715e5559d4a25f53b6d1e56352a8d0d086637092bfaa48462df743',
#     'remixuacck': '2ebea3d3e95e173256',
#     'remixscreen_width': '1920',
#     'remixscreen_height': '1080',
#     'remixscreen_orient': '1',
#     'remixnp': '0',
#     'remixlang': '0',
#     'remixmdevice': '1920/1080/1/!!-!!!!!!!!-/801',
#     'remixff': '10111111111111',
#     'remixmvk-fp': 'a72c750aeb9a358407652b9381a367f8',
#     'remixpuad': 'bJ2RnZWzv3h4QtoFHFcFY4PjlZG5S9TPsyyi2jSjzAM',
#     'remixnsid': 'vk1.a.Oy5Cy-gW1OmcDDKWt0TmlXxcQV-rLx38GdVVgc6qx9p6Q-EIueFHybBiGbZKEPWOhE2Fo3P37MY6sGRsFD3nU7etFD91DjZtRYqz_-8Wzn1GgVvM4Vygsl1NB0dsQQgwVjdfTY-LFvLcBPfzSlPCulTvo-k4cvb9avu52vXArmDW0eE-DGLfUSFBUA3G264G',
#     'remixsid': '1_tBwgDI0_4OsBOnY34vuYFdsUjoQp5Ac11WqZ49ycGxtYiFsmWkeGJ0Pu3YWF5Kn--CCYQVYeyNTbCk_ZK7jMUw',
#     'remixua': '43%7C-1%7C202%7C2246525422',
#     'remixrefkey': 'ee1cef682a2683f95e',
#     'remixgp': '7c67f04ff85ddcbfe6d493ab992998f7',
#     'remixscreen_winzoom': '2.11',
#     'remixseenads': '0',
#     'tmr_detect': '0%7C1697576599269',
# }

# headers = {
#     'authority': 'vk.com',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'accept-language': 'ru,en-US;q=0.9,en-GB;q=0.8,en;q=0.7,ru-RU;q=0.6',
#     'cache-control': 'no-cache',
#     'content-type': 'application/x-www-form-urlencoded',
#     # 'cookie': 'remixscreen_dpr=1; remixscreen_depth=24; remixluas2=ZmEwMGFiNzQ3OWEwZWMzNGZmMWExODUz; remixdark_color_scheme=0; remixcolor_scheme_mode=light; tmr_lvid=ca95398f42e562e68c1e94499914f7c0; tmr_lvidTS=1590861869071; _ga=GA1.2.1261002999.1677948576; remixstlid=9081614195937680450_enfGZcM352K9xqzEMVifkMsh8ZsTXSdiCBLElMSoDh8; remixstid=1095409668_Kt9QFGzZbYccyq4sPN3e6fUlFcpDg3EKQIqJpOjaZzk; remixdt=7200; remixuas=OTM0ZWUwNGVjNzQyZjJhZGY2MjEyYTA4; remixdmgr=53035f5b23715e5559d4a25f53b6d1e56352a8d0d086637092bfaa48462df743; remixuacck=2ebea3d3e95e173256; remixscreen_width=1920; remixscreen_height=1080; remixscreen_orient=1; remixnp=0; remixlang=0; remixmdevice=1920/1080/1/!!-!!!!!!!!-/801; remixff=10111111111111; remixmvk-fp=a72c750aeb9a358407652b9381a367f8; remixpuad=bJ2RnZWzv3h4QtoFHFcFY4PjlZG5S9TPsyyi2jSjzAM; remixnsid=vk1.a.Oy5Cy-gW1OmcDDKWt0TmlXxcQV-rLx38GdVVgc6qx9p6Q-EIueFHybBiGbZKEPWOhE2Fo3P37MY6sGRsFD3nU7etFD91DjZtRYqz_-8Wzn1GgVvM4Vygsl1NB0dsQQgwVjdfTY-LFvLcBPfzSlPCulTvo-k4cvb9avu52vXArmDW0eE-DGLfUSFBUA3G264G; remixsid=1_tBwgDI0_4OsBOnY34vuYFdsUjoQp5Ac11WqZ49ycGxtYiFsmWkeGJ0Pu3YWF5Kn--CCYQVYeyNTbCk_ZK7jMUw; remixua=43%7C-1%7C202%7C2246525422; remixrefkey=ee1cef682a2683f95e; remixgp=7c67f04ff85ddcbfe6d493ab992998f7; remixscreen_winzoom=2.11; remixseenads=0; tmr_detect=0%7C1697576599269',
#     'dnt': '1',
#     'origin': 'https://vk.com',
#     'pragma': 'no-cache',
#     'referer': 'https://vk.com/subbotino_online?act=links',
#     'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'iframe',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
# }

# data = {
#     'act': 'a_photo',
#     'index': '0',
#     'image': 'https://sbm74.ru/kei/sbm74_logo.jpg',
#     'extra': 'link',
#     'hash': '56fed129229fb18224',
# }

# response = requests.post('https://vk.com/share.php', cookies=cookies, headers=headers, data=data)
## parent.onUploadDone(0, {"user_id":14231563,"photo_id":457249409});


import requests

cookies = {
    'remixscreen_dpr': '1',
    'remixscreen_depth': '24',
    'remixluas2': 'ZmEwMGFiNzQ3OWEwZWMzNGZmMWExODUz',
    'remixdark_color_scheme': '0',
    'remixcolor_scheme_mode': 'light',
    'tmr_lvid': 'ca95398f42e562e68c1e94499914f7c0',
    'tmr_lvidTS': '1590861869071',
    '_ga': 'GA1.2.1261002999.1677948576',
    'remixstlid': '9081614195937680450_enfGZcM352K9xqzEMVifkMsh8ZsTXSdiCBLElMSoDh8',
    'remixstid': '1095409668_Kt9QFGzZbYccyq4sPN3e6fUlFcpDg3EKQIqJpOjaZzk',
    'remixdt': '7200',
    'remixuas': 'OTM0ZWUwNGVjNzQyZjJhZGY2MjEyYTA4',
    'remixdmgr': '53035f5b23715e5559d4a25f53b6d1e56352a8d0d086637092bfaa48462df743',
    'remixuacck': '2ebea3d3e95e173256',
    'remixscreen_width': '1920',
    'remixscreen_height': '1080',
    'remixscreen_orient': '1',
    'remixnp': '0',
    'remixlang': '0',
    'remixmdevice': '1920/1080/1/!!-!!!!!!!!-/801',
    'remixff': '10111111111111',
    'remixmvk-fp': 'a72c750aeb9a358407652b9381a367f8',
    'remixpuad': 'bJ2RnZWzv3h4QtoFHFcFY4PjlZG5S9TPsyyi2jSjzAM',
    'remixnsid': 'vk1.a.Oy5Cy-gW1OmcDDKWt0TmlXxcQV-rLx38GdVVgc6qx9p6Q-EIueFHybBiGbZKEPWOhE2Fo3P37MY6sGRsFD3nU7etFD91DjZtRYqz_-8Wzn1GgVvM4Vygsl1NB0dsQQgwVjdfTY-LFvLcBPfzSlPCulTvo-k4cvb9avu52vXArmDW0eE-DGLfUSFBUA3G264G',
    'remixsid': '1_tBwgDI0_4OsBOnY34vuYFdsUjoQp5Ac11WqZ49ycGxtYiFsmWkeGJ0Pu3YWF5Kn--CCYQVYeyNTbCk_ZK7jMUw',
    'remixua': '43%7C-1%7C202%7C2246525422',
    'remixrefkey': 'ee1cef682a2683f95e',
    'remixgp': '7c67f04ff85ddcbfe6d493ab992998f7',
    'remixscreen_winzoom': '2.11',
    'remixseenads': '0',
    'tmr_detect': '0%7C1697576599269',
}

headers = {
    'authority': 'vk.com',
    'accept': '*/*',
    'accept-language': 'ru,en-US;q=0.9,en-GB;q=0.8,en;q=0.7,ru-RU;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'remixscreen_dpr=1; remixscreen_depth=24; remixluas2=ZmEwMGFiNzQ3OWEwZWMzNGZmMWExODUz; remixdark_color_scheme=0; remixcolor_scheme_mode=light; tmr_lvid=ca95398f42e562e68c1e94499914f7c0; tmr_lvidTS=1590861869071; _ga=GA1.2.1261002999.1677948576; remixstlid=9081614195937680450_enfGZcM352K9xqzEMVifkMsh8ZsTXSdiCBLElMSoDh8; remixstid=1095409668_Kt9QFGzZbYccyq4sPN3e6fUlFcpDg3EKQIqJpOjaZzk; remixdt=7200; remixuas=OTM0ZWUwNGVjNzQyZjJhZGY2MjEyYTA4; remixdmgr=53035f5b23715e5559d4a25f53b6d1e56352a8d0d086637092bfaa48462df743; remixuacck=2ebea3d3e95e173256; remixscreen_width=1920; remixscreen_height=1080; remixscreen_orient=1; remixnp=0; remixlang=0; remixmdevice=1920/1080/1/!!-!!!!!!!!-/801; remixff=10111111111111; remixmvk-fp=a72c750aeb9a358407652b9381a367f8; remixpuad=bJ2RnZWzv3h4QtoFHFcFY4PjlZG5S9TPsyyi2jSjzAM; remixnsid=vk1.a.Oy5Cy-gW1OmcDDKWt0TmlXxcQV-rLx38GdVVgc6qx9p6Q-EIueFHybBiGbZKEPWOhE2Fo3P37MY6sGRsFD3nU7etFD91DjZtRYqz_-8Wzn1GgVvM4Vygsl1NB0dsQQgwVjdfTY-LFvLcBPfzSlPCulTvo-k4cvb9avu52vXArmDW0eE-DGLfUSFBUA3G264G; remixsid=1_tBwgDI0_4OsBOnY34vuYFdsUjoQp5Ac11WqZ49ycGxtYiFsmWkeGJ0Pu3YWF5Kn--CCYQVYeyNTbCk_ZK7jMUw; remixua=43%7C-1%7C202%7C2246525422; remixrefkey=ee1cef682a2683f95e; remixgp=7c67f04ff85ddcbfe6d493ab992998f7; remixscreen_winzoom=2.11; remixseenads=0; tmr_detect=0%7C1697576599269',
    'dnt': '1',
    'origin': 'https://vk.com',
    'pragma': 'no-cache',
    'referer': 'https://vk.com/subbotino_online?act=links',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'act': 'add_link',
}

data = {
    'act': 'add_link',
    'al': '1',
    'gid': '7529330',
    'hash': '08f9e7c0705c0e9f9b',
    'index': '0',
    'lid': 'false',
    'lnk': 'https://sbm74.ru/',
    'owner_id': '14231563',
    'photo_id': '457249409',
    'str': 'СБМ74',
}

response = requests.post('https://vk.com/groupsedit.php', params=params, cookies=cookies, headers=headers, data=data)



print(response.text)