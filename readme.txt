��� ����-������ �����:

- � Trassir ������� ������ �� �������:

##############################################################

from datetime import datetime

def ScreenShot():
	if WorkTime():
		object("�����������").screenshot()
		object("�����").screenshot()
		object("������� ���").screenshot()
		object("���������").screenshot()
		alert("������ ���������")
	timeout(60000, ScreenShot) # 1�������� ��������


def WorkTime():
	t = int(datetime.strftime(datetime.now(), "%H"))
	if t > 9 and t < 22: # �������� �������� �������
		return 1
	return 0

ScreenShot()

##############################################################

- ������� ��������� ��������� � ����� ���� ����������� ���������:

---Screenshots (���� trassir ������ ���������)
------BUTAFOR
------CENTER
------PENOREZ
------SVAR
------ � �.�. 

- ������� ����� ��� �������� ������ (�������� D:\VIDEO_TimeLapse) � � ���:
--- D:\VIDEO_TimeLapse
------BUTAFOR
------CENTER
------PENOREZ
------SVAR
------ � �.�.

- ���������� PYTHON ������ 3+
- ����������  FFMPEG

- ������� � ������������ ������ �� ������ �������������� Python � ������ ������� videoCreator (�� ��������)
