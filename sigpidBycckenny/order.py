import csv
import pandas as pd

   

lst_order = ['android.permission.ACCESS_WIFI_STATE', 
		'android.permission.CAMERA', 
		'android.permission.CHANGE_NETWORK_STATE', 
		'android.permission.CHANGE_WIFI_STATE', 
		'android.permission.DISABLE_KEYGUARD', 
		'android.permission.GET_TASKS', 
		'android.permission.INSTALL_PACKAGES', 
		'android.permission.READ_CALL_LOG', 
		'android.permission.READ_CONTACTS', 
		'android.permission.READ_EXTERNAL_STORAGE', 
		'com.android.browser.permission.READ_HISTORY_BOOKMARKS',
		'android.permission.READ_LOGS', 
		'android.permission.READ_PHONE_STATE', 
		'android.permission.READ_SMS', 
		'android.permission.RECEIVE_BOOT_COMPLETED', 
		'android.permission.RESTART_PACKAGES', 
		'android.permission.SEND_SMS', 
		'android.permission.SET_WALLPAPER', 
		'android.permission.SYSTEM_ALERT_WINDOW', 
		'android.permission.WRITE_APN_SETTINGS', 
		'android.permission.WRITE_CONTACTS', 
		'android.permission.WRITE_SETTINGS',
		'class']
df = pd.read_csv('microdataset.csv')
df.to_csv("microdataset_new.csv", index=False, columns=lst_order)