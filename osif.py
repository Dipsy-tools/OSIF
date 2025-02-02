###################################################################
#                        Import Module
import json, sys, hashlib, os, time, marshal, getpass, requests

###################################################################
'''
     kode diperbaharui menggunakan python3
'''
###################################################################

#                             COLOR
if sys.platform in ["linux", "linux2"]:
    W = "\033[0m"
    G = '\033[32;1m'
    R = '\033[31;1m'
else:
    G = ''
    W = ''
    R = ''

###################################################################

#                      Exception
try:
    import requests
except ImportError:
    
    print(('O S I F').center(44))
    print(' ')
    print("[!] Can't import module 'requests'\n")
    sys.exit()

###################################################################

#                    Hapus baris ini (tidak diperlukan di Python 3)
# sys.setdefaultencoding('utf8')

###################################################################

#       	        I don't know
jml = []
jmlgetdata = []
n = []

###################################################################

#                        BANNER
def baliho():
    try:
        token = open('cookie/token.log', 'r').read()
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        a = json.loads(r.text)
        name = a['name']
        n.append(a['name'])

        
        print('ooO--(_)--Ooo'.center(44))
        print(' ' + W)
        print(('[*] ' + name + ' [*]').center(44))
        print(' ')

    except (KeyError, IOError):
        print(R + '_     _'.center(44))
        print(r"o' \\.=./ `o".center(44))
        print('(o o)'.center(44))
        print('ooO--(_)--Ooo'.center(44))
        print(' ' + W)
        print(('O S I F').center(44))
        print(W + '     [' + G + 'Open Source Information Facebook' + W + ']')
        print(' ')

###################################################################

def show_program():
    print('''
                    %sINFORMATION%s
 ------------------------------------------------------

    Author     Dexploit 'Dex'
    Name       OSIF 'Open Source Information Facebook'
    CodeName   DIPSY
    version    full version
    Date       07/11/2019 13:15:09
    Team       Whitehole Security
    Email      dexploit404@gmail.com
    Telegram   @Dexploit404

* if you find any errors or problems, please contact
  author
''' % (G, W))  # Pastikan G dan W sudah terdefinisi di bagian atas

    print('''
     %sCOMMAND                      DESCRIPTION%s
  -------------       -------------------------------------

   get_data           fetching all friends data
   get_info           show information about your friend

   dump_id            fetching all id from friend list
   dump_phone         fetching all phone number from friend list
   dump_mail          fetching all emails from friend list
   dump_<id>_id       fetching all id from your friends <specific>
                      ex: dump_username_id

   token              Generate access token
   cat_token          show your access token
   rm_token           remove access token

   bot                open bot menu

   clear              clear terminal
   help               show help
   about              Show information about this program
   exit               Exit the program
''' % (G, W))

def menu_bot():
    print('''
   %sNumber                  INFO%s
 ---------   ------------------------------------

   [ 01 ]      auto reactions
   [ 02 ]      auto comment
   [ 03 ]      auto poke
   [ 04 ]      accept all friend requests
   [ 05 ]      delete all posts in your timeline
   [ 06 ]      delete all friends
   [ 07 ]      stop following all friends
   [ 08 ]      delete all photo albums

   [ 00 ]      back to main menu
''' % (G, W))

def menu_reaction():
    print('''
   %sNumber                  INFO%s
 ----------   ------------------------------------

   [ 01 ]      like
   [ 02 ]      reaction 'LOVE'
   [ 03 ]      reaction 'WOW'
   [ 04 ]      reaction 'HAHA'
   [ 05 ]      reaction 'SAD'
   [ 06 ]      reaction 'ANGRY'

   [ 00 ]      back to menu bot
''' % (G, W))
####################################################################
#                     GENERATE ACCESS TOKEN
import requests
import os

def login():
    """Menggunakan Access Token Facebook Graph API."""
    access_token = input("Masukkan Access Token Facebook: ").strip()

    # Validasi input token
    if not access_token:
        print("[!] Token tidak boleh kosong.")
        return None

    try:
        # Mengirim permintaan ke Graph API untuk memverifikasi token
        url = f"https://graph.facebook.com/v18.0/me?access_token={access_token}"
        response = requests.get(url)
        
        # Mengecek apakah ada error dalam respon
        user = response.json()

        if "error" in user:
            print(f"[!] Gagal login: {user['error']['message']}")
            return None
        else:
            # Menampilkan nama dan ID pengguna
            print(f"[*] Berhasil login sebagai {user['name']} (ID: {user['id']})")
            
            # Menyimpan token ke file untuk digunakan kembali
            os.makedirs("cookie", exist_ok=True)  # Membuat folder jika belum ada
            with open("cookie/token.log", "w") as f:
                f.write(access_token)
            return access_token
    
    except requests.exceptions.ConnectionError:
        print("[!] Koneksi gagal, coba lagi nanti.")
    except requests.exceptions.RequestException as e:
        print(f"[!] Terjadi kesalahan dalam permintaan: {e}")
    except ValueError as e:
        print(f"[!] Terjadi kesalahan saat memproses respons: {e}")
    except Exception as e:
        print(f"[!] Terjadi kesalahan tak terduga: {e}")

    return None

# Menyimpan token yang berhasil login untuk digunakan di API lain
token = login()

if token:
    print("[*] Token berhasil disimpan dan siap digunakan.")
else:
    print("[!] Gagal mendapatkan token.")

######update11.30######

import requests
import json
import time
import sys

# Fungsi untuk mengambil data dari Graph API
def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Memeriksa apakah ada error HTTP
        data = response.json()
        return data
    except requests.exceptions.ConnectionError:
        print("[!] Koneksi Error! Periksa koneksi internet Anda.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"[!] Terjadi kesalahan dalam permintaan: {e}")
        return None
    except json.decoder.JSONDecodeError:
        print("[!] Gagal memproses respons JSON.")
        return None

# Mendapatkan daftar post di timeline pengguna
def get_posts(access_token):
    print("[*] Mengambil semua post ID...")
    url = f"https://graph.facebook.com/v18.0/me/feed?limit=50&access_token={access_token}"
    result = fetch_data(url)

    if result and "data" in result:
        for post in result["data"]:
            print(f"[*] Post ID: {post['id']}")
        return result["data"]
    else:
        print("[!] Gagal mengambil post atau tidak ada data yang ditemukan.")
        return []

# Contoh penggunaan
if __name__ == "__main__":
    # Masukkan Access Token Facebook di sini
    ACCESS_TOKEN = input("62f8ce9f74b12f84c123cc23437a4a32: ").strip()

    if not ACCESS_TOKEN:
        print("[!] Token tidak boleh kosong.")
        sys.exit(1)

    posts = get_posts(ACCESS_TOKEN)
    if posts:
        print("[*] Daftar post berhasil diambil.")
    else:
        print("[!] Tidak ada post yang ditemukan.")

# Mendapatkan daftar teman
def get_friends(access_token):
    print("[*] Mengambil daftar teman...")
    url = f"https://graph.facebook.com/v18.0/me/friends?limit=5000&access_token={access_token}"
    result = fetch_data(url)

    if result and "data" in result:
        for friend in result["data"]:
            print(f"[*] ID Teman: {friend['id']}")
        return result["data"]
    else:
        print("[!] Gagal mengambil daftar teman!")
        return []
def reaction(posts, amount, reaction_type, token):
	prinr('[*] Start')
	print('[*] All post IDs successfully retrieved')
    try:
        counter = 0
        for post in posts:
            if counter >= amount:
                break
            else:
                counter += 1

            parameters = {'access_token': token, 'type': reaction_type}
            url = f"https://graph.facebook.com/{post['id']}/reactions"
            s = requests.post(url, data=parameters)

            post_id = post['id'].split('_')[0]

            try:
                print(f'\r[{post_id}] {post["message"][:40].replace("\n", " ")}...')
            except KeyError:
                try:
                    print(f'\r[{post_id}] {post["story"].replace("\n", " ")}')
                except KeyError:
                    print(f'\r[{post_id}] Successfully liked')

        print('[*] Done')
        menu_reaction_ask()
    except KeyboardInterrupt:
        print('\r[!] Stopped')
        menu_reaction_ask()
        
        #FFungsi comment
        
        def comment(posts, amount, message, token):
    print('[*] All post IDs successfully retrieved')
    print('[*] Start')

    try:
        counter = 0
        for post in posts:
            if counter >= amount:
                break
            else:
                counter += 1

            parameters = {'access_token': token, 'message': message}
            url = f"https://graph.facebook.com/{post['id']}/comments"
            s = requests.post(url, data=parameters)

            post_id = post['id'].split('_')[0]

            try:
                print(f'[{post_id}] {post["message"][:40].replace("\n", " ")}...')
            except KeyError:
                try:
                    print(f'[{post_id}] {post["story"].replace("\n", " ")}')
                except KeyError:
                    print(f'[{post_id}] Successfully commented')

        print('[*] Done')
        bot()
    except KeyboardInterrupt:
        print('\r[!] Stopped')
        bot()
        
        #FFungsi remove
        
        def remove(posts, token):
    print('[*] All post IDs successfully retrieved')
    print('[*] Start')

    try:
        counter = 0
        for post in posts:
            if counter >= 50:
                break

            url = f"https://graph.facebook.com/{post['id']}?method=delete&access_token={token}"
            r = requests.post(url)
            a = r.json()

            try:
                cek = a['error']['message']
                print(f'[{post["id"]}] Failed')
            except KeyError:
                print(f'[{post["id"]}] Removed')
                counter += 1

        print('[*] Done')
        bot()
    except KeyboardInterrupt:
        print('\r[!] Stopped')
        bot()
        
        #FFungsi confirm
        
        def confirm(posts, token):
    print('[*] All friend requests successfully retrieved')
    print('[*] Start')

    try:
        counter = 0
        for post in posts:
            if counter >= 50:
                break
            else:
                counter += 1

            url = f"https://graph.facebook.com/me/friends/{post['from']['id']}?access_token={token}"
            r = requests.post(url)
            a = r.json()

            try:
                cek = a['error']['message']
                print(f'[{post["from"]["name"]}] Failed')
            except KeyError:
                print(f'[{post["from"]["name"]}] Confirmed')

        print('[*] Done')
        bot()
    except KeyboardInterrupt:
        print('\r[!] Stopped')
        bot()
        
        #FFungsi unfrind
        
        def unfriend(posts, token):
    print('[*] All friends successfully retrieved')
    print('[*] Start')

    try:
        counter = 0
        for post in posts:
            if counter >= 50:
                break

            url = f"https://graph.facebook.com/me/friends/{post['id']}?method=delete&access_token={token}"
            r = requests.post(url)
            a = r.json()

            try:
                cek = a['error']['message']
                print(f'[{post["id"]}] Failed')
            except KeyError:
                print(f'[{post["id"]}] Unfriended')
                counter += 1

        print('[*] Done')
        bot()
    except KeyboardInterrupt:
        print('\r[!] Stopped')
        bot()
        

#	maaf , fitur unfriend saya encrypt karena tidak
#	diperbolehkan oleh para owner bot fb :)
#	buat yg bisa unmarshal , silahkan dipake sendiri ya

	
def unfollow(posts, token):
    print('[*] All IDs successfully retrieved')
    print('[*] Start')

    try:
        counter = 0
        for post in posts['data']:
            if counter >= 50:
                break
            else:
                counter += 1

            url = f"https://graph.facebook.com/{post['id']}/subscribers?method=delete&access_token={token}"
            r = requests.post(url)
            a = r.json()

            try:
                cek = a['error']['message']
                print(f'[{post["name"]}] Failed')
            except KeyError:
                print(f'[{post["name"]}] Unfollowed')

        print('[*] Done')
        bot()
    except KeyboardInterrupt:
        print('\r[!] Stopped')
        bot()
        #ffungsi ffoke
        def poke(posts, token):
    print('[*] All IDs successfully retrieved')
    print('[*] Start')

    try:
        counter = 0
        for post in posts:
            if counter >= 50:
                break
            else:
                counter += 1

            user_id = post['id'].split('_')[0]
            url = f"https://graph.facebook.com/{user_id}/pokes?access_token={token}"
            r = requests.post(url)
            a = r.json()

            try:
                cek = a['error']['message']
                print(f'[{user_id}] Failed')
            except KeyError:
                print(f'[{user_id}] Poked')

        print('[*] Done')
        bot()
    except KeyboardInterrupt:
        print('\r[!] Stopped')
        bot()
    except requests.exceptions.ConnectionError:
        print('[!] Connection Error')
        bot()
        #ffungsi album
        def albums(posts, token):
    print('[*] All IDs successfully retrieved')
    print('[*] Start')

    try:
        counter = 0
        for post in posts:
            if counter >= 50:
                break

            url = f"https://graph.facebook.com/{post['id']}?method=delete&access_token={token}"
            r = requests.post(url)
            a = r.json()

            try:
                cek = a['error']['message']
                print(f'[{post["name"]}] Failed')
            except KeyError:
                print(f'[{post["name"]}] Removed')

        print('[*] Done')
        bot()
    except KeyboardInterrupt:
        print('\r[!] Stopped')
        bot()
    except requests.exceptions.ConnectionError:
        print('[!] Connection Error')
        bot()
######################################################################################################################
#			    Bot reaction
  			   # Prepairing #
def menu_reaction_ask():
    global type

    try:
        cek = input(f'{R}Dipsy{W}/{R}Bot{W}/{R}Reaction{W} >> ')

        if cek in ['1', '01']:
            type = 'LIKE'
            bot_ask()
        elif cek in ['2', '02']:
            type = 'LOVE'
            bot_ask()
        elif cek in ['3', '03']:
            type = 'WOW'
            bot_ask()
        elif cek in ['4', '04']:
            type = 'HAHA'
            bot_ask()
        elif cek in ['5', '05']:
            type = 'SAD'
            bot_ask()
        elif cek in ['6', '06']:
            type = 'ANGRY'
            bot_ask()
        elif cek.lower() == 'menu':
            menu_reaction()
            menu_reaction_ask()
        elif cek.lower() == 'exit':
            print('[!] Exiting program !!')
            sys.exit()
        elif cek.lower() == 'token':
            try:
                with open('cookie/token.log', 'r') as f:
                    print('[!] An access token already exists')
                    cek = input('[?] Are you sure you want to continue [Y/N] ')
                    if cek.lower() != 'y':
                        print('[*] Canceling')
                        bot()
            except IOError:
                pass

            print('\n' + '[*] Generate Access token facebook [*]'.center(44) + '\n')
            print('[Warn] Please turn off your VPN before using this feature !!!')
            id()
        elif cek in ['0', '00']:
            print('[!] Back to bot menu')
            bot()
        else:
            if cek == '':
                menu_reaction_ask()
            else:
                print(f"[!] Command '{cek}' not found")
                print("[!] Type 'menu' to show menu bot")
                menu_reaction_ask()
    except KeyboardInterrupt:
        menu_reaction_ask()

def bot_ask():
    global id, WT, token

    print('[*] Load access token')
    try:
        with open('cookie/token.log', 'r') as f:
            token = f.read()
        print('[*] Success load access token')
    except IOError:
        print('[!] Failed load access token')
        print("[!] Type 'token' to generate access token")
        menu_reaction_ask()

    WT = input(f'{W}[?] [{R}W{W}]allpost or [{R}T{W}]arget ({R}W{W}/{R}T{W}) : ')
    if WT.upper() == 'T':
        id = input('[?] ID Facebook : ')
        if id == '':
            print("[!] ID target can't be empty")
            print('[!] Stopped')
            menu_reaction_ask()
    else:
        WT = 'wallpost'
    like(post(), 50)

def bot():
    global type, message, id, WT, token

    try:
        cek = input(f'{R}D3b2y{W}/{R}Bot{W} >> ')

        if cek in ['1', '01']:
            menu_reaction()
            menu_reaction_ask()
        elif cek in ['2', '02']:
            print('[*] Load access token')
            try:
                with open('cookie/token.log', 'r') as f:
                    token = f.read()
                print('[*] Success load access token')
            except IOError:
                print('[!] Failed load access token')
                print("[!] Type 'token' to generate access token")
                bot()

            WT = input(f'{W}[?] [{R}W{W}]allpost or [{R}T{W}]arget ({R}W{W}/{R}T{W}) : ')
            if WT.lower() == "w" or WT.lower() == '':
                WT = 'wallpost'
            else:
                id = input('[?] ID Target : ')
                if id == '':
                    print("[!] ID target can't be empty")
                    print('[!] Stopped')
                    bot()

            print('--------------------------------------------------')
            print("  [Note] Use the '</>' symbol to change the line\n")

            message = input('[?] Your Message : ')
            if message == '':
                print("[!] Message can't be empty")
                print('[!] Stopped')
                bot()
            else:
                message = message.replace('</>', '\n')

            comment(post(), 50)

        elif cek in ['4', '04']:
            WT = 'req'
            print('[*] Load access token')

            try:
                with open('cookie/token.log', 'r') as f:
                    token = f.read()
                print('[*] Success load access token')
            except IOError:
                print('[!] Failed load access token')
                print("[!] Type 'token' to generate access token")
                bot()
            confirm(post())

        elif cek in ['3', '03']:
            WT = 'wallpost'
            print('[*] Load access token')

            try:
                with open('cookie/token.log', 'r') as f:
                    token = f.read()
                print('[*] Success load access token')
            except IOError:
                print('[!] Failed load access token')
                print("[!] Type 'token' to generate access token")
                bot()
            poke(post())

        elif cek in ['5', '05']:
            WT = 'me'
            print('[*] Load access token')

            try:
                with open('cookie/token.log', 'r') as f:
                    token = f.read()
                print('[*] Success load access token')
            except IOError:
                print('[!] Failed load access token')
                print("[!] Type 'token' to generate access token")
                bot()
            remove(post())

        elif cek in ['6', '06']:
            WT = 'friends'
            print('[*] Load access token')

            try:
                with open('cookie/token.log', 'r') as f:
                    token = f.read()
                print('[*] Success load access token')
            except IOError:
                print('[!] Failed load access token')
                print("[!] Type 'token' to generate access token")
                bot()
            unfriend(post())

        elif cek in ['7', '07']:
            WT = 'subs'
            print('[*] Load access token')

            try:
                with open('cookie/token.log', 'r') as f:
                    token = f.read()
                print('[*] Success load access token')
            except IOError:
                print('[!] Failed load access token')
                print("[!] Type 'token' to generate access token")
                bot()
            unfollow(post())

        elif cek in ['8', '08']:
            WT = 'albums'
            print('[*] Load access token')

            try:
                with open('cookie/token.log', 'r') as f:
                    token = f.read()
                print('[*] Success load access token')
            except IOError:
                print('[!] Failed load access token')
                print("[!] Type 'token' to generate access token")
                bot()
            albums(post())

        elif cek in ['0', '00']:
            print('[*] Back to main menu')
            main()
        elif cek.lower() == 'menu':
            menu_bot()
            bot()
        elif cek.lower() == 'exit':
            print('[!] Exiting program')
            sys.exit()
        elif cek.lower() == 'token':
            try:
                with open('cookie/token.log', 'r') as f:
                    print('[!] An access token already exists')
                    cek = input('[?] Are you sure you want to continue [Y/N] ')
                    if cek.lower() != 'y':
                        print('[*] Canceling')
                        bot()
            except IOError:
                pass

            print('\n' + '[*] Generate Access token facebook [*]'.center(44) + '\n')
            print('[Warn] Please turn off your VPN before using this feature !!!')
            id()
        else:
            if cek == '':
                bot()
            else:
                print(f"[!] Command '{cek}' not found")
                print('[!] Type "menu" to show menu bot')
                bot()
    except KeyboardInterrupt:
        bot()
#
###############################################################################

###############################################################################
#                         Dump Data

def dump_id():
    print("[*] Load Access Token")
    try:
        token = open("cookie/token.log", "r").read().strip()
        print("[*] Success load access token")
    except IOError:
        print("[!] Failed to load access token")
        print("[*] Type 'token' to generate access token")
        main()

    try:
        os.mkdir("output")
    except OSError:
        pass

    print("[*] Fetching all friends' IDs...")
    try:
        r = requests.get("https://graph.facebook.com/me/friends?access_token=" + token)
        a = json.loads(r.text)

        out = open("output/friends_id.txt", "w")  # Menggunakan nama file default
        for i in a["data"]:
            out.write(i["id"] + "\n")
            print(f"\r[*] {i['id']} retrieved", end="", flush=True)
            time.sleep(0.0001)

        out.close()
        print("\n[*] All friends' IDs successfully retrieved")
        print("[*] File saved: output/friends_id.txt")
        main()

    except KeyboardInterrupt:
        print("\r[!] Stopped")
        main()
    except KeyError:
        print("[!] Failed to fetch friends' IDs")
        main()
    except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):
        print("[!] Connection Error")
        print("[!] Stopped")
        main()

def dump_phone():
    print("[*] Load access token")

    try:
        token = open('cookie/token.log', 'r').read()
        print("[*] Success load access token")
    except IOError:
        print("[!] Failed load access token")
        print("[*] Type 'token' to generate access token")
        main()

    try:
        os.mkdir('output')
    except OSError:
        pass

    print("[*] Fetching all phone numbers")
    print("[*] Start")

    try:
        r = requests.get(f'https://graph.facebook.com/me/friends?access_token={token}')
        a = json.loads(r.text)

        filename = 'output/friends_phone.txt'  # Gunakan nama file default jika `n[0]` tidak didefinisikan
        with open(filename, 'w') as out:
            for i in a['data']:
                x = requests.get(f"https://graph.facebook.com/{i['id']}?access_token={token}")
                z = json.loads(x.text)

                try:
                    out.write(z['mobile_phone'] + '\n')
                    print(f"{W}[{G}{z['name']}{W}]{R} >> {W}{z['mobile_phone']}")
                except KeyError:
                    pass

        print("[*] Done")
        print("[*] All phone numbers successfully retrieved")
        print(f"[*] File saved: {filename}")
        main()

    except KeyboardInterrupt:
        print("\r[!] Stopped")
        main()
    except KeyError:
        print("[!] Failed to fetch all phone numbers")
        main()
    except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):
        print("[!] Connection Error")
        print("[!] Stopped")
        main()

def dump_mail():
    print("[*] Load access token")

    try:
        token = open('cookie/token.log', 'r').read()
        print("[*] Success load access token")
    except IOError:
        print("[!] Failed load access token")
        print("[*] Type 'token' to generate access token")
        main()

    try:
        os.mkdir('output')
    except OSError:
        pass

    print("[*] Fetching all emails")
    print("[*] Start")

    try:
        r = requests.get(f'https://graph.facebook.com/me/friends?access_token={token}')
        a = json.loads(r.text)

        filename = 'output/friends_mails.txt'  # Gunakan nama file default jika `n[0]` tidak tersedia
        with open(filename, 'w') as out:
            for i in a['data']:
                x = requests.get(f"https://graph.facebook.com/{i['id']}?access_token={token}")
                z = json.loads(x.text)

                try:
                    out.write(z['email'] + '\n')
                    print(f"{W}[{G}{z['name']}{W}]{R} >> {W}{z['email']}")
                except KeyError:
                    pass

        print("[*] Done")
        print("[*] All emails successfully retrieved")
        print(f"[*] File saved: {filename}")
        main()

    except KeyboardInterrupt:
        print("\r[!] Stopped")
        main()
    except KeyError:
        print("[!] Failed to fetch all emails")
        main()
    except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):
        print("[!] Connection Error")
        print("[!] Stopped")
        main()

def dump_id_id():
    global target_id

    print("[*] Load access token")

    try:
        token = open('cookie/token.log', 'r').read()
        print("[*] Success load access token")
    except IOError:
        print("[!] Failed load access token")
        print("[*] Type 'token' to generate access token")
        main()

    try:
        os.mkdir('output')
    except OSError:
        pass

    print("[*] Fetching all ID from your friend")

    try:
        url = f"https://graph.facebook.com/{target_id}?fields=friends.limit(5000)&access_token={token}"
        r = requests.get(url)
        a = json.loads(r.text)

        filename = f"output/friends_{target_id}_id.txt"  # Nama file default
        with open(filename, 'w') as out:
            for i in a.get('friends', {}).get('data', []):
                out.write(i['id'] + '\n')
                print(f"\r[*] {i['id']} retrieved", end='', flush=True)
                time.sleep(0.0001)

        print("\n[*] All friends ID successfully retrieved")
        print(f"[*] File saved: {filename}")
        main()

    except KeyboardInterrupt:
        print("\n[!] Stopped")
        main()
    except KeyError:
        print("[!] Failed to fetch friend ID")
        try:
            os.remove(filename)
        except OSError:
            pass
        main()
    except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):
        print("[!] Connection Error")
        print("[!] Stopped")
#
###############################################################################

###############################################################################
#                         Main

def main():
    global target_id

    try:
        cek = input(f"{R}D3b2y{W} >> ")  # Mengganti raw_input dengan input untuk Python 3

        if cek.lower() == 'get_data':
            if len(jml) == 0:
                getdata()
            else:
                print(f"[*] You have retrieved {len(jml)} friends data")
                main()
        elif cek.lower() == 'get_info':
            print("\n" + "[*] Information Gathering [*]".center(44) + "\n")
            search()
        elif cek.lower() == 'bot':
            menu_bot()
            bot()
        elif cek.lower() == "cat_token":
            try:
                o = open('cookie/token.log', 'r').read()
                print(f"[*] Your access token !!\n\n{o}\n")
                main()
            except IOError:
                print('[!] Failed to open cookie/token.log')
                print("[!] Type 'token' to generate access token")
                main()

        elif cek.lower() == 'clear':
            if sys.platform == 'win32':
                os.system('cls')
                baliho()
                main()
            else:
                os.system('clear')
                baliho()
                main()

        elif cek.lower() == 'token':
            try:
                open('cookie/token.log')
                print('[!] An access token already exists')
                cek = input('[?] Are you sure you want to continue [Y/N] ')
                if cek.lower() != 'y':
                    print('[*] Cancelling ')
                    bot()
            except IOError:
                pass

            print("\n" + '[*] Generate Access token facebook [*]'.center(44) + '\n')
            print('[Warn] Please turn off your VPN before using this feature !!!')
            id()
        elif cek.lower() == 'rm_token':
            print('''
[Warn] You must create access token again if 
       your access token is deleted
            ''')
            a = input("[!] Type 'delete' to continue: ")
            if a.lower() == 'delete':
                try:
                    os.system('rm -rf cookie/token.log')
                    print('[*] Success delete cookie/token.log')
                    main()
                except OSError:
                    print('[*] Failed to delete cookie/token.log')
                    main()
            else:
                print('[*] Failed to delete cookie/token.log')
                main()
        elif cek.lower() == 'about':
            show_program()
            main()
        elif cek.lower() == 'exit':
            print("[!] Exiting Program")
            sys.exit()
        elif cek.lower() == 'help':
            info_ga()
            main()
        elif cek.lower() == 'dump_id':
            dump_id()
        elif cek.lower() == 'dump_phone':
            dump_phone()
        elif cek.lower() == 'dump_mail':
            dump_mail()

        if 'dump_' in cek.lower() and cek.lower().split('_')[2] == 'id':
            target_id = cek.lower().split('_')[1]
            dump_id_id()
        else:
            if cek == '':
                main()
            else:
                print(f"[!] Command '{cek}' not found")
                print('[!] Type "help" to show command')
                main()
    except KeyboardInterrupt:
        main()
    except IndexError:
        print(f'[!] Invalid parameter on command: {cek}')
        main()
#
######################################################################################################################

################################################################################
#                          Get Data

def getdata():
    global a, token

    print('[*] Load Access Token')

    try:
        token = open("cookie/token.log", "r").read()
        print('[*] Success load access token ')
    except IOError:
        print('[!] failed to open cookie/token.log')
        print("[!] type 'token' to generate access token")
        main()

    print('[*] fetching all friends data')

    try:
        r = requests.get(f'https://graph.facebook.com/me/friends?access_token={token}')
        a = json.loads(r.text)
    except KeyError:
        print('[!] Your access token is expired')
        print("[!] type 'token' to generate access token")
        main()
    except requests.exceptions.ConnectionError:
        print('[!] Connection Error')
        print('[!] Stopped')
        main()

    for i in a['data']:
        jml.append(i['id'])
        print(f'\r[*] fetching {len(jml)} data from friends', end='')
        sys.stdout.flush()
        time.sleep(0.0001)

    print(f'\r[*] {len(jml)} data of friends successfully retrieved')
    main()

def search():
    if len(jml) == 0:
        print("[!] no friend data in the database")
        print('[!] type "get_data" to collect friends data')
        main()
    else:
        pass

    target = input("[!] Search Name or Id : ")

    if target == '':
        print("[!] name or id can't be empty !!")
        search()
    else:
        info(target)

def info(target):
    global a, token

    print('[*] Searching')

    for i in a['data']:
        if target in i['name'] or target in i['id']:
            x = requests.get(f"https://graph.facebook.com/{i['id']}?access_token={token}")
            y = json.loads(x.text)

            print('\n[-------- INFORMATION --------]'.center(44))

            fields = [
                ('Id', i.get('id')),
                ('Username', y.get('username')),
                ('Email', y.get('email')),
                ('Mobile Phone', y.get('mobile_phone')),
                ('Name', y.get('name')),
                ('First name', y.get('first_name')),
                ('Middle name', y.get('middle_name')),
                ('Last name', y.get('last_name')),
                ('Locale', y.get('locale', '').split('_')[0] if y.get('locale') else None),
                ('Location', y.get('location', {}).get('name')),
                ('Hometown', y.get('hometown', {}).get('name')),
                ('Gender', y.get('gender')),
                ('Religion', y.get('religion')),
                ('Relationship Status', y.get('relationship_status')),
                ('Political', y.get('political')),
                ('Updated time', f"{y['updated_time'][:10]} {y['updated_time'][11:19]}" if 'updated_time' in y else None),
                ('Bio', y.get('bio')),
                ('Quotes', y.get('quotes')),
                ('Birthday', y.get('birthday', '').replace('/', '-') if 'birthday' in y else None),
                ('Link', y.get('link'))
            ]

            for label, value in fields:
                if value:
                    print(f'[*] {label}: {value}')

            if 'work' in y:
                print('[*] Work:')
                for work in y['work']:
                    work_fields = [
                        ('Position', work.get('position', {}).get('name')),
                        ('Employer', work.get('employer', {}).get('name')),
                        ('Start Date', '---' if work.get('start_date') == "0000-00" else work.get('start_date')),
                        ('End Date', '---' if work.get('end_date') == "0000-00" else work.get('end_date')),
                        ('Location', work.get('location', {}).get('name'))
                    ]
                    for label, value in work_fields:
                        if value:
                            print(f'   [-] {label}: {value}')
                    print(' ')

            if 'languages' in y:
                print('[*] Languages:')
                for lang in y['languages']:
                    print(f' ~  {lang.get("name")}')

            if 'favorite_teams' in y:
                print('[*] Favourite teams:')
                for team in y['favorite_teams']:
                    print(f' ~  {team.get("name")}')

            if 'education' in y:
                print('[*] School:')
                for edu in y['education']:
                    print(f' ~  {edu.get("school", {}).get("name")}')

    print('[*] Done')
    main()

#
##########################################################################

##########################################################################
#

if __name__ == '__main__':

	baliho()
	main()

#
##########################################################################

