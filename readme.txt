Äëÿ àâòî-ñáîğêè âèäåî:

- â Trassir ñîçäàòü ñêğèïò ïî îáğàçöó:

##############################################################

from datetime import datetime

def ScreenShot():
	if WorkTime():
		object("Áóòàôîğñêèé").screenshot()
		object("Öåíòğ").screenshot()
		object("Ñâàğíîé öåõ").screenshot()
		object("Ïåíîğåçêà").screenshot()
		alert("Ñíèìêè ñîõğàíåíû")
	timeout(60000, ScreenShot) # 1Ìèíóòíûé èíòåğâàë


def WorkTime():
	t = int(datetime.strftime(datetime.now(), "%H"))
	if t > 9 and t < 22: # Äèàïàçîí ğàáî÷åãî âğåìåíè
		return 1
	return 0

ScreenShot()

##############################################################

- Ñîçäàòü ñëåäóşùóş ñòğóêòóğó â ïàïêå êóäà ñîõğàíÿşòñÿ ñêğèíøîòû:

---Screenshots (êóäà trassir êèäàåò ñêğèíøîòû)
------BUTAFOR
------CENTER
------PENOREZ
------SVAR
------ è ò.ä. 

- Ñîçäàòü ïàïêó äëÿ âûõîäíûõ ôàéëîâ (íàïğèìåğ D:\VIDEO_TimeLapse) è â íåé:
--- D:\VIDEO_TimeLapse
------BUTAFOR
------CENTER
------PENOREZ
------SVAR
------ è ò.ä.

- Óñòàíîâèòü PYTHON âåğñèè 3+
- Óñòàíîâèòü  FFMPEG

- Ñîçäàòü â ïëàíèğîâùèêå çàäà÷ó íà çàïóñê èíòåğïğèòàòîğà Python ñ êëş÷¸ì ñêğèïòà videoCreator (ñì êàğòèíêó)
