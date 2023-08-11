import requests
import json
import re


from bs4 import BeautifulSoup



def send_marmiton_query(ingredients,prix,difficulte,temps_passe_cuisine):
    print('On cherche des recettes..')
    recette_list = []
    recette_found = 0

    page = 1

    while page < 100:
        try: 
            headers = {
                'authority': 'www.marmiton.org',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
                # 'cookie': 'didomi_token=eyJ1c2VyX2lkIjoiMTg5ZGU3YzEtZmQ5Yy02ZTM5LTgxY2EtNWI2NDgxMWRkNzJlIiwiY3JlYXRlZCI6IjIwMjMtMDgtMTBUMDg6MDc6MDQuOTIzWiIsInVwZGF0ZWQiOiIyMDIzLTA4LTEwVDA4OjA3OjA0LjkyM1oiLCJ2ZW5kb3JzIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIiwiYzppbnN0YWdyYW0tSDl3RGdjRTQiLCJjOmludGVybWFyY2gtTmFyeUJ3VVoiLCJjOnJlbGV2YW5jLURBWXF3SktVIiwiYzpnb29nbGVvcHQtQlp0QUQzVzUiLCJjOm5lc3RsZS1Qa1lIbXBkVSIsImM6cGVybXV0aXZlLU1zeHFXdDhKIiwiYzpwaW50ZXJlc3QtV2FlNmd5SFMiLCJjOnR3aXR0ZXIteko1N2ZtbVoiLCJjOmhlYXRtYXAiLCJjOm1hcm1pdG9uLTZ5bkVxYnRYIiwiYzpmYWNlYm9vay1IVURxR1FnZCIsImM6dGYxLUZwbU5BN0g4IiwiYzo0dy1tYXJrZXRwbGFjZSIsImM6YWRsb29wLVhGNjNRNDdGIiwiYzpmbHltZW51LTY3aFR5ZmI3IiwiYzpxdWFsaWZpby02RmJLQVpSTCIsImM6Z29vZ2xlYW5hLWF6Q2hya1JiIiwiYzp0aWt0b2stS1pBVVFMWjkiLCJjOnFpb3RhLWhVWUhLd3cyIiwiYzptZXRhLVRnTkgyUDNOIl19LCJwdXJwb3NlcyI6eyJlbmFibGVkIjpbIk1lc3VyZWF1ZGllbmNlIiwicmVzZWF1eHNvY2lhdXgiLCJGb25jdGlvbm5hbGl0ZWFtZWxpb3JhdGlvbiIsImRldmljZV9jaGFyYWN0ZXJpc3RpY3MiLCJnZW9sb2NhdGlvbl9kYXRhIl19LCJ2ZW5kb3JzX2xpIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIl19LCJ2ZXJzaW9uIjoyLCJhYyI6IkJfNkFDQl80LkJfNkFDQl80In0=; euconsent-v2=CPwSZUAPwSZUAAHABBENDRCsAP_AAHvAAAAAHfND_TrMYyNj-XZ9Nrs0eYxOxNSXo-wCjAaJAWgBBQKAIJQG0mAQpAHgBCACIAAEIiJBAQIlDCHACQAA4IABASEAIAiABBIIICIAgEAQAwAICBBDCcAAAQKYgAQEEAUAmgoAAAogQAAAIAAABgAAAAAAAAAAAAAAABA1kAEwVJiABsCQgJpoQigRADCIICoBQAUQCQIAAAAKAABBCASAwCAAAQAAAAAAAABEQAIAAAIAAIAAAAOBAAAAAAAAAAAAIBAARAAAgACAAAAAAAQDAAAABQAAAAgACAECEIAAAASAAAAAAAAMAcpACAIsAtAdABAIsEgAgLQFAAQBHDAAIAjiAAEARxIACAI4.f_gAD3gAAAAA; _pbjs_userid_consent_data=7351206224852308; permutive-id=c73d2eba-5869-4020-8831-e0e1273f7fad; lux_uid=169165482521610821; _fbp=fb.1.1691654825304.1732631691; _hjFirstSeen=1; _hjSession_3052633=eyJpZCI6IjhiNTJlMjY3LTU4YzgtNGMwYy05MzE2LTMwYmYwMTRkOWU0NSIsImNyZWF0ZWQiOjE2OTE2NTQ4MjU0NDEsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; _tt_enable_cookie=1; _ttp=I-6s3bAAwP_lUaQLsdnu9TWCJW5; nadz_dailyVisits=1; _cc_id=28ee0354db42b073be3d0dea65a20ffa; panoramaId_expiry=1692259625106; panoramaId=c01d0a3626de1ad705d3d0686352e32246b000a7425356a054c9752949fd1a56; panoramaIdType=panoIndiv; __gads=ID=dd85d18e6a6a903e:T=1691654824:RT=1691654824:S=ALNI_MasO7zz8pR0b7AJwOdWhEkZegVRwQ; __gpi=UID=00000c7c13ec8600:T=1691654824:RT=1691654824:S=ALNI_MZbC6nymTgU6gio_q8DZRjj6ikQEA; TAPAD=%7B%22id%22%3A%22ee131288-0aba-4452-a520-144606bd3fae%22%7D; SA=1; firstid=1c4c032cff3cb1d49db7339967dca3ad; _gid=GA1.2.1149036945.1691654840; _hjSessionUser_3052633=eyJpZCI6ImE0NzA4N2ZmLWZjMjUtNTBhYS1hNGVhLWMzMjk5M2ZlOGM0MSIsImNyZWF0ZWQiOjE2OTE2NTQ4MjU0MjUsImV4aXN0aW5nIjp0cnVlfQ==; beopid=eeef9866-aca8-46ec-bff5-cdd981256b2a; trc_cookie_storage=taboola%2520global%253Auser-id%3D994e1451-89e4-4e64-a5e0-890a2d932f25-tucta246607; af_session=%7B%22visitorId%22%3A%221691654823672779%22%2C%22pageviewId%22%3A3%2C%22sessionStartTime%22%3A1691654823672%2C%22sessionId%22%3A0%2C%22rankId%22%3A0%2C%22waveId%22%3A0%2C%22sessionUtm%22%3Anull%7D; Wysistat=0.975409684411348_1691654824011%C2%A71%C2%A71691654902555%C2%A71%C2%A71691654824%C2%A70.975409684411348_1691654824011%C2%A71725782824011; af_session=%7B%22visitorId%22%3A%221691654823672779%22%2C%22pageviewId%22%3A4%2C%22sessionStartTime%22%3A1691654902200%2C%22sessionId%22%3A0%2C%22rankId%22%3A0%2C%22waveId%22%3A0%2C%22sessionUtm%22%3Anull%7D; cto_bundle=4biEz19aRW5ZaElENUVvYVBZNjRNeHpJJTJCaUtxUW5IMjlKam5mc3V5RHo5OE1GZWtPenlTS0thcWlPVE83d29seFNVall4eEUxQkRxclgzRWs1S1hTcUR6YXJPTEVwbk5vZHlkelBlRlhTaTJzdnJVdXc4YmVQR0Z5SFQxandkRW9BVXhMallsd2JGVVZZbzRhTEVDY1klMkZvZWlRJTNEJTNE; _ga_1QKNB5N4F4=GS1.1.1691654825.1.1.1691654905.51.0.0; _ga=GA1.1.686638979.1691654825; FCNEC=%5B%5B%22AKsRol9aO8rj7bOBSezyTFY7f85UD-eOU41zL5t78G-Nw6bLQvh9P-XQ8EqYcj0A2fsucEc3UQgJgVoPJKe1a0VyH3EoeOmyU1KeQyx84JNij4NgvhG-u2CcpYddrcxJGNeb7u-BZfsgz7R2Sk2Zcs5pkTnibz76bQ%3D%3D%22%5D%2Cnull%2C%5B%5B5%2C%2271%22%5D%5D%5D; arp_scroll_position=300',
                'referer': 'https://www.marmiton.org/barbecue-pique-nique/les-grillades-tp124672.html',
                'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
            }
            
            params = {
                'aqt': ingredients,
                'page': page,
                'exp': prix,
                'dif': difficulte,
                'ttls' : temps_passe_cuisine
            }

            response = requests.get('https://www.marmiton.org/recettes/recherche.aspx', params=params, headers=headers)
            if response.status_code == 200:
                html = BeautifulSoup(response.text, "html.parser")
                
                recettes_div = html.find('div',{"class":"SHRD__sc-juz8gd-1 kOwNOA"})

                recettes_number_span = recettes_div.find('span',{'class':'MRTN__sc-16jp16z-2 elDEAz'})
                if recettes_number_span is not None:
                    recettes_number_span = recettes_number_span.text.strip()
                    recettes_trouvee = re.findall(r'\d+', recettes_number_span)
                    if recettes_trouvee:
                        recette_found = recettes_trouvee[0]
                
                recettes = recettes_div.find('div',{'class':'MRTN__sc-1gofnyi-0 YLcEb'}).find_all('a')
                for recette in recettes:
                    recette_link = f'https://www.marmiton.org{recette["href"]}'

                    recette_name = recette.find('h4',{'class' : 'MRTN__sc-30rwkm-0 dJvfhM'})
                    if recette_name is not None:
                        recette_name = recette_name.text.strip()
                    
                    recette_note = recette.find('span',{'class':'SHRD__sc-10plygc-0 jHwZwD'})
                    if recette_note is not None:
                        recette_nbr_avis = recette.find('div',{'class':'MRTN__sc-30rwkm-3 fyhZvB'})
                        if recette_nbr_avis is not None:
                            recette_nbr_avis = recette_nbr_avis.text.strip().replace(')','').replace('(','').replace('avis','')
                            recette_note = f'{recette_note.text.strip()} basé sur {recette_nbr_avis}avis'
                        else:
                            recette_note = recette_note.text.strip()

                    recette_image = recette.find('img')
                    if recette_image is not None:
                        recette_image = recette_image["src"]

                    recette_obj = {
                        "recette_link":recette_link,
                        "recette_name":recette_name,
                        "recette_note":recette_note,
                        "recette_image":recette_image
                    }
                    recette_list.append(recette_obj)

                page += 1
            elif response.status_code == 404:
                page = 100
            else:
                print(f'Erreur ({response.status_code})')
        except Exception as e:
            print('Une erreur est survenue ! ',e)
    
    print(f'{recette_found} recette(s) trouvée(s)')
    return recette_list

def add_to_fav_marmiton(s,headers,fav_id):
    try:
        response = s.post(f'https://api-uno.marmiton.org/recipe/notebook/{fav_id}', headers=headers, json={})
        if response.status_code == 200:
            print('Recette ajoutée au favoris avec succès!')
            return True
        else:
            print(f'Erreur de connection ({response.text})')
            return False
        
    except Exception as e:
        print("Erreur de connection ",e)
        return False


def login_to_marmiton(email,password):
    try:
        s = requests.Session()
        headers = {
            'authority': 'api-uno.marmiton.org',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/json',
            # 'cookie': 'didomi_token=eyJ1c2VyX2lkIjoiMTg5ZGViMjEtZDcxOC02NDMxLWIyM2QtMzRhY2EyZTFiNzlhIiwiY3JlYXRlZCI6IjIwMjMtMDgtMTBUMDk6MDY6MDMuNDM0WiIsInVwZGF0ZWQiOiIyMDIzLTA4LTEwVDA5OjA2OjAzLjQzNFoiLCJ2ZW5kb3JzIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIiwiYzppbnN0YWdyYW0tSDl3RGdjRTQiLCJjOmludGVybWFyY2gtTmFyeUJ3VVoiLCJjOnJlbGV2YW5jLURBWXF3SktVIiwiYzpnb29nbGVvcHQtQlp0QUQzVzUiLCJjOm5lc3RsZS1Qa1lIbXBkVSIsImM6cGVybXV0aXZlLU1zeHFXdDhKIiwiYzpwaW50ZXJlc3QtV2FlNmd5SFMiLCJjOnR3aXR0ZXIteko1N2ZtbVoiLCJjOmhlYXRtYXAiLCJjOm1hcm1pdG9uLTZ5bkVxYnRYIiwiYzpmYWNlYm9vay1IVURxR1FnZCIsImM6dGYxLUZwbU5BN0g4IiwiYzo0dy1tYXJrZXRwbGFjZSIsImM6YWRsb29wLVhGNjNRNDdGIiwiYzpmbHltZW51LTY3aFR5ZmI3IiwiYzpxdWFsaWZpby02RmJLQVpSTCIsImM6Z29vZ2xlYW5hLWF6Q2hya1JiIiwiYzp0aWt0b2stS1pBVVFMWjkiLCJjOnFpb3RhLWhVWUhLd3cyIiwiYzptZXRhLVRnTkgyUDNOIl19LCJwdXJwb3NlcyI6eyJlbmFibGVkIjpbIk1lc3VyZWF1ZGllbmNlIiwicmVzZWF1eHNvY2lhdXgiLCJGb25jdGlvbm5hbGl0ZWFtZWxpb3JhdGlvbiIsImRldmljZV9jaGFyYWN0ZXJpc3RpY3MiLCJnZW9sb2NhdGlvbl9kYXRhIl19LCJ2ZW5kb3JzX2xpIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIl19LCJ2ZXJzaW9uIjoyLCJhYyI6IkJfNkFDQl80LkJfNkFDQl80In0=; euconsent-v2=CPwSZUAPwSZUAAHABBENDRCsAP_AAHvAAAAAHfND_TrMYyNj-XZ9Nrs0eYxOxNSXo-wCjAaJAWgBBQKAIJQG0mAQpAHgBCACIAAEIiJBAQIlDCHACQAA4IABASEAIAiABBIIICIAgEAQAwAICBBDCcAAAQKYgAQEEAUAmgoAAAogQAAAIAAABgAAAAAAAAAAAAAAABA1kAEwVJiABsCQgJpoQigRADCIICoBQAUQCQIAAAAKAABBCASAwCAAAQAAAAAAAABEQAIAAAIAAIAAAAOBAAAAAAAAAAAAIBAARAAAgACAAAAAAAQDAAAABQAAAAgACAECEIAAAASAAAAAAAAMAcpACAIsAtAdABAIsEgAgLQFAAQBHDAAIAjiAAEARxIACAI4.f_gAD3gAAAAA; _fbp=fb.1.1691658363691.1364674320; _tt_enable_cookie=1; _ttp=X0wSWDndPwABbWDWGQuXiwAWtbV; permutive-id=e1648656-f8bb-44d7-9f55-691ea7564802; _cc_id=27911e9f65271e283e5af95b915bb4cc; panoramaId_expiry=1692263164715; panoramaId=c01d0a3626de1ad705d3d0686352e32246b000a7425356a054c9752949fd1a56; panoramaIdType=panoIndiv; firstid=f6618a6fb70b184c1323ce867e2211ef; _hjSessionUser_3052633=eyJpZCI6Ijk0YWJlMGIxLWVkYWUtNWJlNy1iMjUyLTc4NTAzZGU1ZWRmNSIsImNyZWF0ZWQiOjE2OTE2NTgzNjM5NjgsImV4aXN0aW5nIjp0cnVlfQ==; ___nrbi=%7B%22firstVisit%22%3A1691667469%2C%22userId%22%3A%22c8f2e573-4712-4d6b-b9ba-f7b9cf652f49%22%2C%22userVars%22%3A%5B%5D%2C%22futurePreviousVisit%22%3A1691667469%2C%22timesVisited%22%3A1%7D; compass_uid=c8f2e573-4712-4d6b-b9ba-f7b9cf652f49; ___nrbic=%7B%22previousVisit%22%3A1691667469%2C%22currentVisitStarted%22%3A1691667469%2C%22sessionId%22%3A%22b383cef0-4673-44cd-bead-c009bf1a7479%22%2C%22sessionVars%22%3A%5B%5B%22mrfExperiment_AB%22%2C%221%22%5D%5D%2C%22visitedInThisSession%22%3Atrue%2C%22pagesViewed%22%3A2%2C%22landingPage%22%3A%22https%3A//www.marmiton.org//recettes/recette_clafoutis-fenouil-saumon_90902.aspx%22%2C%22referrer%22%3A%22%22%7D; _hjIncludedInSessionSample_3052633=0; _hjSession_3052633=eyJpZCI6ImUzMzljNTQzLWRiYTItNGI4NC1hNWIzLTk0ZjVmMzM1ZTVmYiIsImNyZWF0ZWQiOjE2OTE3NTc2MzMwMDMsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _gid=GA1.2.955579226.1691759590; __gads=ID=92057c23f84190e7:T=1691658364:RT=1691760143:S=ALNI_MYq0Q0eiwGMtHTSRGu7f3DIZEt-1Q; __gpi=UID=00000c7c16435e9a:T=1691658364:RT=1691760143:S=ALNI_MYyI3Llcjxe1y30EfBsouSK0gfL-g; cto_bundle=2GT6yV85RGRnJTJCa3B1dDJQV3p5UnJSdUxxSnE2JTJGOSUyRkFFSDdNM0RwakNrc3BrNEpQTHNOcVNZcHhpNFhYUmQyNnhnZlVMOUFZTFl4JTJGcnRBa2dUWUlWelZMdlMlMkY5ZmZtR0NlQ3RrWkElMkZRdE8wTEZjNmlwMlZ2bVZaS0ZOSXI0ZXVHdzFtTGRsYWc2WnYzOWFRMjIwbWtyOWNhWiUyQmZpVWNsaXk4dmY1aWVwYlViMXJmR0lLMEVIaWRLQTU2UUVpMG5zNU5yNiUyRlYzNUhmMzR5eFo1SkpjMUt0THNTZyUzRCUzRA; _dc_gtm_UA-1901803-10=1; _dc_gtm_UA-36715846-3=1; _ga_1QKNB5N4F4=GS1.1.1691757633.4.1.1691760426.8.0.0; FCNEC=%5B%5B%22AKsRol8CKBydikKSeQRWedxw8j1dHVZz2fsNYFQo6PgBy-f1iptCurmXQhN91MfikvLpeBpmALB_c1nqnjDkEXRy0OcAMGkbIh_GVw8AVxs1ydijsZ8g2JGXWSqB4meqy-txGW4QE49qR4wKI3MJ9WzQauY-dDGaRg%3D%3D%22%5D%2Cnull%2C%5B%5B5%2C%22258%22%5D%5D%5D; _ga=GA1.2.1585321460.1691658364; _ga_J5V0QJQZFN=GS1.2.1691759589.4.1.1691760439.0.0.0',
            'origin': 'https://www.marmiton.org',
            'referer': 'https://www.marmiton.org/login?callbackUrl=https://www.marmiton.org/login?callbackUrl=https://www.marmiton.org/recettes/recette_clafoutis-fenouil-saumon_90902.aspx',
            'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
            'x-site-id': '13',
        }

        json_data = {
            'usernameOrEmail': email,
            'password': password,
            'email': '',
            'password2': '',
        }

        response = s.post('https://api-uno.marmiton.org/user-login', headers=headers, json=json_data)
        if response.status_code == 200:
            print('Compte connecté avec succès !')
            return {"session":s,"headers":headers}
        else:
            print(f'Erreur de connection ({response.text})')
            return False
        
    except Exception as e:
        print("Erreur de connection ",e)
        return False

    