# ----- initialisation des modules -----#
import pandas as pd
import numpy
from tkinter import Tk
from tkinter import messagebox
from scipy.signal import argrelextrema
import matplotlib.pyplot as plt
import requests
import datetime
from numpy import *
from matplotlib.pyplot import *
import colorama
from colorama import Fore
import os
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from multiprocessing import Process
import multiprocessing
import math
# from playsound import playsound
from ib_insync import *
import sys
import subprocess
import tempfile
from ftplib import FTP
from ib_insync import *
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import datetime
import ftplib

# ----- initialisation des modules -----#
def achat(ticker,target2,target):
    commande = ["python", "assets/acheter.py", ticker, target2, target]
    subprocess.run(commande, check=True)
# ----- initialisation des couleurs du modules pystyle -----#
class bcolors:
    OK = '\033[92m'  # GREEN
    WARNING = '\033[93m'  # YELLOW
    FAIL = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR
    PURPLE = '\033[35m'  # PURPLE


w = Fore.WHITE
b = Fore.BLACK
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX
c = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX
# ----- initialisation des couleurs du modules pystyle -----#

# ----- initialisation des temps de recherches -----#
date = datetime.datetime.now()
my_lock = threading.RLock()
end = str(pd.Timestamp.today() + pd.DateOffset(5))[0:10]
start_5m = str(pd.Timestamp.today() + pd.DateOffset(-15))[0:10]
start_15m = str(pd.Timestamp.today() + pd.DateOffset(-15))[0:10]
start_30m = str(pd.Timestamp.today() + pd.DateOffset(-15))[0:10]
start_1h = str(pd.Timestamp.today() + pd.DateOffset(-15))[0:10]
start_6h = str(pd.Timestamp.today() + pd.DateOffset(-20))[0:10]
start_1d = str(pd.Timestamp.today() + pd.DateOffset(-50))[0:10]
start_1week = str(pd.Timestamp.today() + pd.DateOffset(-120))[0:10]
start_1month = str(pd.Timestamp.today() + pd.DateOffset(-240))[0:10]
# ----- initialisation des temps de recherches -----#

# ----- initialisation de l'API key et ticker -----#
#api_key = '1KsqKOh1pTAJyWZx6Qm9pvnaNcpKVh_8'
api_key = 'q5li8Y5ldvlF7eP8YI7XdMWbyOA3scWJ'
ticker = 'INVA'
tiker_live = ticker

argument2 = 0
argument3 = 0

# ----- initialisation de l'API key et ticker -----#



# ----- initialisation des fonctions lies au boutons -----#
def save_figure(event):
    now = datetime.datetime.now()
    plt.savefig(f'trouvailles/{now.strftime("%Hh:%M:%S")}')
    #button1.color = '#94ffa4'
    #button1.hovercolor = '#94ffa4'

# ----- initialisation des fonctions lies au boutons -----#

def increment_value(html_content, selector):
    start_tag = f'<td>{selector}</td>'
    end_tag = '</td>'

    start_index = html_content.find(start_tag)
    if start_index != -1:
        start_index = html_content.find('<td>', start_index + len(start_tag))
        end_index = html_content.find(end_tag, start_index)
        if start_index != -1 and end_index != -1:
            value = int(html_content[start_index + 4:end_index])
            new_value = value + 1
            html_content = html_content[:start_index + 4] + str(new_value) + html_content[end_index:]

    return html_content

def courbe(pourcent_chercher2,tiker_live,time1,time_name1,pourcent_chercher,pourcent_perdu,note,debugage,dejatoucher2,mirande3,mirande2,J,I,moyenne_tete,moins50p,local_min,local_max,A,B,C,D,E,F,G,df,place_liveprice,tout_savoir):
    global argument2
    global argument3
    # ----- creer la figure et l'affichage MATPLOTLIB -----#
    Write.Print("<🟢> <🟢> <🟢> <🟢> NOUVELLE FIGURE ! <🟢> <🟢> <🟢> <🟢>", Colors.green, interval=0.000)
    print('')
    try:
        highs = df.iloc[local_max, :]
        lows = df.iloc[local_min, :]
        fig = plt.figure(figsize=(10, 7))
        if pourcent_chercher2 >= 1:
            fig.patch.set_facecolor('#17DE17')
            fig.patch.set_alpha(0.3)
        if pourcent_chercher2 >= 3:
            fig.patch.set_facecolor('#3498DB')
            fig.patch.set_alpha(0.3)
        if pourcent_chercher2 >= 5:
            fig.patch.set_facecolor('#6c00d3')
            fig.patch.set_alpha(0.3)
        if pourcent_chercher2 >= 10:
            fig.patch.set_facecolor('#ffdc00')
            fig.patch.set_alpha(0.3)
        plt.plot([], [], ' ')
        plt.title(
            f'IETE : {tiker_live} | {time1} {time_name1} | +{pourcent_chercher}% depuis LDC | +{pourcent_chercher2}% depuis Jaune | -{pourcent_perdu}% MINI | {note}/10 | {tout_savoir} | {dejatoucher2}',
            fontweight="bold", color='black')
        mirande3['c'].plot(color=['blue'], label='Clotures')
        # df['sma_20'].plot(label='Ema 20', linestyle='-', linewidth=1.2, color='green')
        # df['sma_50'].plot(label='Ema 50', linestyle='-', linewidth=1.2, color='red')
        # df['sma_100'].plot(label='Ema 100', linestyle='-', linewidth=1.2, color='blue')
        # mirande['c'].plot(color=['#FF0000'])
        mirande2['c'].plot(color=['green'], linestyle='--', label='Ligne de coup')
        plt.axhline(y=J[1] + moyenne_tete, linestyle='--', alpha=0.3, color='red',
                    label='100% objectif')
        plt.axhline(y=J[1] + (((moyenne_tete) / 2) + ((moyenne_tete) / 4)), linestyle='--',
                    alpha=0.3, color='black', label='75% objectif')
        plt.axhline(y=J[1] + (moyenne_tete) / 2, linestyle='--', alpha=0.3, color='orange',
                    label='50% objectif')
        plt.axhline(y=J[1] + (moyenne_tete) / 4, linestyle='--', alpha=0.3, color='black',
                    label='25% objectif')
        plt.axhline(y=J[1] - ((moyenne_tete*5) / 100), xmin=0.8, xmax=1, linestyle='-', alpha=0.8, color='red', linewidth=2, label='-50% objectif')
        plt.axhline(y=J[1] + ((moyenne_tete*30) / 100), xmin=0.8, xmax=1, linestyle='-', alpha=0.8, color='green', linewidth=2, label='-50% objectif')
        plt.grid(True, which='major', color='#666666', linestyle='-', alpha=0.1)
        taille_diviser = (local_max[-1] - local_max[-2]) / (local_min[-2] - local_max[-2])
        # point_max = J[0]+((J[0] - I[0])/taille_diviser)
        point_max = J[0] + ((J[0] - I[0]))
        point_max = int(round(point_max, 0))
        # plt.scatter(point_max, df['c'].values[int(round(point_max, 0))], color='red',label='Max temps realisation')
        plt.legend()
        plt.text(local_max[-3], A, "A", ha='left', style='normal', size=10.5, color='red',
                 wrap=True)
        plt.text(J[0], J[1] + (moyenne_tete) / 2, f"{round((J[1] + (moyenne_tete) / 2), 5)}",
                 ha='left', style='normal', size=10.5, color='blue', wrap=True)
        plt.text(J[0], J[1] + (moyenne_tete), f"{round((J[1] + (moyenne_tete)), 5)}",
                 ha='left', style='normal', size=10.5, color='blue', wrap=True)
        plt.text(J[0], J[1] + ((moyenne_tete*30) / 100), f"30 ({round(J[1] + ((moyenne_tete*30) / 100), 5)}) / 60 ({round(J[1] + ((moyenne_tete*60) / 100), 5)})", ha='left', style='normal', size=10.5,
                 color='green', wrap=True)
        plt.text(J[0], J[1] - ((moyenne_tete*5) / 100), f"5 ({round(J[1] - ((moyenne_tete*5) / 100), 5)})", ha='left', style='normal', size=10.5,
                 color='red', wrap=True)
        plt.text(local_min[-3], B, "B", ha='left', style='normal', size=10.5, color='red',
                 wrap=True)
        plt.text(local_max[-2], C, "C", ha='left', style='normal', size=10.5, color='red',
                 wrap=True)
        plt.text(local_min[-2], D, f"D {round(D, 5)}", ha='left', style='normal', size=10.5,
                 color='red', wrap=True)
        plt.text(local_max[-1], E, "E", ha='left', style='normal', size=10.5, color='red',
                 wrap=True)
        plt.text(local_min[-1], F, f"F  {round(F, 5)}", ha='left', style='normal', size=10.5,
                 color='red', wrap=True)
        plt.text(place_liveprice, G, f"G  {round(G, 5)}", ha='left', style='normal', size=10.5,
                 color='red', wrap=True)
        plt.text(I[0], I[1], "I", ha='left', style='normal', size=10.5, color='#00FF36', wrap=True)
        plt.text(J[0], J[1], "J", ha='left', style='normal', size=10.5, color='#00FF36', wrap=True)
        # test_valeur = df['c'].iloc[round(J[0]) + 1]
        # plt.text(round(J[0]), df['c'].iloc[round(J[0])], f"J+1 {test_valeur}", ha='left',style='normal', size=10.5, color='#00FF36', wrap=True)
        plt.scatter(len(df['c']) - 1, df['c'].values[-1], color='blue', label='liveprice')
        plt.scatter(len(df['c']) - 2, df['c'].values[-2], color='orange', label='cloture')
        plt.scatter(local_max[-3], A, color='blue')
        plt.scatter(local_min[-3], B, color='blue')
        plt.scatter(local_max[-2], C, color='blue')
        plt.scatter(local_min[-2], D, color='blue')
        plt.scatter(local_max[-1], E, color='blue')
        plt.scatter(local_min[-1], F, color='blue')
        plt.scatter(J[0], J[1], color='green')
        plt.scatter(I[0], I[1], color='green')
        #plt.scatter(x=highs.index, y=highs['c'], alpha=0.5)
        #plt.scatter(x=lows.index, y=lows['c'], alpha=0.5)
        argument2 = round((J[1] + (moyenne_tete) / 2), 5)
        argument3 = round(J[1] + ((moyenne_tete*30) / 100), 5)
        # Paramètres des boutons
        button_width = 0.2
        button_height = 0.075
        button_space = 0.05
        # Création du bouton pour enregistrer la figure
        button_ax1 = plt.axes([0.125, 0.001, button_width, button_height], facecolor='none')
        button1 = plt.Button(button_ax1, 'Enregistrer', color='white', hovercolor='lightgray')
        button1.on_clicked(save_figure)
        # Création du bouton pour acheter
        button_ax2 = plt.axes([0.9 - button_width, 0.001, button_width, button_height], facecolor='none')
        button2 = plt.Button(button_ax2, 'Acheter', color='white', hovercolor='lightgray')
        target1 = J[1] + ((moyenne_tete*30) / 100)
        target2 = J[1] - ((moyenne_tete*5) / 100)
        button2.on_clicked(lambda event: achat(ticker, target1, target2))
        now = datetime.datetime.now()
        if not os.path.isfile(f'trouvailles/{tiker_live} .png'):
            plt.savefig(f'trouvailles/{tiker_live} {time1} {time_name1} {round(J[1] + ((moyenne_tete*30) / 100), 5)} {round(J[1] - ((moyenne_tete*5) / 100), 5)} .png')
        #plt.show()

            # Informations de connexion FTP
            ftp_server = 'server133.web-hosting.com'
            ftp_username = 'abtrqawg'
            ftp_password = 'Km8V2Q67pUbL'
            ftp_file_path = '/public_html/2.html'

            # Connexion au serveur FTP
            ftp = ftplib.FTP(ftp_server)
            ftp.login(ftp_username, ftp_password)

            # Téléchargement du fichier HTML depuis le serveur FTP
            with open('fichier_local.html', 'wb') as file:
                ftp.retrbinary(f'RETR {ftp_file_path}', file.write)

            # Lire le contenu du fichier HTML local
            with open('fichier_local.html', 'r') as file:
                html_content = file.read()

            # Incrémenter les valeurs spécifiées
            html_content = increment_value(html_content, 'Nombre de trades pris')

            # Écrire le contenu modifié dans le fichier HTML local
            with open('fichier_local.html', 'w') as file:
                file.write(html_content)

            # Téléverser le fichier HTML modifié sur le serveur FTP
            with open('fichier_local.html', 'rb') as file:
                ftp.storbinary(f'STOR {ftp_file_path}', file)

            # Fermer la connexion FTP
            ftp.quit()


    # ----- creer la figure et l'affichage MATPLOTLIB -----#
    except:
        Write.Print("<⛔> <⛔> <⛔> <⛔> ERREUR CRITIQUE <⛔> <⛔> <⛔> <⛔>", Colors.red, interval=0.000)
        print('')


# ----- fonction pour trouver les point intersection de la ligne de coup et de la Courbe -----#
def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        raise Exception('les courbes ne se coupent pas')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y


# ----- fonction pour trouver les point intersection de la ligne de coup et de la Courbe -----#


# ----- fonction Principale -----#
def Finder_IETE(time1, time_name1, start1):
    # global proxies
    global argument2
    global argument3
    global tiker_live
    global time2
    global time_name2
    time2 = time1
    time_name2 = time_name1
    # while True:

    # ----- Appel des données Polygon.io OHLC et creation du DF -----#
    passed1 = False
    with my_lock:
        try:
            api_url_livePrice = f'http://api.polygon.io/v2/last/trade/{tiker_live}?apiKey={api_key}'
            data = requests.get(api_url_livePrice).json()
            df_livePrice = pd.DataFrame(data)

            api_url_OHLC = f'http://api.polygon.io/v2/aggs/ticker/{ticker}/range/{time1}/{time_name1}/{start1}/{end}?adjusted=true&limit=50000&apiKey={api_key}'

            data = requests.get(api_url_OHLC).json()
            df = pd.DataFrame(data['results'])
            la_place_de_p = 0

            for k in range(0, len(df_livePrice.index)):
                if df_livePrice.index[k] == 'p':
                    la_place_de_p = k
            livePrice = df_livePrice['results'].iloc[la_place_de_p]
            passed1 = True
        except:
            Write.Print("<⛔> <⛔> <⛔> <⛔> ERREUR CRITIQUE <⛔> <⛔> <⛔> <⛔>", Colors.red, interval=0.000)
            print('')

    # ----- Appel des données Polygon.io OHLC et creation du DF -----#

    # ----- suppression de la dernière valeur du df pour y rajouter un LIVEPRICE plus precis -----#
    if passed1 == True:
        dernligne = len(df['c']) - 1
        df.drop([dernligne], axis=0, inplace=True)

        # df = df.drop(columns=['o', 'h', 'l', 'v', 'vw', 'n'])
        # df = df.append({'o': NAN, 'h': NAN, 'l': NAN, 'v': NAN, 'vw': NAN, 'n': NAN, 'c': livePrice, 't': NAN}, ignore_index=True)
        df_new_line = pd.DataFrame([[NAN, NAN, NAN, NAN, NAN, NAN, livePrice, NAN]],
                                   columns=['o', 'h', 'l', 'v', 'vw', 'n', 'c', 't'])
        df = pd.concat([df, df_new_line], ignore_index=True)
        df_data_date = []
        df_data_price = []
        for list_df in range(len(df)):
            df_data_date.append(df['t'].iloc[list_df])
            df_data_price.append(df['c'].iloc[list_df])
        data_date = pd.DataFrame(df_data_date, columns=['Date'])
        data_price = pd.DataFrame(df_data_price, columns=['Price'])
        df_wise_index = pd.concat([data_date, data_price], axis=1)

        place_liveprice = (len(df) - 1)

        for data in range(len(df_wise_index)):

            try:

                if df_wise_index['Price'].iloc[data] == df_wise_index['Price'].iloc[data + 1]:
                    df = df.drop(df_wise_index['Date'].iloc[data + 1])
            except:
                # print('ok')
                aaa = 0
        # ----- suppression de la dernière valeur du df pour y rajouter un LIVEPRICE plus precis -----#

        # ----- creation des locals(min/max) -----#
        local_max = argrelextrema(df['c'].values, np.greater, order=1, mode='clip')[0]
        local_min = argrelextrema(df['c'].values, np.less, order=1, mode='clip')[0]
        # ----- creation des locals(min/max) -----#

        # ----- suppression des points morts de la courbe -----#
        test_min = []
        test_max = []

        # if local_min[0] > local_max[0]:
        #        local_max = local_max[1:]
        #        print('On a supprimer le premier point')
        #
        q = 0
        p = 0

        len1 = len(local_min)
        len2 = len(local_max)
        while p < len1 - 5 or p < len2 - 5:
            if local_min[p + 1] < local_max[p]:
                test_min.append(local_min[p])
                local_min = np.delete(local_min, p)

                p = p - 1
            if local_max[p + 1] < local_min[p + 1]:
                test_max.append(local_max[p])
                local_max = np.delete(local_max, p)

                p = p - 1
            p = p + 1

            len1 = len(local_min)
            len2 = len(local_max)


        decalage = 0
        # ----- suppression des points morts de la courbe -----#

        # ----- initialisation des pointeurs de la figure -----#
        passed2 = False
        try:
            A = float(df['c'].iloc[local_max[-3]])
            B = float(df['c'].iloc[local_min[-3]])
            C = float(df['c'].iloc[local_max[-2]])
            D = float(df['c'].iloc[local_min[-2]])
            E = float(df['c'].iloc[local_max[-1]])
            F = float(df['c'].iloc[local_min[-1]])
            G = float(livePrice)


            passed2 = True

        except:
            Write.Print("<🟡> <🟡> <🟡> <🟡> PAS ASSEZ DE DONNEES <🟡> <🟡> <🟡> <🟡>", Colors.yellow, interval=0.000)
            print('')
        # ----- initialisation des pointeurs de la figure -----#
        if passed2 == True:
            # ----- determination du 'PAS' de la pente de la LDC pour la prolonger plus loins que C et E -----#
            if C > E:
                differ = (C - E)
                pas = (local_max[-1] - local_max[-2])
                suite = differ / pas
            if C < E:
                differ = (E - C)
                pas = (local_max[-1] - local_max[-2])
                suite = differ / pas
            # ----- determination du 'PAS' de la pente de la LDC pour la prolonger plus loins que C et E -----#

            # ----- PRINT affichage dans la console -----#
            Write.Print("  >> RECHERCHE IETE  :", Colors.white, interval=0.000)
            Write.Print(f"  {ticker}", Colors.green, interval=0.000)
            Write.Print(f"  {time1} {time_name1}", Colors.cyan, interval=0.000)
            Write.Print("  <<", Colors.white, interval=0.000)
            print('')
            # ----- PRINT affichage dans la console -----#

            # ----- creation des differentes courbe: rouge(surlignage figure), vert(ligne de coup), bleu(la figure en zoomer)-----#
            rouge = []
            vert = []
            bleu = []

            rouge.append(local_max[-3])
            rouge.append(local_min[-3])
            rouge.append(local_max[-2])
            rouge.append(local_min[-2])
            rouge.append(local_max[-1])
            rouge.append(local_min[-1])
            rouge.append(place_liveprice)

            vert.append(local_max[-3])
            vert.append(local_max[-2])
            vert.append(local_max[-1])
            vert.append(place_liveprice)

            i = 0
            passed3 = False
            try:
                for i in range(local_max[-4] - 1, len(df)):
                    bleu.append(i)
                    passed3 = True
            except:
                Write.Print("<🟠> <🟠> <🟠> <🟠> PAS ASSEZ DE DONNEES 2 <🟠> <🟠> <🟠> <🟠>", Colors.orange, interval=0.000)
                print('')
            if passed3 == True:
                mirande2 = df.iloc[vert, :]
                mirande = df.iloc[rouge, :]
                mirande3 = df.iloc[bleu, :]
                # ----- creation des differentes courbe: rouge(surlignage figure), vert(ligne de coup), bleu(la figure en zoomer)-----#

                # ----- determiner la direction pente LDC et allongement apres E et C -----#
                if E > C:
                    mirande2['c'].values[0] = mirande2['c'].values[1] - ((suite * (local_max[-2] - local_max[-3])))
                    mirande2['c'].values[3] = mirande2['c'].values[2] + ((suite * (place_liveprice - local_max[-1])))
                if E < C:
                    mirande2['c'].values[0] = mirande2['c'].values[1] + ((suite * (local_max[-2] - local_max[-3])))
                    mirande2['c'].values[3] = mirande2['c'].values[2] - ((suite * (place_liveprice - local_max[-1])))
                if E == C:
                    mirande2['c'].values[0] = df['c'].values[local_max[-2]]
                    mirande2['c'].values[3] = df['c'].values[local_max[-1]]
                # ----- determiner la direction pente LDC et allongement apres E et C -----#

                # ----- transformer le tableau en DF avec les donnée du DF reel -----#
                vert1 = {'c': vert}
                vert2 = pd.DataFrame(data=vert1)
                rouge1 = {'c': rouge}
                rouge2 = pd.DataFrame(data=rouge1)
                bleu1 = {'c': bleu}
                bleu2 = pd.DataFrame(data=bleu1)
                # ----- transformer le tableau en DF avec les donnée du DF reel -----#

                # ----- preparation des deux courbes pour determiner intersection de I et J -----#
                # --- premiere droite cotée gauche ---#
                AI = [local_max[-3], mirande2['c'].iloc[0]]
                BI = [local_max[-2], mirande2['c'].iloc[1]]
                # --- premiere droite coté gauche ---#

                # --- deuxieme droite coté gauche ---#
                CI = [local_max[-3], A]
                DI = [local_min[-3], B]
                # I = line_intersection((AI, BI), (CI, DI))
                # --- deuxieme droite coté gauche ---#

                # --- premiere droite cotée droit ---#
                AJ = [local_max[-1], mirande2['c'].iloc[2]]
                BJ = [place_liveprice, mirande2['c'].iloc[3]]
                # --- premiere droite cotée droit ---#

                # --- deuxieme droite coté droit ---#
                CJ = [place_liveprice, G]
                DJ = [local_min[-1], F]
                # J = line_intersection((AJ, BJ), (CJ, DJ))
                # --- deuxieme droite coté droit ---#
                # ----- preparation des deux courbes pour determiner intersection de I et J -----#

                # ----- verification qu'il n'y est pas de point mort dans la figure -----# ------------------- VERIFIER !!
                pop = 0
                verif = 0

                for pop in range(0, len(test_min)):
                    if test_min[pop] > local_max[-3] and test_min[pop] < place_liveprice:
                        verif = verif + 1
                pop = 0
                for pop in range(0, len(test_max)):
                    if test_max[pop] > local_max[-3] and test_max[pop] < place_liveprice:
                        verif = verif + 1
                # ----- verification qu'il n'y est pas de point mort dans la figure -----# ------------------- VERIFIER !!

                # ----- condition pour que l'ordre des point de la figure soit respecter -----#
                ordre = False
                if local_max[-3] < local_min[-3] < local_max[-2] < local_min[-2] < local_max[-1] < local_min[-1]:
                    ordre = True
                # ----- condition pour que l'ordre des point de la figure soit respecter -----#

                # ----- condition pour garantir la forme de l'iete  -----#
                if (C - B) < (C - D) and (C - B) < (E - D) and (E - F) < (E - D) and (E - F) < (
                        C - D) and B > D and F > D and B < C and F < E and A >= mirande2['c'].iloc[
                    0] and verif == 0 and ordre == True:
                    # ----- condition pour garantir la forme de l'iete  -----#

                    # ----- essaye de determiner les point d'intersection de la LDC -----#
                    try:
                        J = line_intersection((AJ, BJ), (CJ, DJ))
                        I = line_intersection((AI, BI), (CI, DI))
                        accept = True
                    except:
                        accept = False
                    # ----- essaye de determiner les point d'intersection de la LDC -----#

                    # ----- creation variable des moyennes de la tete et epaules  pour les prochaines conditions-----#
                    if accept == True:
                        moyenne_epaule1 = ((I[1] - B) + (C - B)) / 2
                        moyenne_epaule2 = ((E - F) + (J[1] - F)) / 2
                        moyenne_des_epaule = ((E - F) + (J[1] - F)) + ((E - F) + (J[1] - F)) / 4
                        moyenne_tete = ((C - D) + (E - D)) / 2
                        # ----- creation variable des moyennes de la tete et epaules  pour les prochaines conditions-----#

                        tuche = 0
                        noo = 0
                        place_pc = 0
                        point_max = J[0] + ((J[0] - I[0]))
                        point_max = int(round(point_max, 0))

                        # ----- creation de la fonction Moyenne mobile  -----#
                        def sma(data, window):
                            sma = data.rolling(window=window).mean()
                            return sma

                        df['sma_20'] = sma(df['c'], 20)
                        df['sma_50'] = sma(df['c'], 50)
                        df['sma_100'] = sma(df['c'], 100)
                        df.tail()
                        # ----- creation de la fonction Moyenne mobile  -----#

                        # ----- condition pour que la tete fasse au minimum 2.8% -----#
                        plus_grand = round((J[1] + ((moyenne_tete*30) / 100)), 5)
                        plus_petit = J[1]
                        pourcent_chercher = ((plus_grand - plus_petit) / plus_petit) * 100
                        pourcent_chercher = round(pourcent_chercher, 2)

                        prix_chercher = df['c'].values[-2] + (df['c'].values[-2] * 0.015)
                        difference_chercher = prix_chercher - J[1]
                        tout_savoir = (difference_chercher*100)/moyenne_tete
                        tout_savoir = round(tout_savoir, 2)

                        mini_pourcent = False
                        if pourcent_chercher >= 1.5:
                            mini_pourcent = True
                        # ----- condition pour que la tete fasse au minimum 2.8% -----#



                    # ----- condition pour filtrer iete  -----#
                    if I[1] > B and J[
                        1] > F and moyenne_epaule1 <= moyenne_tete / 2 and moyenne_epaule2 <= moyenne_tete / 2 and moyenne_epaule1 >= moyenne_tete / 4 and moyenne_epaule2 >= moyenne_tete / 4 and accept == True and \
                            df['c'].values[-2] <= J[1] + (moyenne_tete) / 4 and df['c'].values[-2] >= J[1] and \
                            df['c'].index[-2] != local_min[-1] and G >= 1 and J[0] >= local_min[-1]:
                        # ----- condition pour filtrer iete  -----#

                        # ----- systeme de notation des iete en fonction de la beaute et de la perfection de realisation  -----#
                        note = 0
                        pourcentage_10_tete = (10 * (local_max[-1] - local_max[-2])) / 100
                        pourcentage_10_ep1 = (20 * (local_max[-2] - I[0])) / 100
                        pourcentage_10_ep2 = (20 * (J[0] - local_max[-1])) / 100
                        pourcentage_20_moy_epaule = (30 * moyenne_des_epaule) / 100

                        debugage = []

                        if local_min[-2] < (local_max[-2] + local_max[-1]) / 2 + pourcentage_10_tete and local_min[
                            -2] > (local_max[-2] + local_max[
                            -1]) / 2 - pourcentage_10_tete:  # D doit etre au millieu (10% de marge)
                            note = note + 3
                            debugage.append(1)

                        if local_min[-3] < (I[0] + local_max[-2]) / 2 + pourcentage_10_ep1 and local_min[-3] > (
                                I[0] + local_max[-2]) / 2 - pourcentage_10_ep1:  # B doit etre au millieu (10% de marge)
                            note = note + 1
                            debugage.append(2)

                        if local_min[-1] < (J[0] + local_max[-1]) / 2 + pourcentage_10_ep2 and local_min[-1] > (
                                J[0] + local_max[-1]) / 2 - pourcentage_10_ep2:  # F doit etre au millieu (10% de marge)
                            note = note + 1
                            debugage.append(3)

                        if moyenne_epaule1 < moyenne_des_epaule + pourcentage_20_moy_epaule and moyenne_epaule1 > moyenne_des_epaule - pourcentage_20_moy_epaule and moyenne_epaule2 < moyenne_des_epaule + pourcentage_20_moy_epaule and moyenne_epaule2 > moyenne_des_epaule - pourcentage_20_moy_epaule:  # les epaules doivent etre de presque meme hauteur
                            note = note + 1
                            debugage.append(4)

                        if B < F:
                            if (((F - B) * 100) / moyenne_tete) <= 30:
                                note = note + 2
                                debugage.append(5)

                        if B > F:
                            if (((B - F) * 100) / moyenne_tete) <= 30:
                                note = note + 2
                                debugage.append(5)

                        if B == F:
                            note = note + 2
                            debugage.append(5)

                        if (local_max[-1] - local_max[-2]) > local_max[-2] - I[0] and (local_max[-1] - local_max[-2]) > \
                                J[0] - local_max[-1]:  # tete plus large que les 2 epaules
                            note = note + 0.5
                            debugage.append(6)

                        # if il y a pas de bruit:
                        # note = note + 1.5
                        # ----- systeme de notation des iete en fonction de la beaute et de la perfection de realisation  -----#

                        # ----- regarde si la target a deja ete toucher en volatilité avant affichage  -----#
                        dejatoucher = False
                        for i in range(int(df['c'].index[-2]), place_liveprice):
                            if df['h'].iloc[i] >= J[1] + (moyenne_tete*30) / 100 and dejatoucher == False:
                                dejatoucher = True
                                dejatoucher2 = 'OUI'
                        if dejatoucher == False:
                            dejatoucher2 = 'NON'
                        # ----- regarde si la target a deja ete toucher en volatilité avant affichage  -----#

                        # ----- initialisation des données d'aide -----#
                        # playsound('note.wav')
                        moins50p = G - (moyenne_tete) / 2
                        plus_grand = round((J[1] + ((moyenne_tete*30) / 100)), 5)

                        pourcent_chercher2 = ((plus_grand - df['c'].values[-2]) / df['c'].values[-2]) * 100
                        pourcent_chercher2 = round(pourcent_chercher2, 2)


                        # pourcent_perdu = ((round(G, 5)- moins50p)*100)/round(G, 5)
                        pourcent_perdu = ((df['c'].values[-2] - (J[1] - ((moyenne_tete*5) / 100))) * 100) / df['c'].values[-2]
                        pourcent_perdu = round(pourcent_perdu, 2)

                        # ----- initialisation des données d'aide -----#
                        if pourcent_chercher2 >= 0.6:
                            thread = Process(target=courbe, args=(pourcent_chercher2,tiker_live,time1,time_name1,pourcent_chercher,pourcent_perdu,note,debugage,dejatoucher2,mirande3,mirande2,J,I,moyenne_tete,moins50p,local_min,local_max,A,B,C,D,E,F,G,df,place_liveprice,tout_savoir))
                            thread.start()


                print('----------------------------------------------------------------------', flush=True)
                time.sleep(0.5)


# ----- fonction Principale -----#
time2 = None
time_name2= None
# ----- traduction francais anglais pour appel polygon -----#
minute = "minute"
heure = "hour"
jour = "day"
# ----- traduction francais anglais pour appel polygon -----#

# ----- enssembles des Process à lancer en meme temps -----#
th1 = Process(target=Finder_IETE, args=(15, minute, start_15m))
th2 = Process(target=Finder_IETE, args=(20, minute, start_15m))
th3 = Process(target=Finder_IETE, args=(25, minute, start_15m))
th4 = Process(target=Finder_IETE, args=(30, minute, start_30m))
th5 = Process(target=Finder_IETE, args=(35, minute, start_30m))
th6 = Process(target=Finder_IETE, args=(45, minute, start_30m))
th7 = Process(target=Finder_IETE, args=(1, heure, start_1h))
th8 = Process(target=Finder_IETE, args=(2, heure, start_1h))
th9 = Process(target=Finder_IETE, args=(4, heure, start_1h))
th10 = Process(target=Finder_IETE, args=(40, minute, start_30m))
th11 = Process(target=Finder_IETE, args=(50, minute, start_30m))
th12 = Process(target=Finder_IETE, args=(55, minute, start_30m))
th13 = Process(target=Finder_IETE, args=(30, minute, start_30m))
th14 = Process(target=Finder_IETE, args=(75, minute, start_1h))
th15 = Process(target=Finder_IETE, args=(90, minute, start_1h))
th16 = Process(target=Finder_IETE, args=(105, minute, start_1h))  # ici nouveau
th17 = Process(target=Finder_IETE, args=(135, minute, start_1h))
th18 = Process(target=Finder_IETE, args=(150, minute, start_1h))
th19 = Process(target=Finder_IETE, args=(165, minute, start_1h))
th20 = Process(target=Finder_IETE, args=(195, minute, start_1h))
th21 = Process(target=Finder_IETE, args=(210, minute, start_1h))
th22 = Process(target=Finder_IETE, args=(225, minute, start_1h))
th23 = Process(target=Finder_IETE, args=(255, minute, start_1h))

th1.start()
th2.start()
th3.start()
th4.start()
th5.start()
th6.start()
th7.start()
th8.start()
th9.start()
th10.start()
th11.start()
th12.start()
th13.start()
th14.start()
th15.start()
th16.start()  # ici nouveau
th17.start()
th18.start()
th19.start()
th20.start()
th21.start()
th22.start()
th23.start()

th1.join()
th2.join()
th3.join()
th4.join()
th5.join()
th6.join()
th7.join()
th8.join()
th9.join()
th10.join()
th11.join()
th12.join()
th13.join()
th14.join()
th15.join()
th16.join()  # ici nouveau
th17.join()
th18.join()
th19.join()
th20.join()
th21.join()
th22.join()
th23.join()

